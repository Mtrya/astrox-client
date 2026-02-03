# Coverage Analysis

Coverage analysis for satellite constellations and ground observation.

## Grid Types

Coverage can be computed over different grid types:

- Global grids
- Regional grids
- Custom point sets

See `examples/02_coverage/basic_coverage.py` for grid-based coverage.

## Sensors

### Conic Sensor

Cone-shaped sensor (typical for optical payloads).

- **Example**: `examples/03_access/access_j2_position.py`

### Rectangular Sensor

Rectangular field of view (typical for SAR payloads).

## Figure of Merit (FOM)

Coverage quality metrics:

- **Coverage Time**: Total time a point is visible
- **Response Time**: Time to first access
- **Revisit Time**: Time between accesses
- **Number of Assets**: Count of simultaneous coverage

- **Example**: `examples/02_coverage/fom_calculations.py`

## Reports

Coverage statistics and facility-based reports.

- **Example**: `examples/02_coverage/coverage_statistics.py`
