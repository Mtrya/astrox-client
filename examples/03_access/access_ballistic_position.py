# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Compute access using BallisticPosition for a ballistic trajectory.

BallisticPosition represents a ballistic (sub-orbital) trajectory,
useful for missile or rocket ascent/descent analysis.

API: POST /access/AccessComputeV2
"""

from astrox.access import compute_access
from astrox._models import IEntityPositionEntityPositionBallistic
from astrox.models import EntityPath, SitePosition


def main():
    # Ground station
    ground_station = EntityPath(
        Name="Tracking_Station",
        Position=SitePosition(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[-80.6039, 28.5729, 10.0]
        ),
    )

    # Ballistic missile trajectory
    ballistic_vehicle = EntityPath(
        Name="Ballistic_Missile",
        Position=IEntityPositionEntityPositionBallistic(
            **{'$type': 'Ballistic'},
            Start="2022-04-25T04:00:00Z",
            CentralBody="Earth",
            GravitationalParameter=398600441500000,
            LaunchLatitude=28.5729,     # Cape Canaveral lat
            LaunchLongitude=-80.6039,   # Cape Canaveral lon
            LaunchAltitude=10.0,
            BallisticType="DeltaV",
            BallisticTypeValue=6901.943,  # m/s
            ImpactLatitude=35.0,
            ImpactLongitude=120.0,
            ImpactAltitude=0.0,
        ),
    )

    # Compute access
    result = compute_access(
        start="2022-04-25T04:00:00Z",
        stop="2022-04-25T06:00:00Z",
        from_object=ground_station,
        to_object=ballistic_vehicle,
        compute_aer=True,
        out_step=30.0,
    )

    # Output
    print(f"Success: {result['IsSuccess']}")
    print(f"Total Passes: {len(result['Passes'])}")

    for i, interval in enumerate(result['Passes'], 1):
        print(f"\nAccess Window {i}:")
        print(f"  Start: {interval['AccessStart']}")
        print(f"  Stop: {interval['AccessStop']}")
        print(f"  Duration: {interval['Duration']:.2f} seconds")

        aer_data = interval["AllDatas"]
        print(f"  AER Data Points: {len(aer_data)}")


if __name__ == "__main__":
    main()
