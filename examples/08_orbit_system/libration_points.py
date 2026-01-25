"""
Example: Earth-Moon Libration (Lagrange) Points

This example demonstrates how to calculate the five Earth-Moon Lagrange points
(L1, L2, L3, L4, L5). These are points of gravitational equilibrium in the
Earth-Moon system, crucial for mission planning to:

- L1: Gateway to Moon, solar observation (between Earth and Moon)
- L2: Far-side Moon communications, deep space observation
- L3: Opposite Moon's orbit, research purposes
- L4/L5: Trojan points, stable locations for space stations

Lagrange points are used for missions like:
- NASA's Artemis Lunar Gateway (Near Rectilinear Halo Orbit around L2)
- James Webb Space Telescope (Sun-Earth L2)
- Future communication relays and space stations
"""

from astrox.orbit_system import compute_earth_moon_libration


def main():
    """Calculate Earth-Moon Lagrange points at different epochs."""

    # Example 1: Compute libration points at J2000 epoch (v2 API)
    print("=" * 80)
    print("Example 1: Earth-Moon Libration Points (J2000 Epoch, v2 API)")
    print("=" * 80)

    epoch = "2000-01-01T12:00:00Z"  # J2000 standard epoch

    print(f"\nInput:")
    print(f"  Epoch: {epoch} (J2000)")
    print(f"  Version: v2 (default)")
    print(f"  Central body: Earth (default)")
    print(f"  Reference frame: FIXED (default)")
    print(f"  Interpolation: LAGRANGE order 7 (default)")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v2"
    )

    print(f"\nResult (All 5 Lagrange Points):")
    print(f"  {result}")
    print(f"\nExpected approximate locations (Earth-centered FIXED frame):")
    print(f"  L1: ~326,000 km from Earth (toward Moon)")
    print(f"  L2: ~449,000 km from Earth (beyond Moon)")
    print(f"  L3: ~381,000 km from Earth (opposite Moon)")
    print(f"  L4/L5: ~384,400 km from Earth (±60° from Moon in orbit)")

    # Example 2: Specific epoch (current era)
    print("\n" + "=" * 80)
    print("Example 2: Libration Points at Specific Epoch (2024)")
    print("=" * 80)

    epoch = "2024-07-20T20:17:00Z"  # Apollo 11 landing anniversary

    print(f"\nInput:")
    print(f"  Epoch: {epoch} (Apollo 11 anniversary)")
    print(f"  Version: v2")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v2"
    )

    print(f"\nResult:")
    print(f"  {result}")

    # Example 3: Using INERTIAL frame
    print("\n" + "=" * 80)
    print("Example 3: Libration Points in INERTIAL Frame")
    print("=" * 80)

    epoch = "2024-12-31T00:00:00Z"

    print(f"\nInput:")
    print(f"  Epoch: {epoch}")
    print(f"  Reference frame: INERTIAL (non-rotating)")
    print(f"  Version: v2")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v2",
        reference_frame="INERTIAL"
    )

    print(f"\nResult (INERTIAL frame):")
    print(f"  {result}")
    print(f"\nNote: INERTIAL coordinates don't rotate with Earth,")
    print(f"      useful for trajectory planning and analysis.")

    # Example 4: Using v1 API (alternative endpoint)
    print("\n" + "=" * 80)
    print("Example 4: Libration Points (v1 API)")
    print("=" * 80)

    epoch = "2024-03-20T00:00:00Z"  # Vernal equinox

    print(f"\nInput:")
    print(f"  Epoch: {epoch} (Vernal equinox)")
    print(f"  Version: v1 (legacy endpoint)")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v1"
    )

    print(f"\nResult (v1 API):")
    print(f"  {result}")

    # Example 5: Custom interpolation settings
    print("\n" + "=" * 80)
    print("Example 5: Custom Interpolation Settings")
    print("=" * 80)

    epoch = "2024-06-21T00:00:00Z"  # Summer solstice

    print(f"\nInput:")
    print(f"  Epoch: {epoch} (Summer solstice)")
    print(f"  Interpolation algorithm: HERMITE")
    print(f"  Interpolation degree: 5")
    print(f"  Reference frame: FIXED")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v2",
        interpolation_algorithm="HERMITE",
        interpolation_degree=5,
        reference_frame="FIXED"
    )

    print(f"\nResult:")
    print(f"  {result}")

    # Example 6: Moon-centered frame
    print("\n" + "=" * 80)
    print("Example 6: Libration Points (Moon-centered Frame)")
    print("=" * 80)

    epoch = "2024-09-23T00:00:00Z"  # Autumnal equinox

    print(f"\nInput:")
    print(f"  Epoch: {epoch} (Autumnal equinox)")
    print(f"  Central body: Moon")
    print(f"  Reference frame: FIXED")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v2",
        central_body="Moon",
        reference_frame="FIXED"
    )

    print(f"\nResult (Moon-centered):")
    print(f"  {result}")
    print(f"\nNote: Moon-centered coordinates show Lagrange points")
    print(f"      relative to lunar surface, useful for:")
    print(f"      - Gateway orbit design")
    print(f"      - Lunar far-side communications")
    print(f"      - Halo orbit planning")

    # Example 7: Time interval (composite position)
    print("\n" + "=" * 80)
    print("Example 7: Libration Points with Time Interval")
    print("=" * 80)

    epoch = "2025-01-01T00:00:00Z"
    interval = "2025-01-01T00:00:00Z/2025-01-02T00:00:00Z"

    print(f"\nInput:")
    print(f"  Epoch: {epoch}")
    print(f"  Interval: {interval} (24 hours)")
    print(f"  Version: v2")

    result = compute_earth_moon_libration(
        epoch=epoch,
        version="v2",
        interval=interval
    )

    print(f"\nResult (with time interval):")
    print(f"  {result}")

    print("\n" + "=" * 80)
    print("Earth-Moon Lagrange Points Overview:")
    print("=" * 80)
    print("\nL1 (Unstable, ~326,000 km from Earth):")
    print("  - Between Earth and Moon")
    print("  - Gateway to lunar operations")
    print("  - Solar observation missions")
    print("  - Requires station-keeping: ~2-5 m/s/year delta-V")
    print("\nL2 (Unstable, ~449,000 km from Earth):")
    print("  - Beyond Moon from Earth")
    print("  - Lunar far-side communications relay")
    print("  - Deep space observation")
    print("  - Artemis Gateway baseline orbit (NRHO)")
    print("  - Requires station-keeping: ~2-5 m/s/year delta-V")
    print("\nL3 (Unstable, ~381,000 km from Earth):")
    print("  - Opposite Moon's orbit from Earth")
    print("  - Limited practical use")
    print("  - Research and theoretical interest")
    print("\nL4/L5 (Stable, ~384,400 km from Earth, ±60° from Moon):")
    print("  - Stable equilibrium points (Trojan points)")
    print("  - Natural dust/debris accumulation (Kordylewski clouds)")
    print("  - Potential space station locations")
    print("  - Only ~10 m/s/year station-keeping needed")
    print("\nApplications:")
    print("  - NASA Artemis Lunar Gateway (NRHO near L2)")
    print("  - Communication relays for lunar far side")
    print("  - Staging points for deep space missions")
    print("  - Long-duration space habitats (L4/L5)")
    print("=" * 80)


if __name__ == "__main__":
    main()

    # Example output (when server-side error occurs):
    # >>> ================================================================================
    # >>> Example 1: Earth-Moon Libration Points (J2000 Epoch, v2 API)
    # >>> ================================================================================
    # >>>
    # >>> Input:
    # >>>   Epoch: 2000-01-01T12:00:00Z (J2000)
    # >>>   Version: v2 (default)
    # >>>   Central body: Earth (default)
    # >>>   Reference frame: FIXED (default)
    # >>>   Interpolation: LAGRANGE order 7 (default)
    # >>>
    # >>> Traceback (most recent call last):
    # >>>   File "/home/betelgeuse/Developments/astrox-client/examples/08_orbit_system/libration_points.py", line 218, in <module>
    # >>>     main()
    # >>>   File "/home/betelgeuse/Developments/astrox-client/examples/08_orbit_system/libration_points.py", line 39, in main
    # >>>     result = compute_earth_moon_libration(
    # >>>         epoch=epoch,
    # >>>         version="v2"
    # >>>     )
    # >>>   File "/home/betelgeuse/Developments/astrox-client/astrox/orbit_system.py", line 141, in compute_earth_moon_libration
    # >>>     return sess.post(endpoint=endpoint, data=payload)
    # >>>   File "/home/betelgeuse/Developments/astrox-client/astrox/_http.py", line 284, in post
    # >>>     result = _make_request(
    # >>>         endpoint=endpoint,
    # >>>         method="POST",
    # >>>         json=payload
    # >>>     )
    # >>>   File "/home/betelgeuse/Developments/astrox-client/astrox/_http.py", line 124, in _make_request
    # >>>     raise exceptions.AstroxAPIError(
    # >>>         f"API error ({response.status_code}): {message}"
    # >>>     ) from e
    # >>> astrox.exceptions.AstroxAPIError:    at AeroSpace.Models.EntityPositionCzml.GetDateMotionCollection()
    # >>>    at AeroSpace.Models.EntityPositionCzml.CreatePoint()
    # >>>    at AeroSpace.OrbitConverter.OrbitSystem.GetPosInEarthMoonLibrationFrame2(EntityPositionCzml input)
