"""Example: Ballistic Trajectory Propagation

This example demonstrates ballistic trajectory calculation for suborbital
flights, such as:
- Intercontinental ballistic missiles (ICBMs)
- Sounding rockets
- Suborbital space tourism flights
- Artillery trajectories

We'll compute a ballistic trajectory from Cape Canaveral to a downrange
impact point in the Atlantic Ocean.
"""

from astrox.propagator import propagate_ballistic


def main():
    # Launch site: Cape Canaveral, Florida
    launch_lat = 28.5721  # degrees North
    launch_lon = -80.6480  # degrees West
    launch_alt = 10.0  # meters above sea level

    # Impact point: Downrange in Atlantic Ocean
    # Approximately 1000 km downrange
    impact_lat = 30.0  # degrees North
    impact_lon = -70.0  # degrees West
    impact_alt = 0.0  # sea level

    print("Computing ballistic trajectory...")
    print(f"Launch: ({launch_lat:.4f}°, {launch_lon:.4f}°) at {launch_alt} m")
    print(f"Impact: ({impact_lat:.4f}°, {impact_lon:.4f}°) at {impact_alt} m")
    print()

    # Compute trajectory with specified apogee altitude
    # This is a medium-range ballistic trajectory
    result = propagate_ballistic(
        start="2024-01-01T12:00:00.000Z",
        impact_latitude=impact_lat,
        impact_longitude=impact_lon,
        launch_latitude=launch_lat,
        launch_longitude=launch_lon,
        launch_altitude=launch_alt,
        impact_altitude=impact_alt,
        # Specify trajectory by apogee altitude
        ballistic_type="ApogeeAlt",
        ballistic_type_value=200000.0,  # 200 km apogee (suborbital)
        step=5.0,  # 5-second steps for detailed trajectory
    )

    # Print results
    print("=" * 60)
    print("Ballistic Trajectory Results")
    print("=" * 60)
    print(f"Success: {result.get('IsSuccess', 'N/A')}")
    print(f"Message: {result.get('Message', 'N/A')}")

    if 'CzmlPositions' in result:
        positions = result['CzmlPositions']
        num_points = len(positions) // 3
        print(f"\nGenerated {num_points} position points")

        # Calculate trajectory parameters
        if num_points > 0:
            # Find apogee (highest point)
            max_altitude = 0
            earth_radius = 6378137.0

            for i in range(num_points):
                idx = i * 3
                if idx + 2 < len(positions):
                    x, y, z = positions[idx:idx+3]
                    r = (x**2 + y**2 + z**2) ** 0.5
                    altitude = r - earth_radius
                    if altitude > max_altitude:
                        max_altitude = altitude

            # Time of flight
            duration_seconds = (num_points - 1) * 5.0  # 5-second steps
            duration_minutes = duration_seconds / 60.0

            print(f"\nTrajectory Parameters:")
            print(f"  Apogee altitude: {max_altitude/1000:.1f} km")
            print(f"  Time of flight: {duration_minutes:.2f} minutes ({duration_seconds:.0f} seconds)")
            print(f"  Step size: 5 seconds")

            # Calculate ground range (approximate)
            # This is a simplified calculation
            import math
            dlat = abs(impact_lat - launch_lat)
            dlon = abs(impact_lon - launch_lon)
            # Great circle distance approximation
            ground_range = earth_radius * math.sqrt(
                (dlat * math.pi/180)**2 +
                (dlon * math.pi/180 * math.cos(launch_lat * math.pi/180))**2
            )

            print(f"  Ground range: {ground_range/1000:.1f} km")
            print(f"  Average velocity: {ground_range/duration_seconds:.0f} m/s")

    print("\n" + "=" * 60)
    print("Ballistic Trajectory Types:")
    print("  - DeltaV: Specify initial velocity magnitude")
    print("  - DeltaV_MinEcc: Minimum eccentricity trajectory")
    print("  - ApogeeAlt: Specify maximum altitude (used here)")
    print("  - TimeOfFlight: Specify flight duration")
    print()
    print("Applications:")
    print("  - Suborbital space tourism (Blue Origin, Virgin Galactic)")
    print("  - Sounding rockets for atmospheric research")
    print("  - First stage recovery impact prediction")
    print("  - Military trajectory analysis")
    print("=" * 60)


if __name__ == "__main__":
    main()
