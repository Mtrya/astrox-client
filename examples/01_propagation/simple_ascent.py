"""Example: Simple Ascent Trajectory

This example demonstrates simple ascent trajectory modeling for launch
vehicle flight from liftoff to orbit insertion. The model uses a simplified
approach suitable for preliminary mission design.

We'll model a launch from Jiuquan Satellite Launch Center to LEO orbit.
"""

from astrox.propagator import propagate_simple_ascent


def main():
    # Jiuquan Satellite Launch Center (JSLC), China
    # One of China's main launch sites
    launch_lat = 40.9575  # degrees North
    launch_lon = 100.2912  # degrees East
    launch_alt = 1000.0  # meters (approximate elevation)

    # Burnout conditions (end of powered flight)
    # These represent the state when the rocket reaches orbit
    burnout_velocity = 7800.0  # m/s (slightly below orbital velocity)
    burnout_altitude = 200000.0  # 200 km altitude

    # Burnout position (downrange from launch site)
    # After powered ascent, typically several degrees downrange
    burnout_lat = 42.5  # degrees North (downrange)
    burnout_lon = 105.0  # degrees East

    print("Computing launch ascent trajectory...")
    print(f"Launch site: Jiuquan ({launch_lat:.4f}°N, {launch_lon:.4f}°E)")
    print(f"Launch altitude: {launch_alt} m")
    print(f"Burnout conditions:")
    print(f"  Velocity: {burnout_velocity} m/s")
    print(f"  Altitude: {burnout_altitude/1000:.0f} km")
    print(f"  Position: ({burnout_lat:.2f}°N, {burnout_lon:.2f}°E)")
    print()

    # Typical ascent takes 8-10 minutes for LEO
    # We'll use a 480-second (8-minute) ascent
    result = propagate_simple_ascent(
        start="2024-01-01T03:00:00.000Z",  # T-0 (liftoff)
        stop="2024-01-01T03:08:00.000Z",   # T+8 minutes (burnout)
        launch_latitude=launch_lat,
        launch_longitude=launch_lon,
        launch_altitude=launch_alt,
        burnout_velocity=burnout_velocity,
        burnout_latitude=burnout_lat,
        burnout_longitude=burnout_lon,
        burnout_altitude=burnout_altitude,
        central_body="Earth",
        step=1.0,  # 1-second steps for detailed ascent profile
    )

    # Print results
    print("=" * 60)
    print("Simple Ascent Trajectory Results")
    print("=" * 60)
    print(f"Success: {result.get('IsSuccess', 'N/A')}")
    print(f"Message: {result.get('Message', 'N/A')}")

    if 'CzmlPositions' in result:
        positions = result['CzmlPositions']
        num_points = len(positions) // 3
        print(f"\nGenerated {num_points} position points")
        print(f"Step size: 1 second")
        print(f"Ascent duration: 8 minutes (480 seconds)")

        # Analyze trajectory phases
        earth_radius = 6378137.0

        # Sample altitudes at key times
        sample_times = [0, 60, 120, 240, 360, 479]  # seconds
        print(f"\nAltitude profile:")

        for t in sample_times:
            if t < num_points:
                idx = t * 3
                if idx + 2 < len(positions):
                    x, y, z = positions[idx:idx+3]
                    r = (x**2 + y**2 + z**2) ** 0.5
                    altitude_km = (r - earth_radius) / 1000.0
                    velocity = "liftoff" if t == 0 else f"~{burnout_velocity * t/480:.0f} m/s"
                    print(f"  T+{t:3d}s: {altitude_km:6.1f} km  ({velocity})")

        # Calculate downrange distance
        import math
        dlat = abs(burnout_lat - launch_lat) * math.pi / 180
        dlon = abs(burnout_lon - launch_lon) * math.pi / 180
        mean_lat = (launch_lat + burnout_lat) / 2 * math.pi / 180

        downrange_km = earth_radius * math.sqrt(
            dlat**2 + (dlon * math.cos(mean_lat))**2
        ) / 1000.0

        print(f"\nDownrange distance: {downrange_km:.1f} km")
        print(f"Average ascent rate: {burnout_altitude/480:.1f} m/s vertical")

    print("\n" + "=" * 60)
    print("Simple Ascent Model:")
    print("  - Linear interpolation between launch and burnout states")
    print("  - Suitable for preliminary mission design")
    print("  - Does not model staging or detailed aerodynamics")
    print("  - Fast computation for trade studies")
    print()
    print("For detailed launch analysis, use the full rocket")
    print("trajectory optimization in the rocket module.")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
Example output:
>>> Computing launch ascent trajectory...
>>> Launch site: Jiuquan (40.9575°N, 100.2912°E)
>>> Launch altitude: 1000.0 m
>>> Burnout conditions:
>>>   Velocity: 7800.0 m/s
>>>   Altitude: 200 km
>>>   Position: (42.50°N, 105.00°E)
>>>
>>> ============================================================
>>> Simple Ascent Trajectory Results
>>> ============================================================
>>> Success: True
>>> Message: Success
>>>
>>> ============================================================
>>> Simple Ascent Model:
>>>   - Linear interpolation between launch and burnout states
>>>   - Suitable for preliminary mission design
>>>   - Does not model staging or detailed aerodynamics
>>>   - Fast computation for trade studies
>>>
>>> For detailed launch analysis, use the full rocket
>>> trajectory optimization in the rocket module.
>>> ============================================================
"""
