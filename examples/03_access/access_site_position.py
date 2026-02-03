# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Compute access using SitePosition for ground station.

This example demonstrates access computation with a ground station entity
using SitePosition (cartographic coordinates) for the ground station location.

API: POST /api/Access/V2
"""

from astrox.access import compute_access
from astrox.models import (
    ConicSensor,
    EntityPath,
    EntityPositionJ2,
    EntityPositionSite,
)


def main():
    # Define analysis time window (24 hours)
    start = "2022-04-25T04:00:00Z"
    stop = "2022-04-26T04:00:00Z"

    # Ground station: Cape Canaveral, Florida
    ground_station = EntityPath(
        Name="Cape_Canaveral",
        Position=EntityPositionSite(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[-80.6039, 28.5729, 10.0]  # lon, lat, alt (m)
        ),
    )

    # LEO satellite with J2 propagation and conic sensor
    satellite = EntityPath(
        Name="LEO_Satellite",
        Position=EntityPositionJ2(
            **{'$type': 'J2'},
            J2NormalizedValue=0.000484165143790815,  # Earth EGM2008
            RefDistance=6378136.3,  # Earth EGM2008 reference radius (m)
            OrbitEpoch="25 Apr 2022 04:00:00.000000",
            CoordSystem="Inertial",
            CoordType="Classical",
            OrbitalElements=[
                6678137.0,  # Semi-major axis (m) - ~300km altitude
                0.0,  # Eccentricity
                28.5,  # Inclination (deg)
                0.0,  # RAAN (deg)
                0.0,  # Argument of perigee (deg)
                0.0,  # True anomaly (deg)
            ],
        ),
        Sensor=ConicSensor(
            **{'$type': 'Conic'},
            Text="Camera",
            outerHalfAngle=30.0,  # 30-degree cone angle
        ),
    )

    print(f"Analysis Period: {start} to {stop}")
    print(f"Ground Station: {ground_station.Name}")
    print(f"  Location: {ground_station.Position.root.cartographicDegrees}")
    print(f"Satellite: {satellite.Name}")
    print(f"  Orbit: LEO (300km altitude, 28.5° inclination)")
    print(f"  Sensor: {satellite.Sensor.root.Text} ({satellite.Sensor.root.outerHalfAngle}° cone)")
    print()

    # Compute access with AER parameters
    print("Computing access windows...")
    result = compute_access(
        start=start,
        stop=stop,
        from_object=ground_station,
        to_object=satellite,
        compute_aer=True,  # Calculate azimuth, elevation, range
        out_step=60.0,  # Output every 60 seconds
    )

    # Display results
    print()
    print("Access Results:")
    print("-" * 70)

    access_intervals = result["Passes"]
    print(f"Total Access Intervals: {len(access_intervals)}")
    print()

    for i, interval in enumerate(access_intervals, 1):
        print(f"Access Window {i}:")
        print(f"  Start: {interval['AccessStart']}")
        print(f"  Stop:  {interval['AccessStop']}")
        print(f"  Duration: {interval['Duration']:.2f} seconds")

        # AccessAER data points (if compute_aer=True)
        aer_data = interval["AllDatas"]
        print(f"  AER Data Points: {len(aer_data)}")

        # Show first and last AER data point
        first = aer_data[0]
        print(f"    First: Time={first['Time']}, "
              f"Az={first['Azimuth']:.2f}°, "
              f"El={first['Elevation']:.2f}°, "
              f"Range={first['Range']/1000:.2f}km")

        if len(aer_data) > 1:
            last = aer_data[-1]
            print(f"    Last:  Time={last['Time']}, "
                  f"Az={last['Azimuth']:.2f}°, "
                  f"El={last['Elevation']:.2f}°, "
                  f"Range={last['Range']/1000:.2f}km")
        print()

    print()
    print("Access computation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
