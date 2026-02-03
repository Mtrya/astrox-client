# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Compute access using TwoBodyPosition for the satellite.

TwoBodyPosition uses simple two-body propagation for orbit computation.

API: POST /access/AccessComputeV2
"""

from astrox.access import compute_access
from astrox.models import EntityPath, TwoBodyPosition, SitePosition


def main():
    # Ground station: Cape Canaveral, Florida
    ground_station = EntityPath(
        Name="Cape_Canaveral",
        Position=SitePosition(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[-80.6039, 28.5729, 10.0]  # lon, lat, alt (m)
        ),
    )

    # LEO satellite with TwoBody propagation
    satellite = EntityPath(
        Name="LEO_Satellite",
        Position=TwoBodyPosition(
            **{'$type': 'TwoBody'},
            GravitationalParameter=398600441500000,  # Earth EGM2008
            OrbitEpoch="2022-04-25T04:00:00Z",
            CoordSystem="Inertial",
            CoordType="Classical",
            OrbitalElements=[
                6678137.0,  # Semi-major axis (m) - ~300km altitude
                0.0,        # Eccentricity
                28.5,       # Inclination (deg)
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

        if len(aer_data) > 0:
            first = aer_data[0]
            print(f"    First: Az={first['Azimuth']:.2f}°, El={first['Elevation']:.2f}°")


if __name__ == "__main__":
    main()
