"""Example: Rocket Vertical Landing Trajectory Optimization

This example demonstrates how to optimize a rocket vertical landing trajectory
using a 4-segment model with aerodynamics for powered descent landing.
"""

from astrox.rocket import optimize_descent_trajectory


def main():
    """Optimize rocket descent trajectory for vertical landing.

    This example simulates a reusable rocket first stage returning for
    a powered landing, similar to SpaceX Falcon 9 or Blue Origin New Shepard.

    The 4-segment model includes:
    1. Initial segment: Attitude adjustment after stage separation
    2. Turn segment: Boost-back burn to reverse trajectory
    3. Descent segment: Atmospheric re-entry and deceleration
    4. Landing segment: Final powered descent and touchdown
    """

    print("Optimizing rocket vertical landing trajectory...")
    print("=" * 70)

    # Example: First stage landing after suborbital flight
    # Launch site: Cape Canaveral (28.5°N, 80.6°W)
    result = optimize_descent_trajectory(
        name="Falcon 9 First Stage Landing",
        text="Vertical landing trajectory optimization for reusable booster",
        is_optimize=True,

        # Launch site coordinates (Cape Canaveral)
        fa_she_dian_lla=[-80.6, 28.5, 0],  # [lon(deg), lat(deg), alt(m)]
        a0=90.0,  # Launch azimuth (deg) - due east

        # Initial segment (after stage separation at ~80km altitude)
        t0=180.0,  # Time since launch (s)
        x0=[
            # Position in launch inertial frame (m)
            100000, 50000, 80000,
            # Velocity in launch inertial frame (m/s)
            2000, 100, -50,
            # Mass (kg)
            25000
        ],
        phicx0=-45.0,  # Initial pitch angle (deg) - pointing downward
        psicx0=0.0,    # Initial yaw angle (deg)
        sm=15.0,       # Aerodynamic reference area (m²)

        # Segment 1: Attitude adjustment (flip maneuver)
        dt1=10.0,  # Duration (s)

        # Segment 2: Boost-back burn
        phicx20=45.0,   # Turn segment initial pitch angle (deg)
        psicx20=180.0,  # Turn segment initial yaw angle (deg) - reverse direction
        dt2=30.0,       # Working duration (s)
        force2=845000,  # Vacuum thrust (N) - 3 engines
        ips2=3050,      # Vacuum specific impulse (m/s) - RP1/LOX

        # Segment 4: Final landing burn
        height4=2.0,    # Initial height for landing segment (km)
        force4=425000,  # Sea-level thrust (N) - 1 engine
        ips4=2900,      # Sea-level specific impulse (m/s)
        sa4=0.8,        # Engine nozzle area (m²)
        cons_h=0.0,     # Landing point height (km) - sea level
    )

    print("\nOptimization Results:")
    print("-" * 70)

    # Display key results
    if "Name" in result:
        print(f"Mission: {result['Name']}")

    # Check for trajectory data
    if "Trajectory" in result:
        traj = result["Trajectory"]
        print(f"\nTrajectory computed with {len(traj)} points")

        # Show first and last points
        if traj:
            print("\nInitial state:")
            print(f"  Time: {traj[0].get('Time', 'N/A')} s")
            print(f"  Altitude: {traj[0].get('Altitude', 'N/A')} m")
            print(f"  Velocity: {traj[0].get('Velocity', 'N/A')} m/s")

            print("\nFinal state (landing):")
            print(f"  Time: {traj[-1].get('Time', 'N/A')} s")
            print(f"  Altitude: {traj[-1].get('Altitude', 'N/A')} m")
            print(f"  Velocity: {traj[-1].get('Velocity', 'N/A')} m/s")

    # Check for performance metrics
    if "FuelConsumed" in result:
        print(f"\nFuel consumed: {result['FuelConsumed']} kg")

    if "MaxDynamicPressure" in result:
        print(f"Max dynamic pressure: {result['MaxDynamicPressure']} Pa")

    if "LandingAccuracy" in result:
        print(f"Landing accuracy: {result['LandingAccuracy']} m")

    # Display full result for debugging
    print("\n" + "=" * 70)
    print("Full API Response:")
    print("-" * 70)
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
