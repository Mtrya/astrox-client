# Access Computation

Access (visibility) computation between objects in space.

## Position Types

EntityPath supports multiple position types for access calculations:

### TwoBodyPosition
Simple two-body orbital propagation.

- **Example**: `examples/03_access/access_two_body_position.py`

### CentralBodyPosition
Fixed position relative to a central body.

- **Example**: `examples/03_access/access_central_body_position.py`

### BallisticPosition
Ballistic/missile trajectory position.

- **Example**: `examples/03_access/access_ballistic_position.py`

### J2Position
J2-perturbed orbital propagation.

- **Example**: `examples/03_access/access_j2_position.py`

### CzmlPosition
CZML-based trajectory position.

- **Example**: `examples/03_access/access_czml_position.py`

### CzmlPositionsData
Multiple CZML positions for batch access.

- **Example**: `examples/03_access/access_czml_positions_data.py`

### SitePosition
Ground station/site position.

- **Example**: `examples/03_access/access_site_position.py`

### SGP4Position
SGP4-propagated position from TLE.

- **Example**: `examples/03_access/access_sgp4_position.py`

## Chain Computation

Multi-hop access chains through relay satellites.

- **Example**: `examples/03_access/chain_access.py`

## AER Data

Access calculations can include Azimuth, Elevation, and Range (AER) data.

See individual position type examples for AER computation patterns.
