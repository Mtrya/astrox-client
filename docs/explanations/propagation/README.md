# Propagation

Orbital propagation methods for predicting satellite trajectories.

## Methods

### Two-Body Propagation

The simplest orbital propagation model using only the gravitational parameter.

- **Example**: `examples/01_propagation/two_body_cartesian.py`
- **Theory**: [Two-body problem (Wikipedia)](https://en.wikipedia.org/wiki/Two-body_problem)

### J2 Perturbation

Includes Earth's oblateness (J2 term) for more accurate LEO predictions.

- **Example**: `examples/01_propagation/j2_propagation.py`
- **Theory**: [Orbital perturbation analysis (Wikipedia)](https://en.wikipedia.org/wiki/Orbital_perturbation_analysis)

### High-Precision Orbit Propagator (HPOP)

Full force model including drag, solar radiation pressure, and third-body effects.

- **Examples**: `examples/01_propagation/hpop_*.py`
- **Theory**: STK HPOP documentation

### SGP4

Standard propagator for TLE-based orbit prediction.

- **Example**: `examples/01_propagation/sgp4_propagation.py`
- **Theory**: [SGP4 (Wikipedia)](https://en.wikipedia.org/wiki/Simplified_perturbations_models)

### Ballistic Trajectory

For missile and rocket ascent/descent calculations.

- **Examples**: `examples/01_propagation/ballistic_*.py`

## Coordinate Systems

- Inertial (J2000/ICRF)
- Fixed (Earth-fixed)
- LVLH (Local Vertical Local Horizontal)

See individual example files for specific coordinate system usage.
