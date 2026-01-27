from astrox.lighting import solar_aer
from astrox.models import EntityPositionSite


def main():
    print("=" * 70)
    print("Solar AER (Azimuth-Elevation-Range) from Ground Station")
    print("=" * 70)
    print()

    # Define analysis time window (sunrise to sunset)
    start = "2024-06-21T04:00:00Z"  # Summer solstice
    stop = "2024-06-21T20:00:00Z"

    # Ground station: Beijing, China
    ground_station = EntityPositionSite.model_construct(
        **{
            "$type": "SitePosition",
            "cartographicDegrees": [
                116.3974,  # Longitude (deg E)
                39.9087,  # Latitude (deg N)
                50.0,  # Altitude (m)
            ]
        }
    )

    print(f"Analysis Date: June 21, 2024 (Summer Solstice)")
    print(f"Ground Station: Beijing, China")
    print(f"  Longitude: {ground_station.cartographicDegrees[0]:.4f}° E")
    print(f"  Latitude:  {ground_station.cartographicDegrees[1]:.4f}° N")
    print(f"  Altitude:  {ground_station.cartographicDegrees[2]:.1f} m")
    print()
    print(f"Analysis Period: {start} to {stop}")
    print()

    # Calculate solar AER
    print("Calculating solar position (AER) throughout the day...")
    result = solar_aer(
        start=start,
        stop=stop,
        site_position=ground_station,
        time_step_sec=600,  # Sample every 10 minutes
        text="Beijing summer solstice solar AER",
    )

    # Display results
    print()
    print("Solar Position Results:")
    print("-" * 70)

    if "Datas" in result and result["Datas"]:
        aer_data = result["Datas"]
        print(f"Total Data Points: {len(aer_data)}")
        print()

        # Find key solar events
        max_elevation_point = max(aer_data, key=lambda x: x.get("Elevation", -90))
        max_elevation = max_elevation_point.get("Elevation", 0)
        solar_noon_time = max_elevation_point.get("Time", "N/A")

        # Find sunrise and sunset (elevation crosses 0°)
        sunrise_time = None
        sunset_time = None

        for i in range(len(aer_data) - 1):
            el_current = aer_data[i].get("Elevation", 0)
            el_next = aer_data[i + 1].get("Elevation", 0)

            # Sunrise: elevation crosses from negative to positive
            if el_current < 0 and el_next >= 0 and sunrise_time is None:
                sunrise_time = aer_data[i + 1].get("Time", "N/A")

            # Sunset: elevation crosses from positive to negative
            if el_current >= 0 and el_next < 0 and sunset_time is None:
                sunset_time = aer_data[i].get("Time", "N/A")

        print("Key Solar Events:")
        print("-" * 70)
        if sunrise_time:
            print(f"  Sunrise:     {sunrise_time}")
        if sunset_time:
            print(f"  Sunset:      {sunset_time}")
        print(f"  Solar Noon:  {solar_noon_time}")
        print(f"  Max Elevation: {max_elevation:.2f}° (Sun at highest point)")
        print()

        # Show detailed AER data
        print("Detailed Solar Position:")
        print(f"{'Time (UTC)':<25} {'Azimuth (°)':<12} {'Elevation (°)':<15} "
              f"{'Range (AU)':<12}")
        print("-" * 70)

        # Show morning, noon, afternoon, evening
        indices = [0, len(aer_data)//4, len(aer_data)//2,
                   3*len(aer_data)//4, len(aer_data)-1]

        for i in indices:
            point = aer_data[i]
            time = point.get("Time", "N/A")
            azimuth = point.get("Azimuth", 0)
            elevation = point.get("Elevation", 0)
            range_m = point.get("Range", 0)
            range_au = range_m / 1.496e11  # Convert m to AU

            print(f"{time:<25} {azimuth:>10.2f}   {elevation:>12.2f}   "
                  f"{range_au:>10.6f}")

        print()

        # Solar geometry notes
        print("Solar Geometry Notes:")
        print("-" * 70)
        latitude = ground_station.cartographicDegrees[1]
        print(f"Location Latitude: {latitude:.1f}° N")
        print(f"Theoretical Max Solar Elevation: {90 - latitude + 23.5:.1f}° "
              f"(summer solstice)")
        print(f"Measured Max Elevation: {max_elevation:.1f}°")
        print()
        print("Azimuth Convention:")
        print("  0° = North, 90° = East, 180° = South, 270° = West")
        print()
        print("Applications:")
        print("  - Solar panel optimal tilt angle calculation")
        print("  - Building shadow analysis")
        print("  - Solar thermal system design")
        print("  - Daylighting architecture studies")
        print("  - Agricultural sunlight exposure planning")

    else:
        print("No solar AER data returned.")

    print()
    print("Solar AER calculation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()

"""
>>> ======================================================================
>>> Solar AER (Azimuth-Elevation-Range) from Ground Station
>>> ======================================================================
>>>
>>> Analysis Date: June 21, 2024 (Summer Solstice)
>>> Ground Station: Beijing, China
>>>   Longitude: 116.3974° E
>>>   Latitude:  39.9087° N
>>>   Altitude:  50.0 m
>>>
>>> Analysis Period: 2024-06-21T04:00:00Z to 2024-06-21T20:00:00Z
>>>
>>> Calculating solar position (AER) throughout the day...
>>>
>>> Solar Position Results:
>>> ----------------------------------------------------------------------
>>> Total Data Points: 97
>>>
>>> Key Solar Events:
>>> ----------------------------------------------------------------------
>>>   Sunset:      2024-06-21T11:40:00.000Z
>>>   Solar Noon:  2024-06-21T04:20:00.000Z
>>>   Max Elevation: 73.51° (Sun at highest point)
>>>
>>> Detailed Solar Position:
>>> Time (UTC)                Azimuth (°)  Elevation (°)   Range (AU)
>>> ----------------------------------------------------------------------
>>> 2024-06-21T04:00:00.000Z      167.01          73.17     0.001016
>>> 2024-06-21T08:00:00.000Z      268.14          40.50     0.001016
>>> 2024-06-21T12:00:00.000Z      304.27          -3.01     0.001016
>>> 2024-06-21T16:00:00.000Z      355.80         -26.54     0.001016
>>> 2024-06-21T20:00:00.000Z       50.11          -8.02     0.001016
>>>
>>> Solar Geometry Notes:
>>> ----------------------------------------------------------------------
>>> Location Latitude: 39.9° N
>>> Theoretical Max Solar Elevation: 73.6° (summer solstice)
>>> Measured Max Elevation: 73.5°
>>>
>>> Azimuth Convention:
>>>   0° = North, 90° = East, 180° = South, 270° = West
>>>
>>> Applications:
>>>   - Solar panel optimal tilt angle calculation
>>>   - Building shadow analysis
>>>   - Solar thermal system design
>>>   - Daylighting architecture studies
>>>   - Agricultural sunlight exposure planning
>>>
>>> Solar AER calculation completed successfully!
>>> ======================================================================
"""
