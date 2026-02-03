# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Compute access using CzmlPosition for CZML-based position data.

CzmlPosition uses CZML (CZML - Cesium Language) format for position specification,
allowing interpolated position data over time.

API: POST /access/AccessComputeV2
"""

from astrox.access import compute_access
from astrox.models import EntityPath, CzmlPosition, SitePosition


def main():
    # Ground station
    ground_station = EntityPath(
        Name="Ground_Station",
        Position=SitePosition(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[-80.6039, 28.5729, 10.0]
        ),
    )

    # Satellite with CZML position data
    # CZML format: [Time, X, Y, Z, Time, X, Y, Z, ...] where Time is seconds from epoch
    satellite = EntityPath(
        Name="CZML_Satellite",
        Position=CzmlPosition(
            **{'$type': 'CzmlPosition'},
            CentralBody="Earth",
            referenceFrame="INERTIAL",
            interpolationAlgorithm="LAGRANGE",
            interpolationDegree=7,
            epoch="2022-04-25T04:00:00Z",
            cartesian=[
                0.0, 6678137.0, 0.0, 0.0,           # t=0s: position at [X, Y, Z]
                300.0, 6600000.0, 1000000.0, 0.0,   # t=300s
                600.0, 6400000.0, 2000000.0, 0.0,   # t=600s
            ],
        ),
    )

    # Compute access
    result = compute_access(
        start="2022-04-25T04:00:00Z",
        stop="2022-04-25T05:00:00Z",
        from_object=ground_station,
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

        aer_data = interval["AllDatas"]
        print(f"  AER Data Points: {len(aer_data)}")


if __name__ == "__main__":
    main()
