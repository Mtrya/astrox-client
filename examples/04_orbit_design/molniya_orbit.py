"""
Example: Generate Molniya Orbit

This example demonstrates how to design a Molniya orbit. Molniya orbits are
highly elliptical orbits used for high-latitude communications, with:
- High inclination (~63.4° to minimize apsidal precession)
- 12-hour period (semi-synchronous)
- Apogee over high latitudes
- Low perigee altitude (typically 600 km)
"""

from astrox.orbit_wizard import design_molniya


def main():
    """Generate Molniya orbits with different configurations."""

    # Example 1: Classic Molniya with apogee over Russia (90°E)
    print("=" * 80)
    print("Example 1: Classic Molniya (Apogee over Russia at 90°E)")
    print("=" * 80)

    result = design_molniya(
        orbit_epoch="2024-01-15T00:00:00.000Z",
        perigee_altitude=600.0,  # km - typical low perigee
        apogee_longitude=90.0,  # 90°E - over Russia
        argument_of_periapsis=270.0,  # deg - apogee in northern hemisphere
        description="Molniya orbit for Russian communications"
    )

    print(f"\nMolniya Orbit Parameters:")
    print(f"  Epoch: 2024-01-15T00:00:00.000Z")
    print(f"  Perigee altitude: 600.0 km")
    print(f"  Apogee longitude: 90.0°E")
    print(f"  Argument of periapsis: 270.0°")
    print(f"\nResult keys: {list(result.keys())}")
    print(f"Full result:\n{result}")

    # Example 2: Molniya with apogee over North America (-100°W)
    print("\n" + "=" * 80)
    print("Example 2: Molniya (Apogee over North America at 100°W)")
    print("=" * 80)

    result = design_molniya(
        orbit_epoch="2024-06-21T12:00:00.000Z",
        perigee_altitude=500.0,  # km - slightly lower perigee
        apogee_longitude=-100.0,  # 100°W - over North America
        argument_of_periapsis=270.0,  # deg - apogee in northern hemisphere
        description="Molniya orbit for North American coverage"
    )

    print(f"\nMolniya Orbit Parameters:")
    print(f"  Epoch: 2024-06-21T12:00:00.000Z")
    print(f"  Perigee altitude: 500.0 km")
    print(f"  Apogee longitude: -100.0°W")
    print(f"  Argument of periapsis: 270.0°")
    print(f"\nFull result:\n{result}")

    # Example 3: Southern hemisphere Molniya (arg of periapsis = 90°)
    print("\n" + "=" * 80)
    print("Example 3: Southern Hemisphere Molniya (Apogee at 90°)")
    print("=" * 80)

    result = design_molniya(
        orbit_epoch="2024-09-23T00:00:00.000Z",
        perigee_altitude=600.0,  # km
        apogee_longitude=0.0,  # Prime meridian
        argument_of_periapsis=90.0,  # deg - apogee in southern hemisphere
        description="Molniya orbit for southern hemisphere"
    )

    print(f"\nMolniya Orbit Parameters:")
    print(f"  Epoch: 2024-09-23T00:00:00.000Z")
    print(f"  Perigee altitude: 600.0 km")
    print(f"  Apogee longitude: 0.0°")
    print(f"  Argument of periapsis: 90.0° (southern hemisphere)")
    print(f"\nFull result:\n{result}")

    # Example 4: Higher perigee Molniya
    print("\n" + "=" * 80)
    print("Example 4: Higher Perigee Molniya (1000 km)")
    print("=" * 80)

    result = design_molniya(
        orbit_epoch="2024-12-31T23:59:59.000Z",
        perigee_altitude=1000.0,  # km - higher perigee
        apogee_longitude=45.0,  # 45°E
        argument_of_periapsis=270.0,  # deg
        description="Molniya orbit with higher perigee"
    )

    print(f"\nMolniya Orbit Parameters:")
    print(f"  Epoch: 2024-12-31T23:59:59.000Z")
    print(f"  Perigee altitude: 1000.0 km")
    print(f"  Apogee longitude: 45.0°E")
    print(f"  Argument of periapsis: 270.0°")
    print(f"\nFull result:\n{result}")

    print("\n" + "=" * 80)
    print("Notes:")
    print("  - Molniya orbits have ~63.4° inclination (critical inclination)")
    print("  - 12-hour orbital period (semi-synchronous)")
    print("  - Apogee typically at ~40,000 km altitude")
    print("  - Arg of periapsis 270° = apogee over northern hemisphere")
    print("  - Arg of periapsis 90° = apogee over southern hemisphere")
    print("=" * 80)


if __name__ == "__main__":
    main()


"""
>>> ================================================================================
>>> Example 1: Classic Molniya (Apogee over Russia at 90°E)
>>> ================================================================================
>>>
>>> Molniya Orbit Parameters:
>>>   Epoch: 2024-01-15T00:00:00.000Z
>>>   Perigee altitude: 600.0 km
>>>   Apogee longitude: 90.0°E
>>>   Argument of periapsis: 270.0°
>>>
>>> Result keys: ['IsSuccess', 'Message', 'Elements_TOD', 'Elements_Inertial']
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 26554634.94343599, 'Eccentricity': 0.7372158564836563, 'Inclination': 63.4, 'ArgumentOfPeriapsis': 270, 'RightAscensionOfAscendingNode': 203.95170186195477, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 26554634.943435982, 'Eccentricity': 0.7372158564836562, 'Inclination': 63.34837952753034, 'ArgumentOfPeriapsis': 270.1375137541719, 'RightAscensionOfAscendingNode': 203.58324715624477, 'TrueAnomaly': 7.578665451924786e-16, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Example 2: Molniya (Apogee over North America at 100°W)
>>> ================================================================================
>>>
>>> Molniya Orbit Parameters:
>>>   Epoch: 2024-06-21T12:00:00.000Z
>>>   Perigee altitude: 500.0 km
>>>   Apogee longitude: -100.0°W
>>>   Argument of periapsis: 270.0°

>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 26554457.819704406, 'Eccentricity': 0.7409799497056135, 'Inclination': 63.4, 'ArgumentOfPeriapsis': 270, 'RightAscensionOfAscendingNode': -9.823189816749348, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 26554457.819704354, 'Eccentricity': 0.740979949705613, 'Inclination': 63.374283088673, 'ArgumentOfPeriapsis': 269.8507839331963, 'RightAscensionOfAscendingNode': 349.9309910992391, 'TrueAnomaly': 1.8139100917721617e-15, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Example 3: Southern Hemisphere Molniya (Apogee at 90°)
>>> ================================================================================
>>>
>>> Molniya Orbit Parameters:
>>>   Epoch: 2024-09-23T00:00:00.000Z
>>>   Perigee altitude: 600.0 km
>>>   Apogee longitude: 0.0°
>>>   Argument of periapsis: 90.0° (southern hemisphere)
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 26554634.94343599, 'Eccentricity': 0.7372158564836563, 'Inclination': 63.4, 'ArgumentOfPeriapsis': 90, 'RightAscensionOfAscendingNode': 2.3348394710859215, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 26554634.94343605, 'Eccentricity': 0.7372158564836568, 'Inclination': 63.40265922298852, 'ArgumentOfPeriapsis': 89.84633398887581, 'RightAscensionOfAscendingNode': 2.087391404472674, 'TrueAnomaly': -2.9817700138720475e-16, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Example 4: Higher Perigee Molniya (1000 km)
>>> ================================================================================
>>>
>>> Molniya Orbit Parameters:
>>>   Epoch: 2024-12-31T23:59:59.000Z
>>>   Perigee altitude: 1000.0 km
>>>   Apogee longitude: 45.0°E
>>>   Argument of periapsis: 270.0°
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 26555275.04231188, 'Eccentricity': 0.7221592701169904, 'Inclination': 63.4, 'ArgumentOfPeriapsis': 270, 'RightAscensionOfAscendingNode': 145.89539854442563, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 26555275.04231195, 'Eccentricity': 0.7221592701169911, 'Inclination': 63.48037774760977, 'ArgumentOfPeriapsis': 270.12708481848216, 'RightAscensionOfAscendingNode': 145.5181868661328, 'TrueAnomaly': 6.4729257384472354e-15, 'GravitationalParameter': 398600441800000}}
>>>
>>> ================================================================================
>>> Notes:
>>>   - Molniya orbits have ~63.4° inclination (critical inclination)
>>>   - 12-hour orbital period (semi-synchronous)
>>>   - Apogee typically at ~40,000 km altitude
>>>   - Arg of periapsis 270° = apogee over northern hemisphere
>>>   - Arg of periapsis 90° = apogee over southern hemisphere
>>> ================================================================================
"""
