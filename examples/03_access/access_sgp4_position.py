# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Compute access using SGP4Position for TLE-based orbit propagation.

SGP4Position uses Two-Line Elements (TLE) for satellite orbit specification
and SGP4/SDP4 propagation algorithm.

API: POST /access/AccessComputeV2
"""

from astrox.access import compute_access
from astrox.models import EntityPath, SGP4Position, SitePosition


def main():
    # Ground station
    ground_station = EntityPath(
        Name="Ground_Station",
        Position=SitePosition(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[-80.6039, 28.5729, 10.0]
        ),
    )

    # ISS TLE (Two-Line Elements) - example data
    # In production, obtain current TLE from space-track.org or celestrak.com
    iss_tle_line1 = "1 25544U 98067A   22115.12345678  .00012345  00000-0  23456-3 0  9999"
    iss_tle_line2 = "2 25544  51.6416  45.1234 0004567  45.1234  89.8765 15.50012345678901"

    # ISS satellite using SGP4 propagation with TLE
    satellite = EntityPath(
        Name="ISS",
        Position=SGP4Position(
            **{'$type': 'SGP4'},
            SatelliteNumber="25544",
            TLEs=[iss_tle_line1, iss_tle_line2],
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
            last = aer_data[-1]
            print(f"    First: Az={first['Azimuth']:.2f}°, El={first['Elevation']:.2f}°")
            print(f"    Last:  Az={last['Azimuth']:.2f}°, El={last['Elevation']:.2f}°")


if __name__ == "__main__":
    main()
