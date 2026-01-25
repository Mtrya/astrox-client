"""
Calculate lighting time intervals (sunlight, penumbra, umbra).

This example demonstrates calculation of lighting time windows
for a spacecraft or ground station, useful for mission planning
and solar panel power generation analysis.
"""

from astrox.lighting import lighting_times
from astrox.models import EntityPositionJ2


def main():
    print("=" * 70)
    print("Lighting Time Intervals for GEO Satellite")
    print("=" * 70)
    print()

    # Define analysis time window (24 hours around equinox)
    start = "2024-03-20T00:00:00Z"
    stop = "2024-03-21T00:00:00Z"

    # GEO satellite (geostationary orbit)
    spacecraft = EntityPositionJ2(
        **{
            "$type": "J2",
            "OrbitEpoch": "20 Mar 2024 00:00:00.000000",
            "CoordSystem": "Inertial",
            "CoordType": "Classical",
            "J2NormalizedValue": 0.000484165143790815,  # Earth J2 (EGM2008)
            "RefDistance": 6378136.3,  # Earth equatorial radius (m, EGM2008)
            "OrbitalElements": [
                42164137.0,  # Semi-major axis (m) - GEO altitude
                0.0001,  # Eccentricity (near-circular)
                0.1,  # Inclination (deg) - near-equatorial
                0.0,  # RAAN (deg)
                0.0,  # Argument of perigee (deg)
                0.0,  # True anomaly (deg)
            ],
        }
    )

    print(f"Analysis Period: {start} to {stop}")
    print("Spacecraft Orbit:")
    print(f"  Type: Geostationary (GEO)")
    print(f"  Altitude: ~35,786 km")
    print(f"  Inclination: 0.1°")
    print(f"  Analysis Date: March 20 (Spring Equinox)")
    print()

    # Calculate lighting times
    print("Calculating lighting time intervals...")
    result = lighting_times(
        start=start,
        stop=stop,
        position=spacecraft,
        occultation_bodies=["Earth"],  # Earth is the occulting body
        description="GEO satellite lighting analysis",
    )

    # Display results
    print()
    print("Lighting Time Intervals:")
    print("-" * 70)

    # Check if request was successful
    if not result.get("IsSuccess", False):
        print(f"Error: {result.get('Message', 'Unknown error')}")
        return

    # Process sunlight intervals
    if "SunLight" in result and result["SunLight"]:
        sunlight = result["SunLight"]
        if "Intervals" in sunlight and sunlight["Intervals"]:
            intervals = sunlight["Intervals"]
            print()
            print(f"SUNLIGHT INTERVALS ({len(intervals)} periods):")
            print("-" * 70)

            total_sunlight = 0.0
            for i, interval in enumerate(intervals, 1):
                if isinstance(interval, dict):
                    start_time = interval.get("Start", "N/A")
                    stop_time = interval.get("Stop", "N/A")
                    duration = interval.get("Duration", 0.0)
                    total_sunlight += duration

                    print(f"  Period {i}:")
                    print(f"    Start:    {start_time}")
                    print(f"    Stop:     {stop_time}")
                    print(f"    Duration: {duration/3600:.2f} hours")
                else:
                    print(f"  Period {i}: {interval} (not a dict)")

            print(f"\n  Total Sunlight: {total_sunlight/3600:.2f} hours "
                  f"({100*total_sunlight/86400:.1f}% of day)")

            # Show statistics if available
            if "MinDuration" in sunlight:
                min_dur = sunlight["MinDuration"].get("Duration", 0)
                print(f"  Minimum Duration: {min_dur/3600:.2f} hours")
            if "MaxDuration" in sunlight:
                max_dur = sunlight["MaxDuration"].get("Duration", 0)
                print(f"  Maximum Duration: {max_dur/3600:.2f} hours")
            if "MeanDuration" in sunlight:
                print(f"  Mean Duration: {sunlight['MeanDuration']/3600:.2f} hours")
        else:
            print("\nNo sunlight intervals found.")

    # Process penumbra intervals
    if "Penumbra" in result and result["Penumbra"]:
        penumbra = result["Penumbra"]
        if isinstance(penumbra, list) and penumbra:
            print()
            print(f"PENUMBRA INTERVALS ({len(penumbra)} periods):")
            print("-" * 70)

            total_penumbra = 0.0
            for i, interval in enumerate(penumbra, 1):
                if isinstance(interval, dict):
                    start_time = interval.get("Start", "N/A")
                    stop_time = interval.get("Stop", "N/A")
                    duration = interval.get("Duration", 0.0)
                    total_penumbra += duration

                    print(f"  Period {i}:")
                    print(f"    Start:    {start_time}")
                    print(f"    Stop:     {stop_time}")
                    print(f"    Duration: {duration:.1f} seconds ({duration/60:.2f} minutes)")
                else:
                    print(f"  Period {i}: {interval}")

            print(f"\n  Total Penumbra: {total_penumbra/60:.2f} minutes "
                  f"({100*total_penumbra/86400:.1f}% of day)")
        else:
            print("\nNo penumbra intervals found.")

    # Process umbra intervals
    if "Umbra" in result and result["Umbra"]:
        umbra = result["Umbra"]
        if isinstance(umbra, list) and umbra:
            print()
            print(f"UMBRA INTERVALS ({len(umbra)} periods):")
            print("-" * 70)

            total_umbra = 0.0
            for i, interval in enumerate(umbra, 1):
                if isinstance(interval, dict):
                    start_time = interval.get("Start", "N/A")
                    stop_time = interval.get("Stop", "N/A")
                    duration = interval.get("Duration", 0.0)
                    total_umbra += duration

                    print(f"  Period {i}:")
                    print(f"    Start:    {start_time}")
                    print(f"    Stop:     {stop_time}")
                    print(f"    Duration: {duration/60:.2f} minutes")
                else:
                    print(f"  Period {i}: {interval}")

            print(f"\n  Total Umbra: {total_umbra/60:.2f} minutes "
                  f"({100*total_umbra/86400:.1f}% of day)")
        else:
            print("\nNo umbra intervals found.")

    # Summary
    print()
    print("Summary:")
    print("-" * 70)
    print("GEO satellites experience eclipse seasons around equinoxes")
    print("when Earth blocks sunlight. This analysis shows:")
    print("  - Maximum eclipse duration at GEO: ~70 minutes")
    print("  - Eclipse season duration: ~45 days around each equinox")
    print()
    print("Applications:")
    print("  - Solar panel power generation planning")
    print("  - Battery capacity sizing")
    print("  - Thermal control system design")
    print("  - Mission operations scheduling")

    print()
    print("Lighting time calculation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()

    # Example output:
    # >>> ======================================================================
    # >>> Lighting Time Intervals for GEO Satellite
    # >>> ======================================================================
    # >>>
    # >>> Analysis Period: 2024-03-20T00:00:00Z to 2024-03-21T00:00:00Z
    # >>> Spacecraft Orbit:
    # >>>   Type: Geostationary (GEO)
    # >>>   Altitude: ~35,786 km
    # >>>   Inclination: 0.1°
    # >>>   Analysis Date: March 20 (Spring Equinox)
    # >>>
    # >>> Calculating lighting time intervals...
    # >>>
    # >>> Lighting Time Intervals:
    # >>> ----------------------------------------------------------------------
    # >>>
    # >>> SUNLIGHT INTERVALS (2 periods):
    # >>> ----------------------------------------------------------------------
    # >>>   Period 1:
    # >>>     Start:    2024-03-20T00:00:00.000Z
    # >>>     Stop:     2024-03-20T11:22:14.069Z
    # >>>     Duration: 11.37 hours
    # >>>   Period 2:
    # >>>     Start:    2024-03-20T12:33:59.119Z
    # >>>     Stop:     2024-03-21T00:00:00.000Z
    # >>>     Duration: 11.43 hours
    # >>>
    # >>>   Total Sunlight: 22.80 hours (95.0% of day)
    # >>>   Minimum Duration: 11.37 hours
    # >>>   Maximum Duration: 11.43 hours
    # >>>   Mean Duration: 11.40 hours
    # >>>
    # >>> No penumbra intervals found.
    # >>>
    # >>> No umbra intervals found.
    # >>>
    # >>> Summary:
    # >>> ----------------------------------------------------------------------
    # >>> GEO satellites experience eclipse seasons around equinoxes
    # >>> when Earth blocks sunlight. This analysis shows:
    # >>>   - Maximum eclipse duration at GEO: ~70 minutes
    # >>>   - Eclipse season duration: ~45 days around each equinox
    # >>>
    # >>> Applications:
    # >>>   - Solar panel power generation planning
    # >>>   - Battery capacity sizing
    # >>>   - Thermal control system design
    # >>>   - Mission operations scheduling
    # >>>
    # >>> Lighting time calculation completed successfully!
    # >>> ======================================================================
