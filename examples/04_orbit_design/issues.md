# Known Issues - Orbit Design Examples

## Status Summary

All orbit design examples are working correctly as of 2026-01-25.

## Successfully Working Endpoints

### 1. `/orbit/CoordinateConversions` - Working
- `coordinate_conversions.py`: All 5 conversion functions work correctly
  - `kepler_to_rv()`: Kepler elements → position/velocity vectors
  - `rv_to_kepler()`: Position/velocity vectors → Kepler elements
  - `kepler_to_lla_at_ascending_node()`: Kepler → Lat/Lon/Alt at ascending node
  - `geo_lambert_transfer_dv()`: GEO Lambert transfer delta-V calculation
  - `kozai_izsak_mean_elements()`: Osculating → Mean elements (J2 perturbations)

### 2. `/orbit/OrbitWizard` - Working
- `geo_orbit.py`: `design_geo()` function works correctly
  - Generates geostationary orbits at various longitudes
  - Handles both zero and small inclination orbits
  - Returns both TOD and Inertial frame elements

- `molniya_orbit.py`: `design_molniya()` function works correctly
  - Generates Molniya orbits with correct critical inclination (~63.4°)
  - Configurable perigee altitude and apogee longitude
  - Supports both northern (270°) and southern (90°) hemisphere apogees

- `sso_orbit.py`: `design_sso()` function works correctly
  - Generates sun-synchronous orbits at various altitudes
  - Configurable local time of descending node
  - Correctly calculates required inclination for sun-synchronicity

- `walker_constellation.py`: `design_walker()` function works correctly
  - Generates Walker constellations (Delta, Star, Custom patterns)
  - Supports GPS-like (24:6:1), LEO, polar, and custom constellations
  - Properly handles phase factor constraints (F in [1, num_planes-1])

## Notes

- All examples produce consistent results with the API
- Output includes both TOD (True of Date) and Inertial frame orbital elements
- Functions return `IsSuccess: True` and `Message: 'Success!'` when working correctly
- No HTTP errors or validation issues encountered during testing

## Recommendations

- Use `KeplerElements` model from `astrox.models` for seed orbits in Walker constellations
- For GEO orbits, use `design_geo()` with `inclination=0.0` for true geostationary
- For SSO orbits, local time is at descending node (southbound equatorial crossing)
- For Walker constellations, phase factor F must be in range [1, num_planes-1]