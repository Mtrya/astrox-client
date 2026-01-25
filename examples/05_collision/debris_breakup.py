"""
Debris Breakup Models Example

Demonstrates three breakup models for satellite fragmentation:
- Simple: Basic velocity-based breakup with user-defined parameters
- Default: Standard breakup model with directional spreading
- NASA: NASA Standard Breakup Model (most realistic)
"""

from astrox.conjunction_analysis import debris_breakup
from astrox.models import TleInfo

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
    count=50,  # Generate 50 debris particles (max 1000)
    delta_v=200.0,  # Relative velocity magnitude (m/s)
    min_azimuth=0.0,  # Azimuth range (deg)
    max_azimuth=360.0,
    min_elevation=-30.0,  # Elevation range (deg)
    max_elevation=30.0,
    a2m=0.05,  # Area-to-mass ratio (m²/kg)
    ssc_pre="D1",  # Debris SSC prefix
    compute_life_of_time=True,  # Calculate orbital lifetimes
)

print(f"\nGenerated {len(result_simple.get('TLEs', []))} debris TLEs")
print(f"\nFirst 3 debris objects:")
for i, tle in enumerate(result_simple.get("TLEs", [])[:3], 1):
    print(f"\n  Debris {i}:")
    print(f"    Name: {tle.get('SAT_Name', 'N/A')}")
    print(f"    SSC: {tle.get('SAT_Number', 'N/A')}")
    print(f"    TLE Line 1: {tle.get('TLE_Line1', 'N/A')[:60]}...")

if "Lifetimes" in result_simple:
    print(f"\nOrbital lifetimes (years):")
    lifetimes = result_simple["Lifetimes"][:5]
    for i, lifetime in enumerate(lifetimes, 1):
        print(f"  Debris {i}: {lifetime:.1f} years")

print(f"\nBreakup parameters:")
print(f"  Delta-V: {result_simple.get('DeltaV', 'N/A')} m/s")
print(f"  Azimuth range: {result_simple.get('MinAzimuth', 0)}-{result_simple.get('MaxAzimuth', 360)} deg")
print(f"  Elevation range: {result_simple.get('MinElevation', 0)}-{result_simple.get('MaxElevation', 0)} deg")

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
        # [Azimuth (deg), Elevation (deg), Velocity (m/s)]
        0.0,
        10.0,
        150.0,  # Forward cone
        90.0,
        0.0,
        100.0,  # Sideways
        180.0,
        -10.0,
        180.0,  # Backward cone
        270.0,
        5.0,
        120.0,  # Other side
    ],
    a2m=0.03,  # Lower area-to-mass ratio (denser fragments)
    ssc_pre="D2",
    compute_life_of_time=True,
)

print(f"\nGenerated {len(result_default.get('TLEs', []))} debris objects")

if "Altitudes" in result_default and "Periods" in result_default:
    print(f"\nOrbital characteristics (first 5 debris):")
    altitudes = result_default["Altitudes"][:5]
    periods = result_default["Periods"][:5]
    lifetimes = result_default.get("Lifetimes", [])[:5]

    for i in range(min(5, len(altitudes))):
        print(f"\n  Debris {i + 1}:")
        if i < len(altitudes):
            print(f"    Altitude: {altitudes[i]:.1f} km")
        if i < len(periods):
            print(f"    Period: {periods[i]:.1f} min")
        if i < len(lifetimes):
            print(f"    Lifetime: {lifetimes[i]:.1f} years")

# Example 3: NASA Standard Breakup Model
print("\n" + "=" * 70)
print("Example 3: NASA Standard Breakup Model")
print("=" * 70)
print("\nMost realistic model based on NASA standards")

# ENVISAT mass and size
envisat_mass = 8211.0  # kg (actual ENVISAT mass)
envisat_length = 10.0  # m (characteristic length)

result_nasa = debris_breakup(
    mother_satellite=parent_satellite,
    epoch=breakup_epoch,
    method="nasa",
    mass_total=envisat_mass,  # Total satellite mass (kg)
    min_lc=0.1,  # Minimum characteristic length (m)
    a2m=0.04,  # Area-to-mass ratio
    ssc_pre="DN",  # NASA debris prefix
    compute_life_of_time=True,
)

print(f"\nGenerated {len(result_nasa.get('TLEs', []))} debris objects using NASA model")
print(f"Parent satellite mass: {envisat_mass} kg")
print(f"Minimum characteristic length: {envisat_length} m")

if "Lifetimes" in result_nasa:
    lifetimes = result_nasa["Lifetimes"]
    print(f"\nLifetime statistics:")
    print(f"  Shortest: {min(lifetimes):.1f} years")
    print(f"  Longest: {max(lifetimes):.1f} years")
    print(f"  Average: {sum(lifetimes) / len(lifetimes):.1f} years")
    print(f"  Debris with lifetime > 25 years: {sum(1 for lt in lifetimes if lt > 25)}")

print(f"\nSample debris TLEs (NASA model):")
for i, tle in enumerate(result_nasa.get("TLEs", [])[:3], 1):
    print(f"\n  Object {i}:")
    print(f"    {tle.get('TLE_Line1', 'N/A')}")
    print(f"    {tle.get('TLE_Line2', 'N/A')}")

# Example 4: Comparison of breakup models
print("\n" + "=" * 70)
print("Example 4: Model Comparison")
print("=" * 70)

# Small breakup for quick comparison
comparison_params = {
    "mother_satellite": parent_satellite,
    "epoch": breakup_epoch,
    "a2m": 0.04,
    "compute_life_of_time": True,
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
    ssc_pre="CS",
)

# Default model
default_comp = debris_breakup(
    **comparison_params,
    method="default",
    az_el_vel=[0.0, 0.0, 150.0, 90.0, 0.0, 150.0, 180.0, 0.0, 150.0, 270.0, 0.0, 150.0],
    ssc_pre="CD",
)

# NASA model
nasa_comp = debris_breakup(
    **comparison_params,
    method="nasa",
    mass_total=envisat_mass,
    min_lc=0.1,
    ssc_pre="CN",
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
    count = len(result.get("TLEs", []))
    lifetimes = result.get("Lifetimes", [])
    avg_lifetime = sum(lifetimes) / len(lifetimes) if lifetimes else 0
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
