"""
Example: Central Body Frame Conversion

This example demonstrates how to convert position data between different
central body reference frames (e.g., Earth-centered to Moon-centered).

This is essential for:
- Lunar missions (Earth → Moon frame conversion)
- Interplanetary transfers (Earth → Mars, etc.)
- Multi-body trajectory analysis
- Lagrange point calculations
"""

from astrox.models import EntityPositionCzml
from astrox.orbit_system import convert_central_body_frame


def main():
    """Demonstrate central body frame conversions."""

    # Example 1: Convert Earth-centered position to Moon-centered frame
    print("=" * 80)
    print("Example 1: Earth → Moon Frame Conversion")
    print("=" * 80)

    # Earth-centered position (sample satellite in Earth orbit)
    position = EntityPositionCzml(
        **{
            "$type": "CzmlPosition",
            "CentralBody": "Earth",
            "referenceFrame": "INERTIAL",
            "interpolationAlgorithm": "LAGRANGE",
            "interpolationDegree": 7,
            "epoch": "2024-07-20T12:00:00Z",  # Apollo 11 anniversary
            "cartesian": [
                0.0,        # Time offset 0 seconds from epoch
                6878000.0,  # X (m) - approximately LEO altitude
                0.0,        # Y (m)
                0.0         # Z (m)
            ]
        }
    )

    print(f"\nInput Position (Earth-centered):")
    print(f"  Central body: Earth")
    print(f"  Reference frame: INERTIAL")
    print(f"  Epoch: 2024-07-20T12:00:00Z")
    print(f"  Position: [6,878,000, 0, 0] m")
    print(f"  (Approximately on X-axis at LEO altitude)")

    result = convert_central_body_frame(
        position=position,
        to_body="Moon",
        reference_frame="INERTIAL",
        central_body="Earth"
    )

    print(f"\nResult (Moon-centered frame):")
    print(f"  {result}")

    # Example 2: Convert with velocity (FIXED frame)
    print("\n" + "=" * 80)
    print("Example 2: Earth → Moon with Velocity (FIXED Frame)")
    print("=" * 80)

    position_with_velocity = EntityPositionCzml(
        **{
            "$type": "CzmlPosition",
            "CentralBody": "Earth",
            "referenceFrame": "FIXED",  # Earth-fixed rotating frame
            "interpolationAlgorithm": "HERMITE",  # Better for velocity interpolation
            "interpolationDegree": 5,
            "epoch": "2024-12-15T18:30:00Z",
            "cartesianVelocity": [
                # Format: [X, Y, Z, dX, dY, dZ]
                6878000.0,  # X (m)
                0.0,        # Y (m)
                0.0,        # Z (m)
                0.0,        # dX (m/s)
                7500.0,     # dY (m/s) - approximate LEO velocity
                0.0         # dZ (m/s)
            ]
        }
    )

    print(f"\nInput Position/Velocity (Earth FIXED frame):")
    print(f"  Central body: Earth")
    print(f"  Reference frame: FIXED (Earth-rotating)")
    print(f"  Epoch: 2024-12-15T18:30:00Z")
    print(f"  Position: [6,878,000, 0, 0] m")
    print(f"  Velocity: [0, 7,500, 0] m/s")

    result = convert_central_body_frame(
        position=position_with_velocity,
        to_body="Moon",
        reference_frame="FIXED",
        central_body="Earth"
    )

    print(f"\nResult (Moon-centered FIXED frame):")
    print(f"  {result}")

    # Example 3: Convert GEO satellite to Moon frame
    print("\n" + "=" * 80)
    print("Example 3: GEO Satellite → Moon Frame")
    print("=" * 80)

    geo_position = EntityPositionCzml(
        **{
            "$type": "CzmlPosition",
            "CentralBody": "Earth",
            "referenceFrame": "INERTIAL",
            "interpolationAlgorithm": "LINEAR",
            "interpolationDegree": 1,
            "epoch": "2024-01-01T00:00:00Z",
            "cartesian": [
                42164000.0,  # X (m) - GEO radius
                0.0,         # Y (m)
                0.0          # Z (m)
            ]
        }
    )

    print(f"\nInput Position (GEO satellite):")
    print(f"  Central body: Earth")
    print(f"  Reference frame: INERTIAL")
    print(f"  Epoch: 2024-01-01T00:00:00Z")
    print(f"  Position: [42,164,000, 0, 0] m (GEO altitude)")

    result = convert_central_body_frame(
        position=geo_position,
        to_body="Moon",
        reference_frame="INERTIAL",
        central_body="Earth"
    )

    print(f"\nResult (Moon-centered frame):")
    print(f"  {result}")

    # Example 4: Time series conversion (composite position)
    print("\n" + "=" * 80)
    print("Example 4: Time Series Position Conversion")
    print("=" * 80)

    # Position with multiple time steps
    # Format: [time0, x0, y0, z0, time1, x1, y1, z1, ...]
    time_series_position = EntityPositionCzml(
        **{
            "$type": "CzmlPosition",
            "CentralBody": "Earth",
            "referenceFrame": "INERTIAL",
            "interpolationAlgorithm": "LAGRANGE",
            "interpolationDegree": 7,
            "epoch": "2024-03-20T00:00:00Z",
            "interval": "2024-03-20T00:00:00Z/2024-03-20T01:00:00Z",
            "cartesian": [
                0,          # Time offset 0 seconds
                6878000.0,  # X at t=0
                0.0,        # Y at t=0
                0.0,        # Z at t=0
                1800,       # Time offset 30 minutes (1800 seconds)
                0.0,        # X at t=1800
                6878000.0,  # Y at t=1800
                0.0,        # Z at t=1800
                3600,       # Time offset 60 minutes (3600 seconds)
                -6878000.0, # X at t=3600
                0.0,        # Y at t=3600
                0.0         # Z at t=3600
            ]
        }
    )

    print(f"\nInput Position (time series, 3 points):")
    print(f"  Central body: Earth")
    print(f"  Reference frame: INERTIAL")
    print(f"  Epoch: 2024-03-20T00:00:00Z")
    print(f"  Interval: 2024-03-20T00:00:00Z to 2024-03-20T01:00:00Z")
    print(f"  Points: 3 positions over 1 hour")
    print(f"    t=0s:    [6,878,000, 0, 0] m")
    print(f"    t=1800s: [0, 6,878,000, 0] m")
    print(f"    t=3600s: [-6,878,000, 0, 0] m")

    result = convert_central_body_frame(
        position=time_series_position,
        to_body="Moon",
        reference_frame="INERTIAL",
        central_body="Earth"
    )

    print(f"\nResult (Moon-centered frame, time series):")
    print(f"  {result}")

    # Example 5: Direct cartesian input (simplified API)
    print("\n" + "=" * 80)
    print("Example 5: Simple Cartesian Conversion (Direct Input)")
    print("=" * 80)

    print(f"\nInput (Direct cartesian array):")
    print(f"  Position: [10,000,000, 5,000,000, 2,000,000] m")
    print(f"  Epoch: 2024-06-01T12:00:00Z")

    # Using the alternative parameter-based API
    result = convert_central_body_frame(
        position=EntityPositionCzml(
            **{
                "$type": "CzmlPosition",
                "CentralBody": "Earth",
                "referenceFrame": "INERTIAL",
                "epoch": "2024-06-01T12:00:00Z"
            }
        ),
        to_body="Moon",
        cartesian=[10000000.0, 5000000.0, 2000000.0],
        epoch="2024-06-01T12:00:00Z"
    )

    print(f"\nResult (Moon-centered):")
    print(f"  {result}")

    print("\n" + "=" * 80)
    print("Notes on Frame Conversions:")
    print("  - INERTIAL: Non-rotating inertial reference frame")
    print("  - FIXED: Body-fixed rotating reference frame")
    print("  - J2000/ICRF: Standard inertial frames at J2000 epoch")
    print("  - Interpolation algorithms:")
    print("    LINEAR: Fast, simple interpolation")
    print("    LAGRANGE: Higher-order polynomial interpolation")
    print("    HERMITE: Cubic spline (best for velocity data)")
    print("  - Time series format: [t0,x0,y0,z0, t1,x1,y1,z1, ...]")
    print("  - Velocity format: [x,y,z,dx,dy,dz] or time series variant")
    print("=" * 80)


if __name__ == "__main__":
    main()
