"""Example: Two-Body Orbit Propagation

This example demonstrates how to propagate a satellite orbit using simple
two-body dynamics (no perturbations). Two-body propagation is the fastest
method and works well for short-duration predictions.

We'll propagate the ISS orbit for one day using classical orbital elements.
"""

from astrox.propagator import propagate_two_body


def main():
    # ISS orbital parameters (approximate LEO orbit)
    # Classical orbital elements: [a, e, i, w, RAAN, TA]
    # a = semi-major axis (m)
    # e = eccentricity
    # i = inclination (deg)
    # w = argument of periapsis (deg)
    # RAAN = right ascension of ascending node (deg)
    # TA = true anomaly (deg)

    earth_radius = 6378137.0  # meters
    altitude = 408000.0  # 408 km altitude
    semi_major_axis = earth_radius + altitude

    orbital_elements = [
        semi_major_axis,  # a = 6,786,137 m
        0.0001882,        # e (nearly circular)
        51.6461,          # i = 51.6° (ISS inclination)
        64.8995,          # w
        339.8014,         # RAAN
        295.2305,         # TA
    ]

    # Propagate for 1 day with 60-second steps
    result = propagate_two_body(
        start="2024-01-01T00:00:00.000Z",
        stop="2024-01-02T00:00:00.000Z",
        orbit_epoch="2024-01-01T00:00:00.000Z",
        orbital_elements=orbital_elements,
        step=60.0,  # Output every 60 seconds
        coord_type="Classical",  # Using classical orbital elements
        coord_system="Inertial",  # Earth inertial frame
    )

    # Print basic results
    print("=" * 60)
    print("Two-Body Propagation Results (ISS Orbit)")
    print("=" * 60)
    print(f"Success: {result['IsSuccess']}")
    print(f"Message: {result['Message']}")

    # Access position data from 'Position' dict's 'cartesianVelocity' field
    positions = result['Position']['cartesianVelocity']
    num_points = len(positions) // 3
    print(f"\nGenerated {num_points} position points")  # should be 1441 for 1 day at 60s steps
    print(f"Step size: 60 seconds")
    print(f"Duration: 1 day")

    # Show first and last positions
    if num_points > 0:
        print(f"\nFirst position (epoch):")
        print(f"  {positions[:3]}")  # First 3 values: x, y, z
        print(f"\nLast position (after 1 day):")
        print(f"  {positions[-3:]}")  # Last 3 values

    print("\n" + "=" * 60)
    print("Note: Two-body propagation ignores perturbations like J2,")
    print("atmospheric drag, and solar radiation pressure. For more")
    print("accurate results, use J2 or HPOP propagation.")
    print("=" * 60)


if __name__ == "__main__":
    main()
