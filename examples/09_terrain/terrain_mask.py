"""
Calculate terrain mask for ground station.

This example demonstrates terrain mask calculation which provides
azimuth-elevation constraints for ground stations based on surrounding
terrain, useful for satellite tracking and visibility analysis.
"""

from astrox.terrain import get_terrain_mask
from astrox.models import EntityPositionSite


def main():
    print("=" * 70)
    print("Terrain Mask Calculation for Ground Station")
    print("=" * 70)
    print()

    # Ground station in mountainous area: Xichang Satellite Launch Center
    ground_station = EntityPositionSite.model_construct(
        **{
            "$type": "SitePosition",
            "cartographicDegrees": [
                102.0267,  # Longitude (deg E)
                28.2467,  # Latitude (deg N)
                1825.0,  # Altitude (m) - elevated location
            ]
        }
    )

    print("Ground Station: Xichang Satellite Launch Center, China")
    print(f"  Longitude: {ground_station.cartographicDegrees[0]:.4f}° E")
    print(f"  Latitude:  {ground_station.cartographicDegrees[1]:.4f}° N")
    print(f"  Altitude:  {ground_station.cartographicDegrees[2]:.1f} m")
    print()
    print("Note: Located in mountainous terrain of Sichuan Province")
    print()

    # Calculate terrain mask using default method
    print("Calculating terrain mask (default method)...")
    result_default = get_terrain_mask(
        site_position=ground_station,
        method="default",  # High-precision terrain data
        text="Xichang terrain mask - default",
    )

    # Display results
    print()
    print("Terrain Mask Results:")
    print("-" * 70)

    if "AzElMask" in result_default and result_default["AzElMask"]:
        mask_data = result_default["AzElMask"]
        print(f"Mask Data Points: {len(mask_data)} (360° coverage)")
        print()

        # Analyze terrain mask
        elevations = [point.get("Elevation", 0) for point in mask_data]
        min_elevation = min(elevations)
        max_elevation = max(elevations)
        avg_elevation = sum(elevations) / len(elevations)

        print("Terrain Mask Statistics:")
        print(f"  Minimum Elevation Angle: {min_elevation:.2f}°")
        print(f"  Maximum Elevation Angle: {max_elevation:.2f}°")
        print(f"  Average Elevation Angle: {avg_elevation:.2f}°")
        print()

        # Find most obstructed directions
        obstructions = sorted(
            [(point.get("Azimuth", 0), point.get("Elevation", 0))
             for point in mask_data],
            key=lambda x: x[1],
            reverse=True
        )

        print("Most Obstructed Directions (highest terrain):")
        print(f"{'Azimuth (°)':<12} {'Elevation (°)':<15} {'Direction':<12}")
        print("-" * 45)

        for az, el in obstructions[:5]:
            # Determine cardinal direction
            if 337.5 <= az or az < 22.5:
                direction = "North"
            elif 22.5 <= az < 67.5:
                direction = "Northeast"
            elif 67.5 <= az < 112.5:
                direction = "East"
            elif 112.5 <= az < 157.5:
                direction = "Southeast"
            elif 157.5 <= az < 202.5:
                direction = "South"
            elif 202.5 <= az < 247.5:
                direction = "Southwest"
            elif 247.5 <= az < 292.5:
                direction = "West"
            else:
                direction = "Northwest"

            print(f"{az:>10.1f}   {el:>12.2f}   {direction:<12}")

        print()

        # Show sample azimuth-elevation pairs
        print("Sample Terrain Mask Data (by cardinal direction):")
        print(f"{'Direction':<12} {'Azimuth (°)':<12} {'Min Elevation (°)':<18}")
        print("-" * 50)

        cardinal_directions = {
            "North": 0,
            "Northeast": 45,
            "East": 90,
            "Southeast": 135,
            "South": 180,
            "Southwest": 225,
            "West": 270,
            "Northwest": 315,
        }

        for direction, target_az in cardinal_directions.items():
            # Find closest azimuth point
            closest = min(mask_data,
                          key=lambda x: abs(x.get("Azimuth", 0) - target_az))
            az = closest.get("Azimuth", 0)
            el = closest.get("Elevation", 0)
            print(f"{direction:<12} {az:>10.1f}   {el:>15.2f}")

        print()

        # Visibility analysis
        print("Satellite Visibility Impact:")
        print("-" * 70)
        print(f"Minimum satellite elevation for tracking: {max_elevation:.2f}°")
        print()
        print("The terrain mask indicates that satellites must be at least")
        print(f"{max_elevation:.1f}° above the horizon in the most obstructed direction")
        print("to be visible from this ground station.")
        print()

        # Calculate usable sky percentage
        # Assume 10° is standard minimum elevation without terrain
        standard_min_el = 10.0
        terrain_restricted = sum(1 for el in elevations if el > standard_min_el)
        percent_restricted = 100 * terrain_restricted / len(elevations)

        if percent_restricted > 0:
            print(f"Terrain restricts {percent_restricted:.1f}% of azimuth directions")
            print(f"beyond standard {standard_min_el}° minimum elevation.")
        else:
            print(f"All terrain elevations below standard {standard_min_el}° threshold.")

    else:
        print("No terrain mask data returned.")
        print()
        print("Note: This may occur if:")
        print("  - Terrain data not available for this location")
        print("  - Location is in very flat area (minimal terrain)")

    print()
    print("Applications:")
    print("-" * 70)
    print("  - Satellite pass predictions accounting for terrain")
    print("  - Ground station antenna pointing constraints")
    print("  - Satellite visibility time calculations")
    print("  - Tracking schedule optimization")
    print("  - Communication link budget analysis")
    print("  - Ground station site selection")

    print()
    print("Terrain mask calculation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()

    # Example output:
    # >>> ======================================================================
    # >>> Terrain Mask Calculation for Ground Station
    # >>> ======================================================================
    # >>>
    # >>> Ground Station: Xichang Satellite Launch Center, China
    # >>>   Longitude: 102.0267° E
    # >>>   Latitude:  28.2467° N
    # >>>   Altitude:  1825.0 m
    # >>>
    # >>> Note: Located in mountainous terrain of Sichuan Province
    # >>>
    # >>> Calculating terrain mask (default method)...
    # >>> Traceback (most recent call last):
    # >>>   File "/home/betelgeuse/Developments/astrox-client/examples/09_terrain/terrain_mask.py", line 175, in <module>
    # >>>     main()
    # >>>   File "/home/betelgeuse/Developments/astrox-client/examples/09_terrain/terrain_mask.py", line 41, in main
    # >>>     result_default = get_terrain_mask(
    # >>>         site_position=ground_station,
    # >>>         method="default",  # High-precision terrain data
    # >>>         text="Xichang terrain mask - default",
    # >>>     )
    # >>>   File "/home/betelgeuse/Developments/astrox-client/astrox/terrain.py", line 61, in get_terrain_mask
    # >>>     return sess.post(endpoint=endpoint, data=payload)
    # >>>   File "/home/betelgeuse/Developments/astrox-client/astrox/_http.py", line 284, in post
    # >>>     result = _make_request(
    # >>>         endpoint=endpoint,
    # >>>         method="POST",
    # >>>         json=payload,
    # >>>     )
    # >>>   File "/home/betelgeuse/Developments/astrox-client/astrox/_http.py", line 124, in _make_request
    # >>>     raise exceptions.AstroxAPIError(
    # >>>         f"API error ({response.status_code}): {message}"
    # >>>     ) from e
    # >>> astrox.exceptions.AstroxAPIError: Metadata could not be downloaded from the given terrain server.
    # >>>    at ASTROX.Internal.DownloadHelper.GetStream[T](Func`2 func)
    # >>>    at ASTROX.Internal.DownloadHelper.Get[T](Func`2 func)
    # >>>    at ASTROX.Terrain.Internal.LayerJsonTilesetMetadata.CreateFromUri(String uri, IWebProxy proxy, Action`1 requestCallback)
    # >>>    at AeroSpace.Terrain.StkTerrainServer2.xx2duPZpf9(String  )
    # >>>    at AeroSpace.Terrain.StkTerrainServer2..ctor(String baseUri, Ellipsoid shape, ReferenceFrame fixedFrame, Int32 flagPole)
    # >>>    at AeroSpace.Terrain.TerrainMaskCompute.GetAzimuthElevationMask(EntityPositionSite sitePosition, TerrainMaskConfig config)
    # >>>    at AeroSpace.Terrain.TerrainMaskCompute.GetAzimuthElevationMask(AzimuthElevationMaskInput input)
