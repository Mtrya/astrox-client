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
    print(f"Ground Station: {ground_station.Name}")
    print(f"  Location: {ground_station.Position.root.cartographicDegrees}")
    print(f"Satellite: {satellite.Name}")
    print(f"  Orbit: LEO (300km altitude, 28.5° inclination)")
    if satellite.Sensor:
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

    if "Passes" in result and result["Passes"]:
        access_intervals = result["Passes"]
        print(f"Total Access Intervals: {len(access_intervals)}")
        print()

        for i, interval in enumerate(access_intervals, 1):
            print(f"Access Window {i}:")
            print(f"  Start: {interval.get('AccessStart')}")
            print(f"  Stop:  {interval.get('AccessStop')}")
            print(f"  Duration: {interval.get('Duration', 0):.2f} seconds")

            # AccessAER data points (if compute_aer=True)
            if "AllDatas" in interval and interval["AllDatas"]:
                aer_data = interval["AllDatas"]
                print(f"  AER Data Points: {len(aer_data)}")

                # Show first and last AER data point
                first = aer_data[0]
                print(f"    First: Time={first.get('Time', 'N/A')}, "
                      f"Az={first.get('Azimuth', 0):.2f}°, "
                      f"El={first.get('Elevation', 0):.2f}°, "
                      f"Range={first.get('Range', 0)/1000:.2f}km")

                if len(aer_data) > 1:
                    last = aer_data[-1]
                    print(f"    Last:  Time={last.get('Time', 'N/A')}, "
                          f"Az={last.get('Azimuth', 0):.2f}°, "
                          f"El={last.get('Elevation', 0):.2f}°, "
                          f"Range={last.get('Range', 0)/1000:.2f}km")
            elif "MinElevationData" in interval and interval["MinElevationData"]:
                # Summary data available even without AllDatas
                min_el = interval["MinElevationData"]
                max_el = interval["MaxElevationData"] if "MaxElevationData" in interval else None
                print(f"  Elevation: Min={min_el.get('Elevation', 0):.2f}° at {min_el.get('Time', 'N/A')}")
                if max_el:
                    print(f"            Max={max_el.get('Elevation', 0):.2f}° at {max_el.get('Time', 'N/A')}")
            print()
    else:
        print("No access windows found during the analysis period.")

    print()
    print("Access computation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()

"""
>>> ======================================================================
>>> Access Computation: Satellite to Ground Station
>>> ======================================================================
>>>
>>> Analysis Period: 2022-04-25T04:00:00Z to 2022-04-26T04:00:00Z
>>> Ground Station: Cape_Canaveral
>>>   Location: [-80.6039, 28.5729, 10.0]
>>> Satellite: LEO_Satellite
>>>   Orbit: LEO (300km altitude, 28.5° inclination)
>>>   Sensor: Camera (30.0° cone)
>>>
>>> Computing access windows...
>>>
>>> Access Results:
>>> ----------------------------------------------------------------------
>>> No access windows found during the analysis period.
>>>
>>> Access computation completed successfully!
>>> ======================================================================
"""
