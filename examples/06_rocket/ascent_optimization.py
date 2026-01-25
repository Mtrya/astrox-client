"""
Rocket Ascent Trajectory Optimization

Demonstrates optimization of multi-stage rocket ascent trajectories to reach
target orbits using the flight segment model.
"""

from astrox.rocket import optimize_trajectory
# Note: RocketSegmentInfo is not available in public models.py
# This is a known issue - the model needs to be aliased in models.py
from astrox._models import RocketSegmentInfo

# Example 1: Two-stage rocket to LEO
print("=" * 70)
print("Example 1: Two-Stage Rocket to LEO (800 km)")
print("=" * 70)

# Define rocket segments (CZ-2D-like configuration)
stage1_segments = [
    RocketSegmentInfo(
        Name="一级起飞",  # Stage 1 liftoff
        Text="First stage ignition and vertical ascent",
        Fx=2961600.0,  # Total thrust (N) - 4 YF-21C engines
        Ips=2550.0,  # Specific impulse (m/s) at sea level
        Gj=4400.0,  # Jettison mass (kg) - stage 1 dry mass
        Dt=145.0,  # Burn duration (s)
        Sm=7.0,  # Aerodynamic area (m²)
        Sa=4.8,  # Nozzle area (m²)
        Psicx="0.0",  # Yaw angle (deg) - straight up initially
        Phicx_dot=0.0,  # Pitch rate (deg/s) - controlled by t1, alpham
    ),
]

stage2_segments = [
    RocketSegmentInfo(
        Name="二级起飞",  # Stage 2 ignition
        Text="Second stage ignition after interstage separation",
        Fx=742040.0,  # YF-24E engine thrust (N)
        Ips=2942.0,  # Specific impulse (m/s) in vacuum
        Gj=1800.0,  # Stage 2 dry mass (kg)
        Dt=180.0,  # Burn duration (s)
        Sm=5.0,  # Smaller aerodynamic area
        Sa=2.4,  # Nozzle area (m²)
        Psicx="Follow",  # Yaw follows previous stage
        Phicx_dot=0.2,  # Pitch rate during vacuum flight
    ),
]

# Combine all segments
rocket_segments = stage1_segments + stage2_segments

# Target orbit (800 km circular LEO, sun-synchronous)
result_leo = optimize_trajectory(
    gw=1500.0,  # Payload mass (kg)
    t1=15.0,  # Gravity turn start time (s after liftoff)
    alpham=5.0,  # Maximum angle of attack during atmospheric flight (deg)
    natmos=1,  # Number of atmospheric flight segments
    rocket_segments=rocket_segments,
    sma0=7178137.0,  # Target semi-major axis (m) - 800 km altitude
    ecc0=0.001,  # Target eccentricity (nearly circular)
    inc0=98.2,  # Target inclination (deg) - sun-synchronous
    omg0=90.0,  # Target argument of perigee (deg)
    name="CZ-2D SSO Mission",
    text="Launch to 800 km sun-synchronous orbit",
    rocket_type="CZ2D",
    name_fa_she_dian="Jiuquan",
    fa_she_dian_lla=[98.0, 41.0, 1500.0],  # Jiuquan Satellite Launch Center
    a0=185.0,  # Launch azimuth (deg) for sun-synchronous orbit
)

print("\nOptimization Results:")
print(f"Mission: {result_leo.get('Name', 'N/A')}")
print(f"Rocket Type: {result_leo.get('RocketType', 'N/A')}")
print(f"Launch Site: {result_leo.get('LaunchSite', 'N/A')}")
print(f"Payload: {1500.0} kg")
print(f"\nTarget Orbit:")
print(f"  Altitude: 800 km")
print(f"  Inclination: 98.2° (SSO)")
print(f"  Eccentricity: 0.001")
print(f"\nTrajectory Summary:")
if "FlightSegments" in result_leo:
    for i, seg in enumerate(result_leo["FlightSegments"], 1):
        print(f"  Segment {i}: {seg.get('Name', 'N/A')} - {seg.get('Duration', 'N/A')}s")

# Example 2: Three-stage rocket to GTO
print("\n" + "=" * 70)
print("Example 2: Three-Stage Rocket to GTO")
print("=" * 70)

# CZ-3B-like configuration (heavier lift to GTO)
gto_segments = [
    RocketSegmentInfo(
        Name="一级起飞",
        Text="Core stage + 4 boosters liftoff",
        Fx=5923200.0,  # Core + boosters total thrust (N)
        Ips=2550.0,  # Sea-level Isp
        Gj=18000.0,  # Boosters + stage 1 dry mass
        Dt=150.0,  # Burn duration
        Sm=12.0,  # Large aerodynamic area with boosters
        Sa=8.0,  # Combined nozzle area
        Psicx="0.0",
        Phicx_dot=0.0,
    ),
    RocketSegmentInfo(
        Name="二级起飞",
        Text="Second stage in upper atmosphere",
        Fx=742040.0,
        Ips=2942.0,
        Gj=3000.0,  # Stage 2 dry mass
        Dt=185.0,
        Sm=6.0,
        Sa=2.8,
        Psicx="Follow",
        Phicx_dot=0.15,
    ),
    RocketSegmentInfo(
        Name="三级起飞",
        Text="Third stage for GTO insertion",
        Fx=163000.0,  # YF-75 upper stage (H2/LOX)
        Ips=4270.0,  # High Isp for hydrogen engine
        Gj=1200.0,  # Stage 3 dry mass
        Dt=470.0,  # Long burn for GTO
        Sm=4.0,
        Sa=1.5,
        Psicx="Follow",
        Phicx_dot=0.05,  # Slow pitch during GTO insertion
    ),
]

# GTO target orbit
result_gto = optimize_trajectory(
    gw=5500.0,  # Heavier GTO payload
    t1=18.0,  # Slightly later gravity turn
    alpham=4.0,  # Lower AoA limit for stability
    natmos=1,
    rocket_segments=gto_segments,
    sma0=24361137.0,  # GTO semi-major axis (m) - 185 km x 35786 km
    ecc0=0.73,  # GTO eccentricity
    inc0=28.5,  # Equatorial launch inclination
    omg0=178.0,  # Argument of perigee
    name="CZ-3B GTO Mission",
    text="Heavy payload to geostationary transfer orbit",
    rocket_type="CZ3B",
    name_fa_she_dian="Xichang",
    fa_she_dian_lla=[102.0, 28.25, 1800.0],  # Xichang Satellite Launch Center
    a0=95.0,  # Near-equatorial launch azimuth
)

print("\nGTO Mission Results:")
print(f"Payload: {5500.0} kg")
print(f"Target Orbit: 185 km x 35786 km (GTO)")
print(f"Inclination: 28.5°")
print(f"Launch Site: Xichang (low latitude advantage)")

# Example 3: Small launcher to LEO
print("\n" + "=" * 70)
print("Example 3: Small Launcher (KZ-1A to LEO)")
print("=" * 70)

# Simplified solid-propellant small launcher
small_launcher_segments = [
    RocketSegmentInfo(
        Name="一级起飞",
        Text="Solid rocket motor stage 1",
        Fx=1200000.0,  # Solid motor thrust
        Ips=2600.0,  # Solid propellant Isp
        Gj=800.0,  # Dry mass
        Dt=75.0,  # Shorter burn time
        Sm=3.0,
        Sa=1.5,
        Psicx="0.0",
        Phicx_dot=0.0,
    ),
    RocketSegmentInfo(
        Name="二级起飞",
        Text="Solid rocket motor stage 2",
        Fx=400000.0,
        Ips=2750.0,
        Gj=300.0,
        Dt=90.0,
        Sm=2.0,
        Sa=0.8,
        Psicx="Follow",
        Phicx_dot=0.3,
    ),
    RocketSegmentInfo(
        Name="三级起飞",
        Text="Solid rocket motor stage 3",
        Fx=100000.0,
        Ips=2900.0,
        Gj=150.0,
        Dt=120.0,
        Sm=1.5,
        Sa=0.4,
        Psicx="Follow",
        Phicx_dot=0.2,
    ),
]

result_small = optimize_trajectory(
    gw=300.0,  # Small payload
    t1=12.0,
    alpham=6.0,
    natmos=1,
    rocket_segments=small_launcher_segments,
    sma0=6878137.0,  # 500 km altitude
    ecc0=0.002,
    inc0=97.5,  # SSO inclination
    omg0=90.0,
    name="KZ-1A LEO Mission",
    text="Small satellite to LEO",
    rocket_type="KZ1A",
    fa_she_dian_lla=[98.0, 41.0, 1500.0],  # Jiuquan
    a0=188.0,
)

print("\nSmall Launcher Results:")
print(f"Payload: {300.0} kg")
print(f"Target: 500 km LEO")
print(f"Three solid stages")

# Example 4: Optimization with different launch azimuths
print("\n" + "=" * 70)
print("Example 4: Launch Azimuth Optimization")
print("=" * 70)

# Same rocket, different azimuths
base_segments = [
    RocketSegmentInfo(
        Name="一级起飞",
        Fx=2961600.0,
        Ips=2550.0,
        Gj=4400.0,
        Dt=145.0,
        Sm=7.0,
        Sa=4.8,
        Psicx="0.0",
        Phicx_dot=0.0,
    ),
    RocketSegmentInfo(
        Name="二级起飞",
        Fx=742040.0,
        Ips=2942.0,
        Gj=1800.0,
        Dt=180.0,
        Sm=5.0,
        Sa=2.4,
        Psicx="Follow",
        Phicx_dot=0.2,
    ),
]

azimuths = [
    ("Northerly", 185.0, 98.0),  # SSO
    ("Easterly", 95.0, 42.0),  # Low inclination from Jiuquan
    ("Polar", 180.0, 100.0),  # Polar orbit
]

print("\nComparing launch azimuths from Jiuquan:")
for direction, azimuth, target_inc in azimuths:
    result = optimize_trajectory(
        gw=1500.0,
        t1=15.0,
        alpham=5.0,
        natmos=1,
        rocket_segments=base_segments,
        sma0=7178137.0,
        ecc0=0.001,
        inc0=target_inc,
        omg0=90.0,
        fa_she_dian_lla=[98.0, 41.0, 1500.0],
        a0=azimuth,
    )
    print(f"  {direction}: Azimuth {azimuth}° → Inclination {target_inc}°")

print("\n" + "=" * 70)
print("Ascent Trajectory Optimization Complete")
print("=" * 70)
print("\nKey Parameters:")
print("  - gw: Payload mass (kg)")
print("  - t1: Gravity turn initiation time (s)")
print("  - alpham: Maximum angle of attack limit (deg)")
print("  - natmos: Number of atmospheric flight segments")
print("  - sma0, ecc0, inc0, omg0: Target orbital elements")
print("  - a0: Launch azimuth (deg)")
print("\nRocket Segment Parameters:")
print("  - Fx: Total axial thrust (N)")
print("  - Ips: Specific impulse (m/s)")
print("  - Gj: Jettisoned mass at stage end (kg)")
print("  - Dt: Burn duration (s)")
print("  - Sm: Aerodynamic area (m²)")
print("  - Sa: Engine nozzle area (m²)")
print("  - Psicx: Yaw angle (deg or 'Follow')")
print("  - Phicx_dot: Pitch rate (deg/s)")
print("\nSupported Rocket Types:")
print("  CZ2C, CZ2D, CZ3A, CZ3B, CZ3C, CZ4B, CZ4C, CZ7A, KZ1A")

if __name__ == "__main__":
    # Note: This example currently fails with a malformed JSON response from the API
    # The server returns invalid JSON that cannot be parsed
    # Error: JSONDecodeError: Expecting ',' delimiter: line 1575413 column 27 (char 36509292)
    # This is a server-side issue that needs to be fixed
    pass
    # Example output would be shown here if the API worked correctly
    # >>> ======================================================================
    # >>> Example 1: Two-Stage Rocket to LEO (800 km)
    # >>> ======================================================================
    # >>>
    # >>> Optimization Results:
    # >>> Mission: CZ-2D SSO Mission
    # >>> Rocket Type: CZ2D
    # >>> Launch Site: Jiuquan
    # >>> Payload: 1500.0 kg
    # >>>
    # >>> Target Orbit:
    # >>>   Altitude: 800 km
    # >>>   Inclination: 98.2° (SSO)
    # >>>   Eccentricity: 0.001
    # >>>
    # >>> Trajectory Summary:
    # >>>   Segment 1: 一级起飞 - 145.0s
    # >>>   Segment 2: 二级起飞 - 180.0s
    # >>>
    # >>> ======================================================================
    # >>> Example 2: Three-Stage Rocket to GTO
    # >>> ======================================================================
    # >>>
    # >>> GTO Mission Results:
    # >>> Payload: 5500.0 kg
    # >>> Target Orbit: 185 km x 35786 km (GTO)
    # >>> Inclination: 28.5°
    # >>> Launch Site: Xichang (low latitude advantage)
    # >>>
    # >>> ======================================================================
    # >>> Example 3: Small Launcher (KZ-1A to LEO)
    # >>> ======================================================================
    # >>>
    # >>> Small Launcher Results:
    # >>> Payload: 300.0 kg
    # >>> Target: 500 km LEO
    # >>> Three solid stages
    # >>>
    # >>> ======================================================================
    # >>> Example 4: Launch Azimuth Optimization
    # >>> ======================================================================
    # >>>
    # >>> Comparing launch azimuths from Jiuquan:
    # >>>   Northerly: Azimuth 185.0° → Inclination 98.0°
    # >>>   Easterly: Azimuth 95.0° → Inclination 42.0°
    # >>>   Polar: Azimuth 180.0° → Inclination 100.0°
    # >>>
    # >>> ======================================================================
    # >>> Ascent Trajectory Optimization Complete
    # >>> ======================================================================
    # >>>
    # >>> Key Parameters:
    # >>>   - gw: Payload mass (kg)
    # >>>   - t1: Gravity turn initiation time (s)
    # >>>   - alpham: Maximum angle of attack limit (deg)
    # >>>   - natmos: Number of atmospheric flight segments
    # >>>   - sma0, ecc0, inc0, omg0: Target orbital elements
    # >>>   - a0: Launch azimuth (deg)
    # >>>
    # >>> Rocket Segment Parameters:
    # >>>   - Fx: Total axial thrust (N)
    # >>>   - Ips: Specific impulse (m/s)
    # >>>   - Gj: Jettisoned mass at stage end (kg)
    # >>>   - Dt: Burn duration (s)
    # >>>   - Sm: Aerodynamic area (m²)
    # >>>   - Sa: Engine nozzle area (m²)
    # >>>   - Psicx: Yaw angle (deg or 'Follow')
    # >>>   - Phicx_dot: Pitch rate (deg/s)
    # >>>
    # >>> Supported Rocket Types:
    # >>>   CZ2C, CZ2D, CZ3A, CZ3B, CZ3C, CZ4B, CZ4C, CZ7A, KZ1A
