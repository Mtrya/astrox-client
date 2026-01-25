# Function Signature Design Plan

## Overview
Design Python function signatures for all 43 functions across 12 modules, following the established design philosophy:

**Design Principles:**
1. Flatten all input models - expose all fields as function parameters
2. Minimal processing - all optionals default to `None`, let backend handle defaults
3. Preserve API contract - required stays required, optional stays optional
4. Pythonic names - snake_case arguments
5. Parameter order: required → optional → output/method/version → session
6. Nested structures preserved - use domain models like `EntityPath`
7. Use raw model names in implementation (e.g., `EntityPath` not `Entity`)
8. Always return `dict`

## Module-by-Module Function Signatures

### 1. Coverage Module (`astrox/coverage.py`)

**Total: 8 functions (22 endpoints merged)**

#### 1.1 `get_grid_points()`
```python
def get_grid_points(
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    *,
    text: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Get all grid points and cell information from grid definition.

    Endpoint: POST /Coverage/GetGridPoints

    Args:
        grid: Grid definition (ICoverageGrid interface - one of several grid types)
        text: Description/comment
        session: Optional HTTP session

    Returns:
        Grid points with cell information
    """
```

**Schema mapping:**
- `Grid` (required) → `grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds]`
- `Text` (optional) → `text: Optional[str] = None`

---

#### 1.2 `compute_coverage()`
```python
def compute_coverage(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Compute coverage for all grid points.

    Endpoint: POST /Coverage/ComputeCoverage

    Returns coverage time intervals and asset counts for all grid points.

    Args:
        start: Analysis start time (UTCG) format: "yyyy-MM-ddTHH:mm:ss.fffZ"
        stop: Analysis end time (UTCG)
        grid: Grid definition (ICoverageGrid)
        assets: Coverage assets/resources (list of EntityPath)
        description: Description/comment
        grid_point_sensor: Sensor at grid points (ISensor)
        grid_point_constraints: Constraints for grid points (Range, AzElMask, ElevationAngle)
        filter_type: Asset count constraint type ("AtLeastN", "ExactlyN")
        number_of_assets: Minimum coverage resources required
        contain_asset_access_results: Include individual asset coverage results
        contain_coverage_points: Include all point coordinates
        step: Calculation step size (seconds)
        session: Optional HTTP session

    Returns:
        Coverage computation results with satisfaction intervals
    """
```

**Schema mapping:**
- `Start` (required) → `start: str`
- `Stop` (required) → `stop: str`
- `Grid` (required) → `grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds]`
- `Assets` (required) → `assets: list[EntityPath]`
- All optional fields with `None` defaults

---

#### 1.3 `fom_simple_coverage()`
```python
def fom_simple_coverage(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    output: str = "grid_point",  # "grid_point", "grid_point_at_time", "grid_stats", "grid_stats_over_time"
    time: Optional[str] = None,  # Required when output="grid_point_at_time"
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate simple binary coverage (0 or 1).

    Endpoints (merged by output parameter):
    - POST /Coverage/FOM/ValueByGridPoint/SimpleCoverage (output="grid_point")
    - POST /Coverage/FOM/ValueByGridPointAtTime/SimpleCoverage (output="grid_point_at_time")
    - POST /Coverage/FOM/GridStats/SimpleCoverage (output="grid_stats")
    - POST /Coverage/FOM/GridStatsOverTime/SimpleCoverage (output="grid_stats_over_time")

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        grid: Grid definition
        assets: Coverage assets
        output: Output format type
        time: Specific time for "grid_point_at_time" output
        [... rest same as compute_coverage ...]
        session: Optional HTTP session

    Returns:
        FOM results (1 if covered, 0 otherwise)
    """
```

---

#### 1.4 `fom_coverage_time()`
```python
def fom_coverage_time(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    output: str = "grid_point",  # "grid_point", "grid_stats"
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate total coverage time for each grid point.

    Endpoints (merged):
    - POST /Coverage/FOM/ValueByGridPoint/CoverageTime (output="grid_point")
    - POST /Coverage/FOM/GridStats/CoverageTime (output="grid_stats")

    Note: No "grid_stats_over_time" variant exists for CoverageTime.

    Args:
        [Same as fom_simple_coverage except no 'time' parameter]

    Returns:
        Coverage time FOM results
    """
```

---

#### 1.5 `fom_number_of_assets()`
```python
def fom_number_of_assets(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    output: str = "grid_point",  # "grid_point", "grid_point_at_time", "grid_stats", "grid_stats_over_time"
    time: Optional[str] = None,
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate number of assets covering each grid point.

    Endpoints (merged):
    - POST /Coverage/FOM/ValueByGridPoint/NumberOfAssets (output="grid_point")
    - POST /Coverage/FOM/ValueByGridPointAtTime/NumberOfAssets (output="grid_point_at_time")
    - POST /Coverage/FOM/GridStats/NumberOfAssets (output="grid_stats")
    - POST /Coverage/FOM/GridStatsOverTime/NumberOfAssets (output="grid_stats_over_time")
    """
```

---

#### 1.6 `fom_response_time()`
```python
def fom_response_time(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    output: str = "grid_point",
    time: Optional[str] = None,
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate response time (time to reach target).

    Endpoints (merged):
    - POST /Coverage/FOM/ValueByGridPoint/ResponseTime
    - POST /Coverage/FOM/ValueByGridPointAtTime/ResponseTime
    - POST /Coverage/FOM/GridStats/ResponseTime
    - POST /Coverage/FOM/GridStatsOverTime/ResponseTime
    """
```

---

#### 1.7 `fom_revisit_time()`
```python
def fom_revisit_time(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    output: str = "grid_point",
    time: Optional[str] = None,
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate revisit time (time between successive passes).

    Endpoints (merged):
    - POST /Coverage/FOM/ValueByGridPoint/RevisitTime
    - POST /Coverage/FOM/ValueByGridPointAtTime/RevisitTime
    - POST /Coverage/FOM/GridStats/RevisitTime
    - POST /Coverage/FOM/GridStatsOverTime/RevisitTime
    """
```

---

#### 1.8 `report_coverage_by_asset()` & `report_percent_coverage()`
```python
def report_coverage_by_asset(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Get coverage percentage report for each asset.

    Endpoint: POST /Coverage/Report/CoverageByAsset

    Returns min, max, average, and cumulative coverage percentages per asset.
    """

def report_percent_coverage(
    start: str,
    stop: str,
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGridCoverageGridLatitudeBounds, ICoverageGridCoverageGridLatLonBounds, ICoverageGridCovGridLatLonBounds],
    assets: list[EntityPath],
    *,
    description: Optional[str] = None,
    grid_point_sensor: Optional[ISensor] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    filter_type: Optional[str] = None,
    number_of_assets: Optional[int] = None,
    contain_asset_access_results: Optional[bool] = None,
    contain_coverage_points: Optional[bool] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Get instantaneous and cumulative coverage percentage over time.

    Endpoint: POST /Coverage/Report/PercentCoverage
    """
```

---

### 2. Propagator Module (`astrox/propagator.py`)

**Total: 9 functions**

#### 2.1 `propagate_two_body()`
```python
def propagate_two_body(
    start: str,
    stop: str,
    orbit_epoch: str,
    orbital_elements: list[float],
    *,
    step: Optional[float] = None,
    central_body: Optional[str] = None,
    gravitational_parameter: Optional[float] = None,
    coord_system: Optional[str] = None,
    coord_type: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate orbit using two-body dynamics.

    Endpoint: POST /Propagator/TwoBody

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        orbit_epoch: Orbit epoch (UTCG)
        orbital_elements: Orbital elements (6 values)
            - Classical: SemiMajorAxis(m), Eccentricity, Inclination(deg),
                        ArgumentOfPeriapsis(deg), RAAN(deg), TrueAnomaly(deg)
            - Cartesian: X(m), Y(m), Z(m), Vx(m/s), Vy(m/s), Vz(m/s)
        step: Integration step size (s)
        central_body: Central body name (default: "Earth")
        gravitational_parameter: Gravitational constant (m³/s²)
        coord_system: Coordinate system (default: "Inertial")
        coord_type: Coordinate type ("Classical" or "Cartesian", default: "Classical")
        session: Optional HTTP session

    Returns:
        CZML position output
    """
```

---

#### 2.2 `propagate_ballistic()`
```python
def propagate_ballistic(
    start: str,
    impact_latitude: float,
    impact_longitude: float,
    *,
    step: Optional[float] = None,
    central_body: Optional[str] = None,
    gravitational_parameter: Optional[float] = None,
    launch_latitude: Optional[float] = None,
    launch_longitude: Optional[float] = None,
    launch_altitude: Optional[float] = None,
    ballistic_type: Optional[str] = None,
    ballistic_type_value: Optional[float] = None,
    impact_altitude: Optional[float] = None,
    stop: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate ballistic trajectory.

    Endpoint: POST /Propagator/Ballistic

    Args:
        start: Launch time (UTCG)
        impact_latitude: Impact point latitude (deg)
        impact_longitude: Impact point longitude (deg)
        step: Integration step size (s)
        central_body: Central body name
        gravitational_parameter: Gravitational constant (m³/s²)
        launch_latitude: Launch site latitude (deg)
        launch_longitude: Launch site longitude (deg)
        launch_altitude: Launch site altitude (m)
        ballistic_type: Ballistic type ("DeltaV", "DeltaV_MinEcc", "ApogeeAlt", "TimeOfFlight")
        ballistic_type_value: Ballistic type value (m/s, m, or s)
        impact_altitude: Impact point altitude (m)
        stop: End time (computed after propagation if not provided)
        session: Optional HTTP session

    Returns:
        CZML position output
    """
```

---

#### 2.3 `propagate_j2()`
```python
def propagate_j2(
    start: str,
    stop: str,
    j2_normalized_value: float,
    ref_distance: float,
    orbit_epoch: str,
    orbital_elements: list[float],
    *,
    step: Optional[float] = None,
    central_body: Optional[str] = None,
    gravitational_parameter: Optional[float] = None,
    coord_system: Optional[str] = None,
    coord_type: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate orbit using J2 perturbation model.

    Endpoint: POST /Propagator/J2

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        j2_normalized_value: J2 normalized value (Earth: 0.000484165143790815)
        ref_distance: Reference ellipsoid semi-major axis (m)
        orbit_epoch: Orbit epoch (UTCG)
        orbital_elements: Orbital elements (6 values for Classical)
        step: Integration step size (s)
        central_body: Central body name
        gravitational_parameter: Gravitational constant (m³/s²)
        coord_system: Coordinate system
        coord_type: Coordinate type
        session: Optional HTTP session

    Returns:
        CZML position output
    """
```

---

#### 2.4 `propagate_sgp4()`
```python
def propagate_sgp4(
    start: str,
    stop: str,
    tles: list[str],
    *,
    step: Optional[float] = None,
    satellite_number: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate orbit using SGP4 model.

    Endpoint: POST /Propagator/SGP4

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        tles: TLE lines ["tle-line1", "tle-line2"]
        step: Output step size (s)
        satellite_number: Satellite SSC number
        session: Optional HTTP session

    Returns:
        CZML position output
    """
```

---

#### 2.5 `propagate_simple_ascent()`
```python
def propagate_simple_ascent(
    start: str,
    stop: str,
    launch_latitude: float,
    launch_longitude: float,
    launch_altitude: float,
    burnout_velocity: float,
    burnout_latitude: float,
    burnout_longitude: float,
    burnout_altitude: float,
    *,
    central_body: Optional[str] = None,
    step: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate simple ascent trajectory.

    Endpoint: POST /Propagator/SimpleAscent

    Args:
        start: Launch time (UTCG)
        stop: Burnout time (UTCG)
        launch_latitude: Launch latitude (deg)
        launch_longitude: Launch longitude (deg)
        launch_altitude: Launch altitude (m)
        burnout_velocity: Burnout velocity (m/s, Fixed frame)
        burnout_latitude: Burnout latitude (deg)
        burnout_longitude: Burnout longitude (deg)
        burnout_altitude: Burnout altitude (m)
        central_body: Central body name
        step: Integration step size (s)
        session: Optional HTTP session

    Returns:
        CZML position output
    """
```

---

#### 2.6 `propagate_hpop()`
```python
def propagate_hpop(
    start: str,
    stop: str,
    orbit_epoch: str,
    orbital_elements: list[float],
    *,
    description: Optional[str] = None,
    coord_epoch: Optional[str] = None,
    coord_system: Optional[str] = None,
    coord_type: Optional[str] = None,
    gravitational_parameter: Optional[float] = None,
    coefficient_of_drag: Optional[float] = None,
    area_mass_ratio_drag: Optional[float] = None,
    coefficient_of_srp: Optional[float] = None,
    area_mass_ratio_srp: Optional[float] = None,
    hpop_propagator: Optional[Propagator] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate orbit using high-precision orbit propagator (HPOP).

    Endpoint: POST /Propagator/HPOP

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        orbit_epoch: Orbit epoch (UTCG)
        orbital_elements: Orbital elements (6 values)
        description: Description info
        coord_epoch: Coordinate system epoch
        coord_system: Orbit system ("Inertial", "J2000", "ICRF", ...)
        coord_type: Orbit type ("Classical" or "Cartesian")
        gravitational_parameter: Central body gravitational constant (m³/s²)
        coefficient_of_drag: Atmospheric drag coefficient
        area_mass_ratio_drag: Drag area-mass ratio (m²/kg)
        coefficient_of_srp: Solar radiation pressure coefficient
        area_mass_ratio_srp: SRP area-mass ratio (m²/kg)
        hpop_propagator: HPOP propagator configuration (Propagator schema)
        session: Optional HTTP session

    Returns:
        CZML position output
    """
```

---

#### 2.7-2.9 Batch Propagators
```python
def propagate_j2_batch(
    epoch: str,
    all_satellite_elements: list[KeplerElementsWithEpoch],
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate multiple satellites using J2 perturbation to same epoch.

    Endpoint: POST /Propagator/MultiJ2

    Args:
        epoch: Output epoch time (UTCG)
        all_satellite_elements: Collection of satellite orbital elements
                               (list of KeplerElementsWithEpoch)
        session: Optional HTTP session

    Returns:
        All satellites' Kepler elements at output epoch (Earth inertial frame)
    """

def propagate_sgp4_batch(
    epoch: str,
    tles: list[str],
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate multiple satellites using SGP4 to same epoch.

    Endpoint: POST /Propagator/MultiSGP4

    Args:
        epoch: Output epoch time (UTCG)
        tles: TLE lines for all satellites
        session: Optional HTTP session

    Returns:
        All satellites' Kepler elements at epoch (Earth inertial frame)
    """

def propagate_two_body_batch(
    epoch: str,
    all_satellite_elements: list[KeplerElementsWithEpoch],
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Propagate multiple satellites using two-body dynamics to same epoch.

    Endpoint: POST /Propagator/MultiTwoBody
    """
```

---

### 3. Conjunction Analysis Module (`astrox/conjunction_analysis.py`)

**Total: 4 functions (7 endpoints merged)**

#### 3.1 `compute_close_approach()`
```python
def compute_close_approach(
    start_utcg: str,
    stop_utcg: str,
    sat1: Union[TleInfo, EntityPositionCzml],
    *,
    version: str = "v4",  # "v3" or "v4"
    tol_max_distance: Optional[float] = None,
    tol_cross_dt: Optional[float] = None,
    tol_theta: Optional[float] = None,
    tol_dh: Optional[float] = None,
    targets: Optional[list[TleInfo]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Compute space debris close approach / collision analysis.

    Endpoints (merged):
    - POST /CAT/CA_ComputeV3 (version="v3", sat1 is TleInfo)
    - POST /CAT/CA_ComputeV4 (version="v4", sat1 is EntityPositionCzml for rockets)

    Args:
        start_utcg: Analysis start time (UTC) format: "yyyy-MM-ddTHH:mm:ss.fffZ"
        stop_utcg: Analysis end time (UTC)
        sat1: Primary satellite (TleInfo for v3, EntityPositionCzml for v4)
        version: API version ("v3" or "v4", default "v4")
        tol_max_distance: Maximum distance for close approach detection (km)
        tol_cross_dt: Time error tolerance for cross-plane detection (s)
        tol_theta: Orbital plane angle threshold (deg)
        tol_dh: Apogee/perigee altitude filtering error (km)
        targets: Target objects; if None, reads from database
        session: Optional HTTP session

    Returns:
        Collision analysis results with CA_Results array
    """
```

---

#### 3.2 `debris_breakup()`
```python
def debris_breakup(
    mother_satellite: TleInfo,
    epoch: str,
    *,
    method: str = "simple",  # "simple", "default", "nasa"
    ssc_pre: Optional[str] = None,
    a2m: Optional[float] = None,
    count: Optional[int] = None,
    delta_v: Optional[float] = None,
    min_azimuth: Optional[float] = None,
    max_azimuth: Optional[float] = None,
    min_elevation: Optional[float] = None,
    max_elevation: Optional[float] = None,
    az_el_vel: Optional[list[float]] = None,
    mass_total: Optional[float] = None,
    min_lc: Optional[float] = None,
    compute_life_of_time: Optional[bool] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Generate space debris from satellite breakup.

    Endpoints (merged):
    - POST /CAT/DebrisBreakupSimple (method="simple")
    - POST /CAT/DebrisBreakup (method="default")
    - POST /CAT/DebrisBreakupNASA (method="nasa")

    Args:
        mother_satellite: Parent satellite TLE (TleInfo)
        epoch: Debris generation time (UTC) format: "yyyy-MM-ddTHH:mm:ss.fffZ"
        method: Breakup model ("simple", "default", "nasa")
        ssc_pre: Debris SSC prefix (2 chars)
        a2m: Area-to-mass ratio (m²/kg)
        count: Total number of debris particles (simple method only, < 1000)
        delta_v: Relative velocity magnitude (m/s, simple method)
        min_azimuth: Minimum azimuth angle (deg, simple method)
        max_azimuth: Maximum azimuth angle (deg, simple method)
        min_elevation: Minimum elevation angle (deg, simple method)
        max_elevation: Maximum elevation angle (deg, simple method)
        az_el_vel: Azimuth, elevation, velocity parameters (default/nasa methods)
        mass_total: Total mass of parent satellite (nasa method)
        min_lc: Minimum characteristic length (nasa method)
        compute_life_of_time: Whether to compute debris orbital lifetime
        session: Optional HTTP session

    Returns:
        Debris TLEs, breakup parameters, lifetimes, altitudes, periods
    """
```

---

#### 3.3 `get_tle()`
```python
def get_tle(
    name: str,
    ssc: str,
    epoch: str,
    b_star: float,
    sma: float,
    ecc: float,
    inc: float,
    w: float,
    raan: float,
    ta: float,
    *,
    is_mean_elements: Optional[bool] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Generate two-line element set from orbital elements.

    Endpoint: POST /CAT/GetTLE

    Args:
        name: Space target name
        ssc: NORAD SSC (5-digit code)
        epoch: Orbital epoch (UTCG) format: "yyyy-MM-ddTHH:mm:ss.fffZ"
        b_star: Atmospheric drag coefficient
        sma: Semi-major axis (km)
        ecc: Eccentricity
        inc: Orbital inclination (deg, TEME)
        w: Argument of perigee (deg, TEME)
        raan: Right ascension of ascending node (deg, TEME)
        ta: True anomaly (deg, TEME)
        is_mean_elements: Whether elements are mean (True) or osculating (False)
        session: Optional HTTP session

    Returns:
        Generated TLE information (TleInfo)
    """
```

---

#### 3.4 `compute_lifetime()`
```python
def compute_lifetime(
    epoch: str,
    tles: TleInfo,
    sm: float,
    mass: float,
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate orbital lifetime from TLE.

    Endpoint: POST /CAT/LifeTimeTLE

    Args:
        epoch: Analysis epoch (UTCG)
        tles: Two-line element set (TleInfo)
        sm: Surface area or related parameter
        mass: Satellite mass
        session: Optional HTTP session

    Returns:
        Calculated orbital lifetime (years)
    """
```

---

### 4. Lighting Module (`astrox/lighting.py`)

**Total: 3 functions**

```python
def lighting_times(
    start: str,
    stop: str,
    position: IEntityPosition,
    *,
    description: Optional[str] = None,
    az_el_mask_data: Optional[list[float]] = None,
    occultation_bodies: Optional[list[str]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate lighting time intervals (sunlight, penumbra, umbra).

    Endpoint: POST /Lighting/LightingTimes

    Args:
        start: Analysis start time (UTCG) format: "yyyy-MM-ddTHH:mm:ssZ"
        stop: Analysis end time (UTCG)
        position: Entity position (IEntityPosition - spacecraft or ground station)
        description: Description/comment
        az_el_mask_data: Terrain mask data (ground stations only);
                        format: (Az1, El1, Az2, El2, ...) in radians
        occultation_bodies: Occulting body list (1st element is central body)
        session: Optional HTTP session

    Returns:
        SunLight, Penumbra, and Umbra time parameters
    """

def solar_intensity(
    start: str,
    stop: str,
    position: IEntityPosition,
    *,
    description: Optional[str] = None,
    az_el_mask_data: Optional[list[float]] = None,
    time_step_sec: Optional[float] = None,
    occultation_bodies: Optional[list[str]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate solar intensity at entity position.

    Endpoint: POST /Lighting/SolarIntensity

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        position: Entity position (IEntityPosition)
        description: Description
        az_el_mask_data: Terrain mask data (ground stations only)
        time_step_sec: Calculation time step (s)
        occultation_bodies: Occulting body list
        session: Optional HTTP session

    Returns:
        Solar intensity data at uniformly sampled time points
    """

def solar_aer(
    start: str,
    stop: str,
    site_position: EntityPositionSite,
    *,
    text: Optional[str] = None,
    time_step_sec: Optional[int] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate solar azimuth, elevation, and range from ground station.

    Endpoint: POST /Lighting/SolarAER

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        site_position: Ground station position (EntityPositionSite)
        text: Description
        time_step_sec: Calculation time step (s)
        session: Optional HTTP session

    Returns:
        Solar AER data points
    """
```

---

### 5. Orbit Convert Module (`astrox/orbit_convert.py`)

**Total: 5 functions**

```python
def kepler_to_rv(
    semimajor_axis: float,
    eccentricity: float,
    inclination: float,
    argument_of_periapsis: float,
    right_ascension_of_ascending_node: float,
    true_anomaly: float,
    gravitational_parameter: float,
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Convert Kepler elements to position/velocity vectors.

    Endpoint: POST /OrbitConvert/Kepler2RV

    Args:
        semimajor_axis: Orbital semi-major axis (m)
        eccentricity: Orbital eccentricity
        inclination: Orbital inclination (deg)
        argument_of_periapsis: Argument of perigee (deg)
        right_ascension_of_ascending_node: RAAN (deg)
        true_anomaly: True anomaly (deg)
        gravitational_parameter: Gravitational constant (m³/s²)
        session: Optional HTTP session

    Returns:
        Array of position and velocity components
    """

def rv_to_kepler(
    position_velocity: list[float],
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Convert position/velocity vectors to Kepler elements.

    Endpoint: POST /OrbitConvert/RV2Kepler

    Args:
        position_velocity: Position (m) and velocity (m/s) components
                          in Earth inertial frame
        session: Optional HTTP session

    Returns:
        KeplerElements schema
    """

def kepler_to_lla_at_ascending_node(
    semimajor_axis: float,
    eccentricity: float,
    inclination: float,
    argument_of_periapsis: float,
    right_ascension_of_ascending_node: float,
    true_anomaly: float,
    gravitational_parameter: float,
    *,
    orbit_epoch: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Convert Kepler elements to LLA at ascending node.

    Endpoint: POST /OrbitConvert/Kepler2LLAAtAscendNode

    Note: Earth only, two-body orbital propagation.

    Args:
        [Same as kepler_to_rv]
        orbit_epoch: Orbital epoch (UTCG) format: "yyyy-MM-ddTHH:mm:ss.fffZ"
        session: Optional HTTP session

    Returns:
        Array of latitude, longitude, altitude at ascending node
    """

def geo_lambert_transfer_dv(
    kepler_platform: KeplerElements,
    kepler_target: KeplerElements,
    time_of_flight: float,
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate Lambert transfer delta-V from GEO platform to target orbit.

    Endpoint: POST /OrbitConvert/CalGEOYMLambertDv

    Args:
        kepler_platform: GEO platform orbital Kepler elements (KeplerElements)
        kepler_target: Target orbital Kepler elements (KeplerElements)
        time_of_flight: Flight time (s)
        session: Optional HTTP session

    Returns:
        Lambert transfer delta-V components (array of floats)
    """

def kozai_izsak_mean_elements(
    semimajor_axis: float,
    eccentricity: float,
    inclination: float,
    argument_of_periapsis: float,
    right_ascension_of_ascending_node: float,
    true_anomaly: float,
    gravitational_parameter: float,
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Get mean Kepler elements via Kozai-Izsak method.

    Endpoint: POST /OrbitConvert/GetKozaiIzsakMeanElements

    Note: Circular orbits only, J2 short-period terms.

    Args:
        [Same as kepler_to_rv]
        session: Optional HTTP session

    Returns:
        Mean Kepler elements (MeanKeplerElements schema)
    """
```

---

### 6. Orbit Wizard Module (`astrox/orbit_wizard.py`)

**Total: 4 functions**

```python
def design_geo(
    orbit_epoch: str,
    inclination: float,
    sub_satellite_point: float,
    *,
    description: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Generate geostationary orbit.

    Endpoint: POST /OrbitWizard/GEO

    Args:
        orbit_epoch: Orbital epoch (UTCG) format: "yyyy-MM-ddTHH:mm:ss.fffZ"
        inclination: Orbital inclination (deg)
        sub_satellite_point: Sub-satellite point geographic longitude (deg)
        description: Description
        session: Optional HTTP session

    Returns:
        Kepler elements in TOD and inertial frames (GEO_Output)
    """

def design_molniya(
    orbit_epoch: str,
    perigee_altitude: float,
    apogee_longitude: float,
    argument_of_periapsis: float,
    *,
    description: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Generate Molniya orbit.

    Endpoint: POST /OrbitWizard/Molniya

    Args:
        orbit_epoch: Orbital epoch (UTCG)
        perigee_altitude: Perigee altitude (km), typically 600 km
        apogee_longitude: Apogee geographic longitude (deg)
        argument_of_periapsis: Argument of perigee (deg), typically 90° or 270°
        description: Description
        session: Optional HTTP session

    Returns:
        Kepler elements in TOD and inertial frames (Molniya_Output)
    """

def design_sso(
    orbit_epoch: str,
    altitude: float,
    local_time_of_descending_node: float,
    *,
    description: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Generate sun-synchronous orbit.

    Endpoint: POST /OrbitWizard/SSO

    Args:
        orbit_epoch: Orbital epoch (UTCG)
        altitude: Orbital altitude (km)
        local_time_of_descending_node: Local time of descending node
                                       (decimal hours, e.g., 14.5 = 14:30 PM)
        description: Description
        session: Optional HTTP session

    Returns:
        Kepler elements in TOD and inertial frames (SSO_Output)
    """

def design_walker(
    seed_kepler: KeplerElements,
    num_planes: int,
    num_sats_per_plane: int,
    *,
    walker_type: Optional[str] = None,
    inter_plane_phase_increment: Optional[int] = None,
    inter_plane_true_anomaly_increment: Optional[float] = None,
    raan_increment: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Generate Walker constellation.

    Endpoint: POST /OrbitWizard/Walker

    Args:
        seed_kepler: Seed Kepler elements for constellation (KeplerElements)
        num_planes: Number of orbital planes (1-999)
        num_sats_per_plane: Number of satellites per plane (1-999)
        walker_type: Constellation type ("Delta", "Star", or "Custom")
        inter_plane_phase_increment: Phase factor (Delta/Star types, < num_planes)
        inter_plane_true_anomaly_increment: True anomaly increment (deg, Custom type)
        raan_increment: RAAN increment between planes (deg, Custom type)
        session: Optional HTTP session

    Returns:
        Generated Walker constellation Kepler elements (2D array by plane)
    """
```

---

### 7. Orbit System Module (`astrox/orbit_system.py`)

**Total: 2 functions**

```python
def convert_central_body_frame(
    position: EntityPositionCzml,
    to_body: str,
    *,
    reference_frame: Optional[str] = None,
    central_body: Optional[str] = None,
    interpolation_algorithm: Optional[str] = None,
    interpolation_degree: Optional[int] = None,
    epoch: Optional[str] = None,
    interval: Optional[str] = None,
    cartesian: Optional[list[float]] = None,
    cartesian_velocity: Optional[list[float]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Convert position between central body reference frames.

    Endpoint: POST /OrbitSystem/CentralBodyFrame

    Args:
        position: Entity position data (EntityPositionCzml)
        to_body: Target central body name (e.g., "Moon", "Mars")
        reference_frame: Reference frame type (e.g., "INERTIAL", "FIXED")
        central_body: Source central body (default: "Earth")
        interpolation_algorithm: Interpolation method ("LINEAR", "LAGRANGE", "HERMITE")
        interpolation_degree: Interpolation degree
        epoch: Epoch time (UTCG)
        interval: Time interval for composite position
        cartesian: Position array [X, Y, Z] (m)
        cartesian_velocity: Position velocity array [X, Y, Z, dX, dY, dZ] (m, m/s)
        session: Optional HTTP session

    Returns:
        Position data in target central body frame
    """

def libration_points(
    epoch: str,
    *,
    version: str = "v2",  # "v1" or "v2"
    central_body: Optional[str] = None,
    interpolation_algorithm: Optional[str] = None,
    interpolation_degree: Optional[int] = None,
    reference_frame: Optional[str] = None,
    interval: Optional[str] = None,
    cartesian: Optional[list[float]] = None,
    cartesian_velocity: Optional[list[float]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate Earth-Moon libration (Lagrange) points.

    Endpoints (merged):
    - POST /OrbitSystem/EarthMoonLibration (version="v1")
    - POST /OrbitSystem/EarthMoonLibration2 (version="v2", default)

    Args:
        epoch: Epoch time (UTCG) format: "yyyy-MM-ddTHH:mm:ssZ" [REQUIRED]
        version: API version ("v1" or "v2", default "v2")
        central_body: Central body (default: "Earth")
        interpolation_algorithm: Interpolation method (default: "LAGRANGE")
        interpolation_degree: Interpolation degree (default: 7)
        reference_frame: Reference frame (default: "FIXED")
        interval: Time interval for composite position
        cartesian: Position array [X, Y, Z] (m)
        cartesian_velocity: Position velocity array (m, m/s)
        session: Optional HTTP session

    Returns:
        Libration point calculations (STM format)
    """
```

---

### 8. Rocket Module (`astrox/rocket.py`)

**Total: 3 functions**

```python
def optimize_trajectory(
    gw: float,
    t1: float,
    alpham: float,
    natmos: int,
    rocket_segments: list[RocketSegment],
    sma0: float,
    ecc0: float,
    inc0: float,
    omg0: float,
    *,
    name: Optional[str] = None,
    text: Optional[str] = None,
    rocket_type: Optional[str] = None,
    use_mcs_profile: Optional[bool] = None,
    name_fa_she_dian: Optional[str] = None,
    fa_she_dian_lla: Optional[list[float]] = None,
    a0: Optional[float] = None,
    aero_params_file_name: Optional[str] = None,
    profile_optim: Optional[VAMCSProfileDEOptimizer] = None,
    mcs_profiles: Optional[list[MCSProfile]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Optimize rocket ascent trajectory using flight segment model.

    Endpoint: POST /Rocket/RocketSegmentFA

    Args:
        gw: Payload mass (kg) [REQUIRED]
        t1: Turn start time (s) [REQUIRED]
        alpham: Maximum angle of attack during atmospheric flight (deg) [REQUIRED]
        natmos: Number of atmospheric flight segments [REQUIRED]
        rocket_segments: Rocket flight segment sequence [REQUIRED]
        sma0: Target orbit semi-major axis (m) [REQUIRED]
        ecc0: Target orbit eccentricity [REQUIRED]
        inc0: Target orbit inclination (deg) [REQUIRED]
        omg0: Target orbit argument of perigee (deg) [REQUIRED]
        name: Mission name
        text: Mission description
        rocket_type: Rocket type (CZ3A, CZ3B, CZ3C, CZ4B, CZ4C, CZ2C, CZ2D, CZ7A)
        use_mcs_profile: Whether to use MCS file for trajectory
        name_fa_she_dian: Launch site name
        fa_she_dian_lla: Launch site coordinates (lon(deg), lat(deg), alt(m))
        a0: Launch azimuth (deg)
        aero_params_file_name: Aerodynamic data table filename
        profile_optim: VAMCSProfileDEOptimizer configuration
        mcs_profiles: MCS file array
        session: Optional HTTP session

    Returns:
        Optimized trajectory results
    """

def optimize_landing(
    *,
    name: Optional[str] = None,
    text: Optional[str] = None,
    is_optimize: Optional[bool] = None,
    a0: Optional[float] = None,
    fa_she_dian_lla: Optional[list[float]] = None,
    t0: Optional[float] = None,
    x0: Optional[list[float]] = None,
    phicx0: Optional[float] = None,
    psicx0: Optional[float] = None,
    sm: Optional[float] = None,
    dt1: Optional[float] = None,
    phicx20: Optional[float] = None,
    psicx20: Optional[float] = None,
    dt2: Optional[float] = None,
    force2: Optional[float] = None,
    ips2: Optional[float] = None,
    height4: Optional[float] = None,
    force4: Optional[float] = None,
    ips4: Optional[float] = None,
    sa4: Optional[float] = None,
    cons_h: Optional[float] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Optimize rocket vertical landing trajectory.

    Endpoint: POST /Rocket/RocketLanding

    Uses 4-segment model with aerodynamics for powered descent landing.

    Args:
        name: Mission name
        text: Mission description
        is_optimize: Whether to optimize trajectory
        a0: Launch azimuth (deg)
        fa_she_dian_lla: Launch site coordinates (lon(deg), lat(deg), alt(m))
        t0: Initial segment time (s from launch)
        x0: Initial segment state (launch inertial frame: position(m), velocity(m/s), mass(kg))
        phicx0: Initial segment pitch angle (deg)
        psicx0: Initial segment yaw angle (deg)
        sm: Aerodynamic area (m²)
        dt1: Attitude adjustment segment duration (s)
        phicx20: Turn segment initial pitch angle (deg)
        psicx20: Turn segment initial yaw angle (deg)
        dt2: Turn segment working duration (s)
        force2: Turn segment vacuum thrust (N)
        ips2: Turn segment vacuum specific impulse (m/s)
        height4: Landing segment initial height (km)
        force4: Landing segment sea-level thrust (N)
        ips4: Landing segment sea-level specific impulse (m/s)
        sa4: Landing segment engine nozzle area (m²)
        cons_h: Landing point height (km)
        session: Optional HTTP session

    Returns:
        Optimized landing trajectory
    """

def compute_guided_trajectory(
    guidance_config: RocketGuid,
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Calculate rocket trajectory using guidance algorithms.

    Endpoint: POST /Rocket/RocketGuid

    Args:
        guidance_config: Guidance algorithm configuration (RocketGuid discriminated union)
                        Must include $type field: "CZ3BC", "CZ2CD", "CZ4BC", "KZ1A", or "CZ7A"
        session: Optional HTTP session

    Returns:
        Guided trajectory calculation results
    """
```

---

### 9. Terrain Module (`astrox/terrain.py`)

**Total: 1 function (2 endpoints merged)**

```python
def get_terrain_mask(
    site_position: EntityPositionSite,
    *,
    method: str = "default",  # "default" or "simple"
    text: Optional[str] = None,
    terrain_mask_para: Optional[TerrainMaskConfig] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Get azimuth-elevation terrain mask for ground station.

    Endpoints (merged):
    - POST /Terrain/AzElMask (method="default")
    - POST /Terrain/AzElMaskSimple (method="simple")

    Args:
        site_position: Ground station position (EntityPositionSite)
        method: Calculation method ("default" or "simple")
        text: Description
        terrain_mask_para: Terrain mask configuration (TerrainMaskConfig)
        session: Optional HTTP session

    Returns:
        360° azimuth-elevation mask data
    """
```

---

### 10. Access Module (`astrox/access.py`)

**Total: 2 functions**

```python
def compute_access(
    start: str,
    stop: str,
    from_object: EntityPath,
    to_object: EntityPath2,
    *,
    description: Optional[str] = None,
    out_step: Optional[float] = None,
    compute_aer: Optional[bool] = None,
    use_light_time_delay: Optional[bool] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Compute access between two objects.

    Endpoint: POST /access/AccessComputeV2

    Args:
        start: Analysis start time (UTCG) format: "yyyy-MM-ddTHH:mm:ssZ"
        stop: Analysis end time (UTCG)
        from_object: Source entity path (EntityPath)
        to_object: Target entity path (EntityPath2)
        description: Description
        out_step: Output time step (s)
        compute_aer: Whether to calculate AER parameters
        use_light_time_delay: Whether to use light time delay
        session: Optional HTTP session

    Returns:
        Access computation results
    """

def compute_chain(
    start: str,
    stop: str,
    all_objects: list[IEntityObject],
    start_object: str,
    end_object: str,
    *,
    description: Optional[str] = None,
    connections: Optional[list[LinkConnection]] = None,
    use_light_time_delay: Optional[bool] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Compute access chain through multiple objects.

    Endpoint: POST /access/ChainCompute

    Args:
        start: Analysis start time (UTCG)
        stop: Analysis end time (UTCG)
        all_objects: All link objects (array of IEntityObject)
        start_object: Start object name (usually Transmitter)
        end_object: End object name (usually Receiver)
        description: Description
        connections: All possible links between start and end objects (array of LinkConnection)
        use_light_time_delay: Whether to use light time delay
        session: Optional HTTP session

    Returns:
        Chain computation results
    """
```

---

### 11. Astrogator Module (`astrox/astrogator.py`)

**Total: 1 function**

```python
def run_mcs(
    central_body: str,
    main_sequence: list[AgVAMCSSegment],
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    gravitational_parameter: Optional[float] = None,
    entities: Optional[list[EntityPath]] = None,
    propagators: Optional[list[Propagator]] = None,
    engine_models: Optional[list[IAgVAEngine]] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Run Mission Control Sequence (MCS) for trajectory design.

    Endpoint: POST /Astrogator/RunMCS

    Args:
        central_body: Central body name (e.g., Earth, Moon, Mars, Sun)
        main_sequence: Flight segment mission sequence array (array of AgVAMCSSegment)
        name: Object name
        description: Object description
        gravitational_parameter: Central body gravitational constant (m³/s²)
        entities: Other objects collection (array of EntityPath)
        propagators: All integrators (array of Propagator)
        engine_models: All engine models (array of IAgVAEngine)
        session: Optional HTTP session

    Returns:
        MCS execution results
    """
```

---

### 12. Landing Zone Module (`astrox/landing_zone.py`)

**Total: 1 function**

```python
def compute_landing_zone(
    fa_she_dian: list[float],
    luo_dian: list[float],
    zone_xys: list[float],
    *,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Compute landing zone parameters.

    Endpoint: POST /LandingZone

    Args:
        fa_she_dian: Launch point coordinates (lon(deg), lat(deg), alt(m))
        luo_dian: Landing point coordinates (lon(deg), lat(deg), alt(m))
        zone_xys: Boundary point parameters (front is +X axis, right is +Y axis, unit: km)
        session: Optional HTTP session

    Returns:
        Landing zone output
    """
```

---

## Implementation Strategy

### Step 1: Create HTTP Client (`astrox/_http.py`)
Already designed in CLAUDE.md - ContextVar-based session management.

### Step 2: Implement Functions Module by Module
For each function:
1. Extract required vs optional parameters from schema
2. Convert field names to snake_case
3. Order parameters: required → optional → output/method/version → session
4. Set all optional parameters to `None` (minimal processing)
5. Build request payload by converting snake_case back to API field names
6. Call `session.request()` with appropriate HTTP method and endpoint

### Step 3: Type Hints from `astrox/models.py`
Where applicable, use domain models:
- `EntityPath` for entity definitions
- `KeplerElements*` variants for orbital elements
- Keep complex nested structures as `dict` where no clear model exists

### Step 4: Docstring Template
```python
def function_name(
    required_param: type,
    *,
    optional_param: Optional[type] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """Brief one-line description.

    Endpoint: POST /API/Path

    Longer description if needed.

    Args:
        required_param: Description
        optional_param: Description
        session: Optional HTTP session

    Returns:
        Description of return value
    """
```

## Critical Files to Create/Modify

1. `astrox/_http.py` - HTTP client (already designed)
2. `astrox/coverage.py` - 8 functions
3. `astrox/propagator.py` - 9 functions
4. `astrox/conjunction_analysis.py` - 4 functions
5. `astrox/lighting.py` - 3 functions
6. `astrox/orbit_convert.py` - 5 functions
7. `astrox/orbit_wizard.py` - 4 functions
8. `astrox/orbit_system.py` - 2 functions
9. `astrox/rocket.py` - 3 functions
10. `astrox/terrain.py` - 1 function
11. `astrox/access.py` - 2 functions
12. `astrox/astrogator.py` - 1 function
13. `astrox/landing_zone.py` - 1 function

## Next Steps

1. User reviews this plan
2. Begin implementation following the signatures above
3. Test each module with actual API calls
4. Iterate based on API responses and edge cases
