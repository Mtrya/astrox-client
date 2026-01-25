# Endpoint to Function Mapping

This file details the planned endpoint to function mapping, organized by modules.

## `/Coverage` -> `astrox/coverage.py`

1. `/Coverage/GetGridPoints` -> `get_grid_points()`
2. `/Coverage/ComputeCoverage` -> `compute_coverage()`
3. `/Coverage/FOM/ValueByGridPoint/SimpleCoverage` -> `fom_simple_coverage(..., output="grid_point")`
4. `/Coverage/FOM/ValueByGridPointAtTime/SimpleCoverage` -> `fom_simple_coverage(..., output="grid_point_at_time")`
5. `/Coverage/FOM/GridStats/SimpleCoverage` -> `fom_simple_coverage(..., output="grid_stats")`
6. `/Coverage/FOM/GridStatsOverTime/SimpleCoverage` -> `fom_simple_coverage(..., output="grid_stats_over_time")`
7. `/Coverage/FOM/ValueByGridPoint/CoverageTime` -> `fom_coverage_time(..., output="grid_point")`
8. `/Coverage/FOM/GridStats/CoverageTime` -> `fom_coverage_time(..., output="grid_stats")`
9. `/Coverage/FOM/ValueByGridPoint/NumberOfAssets` -> `fom_number_of_assets(..., output="grid_point")`
10. `/Coverage/FOM/ValueByGridPointAtTime/NumberOfAssets` -> `fom_number_of_assets(..., output="grid_point_at_time")`
11. `/Coverage/FOM/GridStats/NumberOfAssets` -> `fom_number_of_assets(..., output="grid_stats")`
12. `/Coverage/FOM/GridStatsOverTime/NumberOfAssets` -> `fom_number_of_assets(..., output="grid_stats_over_time")`
13. `/Coverage/FOM/ValueByGridPoint/ResponseTime` -> `fom_response_time(..., output="grid_point")`
14. `/Coverage/FOM/ValueByGridPointAtTime/ResponseTime` -> `fom_response_time(..., output="grid_point_at_time")`
15. `/Coverage/FOM/GridStats/ResponseTime` -> `fom_response_time(..., output="grid_stats")`
16. `/Coverage/FOM/GridStatsOverTime/ResponseTime` -> `fom_response_time(..., output="grid_stats_over_time")`
17. `/Coverage/FOM/ValueByGridPoint/RevisitTime` -> `fom_revisit_time(..., output="grid_point")`
18. `/Coverage/FOM/ValueByGridPointAtTime/RevisitTime` -> `fom_revisit_time(..., output="grid_point_at_time")`
19. `/Coverage/FOM/GridStats/RevisitTime` -> `fom_revisit_time(..., output="grid_stats")`
20. `/Coverage/FOM/GridStatsOverTime/RevisitTime` -> `fom_revisit_time(..., output="grid_stats_over_time")`
21. `/Coverage/Report/CoverageByAsset` -> `report_coverage_by_asset()`
22. `/Coverage/Report/PercentCoverage` -> `report_percent_coverage()`

Total 22 endpoints, 8 functions.

## `/Propagator` -> `astrox/propagator.py`

1. `/Propagator/TwoBody` -> `propagate_two_body()`
2. `/Propagator/Ballistic` -> `propagate_ballistic()`
3. `/Propagator/J2` -> `propagate_j2()`
4. `/Propagator/SGP4` -> `propagate_sgp4()`
5. `/Propagator/SimpleAscent` -> `propagate_simple_ascent()`
6. `/Propagator/HPOP` -> `propagate_hpop()`
7. `/Propagator/MultiJ2` -> `propagate_j2_batch()`
8. `/Propagator/MultiSGP4` -> `propagate_sgp4_batch()`
9. `/Propagator/MultiTwoBody` -> `propagate_two_body_batch()`

Total 9 endpoints, 9 functions.

## `/CAT` -> `astrox/conjunction_analysis.py`

1. `/CAT/CA_ComputeV3` -> `compute_close_approach(..., version="v3")`
2. `/CAT/CA_ComputeV4` -> `compute_close_approach(..., version="v4")`
3. `/CAT/DebrisBreakupSimple` -> `debris_breakup(..., method="simple")`
4. `/CAT/DebrisBreakup` -> `debris_breakup(..., method="default")`
5. `/CAT/DebrisBreakupNASA` -> `debris_breakup(..., method="nasa")`
6. `/CAT/GetTLE` -> `get_tle()`
7. `/CAT/LifeTimeTLE` -> `compute_lifetime()`

Total 7 endpoints, 4 functions.

## `/Lighting` -> `astrox/lighting.py`

1. `/Lighting/LightingTimes` -> `lighting_times()`
2. `/Lighting/SolarIntensity` -> `solar_intensity()`
3. `/Lighting/SolarAER` -> `solar_aer()`

Total 3 endpoints, 3 functions.

## `/OrbitConvert` -> `astrox/orbit_convert.py`

1. `/OrbitConvert/Kepler2RV` -> `kepler_to_rv()`
2. `/OrbitConvert/RV2Kepler` -> `rv_to_kepler()`
3. `/OrbitConvert/Kepler2LLAAtAscendNode` -> `kepler_to_lla_at_ascending_node()`
4. `/OrbitConvert/CalGEOYMLambertDv` -> `geo_lambert_transfer_dv()`
5. `/OrbitConvert/GetKozaiIzsakMeanElements` -> `kozai_izsak_mean_elements()`

Total 5 endpoints, 5 functions.

## `/OrbitWizard` -> `astrox/orbit_wizard.py`

1. `/OrbitWizard/GEO` -> `design_geo()`
2. `/OrbitWizard/Molniya` -> `design_molniya()`
3. `/OrbitWizard/SSO` -> `design_sso()`
4. `/OrbitWizard/Walker` -> `design_walker()`

Total 4 endpoints, 4 functions.

## `/OrbitSystem` -> `astrox/orbit_system.py`

1. `/OrbitSystem/CentralBodyFrame` -> `convert_central_body_frame()`
2. `/OrbitSystem/EarthMoonLibration` -> `compute_earth_moon_libration(..., version="v1")`
3. `/OrbitSystem/EarthMoonLibration2` -> `compute_earth_moon_libration(..., version="v2")`

Total 3 endpoints, 2 functions.

## `/Rocket` -> `astrox/rocket.py`

1. `/Rocket/RocketSegmentFA` -> `optimize_trajectory()`
2. `/Rocket/RocketLanding` -> `optimize_landing()`
3. `/Rocket/RocketGuid` -> `compute_guided_trajectory()`

Total 3 endpoints, 3 functions.

## `/Terrain` -> `astrox/terrain.py`

1. `/Terrain/AzElMask` -> `get_terrain_mask(..., method="default")`
2. `/Terrain/AzElMaskSimple` -> `get_terrain_mask(..., method="simple")`

Total 2 endpoints, 1 function.

## `/access` -> `astrox/access.py`

1. `/access/AccessComputeV2` -> `compute_access()`
2. `/access/ChainCompute` -> `compute_chain()`

Total 2 endpoints, 2 functions.

## `/Astrogator` -> `astrox/astrogator.py`

1. `/Astrogator/RunMCS` -> `run_mcs()`

Total 1 endpoint, 1 function.

## `/LandingZone` -> `astrox/landing_zone.py`

1. `/LandingZone` -> `compute_landing_zone()`

Total 1 endpoint, 1 function.
