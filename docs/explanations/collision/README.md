# Conjunction Analysis (CAT)

Collision avoidance and debris modeling.

## Close Approach Analysis

### V3 - TLE-based Screening

Screen satellite against the space catalog using TLE data.

- **Example**: `examples/05_collision/close_approach_v3_tle.py`

### V3 with Specified Targets

Check against specific target satellites only.

- **Example**: `examples/05_collision/close_approach_v3_focused.py`

### V4 - Trajectory-based

For rocket trajectories using CZML position data.

- **Example**: `examples/05_collision/close_approach_v4_czml.py`

### High Sensitivity Parameters

Fine-tuned detection thresholds for critical missions.

- **Example**: `examples/05_collision/close_approach_v3_high_sensitivity.py`

## Debris Breakup Models

### Simple Model

Basic velocity-based breakup with uniform distribution.

- **Example**: `examples/05_collision/debris_breakup_simple.py`

### Default Model

Directional breakup with custom velocity parameters.

- **Example**: `examples/05_collision/debris_breakup_default.py`

### NASA Standard Breakup Model

Empirical model based on NASA research.

- **Example**: `examples/05_collision/debris_breakup_nasa.py`

## TLE Operations

TLE propagation and lifetime estimation.

- **Example**: `examples/05_collision/tle_operations.py`
- **Example**: `examples/05_collision/lifetime_calculation.py`
