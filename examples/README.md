# ASTROX Client Examples

This directory contains example scripts demonstrating how to use the `astrox-client` Python SDK to interact with the ASTROX Web API for aerospace and satellite computations.

## Overview

The ASTROX Web API provides 43 functions across 12 domain modules:

| Module | Functions | Description |
|--------|-----------|-------------|
| **Propagation** | 9 | Orbit propagation (two-body, J2, SGP4, HPOP, ballistic, batch) |
| **Coverage** | 8 | Coverage analysis and figures of merit (FOM) calculations |
| **Access** | 2 | Access computation between objects and access chains |
| **Orbit Design** | 11 | Orbit design utilities, coordinate conversions, frame transforms |
| **Collision** | 4 | Conjunction analysis, debris breakup, TLE operations (CAT2) |
| **Rocket** | 3 | Rocket trajectory optimization and guidance |
| **Lighting** | 3 | Solar intensity and lighting time calculations |
| **Orbit System** | 2 | Central body frame conversion, libration points |
| **Terrain** | 1 | Terrain mask calculations |
| **Astrogator** | 1 | Mission Control Sequence (MCS) execution |
| **Landing Zone** | 1 | Landing zone calculations |

## Directory Structure

```
examples/
├── 01_propagation/      # Orbit propagation examples
├── 02_coverage/         # Coverage analysis examples
├── 03_access/           # Access computation examples
├── 04_orbit_design/     # Orbit design and conversion examples
├── 05_collision/        # Collision avoidance and debris examples
├── 06_rocket/           # Rocket trajectory examples
├── 07_lighting/         # Lighting and solar calculations
├── 08_orbit_system/     # Orbit system utilities
├── 09_terrain/          # Terrain calculations
├── 10_astrogator/       # Astrogator MCS examples
└── 11_landing_zone/     # Landing zone examples
```

## Getting Started

### Installation

```bash
pip install astrox-client
```

### Basic Usage Pattern

All examples follow a consistent pattern:

```python
# Import domain functions and models
from astrox.propagator import propagate_two_body
from astrox.models import Cartesian, KeplerElements

# Option 1: Zero-config usage (default session)
result = propagate_two_body(
    start="2024-01-01T00:00:00Z",
    stop="2024-01-02T00:00:00Z",
    orbit_epoch="2024-01-01T00:00:00Z",
    orbital_elements=[6678137, 0, 28.5, 0, 0, 0],
)

# Option 2: Custom configuration (global session)
from astrox import configure

configure(base_url="http://custom:8765", timeout=60)
result = propagate_two_body(...)  # Uses configured session

# Option 3: Explicit session (advanced)
from astrox import HTTPClient

session = HTTPClient(timeout=120)
result = propagate_two_body(..., session=session)
```

## Example Categories

### 1. Propagation (`01_propagation/`)

Orbit propagation with various dynamics models:

- `two_body.py` - Simple two-body propagation
- `j2_propagation.py` - J2 perturbation model
- `sgp4_propagation.py` - SGP4 propagator from TLEs
- `hpop_propagation.py` - High-precision orbit propagator (HPOP)
- `ballistic.py` - Ballistic trajectory propagation
- `simple_ascent.py` - Simple ascent trajectory
- `batch_propagation.py` - Batch propagation (J2, SGP4, two-body)

### 2. Coverage Analysis (`02_coverage/`)

Coverage analysis and figures of merit:

- `basic_coverage.py` - Basic grid coverage computation
- `fom_calculations.py` - FOM calculations (simple coverage, coverage time, etc.)
- `coverage_statistics.py` - Coverage statistics and reporting

### 3. Access Computation (`03_access/`)

Access computation between spacecraft and ground stations:

- `compute_access.py` - Basic access computation
- `chain_access.py` - Access chain computation

### 4. Orbit Design (`04_orbit_design/`)

Orbit design utilities and coordinate conversions:

- `geo_orbit.py` - GEO orbit generation
- `molniya_orbit.py` - Molniya orbit generation
- `sso_orbit.py` - Sun-synchronous orbit (SSO) generation
- `walker_constellation.py` - Walker constellation design
- `coordinate_conversions.py` - Kepler ↔ RV conversions, LLA calculations

### 5. Collision Avoidance (`05_collision/`)

Conjunction analysis and debris modeling (CAT2):

- `close_approach.py` - Close approach detection
- `debris_breakup.py` - Debris breakup modeling
- `tle_operations.py` - TLE generation and operations
- `lifetime_calculation.py` - Orbital lifetime estimation

### 6. Rocket Trajectories (`06_rocket/`)

Rocket trajectory optimization:

- `ascent_optimization.py` - Rocket ascent trajectory optimization
- `descent_optimization.py` - Powered descent landing optimization
- `guidance_trajectory.py` - Guidance algorithm trajectory calculation

### 7. Lighting (`07_lighting/`)

Solar and lighting calculations:

- `solar_intensity.py` - Solar intensity calculations
- `lighting_times.py` - Lighting time windows
- `solar_aer.py` - Solar azimuth-elevation-range (AER) calculations

### 8. Orbit System (`08_orbit_system/`)

Orbit system utilities:

- `frame_conversion.py` - Central body frame conversions
- `libration_points.py` - Earth-Moon libration point calculations

### 9. Terrain (`09_terrain/`)

Terrain calculations:

- `terrain_mask.py` - Terrain mask generation

### 10. Astrogator (`10_astrogator/`)

Mission Control Sequence (MCS):

- `run_mcs.py` - Execute Mission Control Sequence

### 11. Landing Zone (`11_landing_zone/`)

Landing zone calculations:

- `landing_zone.py` - Landing zone computation

## Running Examples

Each example is a standalone Python script that can be run directly:

```bash
# Run a specific example
python examples/01_propagation/two_body.py

# Run with custom API endpoint
ASTROX_BASE_URL=http://localhost:8765 python examples/01_propagation/two_body.py
```

## API Reference

For complete API documentation, see the main project README and function docstrings.

## Contributing

To add new examples:

1. Choose the appropriate category directory
2. Create a descriptive filename (e.g., `custom_propagation.py`)
3. Follow the established pattern: imports, configuration, execution, output
4. Add clear comments explaining each step
5. Include expected outputs or validation

## Resources

- **API Server**: http://astrox.cn:8765/
- **OpenAPI Spec**: http://astrox.cn:8765/openapi/v1.json
- **Project Repository**: https://github.com/your-org/astrox-client
- **PyPI Package**: https://pypi.org/project/astrox-client/
