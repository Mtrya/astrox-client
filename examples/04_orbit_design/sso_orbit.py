"""
Example: Generate Sun-Synchronous Orbit (SSO)

This example demonstrates how to design sun-synchronous orbits. SSO satellites
maintain a constant angle relative to the Sun, enabling consistent lighting
conditions for Earth observation missions.

Common local times:
- Dawn/dusk orbit: 6:00 or 18:00 (low solar interference)
- Morning orbit: 10:00-10:30 (optimal for optical imaging)
- Afternoon orbit: 13:00-14:00 (good contrast for SAR)
"""

from astrox.orbit_wizard import design_sso


def main():
    """Generate sun-synchronous orbits with different local times and altitudes."""

    # Example 1: Dawn/dusk orbit at 600 km
    print("=" * 80)
    print("Example 1: Dawn/Dusk SSO (6:00 AM, 600 km)")
    print("=" * 80)

    result = design_sso(
        orbit_epoch="2024-01-15T00:00:00.000Z",
        altitude=600.0,  # km - typical LEO altitude
        local_time_of_descending_node=6.0,  # 6:00 AM (dawn)
        description="Dawn/dusk SSO for low solar interference"
    )

    print(f"\nSSO Orbit Parameters:")
    print(f"  Epoch: 2024-01-15T00:00:00.000Z")
    print(f"  Altitude: 600.0 km")
    print(f"  Local time (descending node): 06:00 (dawn)")
    print(f"\nResult keys: {list(result.keys())}")
    print(f"Full result:\n{result}")

    # Example 2: Morning orbit at 800 km (common for Earth observation)
    print("\n" + "=" * 80)
    print("Example 2: Morning SSO (10:30 AM, 800 km)")
    print("=" * 80)

    result = design_sso(
        orbit_epoch="2024-03-20T12:00:00.000Z",
        altitude=800.0,  # km - higher altitude for wider coverage
        local_time_of_descending_node=10.5,  # 10:30 AM
        description="Morning SSO for optical Earth observation"
    )

    print(f"\nSSO Orbit Parameters:")
    print(f"  Epoch: 2024-03-20T12:00:00.000Z")
    print(f"  Altitude: 800.0 km")
    print(f"  Local time (descending node): 10:30 (mid-morning)")
    print(f"\nFull result:\n{result}")

    # Example 3: Afternoon orbit at 700 km
    print("\n" + "=" * 80)
    print("Example 3: Afternoon SSO (13:30 PM, 700 km)")
    print("=" * 80)

    result = design_sso(
        orbit_epoch="2024-06-21T18:00:00.000Z",
        altitude=700.0,  # km
        local_time_of_descending_node=13.5,  # 1:30 PM
        description="Afternoon SSO for SAR missions"
    )

    print(f"\nSSO Orbit Parameters:")
    print(f"  Epoch: 2024-06-21T18:00:00.000Z")
    print(f"  Altitude: 700.0 km")
    print(f"  Local time (descending node): 13:30 (early afternoon)")
    print(f"\nFull result:\n{result}")

    # Example 4: Dusk orbit at 500 km
    print("\n" + "=" * 80)
    print("Example 4: Dusk SSO (18:00 PM, 500 km)")
    print("=" * 80)

    result = design_sso(
        orbit_epoch="2024-09-23T06:00:00.000Z",
        altitude=500.0,  # km - lower altitude for higher resolution
        local_time_of_descending_node=18.0,  # 6:00 PM (dusk)
        description="Dusk SSO for twilight imaging"
    )

    print(f"\nSSO Orbit Parameters:")
    print(f"  Epoch: 2024-09-23T06:00:00.000Z")
    print(f"  Altitude: 500.0 km")
    print(f"  Local time (descending node): 18:00 (dusk)")
    print(f"\nFull result:\n{result}")

    # Example 5: High-altitude SSO at 1000 km
    print("\n" + "=" * 80)
    print("Example 5: High-altitude SSO (12:00 PM, 1000 km)")
    print("=" * 80)

    result = design_sso(
        orbit_epoch="2024-12-21T00:00:00.000Z",
        altitude=1000.0,  # km - higher altitude for environmental monitoring
        local_time_of_descending_node=12.0,  # Noon
        description="High-altitude noon SSO"
    )

    print(f"\nSSO Orbit Parameters:")
    print(f"  Epoch: 2024-12-21T00:00:00.000Z")
    print(f"  Altitude: 1000.0 km")
    print(f"  Local time (descending node): 12:00 (noon)")
    print(f"\nFull result:\n{result}")

    print("\n" + "=" * 80)
    print("Notes:")
    print("  - SSO inclination varies with altitude (~97-98° for 600-800 km)")
    print("  - Lower altitude = higher inclination required")
    print("  - Local time is at descending node (southbound equatorial crossing)")
    print("  - Dawn/dusk orbits (6:00/18:00) minimize solar panel shadowing")
    print("  - Mid-morning orbits (10:00-10:30) optimal for optical imaging")
    print("  - Afternoon orbits (13:00-14:00) good for SAR and thermal imaging")
    print("=" * 80)


if __name__ == "__main__":
    main()

    # Example output:
    # >>> ================================================================================
    # >>> Example 1: Dawn/Dusk SSO (6:00 AM, 600 km)
    # >>> ================================================================================
    # >>>
    # >>> SSO Orbit Parameters:
    # >>>   Epoch: 2024-01-15T00:00:00.000Z
    # >>>   Altitude: 600.0 km
    # >>>   Local time (descending node): 06:00 (dawn)
    # >>>
    # >>> Result keys: ['IsSuccess', 'Message', 'Elements_TOD', 'Elements_Inertial']
    # >>> Full result:
    # >>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 6978137, 'Eccentricity': 0, 'Inclination': 97.78764579583225, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 23.951693099924213, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 6978137.000000002, 'Eccentricity': 3.695518308466741e-16, 'Inclination': 97.83931425849163, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 23.628000715672705, 'TrueAnomaly': -0.12406239498976189, 'GravitationalParameter': 398600441800000}}
    # >>>
    # >>> ================================================================================
    # >>> Example 2: Morning SSO (10:30 AM, 800 km)
    # >>> ================================================================================
    # >>>
    # >>> SSO Orbit Parameters:
    # >>>   Epoch: 2024-03-20T12:00:00.000Z
    # >>>   Altitude: 800.0 km
    # >>>   Local time (descending node): 10:30 (mid-morning)
    # >>>
    # >>> Full result:
    # >>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 7178137, 'Eccentricity': 0, 'Inclination': 98.60308416605777, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 156.01159592758688, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 7178137.000000006, 'Eccentricity': 7.600442244993564e-16, 'Inclination': 98.66035707032852, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 155.7208754578168, 'TrueAnomaly': 0.12292646016143123, 'GravitationalParameter': 398600441800000}}
    # >>>
    # >>> ================================================================================
    # >>> Example 3: Afternoon SSO (13:30 PM, 700 km)
    # >>> ================================================================================
    # >>>
    # >>> SSO Orbit Parameters:
    # >>>   Epoch: 2024-06-21T18:00:00.000Z
    # >>>   Altitude: 700.0 km
    # >>>   Local time (descending node): 13:30 (early afternoon)
    # >>>
    # >>> Full result:
    # >>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 7078137, 'Eccentricity': 0, 'Inclination': 98.1879566678083, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 292.9232133151946, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 7078137.000000002, 'Eccentricity': 1.3045018387862303e-17, 'Inclination': 98.06180018676294, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 292.60332797079695, 'TrueAnomaly': -0.0509670608655474, 'GravitationalParameter': 398600441800000}}
    # >>>
    # >>> ================================================================================
    # >>> Example 4: Dusk SSO (18:00 PM, 500 km)
    # >>> ================================================================================
    # >>>
    # >>> SSO Orbit Parameters:
    # >>>   Epoch: 2024-09-23T06:00:00.000Z
    # >>>   Altitude: 500.0 km
    # >>>   Local time (descending node): 18:00 (dusk)
    # >>>
    # >>> Full result:
    # >>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 6878137, 'Eccentricity': 0, 'Inclination': 97.40178499761585, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 92.58124255230207, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 6878136.999999999, 'Eccentricity': 1.0316296717127469e-18, 'Inclination': 97.53918284151844, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 92.26539412327159, 'TrueAnomaly': 0.003198163244479429, 'GravitationalParameter': 398600441800000}}
    # >>>
    # >>> ================================================================================
    # >>> Example 5: High-altitude SSO (12:00 PM, 1000 km)
    # >>> ================================================================================
    # >>>
    # >>> SSO Orbit Parameters:
    # >>>   Epoch: 2024-12-21T00:00:00.000Z
    # >>>   Altitude: 1000.0 km
    # >>>   Local time (descending node): 12:00 (noon)
    # >>>
    # >>> Full result:
    # >>> {'IsSuccess': True, 'Message': 'Success!', 'Elements_TOD': {'SemimajorAxis': 7378137, 'Eccentricity': 0, 'Inclination': 99.47930515814042, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90.05744677856144, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, 'Elements_Inertial': {'SemimajorAxis': 7378136.999999993, 'Eccentricity': 7.81190645763704e-16, 'Inclination': 99.61826608169872, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 89.73715540465051, 'TrueAnomaly': -0.002676594183147884, 'GravitationalParameter': 398600441800000}}
    # >>>
    # >>> ================================================================================
    # >>> Notes:
    # >>>   - SSO inclination varies with altitude (~97-98° for 600-800 km)
    # >>>   - Lower altitude = higher inclination required
    # >>>   - Local time is at descending node (southbound equatorial crossing)
    # >>>   - Dawn/dusk orbits (6:00/18:00) minimize solar panel shadowing
    # >>>   - Mid-morning orbits (10:00-10:30) optimal for optical imaging
    # >>>   - Afternoon orbits (13:00-14:00) good for SAR and thermal imaging
    # >>> ================================================================================
