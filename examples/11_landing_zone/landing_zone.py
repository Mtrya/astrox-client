"""Example: Landing Zone Computation

This example demonstrates how to compute landing zone parameters for
rocket stages or debris impact areas.
"""

from astrox.landing_zone import compute_landing_zone


def main():
    """Compute landing zone for rocket first stage.

    This example calculates the landing zone parameters given:
    - Launch point coordinates
    - Landing point coordinates
    - Zone boundary points

    Useful for:
    - First stage splashdown zones
    - Debris impact predictions
    - Range safety analysis
    - Landing ellipse calculations
    """

    print("Computing landing zone parameters...")
    print("=" * 70)

    # Example 1: First stage landing zone in the Atlantic Ocean
    # Launch: Cape Canaveral, Florida
    # Landing: Downrange in Atlantic Ocean

    print("\nExample 1: Atlantic Ocean Splashdown Zone")
    print("-" * 70)

    result1 = compute_landing_zone(
        # Launch point (Cape Canaveral)
        fa_she_dian=[-80.6, 28.5, 0],  # [lon(deg), lat(deg), alt(m)]

        # Landing point (downrange in Atlantic)
        luo_dian=[-75.0, 27.8, 0],  # [lon(deg), lat(deg), alt(m)]

        # Zone boundary (rectangular zone in local coordinates)
        # Front is +X axis, Right is +Y axis, unit: km
        # This defines a 10km x 5km landing ellipse
        zone_xys=[
            5.0, 2.5,    # Point 1: Front-right corner
            5.0, -2.5,   # Point 2: Front-left corner
            -5.0, -2.5,  # Point 3: Rear-left corner
            -5.0, 2.5    # Point 4: Rear-right corner
        ]
    )

    print("\nLanding Zone Results:")
    if "ZoneVertices" in result1:
        print("Zone vertices (geographic coordinates):")
        for i, vertex in enumerate(result1["ZoneVertices"], 1):
            print(f"  Point {i}: Lon={vertex.get('Lon', 'N/A')}°, "
                  f"Lat={vertex.get('Lat', 'N/A')}°")

    if "ZoneArea" in result1:
        print(f"\nZone area: {result1['ZoneArea']} km²")

    if "CenterPoint" in result1:
        center = result1["CenterPoint"]
        print(f"Zone center: Lon={center.get('Lon', 'N/A')}°, "
              f"Lat={center.get('Lat', 'N/A')}°")

    # Example 2: Landing zone for Chinese rocket over Pacific
    # Launch: Jiuquan, China
    # Landing: Pacific Ocean

    print("\n" + "=" * 70)
    print("\nExample 2: Pacific Ocean Landing Zone")
    print("-" * 70)

    result2 = compute_landing_zone(
        # Launch point (Jiuquan)
        fa_she_dian=[100.3, 40.6, 1000],  # [lon(deg), lat(deg), alt(m)]

        # Landing point (Pacific Ocean)
        luo_dian=[170.0, 10.0, 0],  # [lon(deg), lat(deg), alt(m)]

        # Larger zone for long-range flight
        # 20km x 10km ellipse
        zone_xys=[
            10.0, 5.0,    # Point 1
            10.0, -5.0,   # Point 2
            -10.0, -5.0,  # Point 3
            -10.0, 5.0    # Point 4
        ]
    )

    print("\nLanding Zone Results:")
    if "ZoneVertices" in result2:
        print("Zone vertices (geographic coordinates):")
        for i, vertex in enumerate(result2["ZoneVertices"], 1):
            print(f"  Point {i}: Lon={vertex.get('Lon', 'N/A')}°, "
                  f"Lat={vertex.get('Lat', 'N/A')}°")

    if "ZoneArea" in result2:
        print(f"\nZone area: {result2['ZoneArea']} km²")

    # Display full results
    print("\n" + "=" * 70)
    print("Full API Response (Example 1):")
    print("-" * 70)
    import json
    print(json.dumps(result1, indent=2, ensure_ascii=False))

    print("\n" + "=" * 70)
    print("Full API Response (Example 2):")
    print("-" * 70)
    print(json.dumps(result2, indent=2, ensure_ascii=False))

    print("\n" + "=" * 70)
    print("Use Cases:")
    print("- Range safety analysis for launch operations")
    print("- First stage recovery planning")
    print("- Debris impact zone calculations")
    print("- Landing ellipse definition for mission planning")
    print("- Maritime exclusion zone notifications")


if __name__ == "__main__":
    main()

"""
>>> Computing landing zone parameters...
>>> ======================================================================
>>>
>>> Example 1: Atlantic Ocean Splashdown Zone
>>> ----------------------------------------------------------------------
>>>
>>> Landing Zone Results:
>>>
>>> ======================================================================
>>>
>>> Example 2: Pacific Ocean Landing Zone
>>> ----------------------------------------------------------------------
>>>
>>> Landing Zone Results:
>>>
>>> ======================================================================
>>> Full API Response (Example 1):
>>> ----------------------------------------------------------------------
>>> {
>>>   "IsSuccess": true,
>>>   "Message": "Success",
>>>   "cartographicDegrees": [
>>>     -74.95408892336079,
>>>     27.770377240284482,
>>>     2.9376450603820508,
>>>     -74.94579563458493,
>>>     27.814890149464613,
>>>     2.934315810957404,
>>>     -75.04593597550145,
>>>     27.82960736703625,
>>>     2.9376366623127814,
>>>     -75.05418958059404,
>>>     27.785088556808244,
>>>     2.9343200310388626
>>>   ]
>>> }
>>>
>>> ======================================================================
>>> Full API Response (Example 2):
>>> ----------------------------------------------------------------------
>>> {
>>>   "IsSuccess": true,
>>>   "Message": "Success",
>>>   "cartographicDegrees": [
>>>     170.0407285167013,
>>>     9.907333744586538,
>>>     10.026475177487681,
>>>     170.09922252920617,
>>>     9.976693761649592,
>>>     9.976040715909658,
>>>     169.95924839842903,
>>>     10.09266075439474,
>>>     10.026438043195027,
>>>     169.90076333780814,
>>>     10.023276624963254,
>>>     9.976031427167037
>>>   ]
>>> }
>>>
>>> ======================================================================
>>> Use Cases:
>>> - Range safety analysis for launch operations
>>> - First stage recovery planning
>>> - Debris impact zone calculations
>>> - Landing ellipse definition for mission planning
>>> - Maritime exclusion zone notifications
"""
