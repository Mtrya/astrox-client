"""
Coverage Statistics and Reporting Example

Demonstrates:
- report_coverage_by_asset() - Coverage percentage report for each satellite
- report_percent_coverage() - Overall coverage percentage over time

These functions provide statistical summaries of coverage performance:
- Per-asset metrics: min/max/average/cumulative coverage for each satellite
- Time-series metrics: instantaneous and cumulative coverage over time
"""

from __future__ import annotations

from astrox.coverage import report_coverage_by_asset, report_percent_coverage
from astrox.models import (
    EntityPath,
    J2Position,
)
from astrox._models import (
    CoverageGridLatitudeBounds,
    CoverageGridLatLonBounds,
)


def create_regional_constellation():
    """Create a 4-satellite regional constellation for Asia-Pacific coverage."""
    satellites = []

    # Regional constellation optimized for Asia-Pacific (30°N latitude)
    # Using inclined geosynchronous orbits (Tundra-like)
    altitude = 35786000.0  # GEO altitude
    sma = 6378137.0 + altitude

    for i in range(4):
        longitude_spacing = 90.0  # 90° spacing in longitude
        raan = i * longitude_spacing

        satellite = EntityPath(
            Name=f"Regional-Sat{i + 1}",
            Description=f"Regional satellite {i + 1} (RAAN={raan}°)",
            Position=J2Position(
                **{'$type': 'J2'},
                CentralBody="Earth",
                J2NormalizedValue=0.000484165143790815,
                RefDistance=6378137.0,
                OrbitEpoch="2024-01-01T00:00:00.000Z",
                CoordSystem="Inertial",
                CoordType="Classical",
                OrbitalElements=[
                    sma,        # Semi-major axis (m)
                    0.001,      # Eccentricity
                    30.0,       # Inclination (deg)
                    270.0,      # Argument of periapsis (deg)
                    raan,       # RAAN (deg)
                    0.0,        # True anomaly (deg)
                ],
            ),
        )
        satellites.append(satellite)

    return satellites


def create_leo_constellation():
    """Create a 9-satellite LEO constellation (3 planes, 3 sats/plane)."""
    satellites = []

    altitude = 700000.0  # 700 km
    sma = 6378137.0 + altitude
    inclination = 60.0

    for plane in range(3):
        raan = plane * 120.0  # 120° between planes
        for sat in range(3):
            ta = sat * 120.0  # 120° between sats in plane

            satellite = EntityPath(
                Name=f"LEO-P{plane + 1}S{sat + 1}",
                Description=f"LEO Plane {plane + 1}, Sat {sat + 1}",
                Position=J2Position(
                    **{'$type': 'J2'},
                    CentralBody="Earth",
                    J2NormalizedValue=0.000484165143790815,
                    RefDistance=6378137.0,
                    OrbitEpoch="2024-01-01T00:00:00.000Z",
                    CoordSystem="Inertial",
                    CoordType="Classical",
                    OrbitalElements=[
                        sma,           # Semi-major axis (m)
                        0.001,         # Eccentricity
                        inclination,   # Inclination (deg)
                        0.0,           # Argument of periapsis (deg)
                        raan,          # RAAN (deg)
                        ta,            # True anomaly (deg)
                    ],
                ),
            )
            satellites.append(satellite)

    return satellites


def demo_coverage_by_asset():
    """Demonstrate per-asset coverage statistics."""
    print("=" * 70)
    print("1. COVERAGE BY ASSET - Per-Satellite Performance")
    print("=" * 70)
    print("\nReports min/max/average/cumulative coverage % for each satellite.")

    # Time window
    start_time = "2024-01-01T00:00:00.000Z"
    stop_time = "2024-01-01T12:00:00.000Z"

    # Create LEO constellation
    satellites = create_leo_constellation()
    print(f"\nConstellation: {len(satellites)} satellites (3x3 LEO)")
    print(f"Altitude: 700 km, Inclination: 60°")

    # Global grid for comprehensive coverage
    grid = CoverageGridLatitudeBounds(
        MinLatitude=-70.0,
        MaxLatitude=70.0,
        Resolution=20.0,  # Coarse grid for faster demo
        Height=0.0,
    )

    print(f"\nGrid: ±70° latitude, 20° resolution")
    print(f"Analysis: 12 hours")
    print("\nComputing per-asset coverage statistics...")

    result = report_coverage_by_asset(
        start=start_time,
        stop=stop_time,
        grid=grid,
        assets=satellites,
        description="LEO constellation per-asset coverage",
        step=180.0,  # 3-minute steps
    )

    if result.get("IsSuccess"):
        print("\n✓ Computation successful!\n")

        asset_data = result.get("CoverageByAssetDatas", [])
        if asset_data:
            print(f"{'Satellite':<15} {'Min %':<10} {'Max %':<10} {'Avg %':<10} {'Cumul %':<12}")
            print("-" * 70)

            for data in asset_data:
                name = data.get("AssetName", "Unknown")
                min_pct = data.get("MinPercentCovered", 0)
                max_pct = data.get("MaxPercentCovered", 0)
                avg_pct = data.get("AveragePercentCovered", 0)
                cum_pct = data.get("CumulativePercentCovered", 0)

                print(
                    f"{name:<15} {min_pct:>8.2f}% {max_pct:>8.2f}% "
                    f"{avg_pct:>8.2f}% {cum_pct:>10.2f}%"
                )

            # Calculate constellation-level statistics
            total_avg = sum(d.get("AveragePercentCovered", 0) for d in asset_data)
            total_cum = sum(d.get("CumulativePercentCovered", 0) for d in asset_data)

            print("-" * 70)
            print(f"{'TOTAL':<15} {'':<10} {'':<10} {total_avg:>8.2f}% {total_cum:>10.2f}%")

            print("\nInterpretation:")
            print("  - Min/Max: Range of instantaneous coverage percentage")
            print("  - Average: Mean coverage percentage over analysis period")
            print("  - Cumulative: Total unique area covered by this satellite")
        else:
            print("  No per-asset data returned")
    else:
        print(f"\n✗ Error: {result.get('Message', 'Unknown error')}")


def demo_percent_coverage():
    """Demonstrate overall coverage percentage over time."""
    print("\n" + "=" * 70)
    print("2. PERCENT COVERAGE - Overall Coverage Evolution")
    print("=" * 70)
    print("\nReports instantaneous and cumulative coverage % over time.")

    # Time window
    start_time = "2024-01-01T00:00:00.000Z"
    stop_time = "2024-01-01T24:00:00.000Z"  # Full day

    # Create regional constellation
    satellites = create_regional_constellation()
    print(f"\nConstellation: {len(satellites)} satellites (regional)")
    print(f"Type: Inclined geosynchronous (GEO altitude, 30° inc)")

    # Regional grid for Asia-Pacific
    grid = CoverageGridLatLonBounds(
        MinLatitude=0.0,
        MaxLatitude=60.0,
        MinLongitude=60.0,
        MaxLongitude=180.0,
        Resolution=15.0,
        Height=0.0,
    )

    print(f"\nGrid: Asia-Pacific region (0°-60°N, 60°-180°E)")
    print(f"Resolution: 15°")
    print(f"Analysis: 24 hours")
    print("\nComputing coverage percentage over time...")

    result = report_percent_coverage(
        start=start_time,
        stop=stop_time,
        grid=grid,
        assets=satellites,
        description="Regional constellation coverage evolution",
        step=600.0,  # 10-minute steps for 24-hour analysis
    )

    if result.get("IsSuccess"):
        print("\n✓ Computation successful!\n")

        # Get time series data
        instant_data = result.get("InstantaneousPercentCoverages", [])
        cumul_data = result.get("CumulativePercentCoverages", [])

        print(f"Time points sampled: {len(instant_data)}")

        if instant_data and cumul_data:
            # Show statistics
            instant_values = [d.get("Value", 0) for d in instant_data]
            cumul_values = [d.get("Value", 0) for d in cumul_data]

            min_instant = min(instant_values)
            max_instant = max(instant_values)
            avg_instant = sum(instant_values) / len(instant_values)
            final_cumul = cumul_values[-1] if cumul_values else 0

            print(f"\nInstantaneous Coverage Statistics:")
            print(f"  Minimum: {min_instant:.2f}%")
            print(f"  Maximum: {max_instant:.2f}%")
            print(f"  Average: {avg_instant:.2f}%")
            print(f"\nCumulative Coverage:")
            print(f"  Final (after 24 hrs): {final_cumul:.2f}%")

            # Show sample time points
            print(f"\nSample Coverage Over Time:")
            print(f"{'Time':<22} {'Instant %':<12} {'Cumul %':<12}")
            print("-" * 50)

            # Show 6 evenly-spaced samples
            n_samples = min(6, len(instant_data))
            for i in range(n_samples):
                idx = i * (len(instant_data) - 1) // (n_samples - 1) if n_samples > 1 else 0
                time = instant_data[idx].get("Time", "N/A")
                instant_val = instant_data[idx].get("Value", 0)
                cumul_val = cumul_data[idx].get("Value", 0) if idx < len(cumul_data) else 0

                print(f"{time:<22} {instant_val:>10.2f}% {cumul_val:>10.2f}%")

            print("\nInterpretation:")
            print("  - Instantaneous: % of grid covered at each time instant")
            print("  - Cumulative: % of grid that has been covered at least once")
        else:
            print("  No time series data returned")
    else:
        print(f"\n✗ Error: {result.get('Message', 'Unknown error')}")


def demo_comparison_scenarios():
    """Compare coverage statistics for different scenarios."""
    print("\n" + "=" * 70)
    print("3. SCENARIO COMPARISON - Different Constellations")
    print("=" * 70)
    print("\nComparing coverage statistics for LEO vs Regional constellations.")

    start_time = "2024-01-01T00:00:00.000Z"
    stop_time = "2024-01-01T12:00:00.000Z"

    # Common grid for comparison
    grid = CoverageGridLatitudeBounds(
        MinLatitude=-60.0,
        MaxLatitude=60.0,
        Resolution=20.0,
        Height=0.0,
    )

    scenarios = [
        ("LEO (9 sats)", create_leo_constellation()),
        ("Regional (4 sats)", create_regional_constellation()),
    ]

    results_table = []

    for name, satellites in scenarios:
        print(f"\n--- Analyzing: {name} ({len(satellites)} satellites) ---")

        # Get per-asset statistics
        result = report_coverage_by_asset(
            start=start_time,
            stop=stop_time,
            grid=grid,
            assets=satellites,
            step=180.0,
        )

        if result.get("IsSuccess"):
            asset_data = result.get("CoverageByAssetDatas", [])
            avg_coverage = sum(d.get("AveragePercentCovered", 0) for d in asset_data)
            cum_coverage = max(d.get("CumulativePercentCovered", 0) for d in asset_data)

            results_table.append(
                {
                    "Scenario": name,
                    "Satellites": len(satellites),
                    "Avg Coverage": avg_coverage,
                    "Best Cumul": cum_coverage,
                }
            )
            print(f"  Average coverage (total): {avg_coverage:.2f}%")
            print(f"  Best cumulative coverage: {cum_coverage:.2f}%")
        else:
            print(f"  Error: {result.get('Message', 'Unknown')}")

    # Display comparison
    if results_table:
        print("\n" + "=" * 70)
        print("COMPARISON SUMMARY")
        print("=" * 70)
        print(
            f"{'Scenario':<20} {'Sats':<8} {'Avg Cov %':<15} {'Best Cumul %':<15}"
        )
        print("-" * 70)
        for r in results_table:
            print(
                f"{r['Scenario']:<20} {r['Satellites']:<8} "
                f"{r['Avg Coverage']:>13.2f}% {r['Best Cumul']:>13.2f}%"
            )


def demo_sensor_impact():
    """Demonstrate coverage statistics for simple constellation."""
    print("\n" + "=" * 70)
    print("4. SIMPLE CONSTELLATION - Coverage Analysis")
    print("=" * 70)
    print("\nAnalyzing coverage for a simple 3-satellite constellation.")

    start_time = "2024-01-01T00:00:00.000Z"
    stop_time = "2024-01-01T06:00:00.000Z"

    # Simple 3-satellite constellation
    satellites = []
    for i in range(3):
        satellites.append(
            EntityPath(
                Name=f"Sat{i + 1}",
                Position=J2Position(
                    **{'$type': 'J2'},
                    CentralBody="Earth",
                    J2NormalizedValue=0.000484165143790815,
                    RefDistance=6378137.0,
                    OrbitEpoch="2024-01-01T00:00:00.000Z",
                    CoordSystem="Inertial",
                    CoordType="Classical",
                    OrbitalElements=[
                        6378137.0 + 600000.0,  # Semi-major axis (m)
                        0.001,                 # Eccentricity
                        55.0,                  # Inclination (deg)
                        0.0,                   # Argument of periapsis (deg)
                        i * 120.0,             # RAAN (deg)
                        0.0,                   # True anomaly (deg)
                    ],
                ),
            )
        )

    grid = CoverageGridLatitudeBounds(
        MinLatitude=-60.0,
        MaxLatitude=60.0,
        Resolution=20.0,
        Height=0.0,
    )

    print("\nTesting coverage with same constellation...")

    result = report_percent_coverage(
        start=start_time,
        stop=stop_time,
        grid=grid,
        assets=satellites,
        step=120.0,
    )

    if result.get("IsSuccess"):
        instant_data = result.get("InstantaneousPercentCoverages", [])
        if instant_data:
            instant_values = [d.get("Value", 0) for d in instant_data]
            avg_instant = sum(instant_values) / len(instant_values)
            max_instant = max(instant_values)

            print(f"  Average instantaneous coverage: {avg_instant:.2f}%")
            print(f"  Peak instantaneous coverage: {max_instant:.2f}%")
    else:
        print(f"  Error: {result.get('Message', 'Unknown')}")


def main():
    """Run all coverage statistics examples."""
    print("\n" + "=" * 70)
    print("ASTROX COVERAGE STATISTICS EXAMPLES")
    print("=" * 70)
    print("\nDemonstrating coverage reporting functions:")
    print("  - report_coverage_by_asset(): Per-satellite performance")
    print("  - report_percent_coverage(): Overall coverage evolution")
    print()

    # Run examples
    demo_coverage_by_asset()
    demo_percent_coverage()
    demo_comparison_scenarios()
    demo_sensor_impact()

    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()


"""
Example output (with HTTP 500 server error):
>>> ======================================================================
>>> ASTROX COVERAGE STATISTICS EXAMPLES
>>> ======================================================================
>>>
>>> Demonstrating coverage reporting functions:
>>>   - report_coverage_by_asset(): Per-satellite performance
>>>   - report_percent_coverage(): Overall coverage evolution
>>>
>>> ======================================================================
>>> 1. COVERAGE BY ASSET - Per-Satellite Performance
>>> ======================================================================
>>>
>>> Reports min/max/average/cumulative coverage % for each satellite.
>>>
>>> Constellation: 9 satellites (3x3 LEO)
>>> Altitude: 700 km, Inclination: 60°
>>>
>>> Grid: ±70° latitude, 20° resolution
>>> Analysis: 12 hours
>>>
>>> Computing per-asset coverage statistics...
>>> Traceback (most recent call last):
>>>   File "examples/02_coverage/coverage_statistics.py", line 427, in <module>
>>>     main()
>>>   File "examples/02_coverage/coverage_statistics.py", line 416, in main
>>>     demo_coverage_by_asset()
>>>   File "examples/02_coverage/coverage_statistics.py", line 132, in demo_coverage_by_asset
>>>     result = report_coverage_by_asset(...)
>>>   File "/home/betelgeuse/Developments/astrox-client/astrox/coverage.py", line 785, in report_coverage_by_asset
>>>     return sess.post(endpoint="/Coverage/Report/CoverageByAsset", data=payload)
>>>   File "/home/betelgeuse/Developments/astrox-client/astrox/_http.py", line 284, in post
>>>     result = _make_request(...)
>>>   File "/home/betelgeuse/Developments/astrox-client/astrox/_http.py", line 108, in _make_request
>>>     raise last_exception
>>> astrox.exceptions.AstroxHTTPError: HTTP 500: Internal Server Error
"""
