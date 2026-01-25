"""Example: Rocket Guidance Trajectory Calculation

This example demonstrates how to calculate rocket trajectories using
guidance algorithms for various Chinese launch vehicles.
"""

from astrox.rocket import calculate_guidance_trajectory


def main():
    """Calculate rocket trajectory using guidance algorithm.

    This example shows how to use pre-configured guidance algorithms
    for specific rocket types. The ASTROX API supports guidance configs
    for several Chinese launch vehicles:
    - CZ3BC (Long March 3B/C)
    - CZ2CD (Long March 2C/D)
    - CZ4BC (Long March 4B/C)
    - KZ1A (Kuaizhou-1A)
    - CZ7A (Long March 7A)

    Each guidance config is a discriminated union with a $type field.
    """

    print("Calculating rocket trajectory with CZ3BC guidance...")
    print("=" * 70)

    # Example: Long March 3B/C guidance for GTO mission
    # Note: The exact structure depends on the RocketGuid discriminated union
    # For this example, we'll use a simplified structure

    guidance_config = {
        "$type": "CZ3BC",  # Discriminator for Long March 3B/C

        # Mission parameters
        "Name": "GTO Communication Satellite Launch",
        "TargetOrbit": {
            "SMA": 24578137,    # Semi-major axis (m) - GTO
            "Ecc": 0.7305,      # Eccentricity - GTO
            "Inc": 28.5,        # Inclination (deg)
            "RAAN": 0,          # Right ascension (deg)
            "AOP": 178,         # Argument of perigee (deg)
            "TA": 0             # True anomaly (deg)
        },

        # Launch site (Xichang)
        "LaunchSite": {
            "Longitude": 102.0,  # deg
            "Latitude": 28.2,    # deg
            "Altitude": 1820     # m
        },

        # Vehicle configuration
        "PayloadMass": 5500,  # kg
        "LaunchAzimuth": 97.0  # deg - eastward launch
    }

    result = calculate_guidance_trajectory(guidance_config)

    print("\nGuidance Calculation Results:")
    print("-" * 70)

    # Display mission info
    if "Name" in result:
        print(f"Mission: {result['Name']}")

    # Check for trajectory data
    if "Trajectory" in result:
        traj = result["Trajectory"]
        print(f"\nTrajectory computed with {len(traj)} state points")

        # Analyze trajectory phases
        if traj:
            print("\nLiftoff:")
            print(f"  Time: {traj[0].get('Time', 'N/A')} s")
            print(f"  Altitude: {traj[0].get('Altitude', 'N/A')} m")

            # Find MECO (Main Engine Cutoff) - when altitude increases significantly
            meco_point = traj[len(traj) // 3]  # Rough estimate
            print(f"\nApproximate MECO:")
            print(f"  Time: {meco_point.get('Time', 'N/A')} s")
            print(f"  Altitude: {meco_point.get('Altitude', 'N/A')} m")
            print(f"  Velocity: {meco_point.get('Velocity', 'N/A')} m/s")

            # Final orbital insertion
            print(f"\nOrbital Insertion:")
            print(f"  Time: {traj[-1].get('Time', 'N/A')} s")
            print(f"  Altitude: {traj[-1].get('Altitude', 'N/A')} m")
            print(f"  Velocity: {traj[-1].get('Velocity', 'N/A')} m/s")

    # Check for achieved orbit
    if "AchievedOrbit" in result:
        orbit = result["AchievedOrbit"]
        print("\nAchieved Orbit:")
        print(f"  Perigee: {orbit.get('Perigee', 'N/A')} km")
        print(f"  Apogee: {orbit.get('Apogee', 'N/A')} km")
        print(f"  Inclination: {orbit.get('Inclination', 'N/A')} deg")

    # Check for performance metrics
    if "FuelConsumed" in result:
        print(f"\nTotal fuel consumed: {result['FuelConsumed']} kg")

    if "FlightTime" in result:
        print(f"Total flight time: {result['FlightTime']} s")

    # Display full result
    print("\n" + "=" * 70)
    print("Full API Response:")
    print("-" * 70)
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))

    print("\n" + "=" * 70)
    print("Note: Different rocket types (CZ2CD, CZ4BC, KZ1A, CZ7A) may require")
    print("different guidance configuration parameters. Refer to the API")
    print("documentation for each specific rocket type.")


if __name__ == "__main__":
    main()
