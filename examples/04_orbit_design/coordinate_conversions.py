"""
Example: Orbit Coordinate Conversions

This example demonstrates various orbital coordinate system conversions:
1. Kepler elements to position/velocity vectors (Kepler → R/V)
2. Position/velocity vectors to Kepler elements (R/V → Kepler)
3. Kepler elements to Latitude/Longitude/Altitude at ascending node
4. Lambert transfer delta-V calculation (GEO platform to target orbit)
5. Kozai-Izsak mean elements (J2 perturbation corrections)

These conversions are essential for orbit analysis, mission planning,
and trajectory optimization.
"""

from astrox.models import KeplerElements
from astrox.orbit_convert import (
    kepler_to_rv,
    rv_to_kepler,
    kepler_to_lla_at_ascending_node,
    geo_lambert_transfer_dv,
    kozai_izsak_mean_elements,
)


# Earth gravitational parameter (m³/s²)
EARTH_MU = 3.986004418e14


def main():
    """Demonstrate all orbital coordinate conversion functions."""

    # Example 1: Kepler to R/V (ISS-like orbit)
    print("=" * 80)
    print("Example 1: Kepler Elements → Position/Velocity Vectors")
    print("=" * 80)

    print("\nInput Kepler Elements (ISS-like LEO orbit):")
    print(f"  Semi-major axis: 6,778,000 m (~400 km altitude)")
    print(f"  Eccentricity: 0.0005 (nearly circular)")
    print(f"  Inclination: 51.6°")
    print(f"  Argument of periapsis: 0.0°")
    print(f"  RAAN: 45.0°")
    print(f"  True anomaly: 30.0°")

    result = kepler_to_rv(
        semimajor_axis=6778000.0,  # m (~400 km altitude)
        eccentricity=0.0005,  # Nearly circular
        inclination=51.6,  # deg (ISS inclination)
        argument_of_periapsis=0.0,  # deg
        right_ascension_of_ascending_node=45.0,  # deg
        true_anomaly=30.0,  # deg
        gravitational_parameter=EARTH_MU
    )

    print(f"\nResult (Position and Velocity):")
    if isinstance(result, list) and len(result) >= 6:
        print(f"  Position X: {result[0]:.3f} m")
        print(f"  Position Y: {result[1]:.3f} m")
        print(f"  Position Z: {result[2]:.3f} m")
        print(f"  Velocity dX: {result[3]:.3f} m/s")
        print(f"  Velocity dY: {result[4]:.3f} m/s")
        print(f"  Velocity dZ: {result[5]:.3f} m/s")
    else:
        print(f"  {result}")

    # Example 2: R/V to Kepler (reverse conversion)
    print("\n" + "=" * 80)
    print("Example 2: Position/Velocity Vectors → Kepler Elements")
    print("=" * 80)

    # Use sample R/V from a GEO-like orbit
    position_velocity = [
        42164000.0, 0.0, 0.0,  # Position (m) - on X-axis at GEO radius
        0.0, 3074.66, 0.0  # Velocity (m/s) - circular velocity at GEO
    ]

    print(f"\nInput Position/Velocity:")
    print(f"  Position: [{position_velocity[0]:.1f}, {position_velocity[1]:.1f}, {position_velocity[2]:.1f}] m")
    print(f"  Velocity: [{position_velocity[3]:.3f}, {position_velocity[4]:.3f}, {position_velocity[5]:.3f}] m/s")

    result = rv_to_kepler(position_velocity=position_velocity)

    print(f"\nResult (Kepler Elements):")
    print(f"  {result}")

    # Example 3: Kepler to LLA at ascending node
    print("\n" + "=" * 80)
    print("Example 3: Kepler → Lat/Lon/Alt at Ascending Node")
    print("=" * 80)

    print("\nInput Kepler Elements (SSO orbit):")
    print(f"  Semi-major axis: 7,178,000 m (~800 km altitude)")
    print(f"  Eccentricity: 0.001 (nearly circular)")
    print(f"  Inclination: 98.0° (sun-synchronous)")
    print(f"  Argument of periapsis: 0.0°")
    print(f"  RAAN: 120.0°")
    print(f"  True anomaly: 0.0°")
    print(f"  Epoch: 2024-06-21T12:00:00.000Z")

    result = kepler_to_lla_at_ascending_node(
        semimajor_axis=7178000.0,  # m (~800 km altitude)
        eccentricity=0.001,  # Nearly circular
        inclination=98.0,  # deg (sun-synchronous)
        argument_of_periapsis=0.0,  # deg
        right_ascension_of_ascending_node=120.0,  # deg
        true_anomaly=0.0,  # deg
        gravitational_parameter=EARTH_MU,
        orbit_epoch="2024-06-21T12:00:00.000Z"
    )

    print(f"\nResult (LLA at Ascending Node):")
    if isinstance(result, list) and len(result) >= 3:
        print(f"  Latitude: {result[0]:.6f}°")
        print(f"  Longitude: {result[1]:.6f}°")
        print(f"  Altitude: {result[2]:.3f} m")
    else:
        print(f"  {result}")

    # Example 4: GEO Lambert transfer delta-V
    print("\n" + "=" * 80)
    print("Example 4: GEO Lambert Transfer Delta-V Calculation")
    print("=" * 80)

    # GEO platform orbit
    kepler_platform = KeplerElements(
        SemimajorAxis=42164000.0,  # m (GEO radius)
        Eccentricity=0.0,  # Circular
        Inclination=0.0,  # deg (equatorial)
        ArgumentOfPeriapsis=0.0,  # deg
        RightAscensionOfAscendingNode=0.0,  # deg
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    # Target orbit (slightly inclined GEO)
    kepler_target = KeplerElements(
        SemimajorAxis=42164000.0,  # m (same altitude)
        Eccentricity=0.0,  # Circular
        Inclination=5.0,  # deg (5° plane change)
        ArgumentOfPeriapsis=0.0,  # deg
        RightAscensionOfAscendingNode=90.0,  # deg (different RAAN)
        TrueAnomaly=0.0,  # deg
        GravitationalParameter=EARTH_MU
    )

    time_of_flight = 3600.0  # 1 hour transfer

    print(f"\nPlatform orbit (GEO):")
    print(f"  Semi-major axis: 42,164 km")
    print(f"  Inclination: 0.0°")
    print(f"  RAAN: 0.0°")

    print(f"\nTarget orbit (inclined GEO):")
    print(f"  Semi-major axis: 42,164 km")
    print(f"  Inclination: 5.0°")
    print(f"  RAAN: 90.0°")

    print(f"\nTransfer time: {time_of_flight} seconds (1 hour)")

    result = geo_lambert_transfer_dv(
        kepler_platform=kepler_platform,
        kepler_target=kepler_target,
        time_of_flight=time_of_flight
    )

    print(f"\nResult (Delta-V components):")
    print(f"  {result}")

    # Example 5: Kozai-Izsak mean elements (J2 corrections)
    print("\n" + "=" * 80)
    print("Example 5: Kozai-Izsak Mean Elements (J2 Perturbations)")
    print("=" * 80)

    print("\nInput Osculating Kepler Elements (LEO circular orbit):")
    print(f"  Semi-major axis: 6,928,000 m (~550 km altitude)")
    print(f"  Eccentricity: 0.0 (circular)")
    print(f"  Inclination: 55.0°")
    print(f"  Argument of periapsis: 0.0°")
    print(f"  RAAN: 30.0°")
    print(f"  True anomaly: 45.0°")

    result = kozai_izsak_mean_elements(
        semimajor_axis=6928000.0,  # m (~550 km altitude)
        eccentricity=0.0,  # Circular orbit
        inclination=55.0,  # deg
        argument_of_periapsis=0.0,  # deg
        right_ascension_of_ascending_node=30.0,  # deg
        true_anomaly=45.0,  # deg
        gravitational_parameter=EARTH_MU
    )

    print(f"\nResult (Mean Kepler Elements accounting for J2):")
    print(f"  {result}")
    print(f"\nNote: Mean elements account for J2 short-period perturbations,")
    print(f"      providing more stable orbital parameters for propagation.")

    print("\n" + "=" * 80)
    print("Summary of Conversion Functions:")
    print("  1. kepler_to_rv: Classical elements → Cartesian state vectors")
    print("  2. rv_to_kepler: Cartesian state vectors → Classical elements")
    print("  3. kepler_to_lla_at_ascending_node: Elements → Ground track position")
    print("  4. geo_lambert_transfer_dv: Calculate transfer maneuver delta-V")
    print("  5. kozai_izsak_mean_elements: Osculating → Mean elements (J2)")
    print("=" * 80)


if __name__ == "__main__":
    main()

    # Example output:
    # >>> ================================================================================
    # >>> Example 1: Kepler Elements → Position/Velocity Vectors
    # >>> ================================================================================
    # >>>
    # >>> Input Kepler Elements (ISS-like LEO orbit):
    # >>>   Semi-major axis: 6,778,000 m (~400 km altitude)
    # >>>   Eccentricity: 0.0005 (nearly circular)
    # >>>   Inclination: 51.6°
    # >>>   Argument of periapsis: 0.0°
    # >>>   RAAN: 45.0°
    # >>>   True anomaly: 30.0°
    # >>>
    # >>> Result (Position and Velocity):
    # >>>   Position X: 2660998.308 m
    # >>>   Position Y: 5636727.335 m
    # >>>   Position Z: 2654786.906 m
    # >>>   Velocity dX: -5629.905 m/s
    # >>>   Velocity dY: 207.360 m/s
    # >>>   Velocity dZ: 5207.697 m/s
    # >>>
    # >>> ================================================================================
    # >>> Example 2: Position/Velocity Vectors → Kepler Elements
    # >>> ================================================================================
    # >>>
    # >>> Input Position/Velocity:
    # >>>   Position: [42164000.0, 0.0, 0.0] m
    # >>>   Velocity: [0.000, 3074.660, 0.000] m/s
    # >>>
    # >>> Result (Kepler Elements):
    # >>>   {'SemimajorAxis': 42163827.647893235, 'Eccentricity': 4.087676958594802e-06, 'Inclination': 0, 'ArgumentOfPeriapsis': 180, 'RightAscensionOfAscendingNode': 0, 'TrueAnomaly': 180, 'GravitationalParameter': 398600441800000}
    # >>>
    # >>> ================================================================================
    # >>> Example 3: Kepler → Lat/Lon/Alt at Ascending Node
    # >>> ================================================================================
    # >>>
    # >>> Input Kepler Elements (SSO orbit):
    # >>>   Semi-major axis: 7,178,000 m (~800 km altitude)
    # >>>   Eccentricity: 0.001 (nearly circular)
    # >>>   Inclination: 98.0° (sun-synchronous)
    # >>>   Argument of periapsis: 0.0°
    # >>>   RAAN: 120.0°
    # >>>   True anomaly: 0.0°
    # >>>   Epoch: 2024-06-21T12:00:00.000Z
    # >>>
    # >>> Result (LLA at Ascending Node):
    # >>>   Latitude: 4.849971°
    # >>>   Longitude: -0.066663°
    # >>>   Altitude: 792685.029 m
    # >>>
    # >>> ================================================================================
    # >>> Example 4: GEO Lambert Transfer Delta-V Calculation
    # >>> ================================================================================
    # >>>
    # >>> Platform orbit (GEO):
    # >>>   Semi-major axis: 42,164 km
    # >>>   Inclination: 0.0°
    # >>>   RAAN: 0.0°
    # >>>
    # >>> Target orbit (inclined GEO):
    # >>>   Semi-major axis: 42,164 km
    # >>>   Inclination: 5.0°
    # >>>   RAAN: 90.0°
    # >>>
    # >>> Transfer time: 3600.0 seconds (1 hour)
    # >>>
    # >>> Result (Delta-V components):
    # >>>   [-14207.954217415605, 8634.823122814667, 274.2412632717466, -12029.609281278354, 11491.90043294306, -8.33619858941259]
    # >>>
    # >>> ================================================================================
    # >>> Example 5: Kozai-Izsak Mean Elements (J2 Perturbations)
    # >>> ================================================================================
    # >>>
    # >>> Input Osculating Kepler Elements (LEO circular orbit):
    # >>>   Semi-major axis: 6,928,000 m (~550 km altitude)
    # >>>   Eccentricity: 0.0 (circular)
    # >>>   Inclination: 55.0°
    # >>>   Argument of periapsis: 0.0°
    # >>>   RAAN: 30.0°
    # >>>   True anomaly: 45.0°
    # >>>
    # >>> Result (Mean Kepler Elements accounting for J2):
    # >>>   {'SemimajorAxis': 6928001.251186955, 'Eccentricity': 0.0003079965619241003, 'Inclination': 55.00000171983196, 'ArgOfPerigee': -43.31561485972555, 'RAAN': 29.97742491696035, 'MeanAnomaly': 88.28887549135636, 'ArgOfLatitude': 45.00853910300361, 'LongitudeOfPerigee': 346.6618100572348, 'MeanLongitude': 74.95068554859117}
    # >>>
    # >>> Note: Mean elements account for J2 short-period perturbations,
    # >>>       providing more stable orbital parameters for propagation.
    # >>>
    # >>> ================================================================================
    # >>> Summary of Conversion Functions:
    # >>>   1. kepler_to_rv: Classical elements → Cartesian state vectors
    # >>>   2. rv_to_kepler: Cartesian state vectors → Classical elements
    # >>>   3. kepler_to_lla_at_ascending_node: Elements → Ground track position
    # >>>   4. geo_lambert_transfer_dv: Calculate transfer maneuver delta-V
    # >>>   5. kozai_izsak_mean_elements: Osculating → Mean elements (J2)
    # >>> ================================================================================
