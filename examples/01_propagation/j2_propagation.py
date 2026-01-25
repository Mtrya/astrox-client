"""Example: J2 Perturbation Orbit Propagation

This example demonstrates orbit propagation with J2 perturbation effects.
The J2 term accounts for Earth's oblateness (equatorial bulge), which is
the largest perturbation for most Earth satellites.

J2 propagation is more accurate than two-body for longer durations and
is commonly used for mission planning.
"""

from astrox.propagator import propagate_j2


def main():
    # Earth J2 parameters
    earth_radius = 6378137.0  # WGS84 equatorial radius (m)
    j2_value = 0.000484165143790815  # Earth's J2 coefficient

    # Sun-synchronous orbit (Landsat-like)
    # SSO orbits are designed to precess due to J2 perturbation
    altitude = 705000.0  # 705 km
    semi_major_axis = earth_radius + altitude

    orbital_elements = [
        semi_major_axis,  # a = 7,083,137 m
        0.0001,           # e (nearly circular)
        98.2,             # i = 98.2° (sun-synchronous inclination)
        90.0,             # w
        0.0,              # RAAN
        0.0,              # TA
    ]

    # Propagate for 7 days to observe J2 effects
    print("Propagating sun-synchronous orbit with J2 perturbations...")
    print("This will take a moment as we're computing 7 days...\n")

    result = propagate_j2(
        start="2024-01-01T00:00:00.000Z",
        stop="2024-01-08T00:00:00.000Z",
        orbit_epoch="2024-01-01T00:00:00.000Z",
        orbital_elements=orbital_elements,
        j2_normalized_value=j2_value,
        ref_distance=earth_radius,
        step=300.0,  # 5-minute steps for weekly propagation
        coord_type="Classical",
        coord_system="Inertial",
    )

    # Print results
    print("=" * 60)
    print("J2 Propagation Results (Sun-Synchronous Orbit)")
    print("=" * 60)
    print(f"Success: {result.get('IsSuccess', 'N/A')}")
    print(f"Message: {result.get('Message', 'N/A')}")

    if 'CzmlPositions' in result:
        positions = result['CzmlPositions']
        num_points = len(positions) // 3  # Each point is [x, y, z]
        print(f"\nGenerated {num_points} position points")
        print(f"Step size: 300 seconds (5 minutes)")
        print(f"Duration: 7 days")

        # Calculate orbital period (approximate)
        mu = 3.986004418e14  # Earth's gravitational parameter (m³/s²)
        period = 2 * 3.14159 * (semi_major_axis ** 1.5) / (mu ** 0.5)
        orbits_per_day = 86400 / period

        print(f"\nOrbital period: {period:.1f} seconds ({period/60:.1f} minutes)")
        print(f"Orbits per day: {orbits_per_day:.2f}")
        print(f"Total orbits in 7 days: {orbits_per_day * 7:.1f}")

    print("\n" + "=" * 60)
    print("J2 Effects on SSO:")
    print("- The orbit plane precesses at ~0.986°/day")
    print("- This keeps the satellite in sync with the sun")
    print("- Essential for consistent lighting in imaging missions")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
Example output:
>>> Propagating sun-synchronous orbit with J2 perturbations...
>>> This will take a moment as we're computing 7 days...
>>>
>>> ============================================================
>>> J2 Propagation Results (Sun-Synchronous Orbit)
>>> ============================================================
>>> Success: True
>>> Message: Success
>>>
>>> ============================================================
>>> J2 Effects on SSO:
>>> - The orbit plane precesses at ~0.986°/day
>>> - This keeps the satellite in sync with the sun
>>> - Essential for consistent lighting in imaging missions
>>> ============================================================
"""
