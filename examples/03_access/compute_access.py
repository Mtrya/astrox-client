"""
Compute access between satellite and ground station.

This example demonstrates satellite-to-ground station access computation
with sensor constraints and AER calculations.

The API returns access windows (passes) with detailed Azimuth, Elevation,
and Range (AER) data for each time step during the access interval.
"""

from astrox.access import compute_access
from astrox.models import (
    ConicSensor,
    EntityPath,
    EntityPositionJ2,
    EntityPositionSite,
)


def main():
    """Compute satellite-to-ground station access with AER data."""
    print("=" * 70)
    print("Access Computation: Satellite to Ground Station")
    print("=" * 70)
    print()

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
    print(f"Ground Station: {ground_station.Name}")  # Name='Cape_Canaveral'
    print(f"  Location: {ground_station.Position.root.cartographicDegrees}")  # [-80.6039, 28.5729, 10.0]
    print(f"Satellite: {satellite.Name}")  # Name='LEO_Satellite'
    print(f"  Orbit: LEO (300km altitude, 28.5° inclination)")
    if satellite.Sensor:
        print(f"  Sensor: {satellite.Sensor.root.Text} ({satellite.Sensor.root.outerHalfAngle}° cone)")  # Text='Camera', outerHalfAngle=30.0
    print()

    # Compute access with AER parameters
    print("Computing access windows...")
    # The API returns access passes with AER data (azimuth, elevation, range)
    # Endpoint: POST /access/AccessComputeV2
    result = compute_access(
        start=start,
        stop=stop,
        from_object=ground_station,
        to_object=satellite,
        compute_aer=True,  # Calculate azimuth, elevation, range
        out_step=60.0,  # Output every 60 seconds
    )

    # Display results
    # Based on actual API response: {'Passes': [{'AccessStart': str, 'AccessStop': str, 'Duration': float, 'AllDatas': [...]}, ...]}
    print()
    print("Access Results:")
    print("-" * 70)

    access_intervals = result["Passes"]
    print(f"Total Access Intervals: {len(access_intervals)}")  # e.g., 1
    print()

    for i, interval in enumerate(access_intervals, 1):
        print(f"Access Window {i}:")
        print(f"  Start: {interval['AccessStart']}")  # e.g., '2022-04-25T16:07:55.725Z'
        print(f"  Stop:  {interval['AccessStop']}")   # e.g., '2022-04-25T16:07:59.021Z'
        print(f"  Duration: {interval['Duration']:.2f} seconds")  # e.g., 3.30

        # AccessAER data points (if compute_aer=True)
        aer_data = interval["AllDatas"]
        print(f"  AER Data Points: {len(aer_data)}")  # e.g., 2

        # Show first and last AER data point
        first = aer_data[0]
        print(f"    First: Time={first['Time']}, "
              f"Az={first['Azimuth']:.2f}°, "     # e.g., 170.66°
              f"El={first['Elevation']:.2f}°, "   # e.g., -0.10°
              f"Range={first['Range']/1000:.2f}km")  # e.g., 1988.29km

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

