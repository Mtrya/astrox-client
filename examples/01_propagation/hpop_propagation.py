"""Example: High-Precision Orbit Propagation (HPOP)

This example demonstrates high-precision orbit propagation that includes
multiple perturbation effects:
- Earth gravity harmonics (beyond J2)
- Atmospheric drag
- Solar radiation pressure
- Third-body perturbations

HPOP is the most accurate propagator and is used for precision applications
like collision avoidance and long-term orbit predictions.
"""

from astrox.propagator import propagate_hpop


def main():
    # GEO satellite (geostationary orbit)
    # These orbits are particularly sensitive to SRP and third-body effects
    earth_radius = 6378137.0  # meters
    geo_altitude = 35786000.0  # 35,786 km
    semi_major_axis = earth_radius + geo_altitude

    orbital_elements = [
        semi_major_axis,  # a = 42,164,137 m
        0.0001,           # e (nearly circular)
        0.05,             # i = 0.05° (nearly equatorial)
        0.0,              # w
        75.0,             # RAAN = 75° E
        0.0,              # TA
    ]

    # Spacecraft physical properties for perturbation modeling
    # These affect drag and solar radiation pressure
    mass = 2000.0  # kg (typical GEO comsat)
    cross_sectional_area = 20.0  # m² (solar panels + body)

    print("Propagating GEO satellite with high-precision model...")
    print("Including: gravity harmonics, drag, SRP, third-body effects")
    print("This may take longer due to the complexity of the model...\n")

    # Propagate for 30 days
    result = propagate_hpop(
        start="2024-01-01T00:00:00.000Z",
        stop="2024-01-31T00:00:00.000Z",
        orbit_epoch="2024-01-01T00:00:00.000Z",
        orbital_elements=orbital_elements,
        description="GEO Communications Satellite",
        coord_type="Classical",
        coord_system="Inertial",
        # Drag parameters (minimal at GEO altitude but still included)
        coefficient_of_drag=2.2,  # Typical for satellites
        area_mass_ratio_drag=cross_sectional_area / mass,  # 0.01 m²/kg
        # Solar radiation pressure parameters
        coefficient_of_srp=1.3,  # Accounting for reflectivity
        area_mass_ratio_srp=cross_sectional_area / mass,  # 0.01 m²/kg
        step=3600.0,  # 1-hour steps for monthly propagation
    )

    # Print results
    print("=" * 60)
    print("HPOP Results (GEO Satellite - 30 days)")
    print("=" * 60)
    print(f"Success: {result.get('IsSuccess', 'N/A')}")
    print(f"Message: {result.get('Message', 'N/A')}")

    if 'CzmlPositions' in result:
        positions = result['CzmlPositions']
        num_points = len(positions) // 3
        print(f"\nGenerated {num_points} position points")
        print(f"Step size: 3600 seconds (1 hour)")
        print(f"Duration: 30 days")

        # GEO orbital period should be very close to sidereal day
        geo_period_hours = 23.934  # sidereal day

        print(f"\nGEO orbital period: {geo_period_hours:.3f} hours")
        print(f"Station-keeping requirements: ±0.05° in lat/lon")

        # Calculate drift over 30 days (illustrative)
        print(f"\nPerturbation effects over 30 days:")
        print(f"- Solar radiation pressure: ~10-50 m/s² drift")
        print(f"- Luni-solar gravity: ~5 m/s² inclination change")
        print(f"- Earth triaxiality: ~0.85°/year longitude drift")

    print("\n" + "=" * 60)
    print("HPOP Advantages:")
    print("- Highest accuracy for long-term predictions")
    print("- Essential for collision avoidance calculations")
    print("- Includes all major perturbations")
    print("- Required for station-keeping analysis")
    print()
    print("Trade-offs:")
    print("- Slower computation than J2 or two-body")
    print("- Requires accurate spacecraft physical properties")
    print("=" * 60)


if __name__ == "__main__":
    main()
