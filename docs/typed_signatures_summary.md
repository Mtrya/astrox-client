# Typed Function Signatures Summary

## Overview

Successfully updated all 43 function signatures across 12 modules to use proper Pydantic model types instead of generic `dict` parameters.

**Total changes:** 93 parameter type updates
**Models introduced:** 32 distinct Pydantic types from OpenAPI spec

## Verification Complete

✅ **One-layer flattening is sufficient** - confirmed by model depth analysis
✅ **All dict parameters replaced** - 93 updates across all modules
✅ **Type safety achieved** - proper domain models for all complex parameters
✅ **Union types for variants** - correctly handles API version differences
✅ **Ready for implementation** - signatures are complete and consistent

## Key Type Replacements by Category

### 1. Coverage Grid Types (64 occurrences)

**Before:**
```python
def get_grid_points(
    grid: dict,  # ❌ Unclear to users
    ...
)
```

**After:**
```python
def get_grid_points(
    grid: Union[
        ICoverageGridCoverageGridGlobal,
        ICoverageGridCoverageGridLatitudeBounds,
        ICoverageGridCoverageGridLatLonBounds,
        ICoverageGridCovGridLatLonBounds
    ],  # ✅ Clear, typed, discoverable
    ...
)
```

**Impact:** 8 coverage functions, all with properly typed grids, assets, sensors, and constraints.

### 2. Entity & Position Types

| Before | After | Usage |
|--------|-------|-------|
| `from_object: dict` | `from_object: EntityPath` | Access compute |
| `to_object: dict` | `to_object: EntityPath2` | Access compute |
| `position: dict` | `position: IEntityPosition2` | Lighting functions |
| `site_position: dict` | `site_position: EntityPositionSite2/Site4` | Solar AER, terrain |
| `assets: list` | `assets: list[EntityPath3]` | Coverage functions |

### 3. Orbital Elements Types

| Before | After | Usage |
|--------|-------|-------|
| `kepler_platform: dict` | `kepler_platform: KeplerElements3` | GEO Lambert transfer |
| `kepler_target: dict` | `kepler_target: KeplerElements2` | GEO Lambert transfer |
| `seed_kepler: dict` | `seed_kepler: KeplerElements8` | Walker constellation |
| `all_satellite_elements: list` | `all_satellite_elements: list[KeplerElementsWithEpoch]` | Batch propagators |

**Note:** Different numbered variants (KeplerElements2, KeplerElements3, KeplerElements8) exist in the spec with subtle field differences. Using exact schema names preserves correctness.

### 4. TLE & Collision Analysis Types

| Before | After | Usage |
|--------|-------|-------|
| `sat1: dict` | `sat1: Union[TleInfo, EntityPositionCzml]` | Close approach (version-dependent) |
| `mother_satellite: dict` | `mother_satellite: TleInfo` | Debris breakup |
| `tles: dict` | `tles: TleInfo2` | Orbital lifetime |
| `targets: Optional[list]` | `targets: Optional[list[TleInfo]]` | Close approach targets |

### 5. Sensor & Constraint Types

| Before | After | Usage |
|--------|-------|-------|
| `grid_point_sensor: Optional[dict]` | `grid_point_sensor: Optional[ISensor2]` | Coverage functions |
| `grid_point_constraints: Optional[list]` | `grid_point_constraints: Optional[list[IContraint]]` | Coverage functions |

### 6. Rocket Types

| Before | After | Usage |
|--------|-------|-------|
| `rocket_segments: list` | `rocket_segments: list[RocketSegment]` | Trajectory optimization |
| `guidance_config: dict` | `guidance_config: RocketGuid` | Guided trajectory |
| `profile_optim: Optional[dict]` | `profile_optim: Optional[VAMCSProfileDEOptimizer]` | Trajectory optimization |
| `mcs_profiles: Optional[list]` | `mcs_profiles: Optional[list[MCSProfile]]` | Trajectory optimization |

### 7. Propagator Types

| Before | After | Usage |
|--------|-------|-------|
| `hpop_propagator: Optional[dict]` | `hpop_propagator: Optional[Propagator2]` | HPOP propagation |

### 8. Astrogator/MCS Types

| Before | After | Usage |
|--------|-------|-------|
| `main_sequence: list` | `main_sequence: list[AgVAMCSSegment]` | MCS run |
| `entities: Optional[list]` | `entities: Optional[list[EntityPath3]]` | MCS run |
| `propagators: Optional[list]` | `propagators: Optional[list[Propagator]]` | MCS run |
| `engine_models: Optional[list]` | `engine_models: Optional[list[IAgVAEngine]]` | MCS run |

### 9. Access Chain Types

| Before | After | Usage |
|--------|-------|-------|
| `all_objects: list` | `all_objects: list[IEntityObject]` | Chain compute |
| `connections: Optional[list]` | `connections: Optional[list[LinkConnection]]` | Chain compute |

### 10. Terrain Types

| Before | After | Usage |
|--------|-------|-------|
| `terrain_mask_para: Optional[dict]` | `terrain_mask_para: Optional[TerrainMaskConfig]` | Terrain mask |

## Module-by-Module Breakdown

| Module | Functions | Parameters Updated | Key Types Introduced |
|--------|-----------|-------------------|---------------------|
| coverage.py | 8 | 64 | CoverageGrid union, EntityPath3, ISensor2, IContraint |
| propagator.py | 9 | 3 | Propagator2, KeplerElementsWithEpoch |
| conjunction_analysis.py | 4 | 5 | TleInfo, TleInfo2, EntityPositionCzml |
| lighting.py | 3 | 3 | IEntityPosition2, EntityPositionSite2 |
| orbit_convert.py | 5 | 2 | KeplerElements2, KeplerElements3 |
| orbit_wizard.py | 4 | 1 | KeplerElements8 |
| orbit_system.py | 2 | 1 | EntityPositionCzml2 |
| rocket.py | 3 | 5 | RocketSegment, RocketGuid, VAMCSProfileDEOptimizer, MCSProfile |
| terrain.py | 1 | 2 | EntityPositionSite4, TerrainMaskConfig |
| access.py | 2 | 4 | EntityPath, EntityPath2, IEntityObject, LinkConnection |
| astrogator.py | 1 | 4 | AgVAMCSSegment, EntityPath3, Propagator, IAgVAEngine |
| landing_zone.py | 1 | 0 | *(all primitives)* |

**Total:** 43 functions, 93 parameter updates

## Benefits of Typed Signatures

### 1. IDE Autocomplete & Discovery

**Before (dict):**
```python
# User has no idea what fields to pass
result = get_grid_points(grid={...})  # ❌ What goes in here?
```

**After (typed):**
```python
from astrox.models import GlobalGrid

# IDE shows all available fields with types
grid = GlobalGrid(
    CentralBodyName="Earth",  # ← autocomplete!
    Resolution=6.0,           # ← type hints!
    Height=0.0                # ← validation!
)
result = get_grid_points(grid=grid)  # ✅ Clear and safe
```

### 2. Type Checking & Validation

```python
# Pydantic validates before API call
grid = GlobalGrid(
    Resolution="six"  # ❌ TypeError: Resolution must be float
)

# IDE catches mistakes immediately
grid = LatitudeBoundsGrid(
    MinLatitude=-45.0,
    MaxLatitude=45.0,
    # Missing required field MaxLatitude → IDE warns!
)
```

### 3. Self-Documenting Code

```python
# Function signature tells you exactly what's needed
def compute_coverage(
    start: str,
    stop: str,
    grid: Union[GlobalGrid, LatitudeBoundsGrid, LatLonBoundsGrid, ...],
    assets: list[EntityPath3],
    *,
    grid_point_sensor: Optional[ISensor2] = None,
    grid_point_constraints: Optional[list[IContraint]] = None,
    ...
) -> dict:
    """No need to guess types - it's all in the signature!"""
```

### 4. Version Safety

```python
# Union types handle API version differences
def compute_close_approach(
    sat1: Union[TleInfo, EntityPositionCzml],  # Different types for v3 vs v4
    *,
    version: str = "v4",
    ...
):
    """Type system ensures correct model for each version."""
```

## Important Design Decisions

### 1. Raw Schema Names (Not Aliased)

We use exact OpenAPI schema names in function signatures:
- `EntityPath3` (not `Entity`)
- `KeplerElements8` (not `KeplerElements`)
- `ICoverageGridCoverageGridGlobal` (not `GlobalGrid`)

**Rationale:** Pythonic aliases will be created in `astrox/models.py` later. Keeping raw names in the plan ensures traceability to the OpenAPI spec.

### 2. Preserved Primitives

Some parameters remain as basic types:
```python
orbital_elements: list[float]  # Not a domain model, just 6 numbers
fa_she_dian: list[float]       # Just [lon, lat, alt]
zone_xys: list[float]          # Just boundary coordinates
```

**Rationale:** These are raw numeric arrays, not domain objects. Creating models for them would be over-engineering.

### 3. Return Types Stay as `dict`

All functions still return `dict` rather than typed output models.

**Rationale:** Per design philosophy - minimal processing, let users consume raw JSON. Output validation is less critical than input validation.

### 4. Union Types for Variants

Grid types use Union instead of parent type:
```python
grid: Union[GlobalGrid, LatitudeBoundsGrid, ...]  # ✅ Correct
# NOT:
grid: ICoverageGrid  # ❌ This is an interface, not a concrete type
```

**Rationale:** OpenAPI discriminated unions map to Python Union types for proper type checking.

## Next Steps

### 1. Rewrite `astrox/models.py`

Create pythonic aliases for all domain models:
```python
# astrox/models.py
from astrox._models import (
    # Grid types
    ICoverageGridCoverageGridGlobal as GlobalGrid,
    ICoverageGridCoverageGridLatitudeBounds as LatitudeBoundsGrid,
    ICoverageGridCoverageGridLatLonBounds as LatLonBoundsGrid,
    ICoverageGridCovGridLatLonBounds as CentralBodyLatLonBoundsGrid,

    # Union for coverage grids
    # (we'll need to create this as a type alias)
)

# Export union type
from typing import Union
CoverageGrid = Union[GlobalGrid, LatitudeBoundsGrid, LatLonBoundsGrid, CentralBodyLatLonBoundsGrid]

__all__ = [
    "GlobalGrid",
    "LatitudeBoundsGrid",
    "LatLonBoundsGrid",
    "CentralBodyLatLonBoundsGrid",
    "CoverageGrid",
    # ... ~90+ more aliases
]
```

### 2. Update Function Signatures to Use Aliases

Once `models.py` is complete, update function signatures:
```python
# Before (raw names):
def get_grid_points(
    grid: Union[ICoverageGridCoverageGridGlobal, ICoverageGrid...],
    ...
)

# After (pythonic aliases):
def get_grid_points(
    grid: CoverageGrid,  # ✅ Clean union type alias
    ...
)
```

### 3. Implement Functions Module by Module

Start implementing the 43 functions following the typed signatures.

### 4. Test with Real API

Validate that Pydantic models serialize correctly to API JSON format.

## Files Updated

1. ✅ **docs/function_signatures.md** - All 43 function signatures with proper types
2. ✅ **docs/flattening_analysis_summary.md** - Analysis confirming one-layer flattening works
3. ✅ **docs/model_depth_analysis.md** - Complete field-by-field model analysis
4. ✅ **scripts/analyze_model_depth.py** - Tool for analyzing model structure
5. ✅ **docs/typed_signatures_summary.md** - This document

## Conclusion

**Status:** ✅ Function signature design is complete and ready for implementation.

All 93 dict/untyped-list parameters have been replaced with proper Pydantic model types from the OpenAPI spec. The signatures are:
- **Type-safe** - IDE autocomplete and validation
- **Self-documenting** - Clear from signatures what's required
- **Traceable** - Uses exact OpenAPI schema names
- **Ready to implement** - Complete and consistent

Next step: Rewrite `astrox/models.py` with pythonic aliases, then implement the actual functions.
