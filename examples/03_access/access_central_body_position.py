# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Compute access using CentralBodyPosition for a fixed central body point.

CentralBodyPosition represents a point fixed to a central body (e.g., Earth).
This is useful for ground stations or fixed surface points.

API: POST /access/AccessComputeV2
"""

from astrox.access import compute_access
from astrox.models import EntityPath, CentralBodyPosition, TwoBodyPosition


def main():
    # Fixed point on Earth's surface using CentralBodyPosition
    ground_point = EntityPath(
        Name="Beijing_Ground",
        Position=CentralBodyPosition(
            **{'$type': 'CentralBody'},
            Name="Earth",
        ),
    )

    # LEO satellite with TwoBody propagation
    satellite = EntityPath(
        Name="LEO_Satellite",
        Position=TwoBodyPosition(
            **{'$type': 'TwoBody'},
            GravitationalParameter=398600441500000,
            OrbitEpoch="2022-04-25T04:00:00Z",
            CoordSystem="Inertial",
            CoordType="Classical",
            OrbitalElements=[
                6678137.0,  # Semi-major axis (m)
                0.0,        # Eccentricity
                45.0,       # Inclination (deg)
                0.0,        # RAAN (deg)
                0.0,        # Argument of perigee (deg)
                0.0,        # True anomaly (deg)
            ],
        ),
    )

    # Compute access
    result = compute_access(
        start="2022-04-25T04:00:00Z",
        stop="2022-04-26T04:00:00Z",
        from_object=ground_point,
        to_object=satellite,
        compute_aer=True,
        out_step=60.0,
    )

    # Output
    print(f"Success: {result['IsSuccess']}")
    print(f"Total Passes: {len(result['Passes'])}")

    for i, interval in enumerate(result['Passes'], 1):
        print(f"\nAccess Window {i}:")
        print(f"  Start: {interval['AccessStart']}")
        print(f"  Stop: {interval['AccessStop']}")
        print(f"  Duration: {interval['Duration']:.2f} seconds")


if __name__ == "__main__":
    main()
