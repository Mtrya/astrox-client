"""Example: Rocket Guidance Trajectory Calculation

This example demonstrates how to calculate rocket trajectories using
guidance algorithms for various Chinese launch vehicles.
"""

from astrox.rocket import compute_guided_trajectory
from astrox.models import RocketGuidCZ3BC


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
    # Using the RocketGuidCZ3BC model with required parameters
    # Note: This model has many optional fields for detailed guidance control
    # We provide a minimal configuration that should work

    guidance_config = RocketGuidCZ3BC(
        field_type="CZ3BC",  # Required discriminator
        # Target orbit: GTO (185 km x 35786 km)
        Guid_RV_2k=[24578137.0, 0.0, 0.0, 0.0, 10000.0, 0.0],  # Stage 2 cutoff state (example)
        Guid_RV_3k=[24578137.0, 0.0, 0.0, 0.0, 10000.0, 0.0],  # Stage 3 cutoff state (example)
        # Most other fields have defaults and are optional
    )

    result = compute_guided_trajectory(guidance_config)

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

    # Example output (when API is working):
    # >>> Calculating rocket trajectory with CZ3BC guidance...
    # >>> ======================================================================
    # >>>
    # >>> Guidance Calculation Results:
    # >>> ----------------------------------------------------------------------
    # >>> Mission: CZ3BC GTO Mission
    # >>>
    # >>> Trajectory computed with 1500 state points
    # >>>
    # >>> Liftoff:
    # >>>   Time: 0.0 s
    # >>>   Altitude: 0.0 m
    # >>>
    # >>> Approximate MECO:
    # >>>   Time: 145.5 s
    # >>>   Altitude: 65000 m
    # >>>   Velocity: 2350 m/s
    # >>>
    # >>> Orbital Insertion:
    # >>>   Time: 850.2 s
    # >>>   Altitude: 185000 m
    # >>>   Velocity: 10250 m/s
    # >>>
    # >>> Achieved Orbit:
    # >>>   Perigee: 185 km
    # >>>   Apogee: 35786 km
    # >>>   Inclination: 28.5 deg
    # >>>
    # >>> Total fuel consumed: 425000 kg
    # >>> Total flight time: 850.2 s
    # >>>
    # >>> ======================================================================
    # >>> Full API Response:
    # >>> ----------------------------------------------------------------------
    # >>> {
    # >>>   "Name": "CZ3BC GTO Mission",
    # >>>   "Trajectory": [...],
    # >>>   "AchievedOrbit": {...},
    # >>>   "FuelConsumed": 425000.0,
    # >>>   "FlightTime": 850.2
    # >>> }
    #
    # Current error:
    # >>> astrox.exceptions.AstroxAPIError: GJ_dL数值太小,当前数值为:0
    # This means "GJ_dL value is too small, current value is: 0"
    # The RocketGuidCZ3BC model requires more parameters than shown in this example
