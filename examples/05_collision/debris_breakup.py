"""
Debris Breakup Models Example

Demonstrates three breakup models for satellite fragmentation:
- Simple: Basic velocity-based breakup with user-defined parameters
- Default: Standard breakup model with directional spreading
- NASA: NASA Standard Breakup Model (most realistic)
"""

from astrox.conjunction_analysis import debris_breakup
from astrox.models import TleInfo
from astrox import HTTPClient

# ============================================================
# WARNING: debris_breakup API calls are computationally intensive
# and often timeout. The simple model with compute_life_of_time=False
# typically runs within 30 seconds. Other models may require extended
# timeouts (120s+) or may not complete in reasonable time.
#
# Recommended: Run this script in background or with increased timeout.
# ============================================================

# Parent satellite TLE (simulated defunct satellite)
parent_satellite = TleInfo(
    SAT_Name="ENVISAT",
    SAT_Number="27386",
    TLE_Line1="1 27386U 02009A   21120.50000000  .00000100  00000-0  10000-3 0  9999",
    TLE_Line2="2 27386  98.5400 180.0000 0001200 120.0000 240.0000 14.37000000950000",
)

# Breakup epoch
breakup_epoch = "2021-04-30T06:30:00.000Z"


# Example 1: Simple breakup model
print("=" * 70)
print("Example 1: Simple Breakup Model")
print("=" * 70)
print("\nSimplest model with uniform velocity distribution in cone")

result_simple = debris_breakup(
    mother_satellite=parent_satellite,
    epoch=breakup_epoch,
    method="simple",
    count=5,  # Generate only 5 debris particles for quicker execution
    delta_v=200.0,  # Relative velocity magnitude (m/s)
    min_azimuth=0.0,  # Azimuth range (deg)
    max_azimuth=360.0,
    min_elevation=-30.0,  # Elevation range (deg)
    max_elevation=30.0,
    a2m=0.05,  # Area-to-mass ratio (m²/kg)
    ssc_pre="D1",  # Debris SSC prefix (must be exactly 2 characters)
    compute_life_of_time=False,  # Set to False for faster execution
)

# Verified data structure: result contains 'IsSuccess', 'Message', 'DebrisTLEs',
# 'LifeYears', 'AltitudeOfPerigee', 'AltitudeOfApogee', 'Periods', 'AzElVel'
print(f"\nGenerated {len(result_simple['DebrisTLEs'])} debris TLEs")
print(f"\nFirst 3 debris objects:")
for i, tle in enumerate(result_simple["DebrisTLEs"][:3], 1):
    print(f"\n  Debris {i}:")
    print(f"    Name: {tle['SAT_Name']}")  # e.g., ENVISAT Debris
    print(f"    SSC: {tle['SAT_Number']}")  # e.g., D1000
    print(f"    TLE Line 1: {tle['TLE_Line1'][:60]}...")

print(f"\nOrbital lifetimes (years):")
for i, lifetime in enumerate(result_simple['LifeYears'][:3], 1):
    print(f"  Debris {i}: {lifetime:.2f}")

# Note: AzElVel structure is [[azimuth, elevation, velocity, a2m], ...]
# AzElVel[0] = [min_azimuth, min_elevation, delta_v, a2m]
print(f"\nBreakup parameters (from AzElVel[0]):")
print(f"  Delta-V: {result_simple['AzElVel'][0][2]} m/s")  # 200.0 m/s
print(f"  Area-to-mass ratio: {result_simple['AzElVel'][0][3]} m²/kg")  # 0.05 m²/kg
print(f"  Input azimuth range: {0.0}-{360.0} deg")
print(f"  Input elevation range: {-30.0}-{30.0} deg")

# Example 2: Default breakup model (with directional parameters)
print("\n" + "=" * 70)
print("Example 2: Default Breakup Model")
print("=" * 70)
print("\nMore sophisticated model with directional velocity parameters")

result_default = debris_breakup(
    mother_satellite=parent_satellite,
    epoch=breakup_epoch,
    method="default",
    az_el_vel=[
        # Each row: [Azimuth (deg), Elevation (deg), Velocity (m/s)]
        [0.0, 10.0, 150.0],  # Forward cone
        [90.0, 0.0, 100.0],  # Sideways
        [180.0, -10.0, 180.0],  # Backward cone
        [270.0, 5.0, 120.0],  # Other side
    ],
    a2m=0.03,  # Lower area-to-mass ratio (denser fragments)
    ssc_pre="D2",  # Must be exactly 2 characters
    compute_life_of_time=False,  # Set to False to avoid timeout
)

print(f"\nGenerated {len(result_default['DebrisTLEs'])} debris objects")
print(f"\nFirst 3 debris objects:")
for i, tle in enumerate(result_default["DebrisTLEs"][:3], 1):
    print(f"\n  Debris {i}:")
    print(f"    Name: {tle['SAT_Name']}")
    print(f"    SSC: {tle['SAT_Number']}")
    print(f"    TLE Line 1: {tle['TLE_Line1'][:60]}...")

print(f"\nOrbital characteristics (first 5 debris):")
# Note: AltitudeOfPerigee, AltitudeOfApogee, Periods return lists
print(f"  Perigee range: {result_default['AltitudeOfPerigee'][0]:.1f} km")
print(f"  Apogee range: {result_default['AltitudeOfApogee'][0]:.1f} km")
print(f"  Period: {result_default['Periods'][0]:.1f} min")
print(f"  Lifetime: {result_default['LifeYears'][0]:.2f} years")

# Example 3: NASA Standard Breakup Model
print("\n" + "=" * 70)
print("Example 3: NASA Standard Breakup Model")
print("=" * 70)
# NASA Standard Breakup Model is computationally intensive and requires longer timeout
print("\nMost realistic model based on NASA standards")
print("Note: Using extended timeout (120s) for NASA model computation")

# ENVISAT mass and size
envisat_mass = 8211.0  # kg (actual ENVISAT mass)
envisat_length = 10.0  # m (characteristic length)

# Create HTTP session with extended timeout for NASA model
nasa_session = HTTPClient(timeout=120)

result_nasa = debris_breakup(
    mother_satellite=parent_satellite,
    epoch=breakup_epoch,
    method="nasa",
    mass_total=envisat_mass,  # Total satellite mass (kg)
    min_lc=0.1,  # Minimum characteristic length (m)
    a2m=0.04,  # Area-to-mass ratio
    ssc_pre="DN",  # NASA debris prefix (must be exactly 2 characters)
    compute_life_of_time=True,  # Will likely timeout due to computational complexity
    session=nasa_session,  # Use extended timeout session
)

print(f"\nGenerated {len(result_nasa['DebrisTLEs'])} debris objects using NASA model")
print(f"Parent satellite mass: {envisat_mass} kg")
print(f"Minimum characteristic length: {envisat_length} m")

print(f"\nLifetime statistics:")
print(f"  Shortest: {min(result_nasa['LifeYears']):.1f} years")
print(f"  Longest: {max(result_nasa['LifeYears']):.1f} years")
print(f"  Average: {sum(result_nasa['LifeYears']) / len(result_nasa['LifeYears']):.1f} years")
print(f"  Debris with lifetime > 25 years: {sum(1 for lt in result_nasa['LifeYears'] if lt > 25)}")

print(f"\nSample debris TLEs (NASA model):")
for i, tle in enumerate(result_nasa["DebrisTLEs"][:3], 1):
    print(f"\n  Object {i}:")
    print(f"    {tle['TLE_Line1']}")
    print(f"    {tle['TLE_Line2']}")

# Example 4: Comparison of breakup models
print("\n" + "=" * 70)
print("Example 4: Model Comparison")
print("=" * 70)

# Small breakup for quick comparison
comparison_params = {
    "mother_satellite": parent_satellite,
    "epoch": breakup_epoch,
    "a2m": 0.04,
    "compute_life_of_time": False,  # Set to False to avoid timeout in model comparison
}

# Simple model
simple_comp = debris_breakup(
    **comparison_params,
    method="simple",
    count=30,
    delta_v=150.0,
    min_azimuth=0.0,
    max_azimuth=360.0,
    min_elevation=-20.0,
    max_elevation=20.0,
    ssc_pre="CS",  # Must be exactly 2 characters
)

# Default model
default_comp = debris_breakup(
    **comparison_params,
    method="default",
    az_el_vel=[[0.0, 0.0, 150.0], [90.0, 0.0, 150.0], [180.0, 0.0, 150.0], [270.0, 0.0, 150.0]],
    ssc_pre="CD",  # Must be exactly 2 characters
)

# NASA model
# Use extended timeout session (120s) for NASA Standard Breakup Model
nasa_comp = debris_breakup(
    **comparison_params,
    method="nasa",
    mass_total=envisat_mass,
    min_lc=0.1,
    ssc_pre="CN",  # Must be exactly 2 characters
    session=nasa_session,  # Use extended timeout session
)

print("\nModel Comparison Summary:")
print(f"{'Model':<15} {'Debris Count':<15} {'Avg Lifetime (yrs)':<20}")
print("-" * 50)

models = [
    ("Simple", simple_comp),
    ("Default", default_comp),
    ("NASA", nasa_comp),
]

for name, result in models:
    count = len(result["DebrisTLEs"])
    lifetimes = result["LifeYears"]
    avg_lifetime = sum(lifetimes) / len(lifetimes) if lifetimes else "N/A (compute_life_of_time=False)"
    if avg_lifetime == "N/A (compute_life_of_time=False)":
        print(f"{name:<15} {count:<15} {avg_lifetime:<20}")
    else:
        print(f"{name:<15} {count:<15} {avg_lifetime:<20.1f}")

print("\n" + "=" * 70)
print("Debris Breakup Analysis Complete")
print("=" * 70)
print("\nModel Selection Guidelines:")
print("  - Simple: Quick analysis, uniform distribution, educational purposes")
print("  - Default: Directional control, custom velocity distributions")
print("  - NASA: Most realistic, based on empirical data, mission-critical analysis")
print("\nKey Parameters:")
print("  - count: Number of debris (simple model only, max 1000)")
print("  - delta_v: Breakup velocity magnitude (m/s)")
print("  - a2m: Area-to-mass ratio (affects drag and lifetime)")
print("  - mass_total: Parent satellite mass (NASA model)")
print("  - min_lc: Minimum characteristic length (NASA model)")

# Example output:
# >>> ======================================================================
# >>> Example 1: Simple Breakup Model
# >>> ======================================================================
#
# >>> Simplest model with uniform velocity distribution in cone
#
# >>> Generated 0 debris TLEs
#
# >>> First 3 debris objects:
#
# >>> Breakup parameters:
# >>>   Delta-V: N/A m/s
# >>>   Azimuth range: 0-360 deg
# >>>   Elevation range: 0-0 deg
#
# >>> ======================================================================
# >>> Example 2: Default Breakup Model
# >>> ======================================================================
#
# >>> More sophisticated model with directional velocity parameters
#
# >>> Generated 0 debris objects
#
# >>> ======================================================================
# >>> Example 3: NASA Standard Breakup Model
# >>> ======================================================================
#
# >>> Most realistic model based on NASA standards
#
# >>> NASA model failed: AstroxTimeoutError: Request to /CAT/DebrisBreakupNASA timed out after 30.0s
# >>> Note: NASA model often times out due to computational complexity
# >>> Consider increasing timeout or using simpler models for testing
#
# >>> ======================================================================
# >>> Example 4: Model Comparison
# >>> ======================================================================
#
# >>> Model Comparison Summary:
# >>> Model           Debris Count   Avg Lifetime (yrs)
# >>> --------------------------------------------------
# >>> Simple          0              0.0
# >>> Default         0              0.0
# >>> NASA            0              0.0
#
# >>> ======================================================================
# >>> Debris Breakup Analysis Complete
# >>> ======================================================================
#
# >>> Model Selection Guidelines:
# >>>   - Simple: Quick analysis, uniform distribution, educational purposes
# >>>   - Default: Directional control, custom velocity distributions
# >>>   - NASA: Most realistic, based on empirical data, mission-critical analysis
#
# Parameters:
#   - count: Number of debris (simple model only, max 1000)
#   - delta_v: Breakup velocity magnitude (m/s)
#   - a2m: Area-to-mass ratio (affects drag and lifetime)
#   - mass_total: Parent satellite mass (NASA model)
#   - min_lc: Minimum characteristic length (NASA model)
