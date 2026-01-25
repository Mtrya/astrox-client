"""
Compute access between satellite and ground station.

This example demonstrates satellite-to-ground station access computation
with sensor constraints and AER calculations.
"""

from astrox.access import compute_access
from astrox.models import (
    ConicSensor,
    EntityPath,
    EntityPositionJ2,
    EntityPositionSite,
)


def main():
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
            cartographicDegrees=[-80.6039, 28.5729, 10.0]  # lon, lat, alt (m)
        ),
    )

    # LEO satellite with J2 propagation and conic sensor
    satellite = EntityPath(
        Name="LEO_Satellite",
        Position=EntityPositionJ2(
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
        Sensors=[
            ConicSensor(
                Name="Camera",
                HalfAngle=30.0,  # 30-degree cone angle
            )
        ],
    )

    print(f"Analysis Period: {start} to {stop}")
    print(f"Ground Station: {ground_station.Name}")
    print(f"  Location: {ground_station.Position.cartographicDegrees}")
    print(f"Satellite: {satellite.Name}")
    print(f"  Orbit: LEO (300km altitude, 28.5° inclination)")
    print(f"  Sensor: {satellite.Sensors[0].Name} ({satellite.Sensors[0].HalfAngle}° cone)")
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

    if "AccessData" in result and result["AccessData"]:
        access_intervals = result["AccessData"]
        print(f"Total Access Intervals: {len(access_intervals)}")
        print()

        for i, interval in enumerate(access_intervals, 1):
            print(f"Access Window {i}:")
            print(f"  Start: {interval.get('Start')}")
            print(f"  Stop:  {interval.get('Stop')}")
            print(f"  Duration: {interval.get('Duration', 0):.2f} seconds")

            if "AccessAER" in interval and interval["AccessAER"]:
                aer_data = interval["AccessAER"]
                print(f"  AER Data Points: {len(aer_data)}")

                # Show first and last AER data point
                first = aer_data[0]
                print(f"    First: Az={first.get('Azimuth', 0):.2f}°, "
                      f"El={first.get('Elevation', 0):.2f}°, "
                      f"Range={first.get('Range', 0)/1000:.2f}km")

                if len(aer_data) > 1:
                    last = aer_data[-1]
                    print(f"    Last:  Az={last.get('Azimuth', 0):.2f}°, "
                          f"El={last.get('Elevation', 0):.2f}°, "
                          f"Range={last.get('Range', 0)/1000:.2f}km")
            print()
    else:
        print("No access windows found during the analysis period.")

    print()
    print("Access computation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
