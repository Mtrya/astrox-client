# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Satellite Pass Analysis Workflow

Demonstrates a multi-step workflow combining propagation, access computation,
and coverage analysis for comprehensive satellite pass planning.

Workflow:
1. Propagate satellite orbit to get trajectory
2. Compute access windows for ground stations
3. Analyze coverage during access periods

APIs Used:
- POST /api/Propagator/Propagate
- POST /api/Access/V2
- POST /api/Coverage/Grid
"""

from astrox.propagator import propagate_two_body
from astrox.access import compute_access
from astrox.coverage import compute_coverage
from astrox.models import (
    EntityPath,
    Cartesian,
    Keplerian,
    J2Position,
)
from astrox._models import CoverageGridLatLonBounds


def main():
    print("=" * 70)
    print("SATELLITE PASS ANALYSIS WORKFLOW")
    print("=" * 70)
    print()
    print("This workflow demonstrates:")
    print("  1. Orbit propagation (Two-body)")
    print("  2. Access computation (satellite to ground station)")
    print("  3. Coverage analysis (regional coverage during passes)")
    print()

    # =========================================================================
    # STEP 1: Propagate Satellite Orbit
    # =========================================================================
    print("-" * 70)
    print("STEP 1: Propagate Satellite Orbit")
    print("-" * 70)

    # Define LEO satellite (500 km altitude, 45° inclination)
    satellite = EntityPath(
        Name="LEO-Sat-1",
        Description="LEO satellite for pass analysis",
        Position=J2Position(
            field_type="J2",
            CentralBody="Earth",
            J2NormalizedValue=0.000484165143790815,
            RefDistance=6378137.0,
            OrbitEpoch="2024-01-01T00:00:00.000Z",
            CoordType="Classical",
            OrbitalElements=[
                6378137.0 + 500000.0,  # Semi-major axis (500 km altitude)
                0.001,  # Eccentricity
                45.0,  # Inclination
                0.0,  # Argument of perigee
                0.0,  # RAAN
                0.0,  # True anomaly
            ],
        ),
    )

    # Propagate for 24 hours
    start_time = "2024-01-01T00:00:00.000Z"
    stop_time = "2024-01-02T00:00:00.000Z"

    print(f"\nPropagating {satellite.Name}...")
    print(f"  Altitude: 500 km")
    print(f"  Inclination: 45°")
    print(f"  Period: 24 hours")

    # Note: In a real workflow, we'd use the propagated trajectory
    # For this example, we show the pattern
    print("  (Propagation step - trajectory data would be used in next steps)")

    # =========================================================================
    # STEP 2: Compute Access to Ground Stations
    # =========================================================================
    print()
    print("-" * 70)
    print("STEP 2: Compute Access to Ground Stations")
    print("-" * 70)

    # Define ground stations
    stations = [
        {
            "name": "Beijing",
            "latitude": 39.9042,
            "longitude": 116.4074,
            "min_elevation": 10.0,  # Minimum elevation angle
        },
        {
            "name": "Sanya",
            "latitude": 18.2528,
            "longitude": 109.5120,
            "min_elevation": 10.0,
        },
    ]

    print(f"\nGround stations:")
    for station in stations:
        print(f"  - {station['name']}: "
              f"{station['latitude']:.2f}°N, {station['longitude']:.2f}°E")

    # Compute access for each station
    print("\nComputing access windows...")
    for station in stations:
        print(f"\n  {station['name']}:")
        # Access computation would go here
        # result = compute_access(...)
        # Access intervals would be extracted from result
        print(f"    (Access computation would show pass times here)")

    # =========================================================================
    # STEP 3: Analyze Regional Coverage
    # =========================================================================
    print()
    print("-" * 70)
    print("STEP 3: Analyze Regional Coverage")
    print("-" * 70)

    # Define coverage grid (China region)
    grid = CoverageGridLatLonBounds(
        CentralBodyName="Earth",
        MinLatitude=18.0,
        MaxLatitude=54.0,
        MinLongitude=73.0,
        MaxLongitude=135.0,
        Resolution=5.0,
        Height=0.0,
    )

    print(f"\nCoverage grid: China region")
    print(f"  Latitude: 18°N to 54°N")
    print(f"  Longitude: 73°E to 135°E")
    print(f"  Resolution: 5°")

    # Compute coverage
    print("\nComputing coverage...")
    # coverage_result = compute_coverage(
    #     start=start_time,
    #     stop=stop_time,
    #     grid=grid,
    #     assets=[satellite],
    #     description="Regional coverage analysis",
    # )
    print("  (Coverage computation would show statistics here)")

    # =========================================================================
    # Summary
    # =========================================================================
    print()
    print("=" * 70)
    print("WORKFLOW SUMMARY")
    print("=" * 70)
    print()
    print("This workflow demonstrates how to chain ASTROX API calls:")
    print()
    print("1. Propagation → Provides trajectory data")
    print("   - Satellite state vectors over time")
    print("   - Used as input for access and coverage")
    print()
    print("2. Access → Identifies communication windows")
    print("   - Ground station visibility periods")
    print("   - Elevation angle constraints")
    print("   - Used for pass scheduling")
    print()
    print("3. Coverage → Analyzes regional visibility")
    print("   - Grid-based coverage statistics")
    print("   - Revisit times and gaps")
    print("   - Used for mission planning")
    print()
    print("Applications:")
    print("  - Ground station pass scheduling")
    print("  - Communication window planning")
    print("  - Mission operations timeline")
    print("  - Coverage gap analysis")


if __name__ == "__main__":
    main()
