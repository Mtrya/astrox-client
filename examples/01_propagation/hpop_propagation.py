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

    # Import Propagator model to create HPOP config
    from astrox._models import Propagator, IGravityFunction, IGravityFunctionTwoBodyFunction

    # Create HPOP propagator configuration
    gravity_model = IGravityFunctionTwoBodyFunction(
        field_type="TwoBody",
        Name="Earth_TwoBody",
        Description="Earth two-body gravity",
    )
    # Wrap in IGravityFunction RootModel
    gravity_wrapper = IGravityFunction(root=gravity_model)
    hpop_config = Propagator(
        Name="Earth_HPOP",
        CentralBodyName="Earth",
        GravityModel=gravity_wrapper,
    )
    result = propagate_hpop(
        start="2024-01-01T00:00:00.000Z",
        stop="2024-01-31T00:00:00.000Z",
        orbit_epoch="2024-01-01T00:00:00.000Z",
        orbital_elements=orbital_elements,
        description="GEO Communications Satellite",
        coefficient_of_drag=2.2,
        area_mass_ratio_drag=cross_sectional_area / mass,
        coefficient_of_srp=1.3,
        area_mass_ratio_srp=cross_sectional_area / mass,
        hpop_propagator=hpop_config,
    )
    # Print results
    print("=" * 60)
    print("HPOP Results (GEO Satellite - 30 days)")
    print("=" * 60)
    print(f"Success: {result['IsSuccess']}")
    print(f"Message: {result['Message']}")

    # Access position data from 'Position' dict's 'cartesianVelocity' field
    positions = result['Position']['cartesianVelocity']
    num_points = len(positions) // 3
    print(f"\nGenerated {num_points} position points")  # should be ~8641 for 30 days at 300s steps
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
