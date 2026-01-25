"""
Example: Generate Geostationary Orbit (GEO)

This example demonstrates how to design a geostationary orbit using the orbit wizard.
GEO satellites orbit at approximately 35,786 km altitude with zero inclination,
maintaining a fixed position over the Earth's equator.
"""

from astrox.orbit_wizard import design_geo


def main():
    """Generate geostationary orbit with different configurations."""

    # Example 1: Classic GEO at 0° inclination over 100°E longitude
    print("=" * 80)
    print("Example 1: Classic GEO (0° inclination, 100°E)")
    print("=" * 80)

    result = design_geo(
        orbit_epoch="2024-01-15T00:00:00.000Z",
        inclination=0.0,  # Zero inclination for true geostationary
        sub_satellite_point=100.0,  # 100°E longitude
        description="Classic GEO satellite at 100°E"
    )

    print(f"\nGEO Orbit Parameters (100°E):")
    print(f"  Epoch: 2024-01-15T00:00:00.000Z")
    print(f"  Inclination: 0.0°")
    print(f"  Sub-satellite point: 100.0°E")
    print(f"\nResult keys: {list(result.keys())}")
    print(f"Full result:\n{result}")

    # Example 2: Slightly inclined GEO (0.05° inclination) over 0° longitude
    print("\n" + "=" * 80)
    print("Example 2: Inclined GEO (0.05° inclination, 0°E Prime Meridian)")
    print("=" * 80)

    result = design_geo(
        orbit_epoch="2024-06-21T12:00:00.000Z",
        inclination=0.05,  # Slight inclination (realistic after orbit maintenance)
        sub_satellite_point=0.0,  # Prime meridian
        description="Inclined GEO over Prime Meridian"
    )

    print(f"\nGEO Orbit Parameters (0°E):")
    print(f"  Epoch: 2024-06-21T12:00:00.000Z")
    print(f"  Inclination: 0.05°")
    print(f"  Sub-satellite point: 0.0°E")
    print(f"\nFull result:\n{result}")

    # Example 3: GEO over Western Hemisphere (-75°W)
    print("\n" + "=" * 80)
    print("Example 3: GEO over Western Hemisphere (-75°W)")
    print("=" * 80)

    result = design_geo(
        orbit_epoch="2024-09-23T00:00:00.000Z",
        inclination=0.0,
        sub_satellite_point=-75.0,  # 75°W longitude (western hemisphere)
        description="GEO satellite at 75°W"
    )

    print(f"\nGEO Orbit Parameters (75°W):")
    print(f"  Epoch: 2024-09-23T00:00:00.000Z")
    print(f"  Inclination: 0.0°")
    print(f"  Sub-satellite point: -75.0°W")
    print(f"\nFull result:\n{result}")

    # Example 4: GEO over Asia-Pacific region (145°E)
    print("\n" + "=" * 80)
    print("Example 4: GEO over Asia-Pacific (145°E)")
    print("=" * 80)

    result = design_geo(
        orbit_epoch="2024-12-31T23:59:59.000Z",
        inclination=0.0,
        sub_satellite_point=145.0,  # 145°E longitude (Asia-Pacific)
        description="GEO satellite at 145°E"
    )

    print(f"\nGEO Orbit Parameters (145°E):")
    print(f"  Epoch: 2024-12-31T23:59:59.000Z")
    print(f"  Inclination: 0.0°")
    print(f"  Sub-satellite point: 145.0°E")
    print(f"\nFull result:\n{result}")

    print("\n" + "=" * 80)
    print("Note: GEO orbits are at approximately 35,786 km altitude")
    print("      with orbital period of 24 hours (sidereal day)")
    print("=" * 80)


if __name__ == "__main__":
    main()


"""
>>> ================================================================================
>>> Example 1: Classic GEO (0° inclination, 100°E)
>>> ================================================================================
>>>
>>> GEO Orbit Parameters (100°E):
>>>   Epoch: 2024-01-15T00:00:00.000Z
>>>   Inclination: 0.0°
>>>   Sub-satellite point: 100.0°E
>>>
>>> Result keys: ['IsSuccess', 'Message', 'Elements_TOD', 'Elements_Inertial']
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 42166258.667, 'Eccentricity': 0, 'Inclination': 0, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 213.9516930999242, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 42166258.66700005, 'Eccentricity': 6.975859548358518e-16, 'Inclination': 0.133329069602188, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90.83580461167782, 'TrueAnomaly': 122.8090622288762, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Example 2: Inclined GEO (0.05° inclination, 0°E Prime Meridian)
>>> ================================================================================
>>>
>>> GEO Orbit Parameters (0°E):
>>>   Epoch: 2024-06-21T12:00:00.000Z
>>>   Inclination: 0.05°
>>>   Sub-satellite point: 0.0°E
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 42166258.667, 'Eccentricity': 0, 'Inclination': 0.05, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90.17680147319848, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 42166258.66700001, 'Eccentricity': 4.1854934918889577e-16, 'Inclination': 0.18585832139980463, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90.55455570475837, 'TrueAnomaly': -0.6904171158448035, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Example 3: GEO over Western Hemisphere (-75°W)
>>> ================================================================================
>>>
>>> GEO Orbit Parameters (75°W):
>>>   Epoch: 2024-09-23T00:00:00.000Z
>>>   Inclination: 0.0°
>>>   Sub-satellite point: -75.0°W
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 42166258.667, 'Eccentricity': 0, 'Inclination': 0, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 287.3348307090554, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 42166258.66700004, 'Eccentricity': 8.383763035406949e-16, 'Inclination': 0.13742843351927173, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90.94425567875449, 'TrueAnomaly': -163.925675233715, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Example 4: GEO over Asia-Pacific (145°E)
>>> ================================================================================
>>>
>>> GEO Orbit Parameters (145°E):
>>>   Epoch: 2024-12-31T23:59:59.000Z
>>>   Inclination: 0.0°
>>>   Sub-satellite point: 145.0°E
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 42166258.667, 'Eccentricity': 0, 'Inclination': 0, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 245.8953898141796, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 42166258.66700003, 'Eccentricity': 6.99434388619041e-16, 'Inclination': 0.1392199697867456, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90.81049661917943, 'TrueAnomaly': 154.76450521204674, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Note: GEO orbits are at approximately 35,786 km altitude
>>>       with orbital period of 24 hours (sidereal day)
>>> ================================================================================
"""
