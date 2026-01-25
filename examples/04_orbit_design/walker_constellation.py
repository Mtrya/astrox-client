"""
Example: Generate Walker Constellation

This example demonstrates how to design Walker constellations, which are
symmetric satellite distributions used for global coverage (GPS, Galileo, etc.).

Walker notation: T/P/F where:
- T = Total number of satellites
- P = Number of orbital planes
- F = Phase factor (relative phasing between planes)

Common constellations:
- GPS: 24/6/1 (24 satellites, 6 planes, phase factor 1)
- Galileo: 27/3/1 (27 satellites, 3 planes, phase factor 1)
- OneWeb: 648/18/1 (648 satellites, 18 planes, phase factor 1)
"""

from astrox.models import KeplerElements
from astrox.orbit_wizard import design_walker


# Earth gravitational parameter (m³/s²)
EARTH_MU = 3.986004418e14


def main():
    """Generate Walker constellations with different configurations."""

    # Example 1: GPS-like constellation (24:6:1 Delta pattern)
    print("=" * 80)
    print("Example 1: GPS-like Walker Delta Constellation (24:6:1)")
    print("=" * 80)

    # Seed orbit: MEO at ~20,200 km altitude, 55° inclination
    seed_kepler = KeplerElements(
        SemimajorAxis=26560000.0,  # ~20,200 km altitude (m)
        Eccentricity=0.0,  # Circular orbit
        Inclination=55.0,  # deg
        ArgumentOfPeriapsis=0.0,  # deg (circular, so doesn't matter)
        RightAscensionOfAscendingNode=0.0,  # deg (seed plane)
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    result = design_walker(
        seed_kepler=seed_kepler,
        num_planes=6,
        num_sats_per_plane=4,  # 6 planes × 4 sats = 24 total
        walker_type="Delta",
        inter_plane_phase_increment=1,  # Phase factor F=1
    )

    print(f"\nWalker Constellation: 24:6:1 (GPS-like)")
    print(f"  Total satellites: 24")
    print(f"  Number of planes: 6")
    print(f"  Satellites per plane: 4")
    print(f"  Pattern: Delta")
    print(f"  Phase factor: 1")
    print(f"\nSeed orbit:")
    print(f"  Altitude: ~20,200 km")
    print(f"  Inclination: 55.0°")
    print(f"  Eccentricity: 0.0 (circular)")
    print(f"\nResult keys: {list(result.keys())}")
    print(f"Full result:\n{result}")

    # Example 2: Smaller LEO constellation (18:3:1 Delta pattern)
    print("\n" + "=" * 80)
    print("Example 2: LEO Walker Delta Constellation (18:3:1)")
    print("=" * 80)

    # Seed orbit: LEO at 1000 km altitude, 87° inclination (near-polar)
    seed_kepler = KeplerElements(
        SemimajorAxis=7378000.0,  # 1000 km altitude (Earth radius ~6378 km)
        Eccentricity=0.0,  # Circular orbit
        Inclination=87.0,  # deg (near-polar for global coverage)
        ArgumentOfPeriapsis=0.0,  # deg
        RightAscensionOfAscendingNode=0.0,  # deg
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    result = design_walker(
        seed_kepler=seed_kepler,
        num_planes=3,
        num_sats_per_plane=6,  # 3 planes × 6 sats = 18 total
        walker_type="Delta",
        inter_plane_phase_increment=1,  # Phase factor F=1
    )

    print(f"\nWalker Constellation: 18:3:1")
    print(f"  Total satellites: 18")
    print(f"  Number of planes: 3")
    print(f"  Satellites per plane: 6")
    print(f"  Pattern: Delta")
    print(f"  Phase factor: 1")
    print(f"\nSeed orbit:")
    print(f"  Altitude: 1000 km")
    print(f"  Inclination: 87.0° (near-polar)")
    print(f"\nFull result:\n{result}")

    # Example 3: Polar constellation (12:4:1 Delta pattern)
    print("\n" + "=" * 80)
    print("Example 3: Polar Walker Delta Constellation (12:4:1)")
    print("=" * 80)

    # Seed orbit: LEO at 600 km altitude, 90° inclination (polar)
    seed_kepler = KeplerElements(
        SemimajorAxis=6978000.0,  # 600 km altitude
        Eccentricity=0.0,  # Circular orbit
        Inclination=90.0,  # deg (polar orbit)
        ArgumentOfPeriapsis=0.0,  # deg
        RightAscensionOfAscendingNode=0.0,  # deg
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    result = design_walker(
        seed_kepler=seed_kepler,
        num_planes=4,
        num_sats_per_plane=3,  # 4 planes × 3 sats = 12 total
        walker_type="Delta",
        inter_plane_phase_increment=1,  # Phase factor F=1 (must be 1 to num_planes-1)
    )

    print(f"\nWalker Constellation: 12:4:1")
    print(f"  Total satellites: 12")
    print(f"  Number of planes: 4")
    print(f"  Satellites per plane: 3")
    print(f"  Pattern: Delta")
    print(f"  Phase factor: 1")
    print(f"\nSeed orbit:")
    print(f"  Altitude: 600 km")
    print(f"  Inclination: 90.0° (polar)")
    print(f"\nFull result:\n{result}")

    # Example 4: Custom constellation with manual spacing
    print("\n" + "=" * 80)
    print("Example 4: Custom Walker Constellation (8 satellites)")
    print("=" * 80)

    # Seed orbit: MEO at 10,000 km altitude, 60° inclination
    seed_kepler = KeplerElements(
        SemimajorAxis=16378000.0,  # 10,000 km altitude
        Eccentricity=0.0,  # Circular orbit
        Inclination=60.0,  # deg
        ArgumentOfPeriapsis=0.0,  # deg
        RightAscensionOfAscendingNode=0.0,  # deg
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    result = design_walker(
        seed_kepler=seed_kepler,
        num_planes=2,
        num_sats_per_plane=4,  # 2 planes × 4 sats = 8 total
        walker_type="Custom",
        inter_plane_true_anomaly_increment=45.0,  # deg spacing in true anomaly
        raan_increment=90.0,  # deg spacing between planes
    )

    print(f"\nCustom Walker Constellation:")
    print(f"  Total satellites: 8")
    print(f"  Number of planes: 2")
    print(f"  Satellites per plane: 4")
    print(f"  Pattern: Custom")
    print(f"  True anomaly increment: 45.0°")
    print(f"  RAAN increment: 90.0°")
    print(f"\nSeed orbit:")
    print(f"  Altitude: 10,000 km")
    print(f"  Inclination: 60.0°")
    print(f"\nFull result:\n{result}")

    # Example 5: Star pattern constellation
    print("\n" + "=" * 80)
    print("Example 5: Walker Star Constellation (9:3:2)")
    print("=" * 80)

    # Seed orbit: LEO at 800 km altitude, 75° inclination
    seed_kepler = KeplerElements(
        SemimajorAxis=7178000.0,  # 800 km altitude
        Eccentricity=0.0,  # Circular orbit
        Inclination=75.0,  # deg
        ArgumentOfPeriapsis=0.0,  # deg
        RightAscensionOfAscendingNode=0.0,  # deg
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    result = design_walker(
        seed_kepler=seed_kepler,
        num_planes=3,
        num_sats_per_plane=3,  # 3 planes × 3 sats = 9 total
        walker_type="Star",
        inter_plane_phase_increment=2,  # Phase factor F=2
    )

    print(f"\nWalker Constellation: 9:3:2 (Star)")
    print(f"  Total satellites: 9")
    print(f"  Number of planes: 3")
    print(f"  Satellites per plane: 3")
    print(f"  Pattern: Star")
    print(f"  Phase factor: 2")
    print(f"\nSeed orbit:")
    print(f"  Altitude: 800 km")
    print(f"  Inclination: 75.0°")
    print(f"\nFull result:\n{result}")

    print("\n" + "=" * 80)
    print("Notes on Walker Constellations:")
    print("  - Delta pattern: Most common, provides uniform coverage")
    print("  - Star pattern: Alternative symmetric distribution")
    print("  - Custom pattern: Manual control over spacing")
    print("  - Phase factor F: Controls relative phasing between planes")
    print("    IMPORTANT: F must be in range [1, num_planes-1]")
    print("    F cannot be 0 or >= num_planes")
    print("    For 4 planes: valid F values are 1, 2, 3")
    print("    For 6 planes: valid F values are 1, 2, 3, 4, 5")
    print("  - RAAN spacing: Planes equally distributed around equator")
    print("  - True anomaly: Satellites equally spaced within each plane")
    print("=" * 80)


if __name__ == "__main__":
    main()


"""
>>> ================================================================================
>>> Example 1: GPS-like Walker Delta Constellation (24:6:1)
>>> ================================================================================
>>>
>>> Walker Constellation: 24:6:1 (GPS-like)
>>>   Total satellites: 24
>>>   Number of planes: 6
>>>   Satellites per plane: 4
>>>   Pattern: Delta
>>>   Phase factor: 1
>>>
>>> Seed orbit:
>>>   Altitude: ~20,200 km
>>>   Inclination: 55.0°
>>>   Eccentricity: 0.0 (circular)
>>>
>>> Result keys: ['IsSuccess', 'Message', 'WalkerSatellites']
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'WalkerSatellites': [[{'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 90, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 180, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 270, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 15, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 105, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 195, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 285, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 30, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 120, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 210, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 300, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 45, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 135, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 225, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 315, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 60, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 150, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 240, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 330, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 300, 'TrueAnomaly': 75, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 300, 'TrueAnomaly': 165, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 300, 'TrueAnomaly': 255, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 26560000, 'Eccentricity': 0, 'Inclination': 55, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 300, 'TrueAnomaly': 345, 'GravitationalParameter': 398600441800000}]]}
>>>
>>> ================================================================================
>>> Example 2: LEO Walker Delta Constellation (18:3:1)
>>> ================================================================================
>>>
>>> Walker Constellation: 18:3:1
>>>   Total satellites: 18
>>>   Number of planes: 3
>>>   Satellites per plane: 6
>>>   Pattern: Delta
>>>   Phase factor: 1
>>>
>>> Seed orbit:
>>>   Altitude: 1000 km
>>>   Inclination: 87.0° (near-polar)
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'WalkerSatellites': [[{'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 60, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 120, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 180, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 240, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 300, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 20, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 80, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 140, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 200, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 260, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 320, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 40, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 100, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 160, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 220, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 280, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7378000, 'Eccentricity': 0, 'Inclination': 87, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 240, 'TrueAnomaly': 340, 'GravitationalParameter': 398600441800000}]]}
>>>
>>> ================================================================================
>>> Example 3: Polar Walker Delta Constellation (12:4:1)
>>> ================================================================================
>>>
>>> Walker Constellation: 12:4:1
>>>   Total satellites: 12
>>>   Number of planes: 4
>>>   Satellites per plane: 3
>>>   Pattern: Delta
>>>   Phase factor: 1
>>>
>>> Seed orbit:
>>>   Altitude: 600 km
>>>   Inclination: 90.0° (polar)
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'WalkerSatellites': [[{'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 120, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 240, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 30, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 150, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 270, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 60, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 180, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 180, 'TrueAnomaly': 300, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 270, 'TrueAnomaly': 90, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 270, 'TrueAnomaly': 210, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 6978000, 'Eccentricity': 0, 'Inclination': 90, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 270, 'TrueAnomaly': 330, 'GravitationalParameter': 398600441800000}]]}
>>>
>>> ================================================================================
>>> Example 4: Custom Walker Constellation (8 satellites)
>>> ================================================================================
>>>
>>> Custom Walker Constellation:
>>>   Total satellites: 8
>>>   Number of planes: 2
>>>   Satellites per plane: 4
>>>   Pattern: Custom
>>>   True anomaly increment: 45.0°
>>>   RAAN increment: 90.0°
>>>
>>> Seed orbit:
>>>   Altitude: 10,000 km
>>>   Inclination: 60.0°
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'WalkerSatellites': [[{'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 90, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 180, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 270, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 45, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 135, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 225, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 16378000, 'Eccentricity': 0, 'Inclination': 60, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 90, 'TrueAnomaly': 315, 'GravitationalParameter': 398600441800000}]]}
>>>
>>> ================================================================================
>>> Example 5: Walker Star Constellation (9:3:2)
>>> ================================================================================
>>>
>>> Walker Constellation: 9:3:2 (Star)
>>>   Total satellites: 9
>>>   Number of planes: 3
>>>   Satellites per plane: 3
>>>   Pattern: Star
>>>   Phase factor: 2
>>>
>>> Seed orbit:
>>>   Altitude: 800 km
>>>   Inclination: 75.0°
>>>
>>> Full result:
>>> {'IsSuccess': True, 'Message': 'Success!', 'WalkerSatellites': [[{'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 0, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 120, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 240, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 80, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 200, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 60, 'TrueAnomaly': 320, 'GravitationalParameter': 398600441800000}], [{'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 160, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 280, 'GravitationalParameter': 398600441800000}, {'SemimajorAxis': 7178000, 'Eccentricity': 0, 'Inclination': 75, 'ArgumentOfPeriapsis': 0, 'RightAscensionOfAscendingNode': 120, 'TrueAnomaly': 40, 'GravitationalParameter': 398600441800000}]]}
>>>
>>> ================================================================================
>>> Notes on Walker Constellations:
>>>   - Delta pattern: Most common, provides uniform coverage
>>>   - Star pattern: Alternative symmetric distribution
>>>   - Custom pattern: Manual control over spacing
>>>   - Phase factor F: Controls relative phasing between planes
>>>     IMPORTANT: F must be in range [1, num_planes-1]
>>>     F cannot be 0 or >= num_planes
>>>     For 4 planes: valid F values are 1, 2, 3
>>>     For 6 planes: valid F values are 1, 2, 3, 4, 5
>>>   - RAAN spacing: Planes equally distributed around equator
>>>   - True anomaly: Satellites equally spaced within each plane
>>> ================================================================================
"""
