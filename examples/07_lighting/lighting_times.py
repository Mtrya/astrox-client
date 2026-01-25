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
        OrbitEpoch="20 Mar 2024 00:00:00.000000",
        CoordSystem="Inertial",
        CoordType="Classical",
        OrbitalElements=[
            42164137.0,  # Semi-major axis (m) - GEO altitude
            0.0001,  # Eccentricity (near-circular)
            0.1,  # Inclination (deg) - near-equatorial
            0.0,  # RAAN (deg)
            0.0,  # Argument of perigee (deg)
            0.0,  # True anomaly (deg)
        ],
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

    # Process sunlight intervals
    if "SunLight" in result and result["SunLight"]:
        sunlight = result["SunLight"]
        print()
        print(f"SUNLIGHT INTERVALS ({len(sunlight)} periods):")
        print("-" * 70)

        total_sunlight = 0.0
        for i, interval in enumerate(sunlight, 1):
            start_time = interval.get("Start", "N/A")
            stop_time = interval.get("Stop", "N/A")
            duration = interval.get("Duration", 0.0)
            total_sunlight += duration

            print(f"  Period {i}:")
            print(f"    Start:    {start_time}")
            print(f"    Stop:     {stop_time}")
            print(f"    Duration: {duration/3600:.2f} hours")

        print(f"\n  Total Sunlight: {total_sunlight/3600:.2f} hours "
              f"({100*total_sunlight/86400:.1f}% of day)")

    # Process penumbra intervals
    if "Penumbra" in result and result["Penumbra"]:
        penumbra = result["Penumbra"]
        print()
        print(f"PENUMBRA INTERVALS ({len(penumbra)} periods):")
        print("-" * 70)

        total_penumbra = 0.0
        for i, interval in enumerate(penumbra, 1):
            start_time = interval.get("Start", "N/A")
            stop_time = interval.get("Stop", "N/A")
            duration = interval.get("Duration", 0.0)
            total_penumbra += duration

            print(f"  Period {i}:")
            print(f"    Start:    {start_time}")
            print(f"    Stop:     {stop_time}")
            print(f"    Duration: {duration:.1f} seconds ({duration/60:.2f} minutes)")

        print(f"\n  Total Penumbra: {total_penumbra/60:.2f} minutes "
              f"({100*total_penumbra/86400:.1f}% of day)")

    # Process umbra intervals
    if "Umbra" in result and result["Umbra"]:
        umbra = result["Umbra"]
        print()
        print(f"UMBRA INTERVALS ({len(umbra)} periods):")
        print("-" * 70)

        total_umbra = 0.0
        for i, interval in enumerate(umbra, 1):
            start_time = interval.get("Start", "N/A")
            stop_time = interval.get("Stop", "N/A")
            duration = interval.get("Duration", 0.0)
            total_umbra += duration

            print(f"  Period {i}:")
            print(f"    Start:    {start_time}")
            print(f"    Stop:     {stop_time}")
            print(f"    Duration: {duration/60:.2f} minutes")

        print(f"\n  Total Umbra: {total_umbra/60:.2f} minutes "
              f"({100*total_umbra/86400:.1f}% of day)")

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
