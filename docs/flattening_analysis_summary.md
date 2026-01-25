# Function Parameter Flattening Analysis

## Question
Is one-layer flattening sufficient for all Input/Output models? Specifically, after flattening `xxxInput` → `dict{key: value}`, are all values either:
1. Native types (str, int, float, bool)
2. Pydantic models
3. Lists of the above

Or do we have problematic nested dicts?

## Answer: ✓ **One-layer flattening is sufficient!**

## Analysis Results

**Analyzed:** 53 Input/Output models across all 73 endpoints

**Field type distribution:**
- Native Types (str, int, float, bool): **288 fields** (71%)
- Pydantic Models: **85 fields** (21%)
- Lists: **27 fields** (7%)
- Unions: **23 fields** (6%)
- **Problematic Dicts: 2 fields** (<1%)

## The One Exception

**`ChainOutput`** (used by `/api/Access/ChainCompute` endpoint):

```python
# Problematic fields:
- IndividualStrandAccess: Dict[str, List[Any]]
- IndividualObjectAccess: Dict[str, List[Any]]
```

**Why problematic:** The OpenAPI spec has `items: {}` (empty), meaning the array items are untyped. Based on field descriptions (Chinese comments), these should be `Dict[str, List[TimeIntervalData]]` but the spec doesn't define the item type.

**Impact:** Only affects the `chain_compute()` function in `access.py`.

**Recommended handling:**
```python
def chain_compute(
    chains: list[list[str]],
    from_object: EntityPath,
    to_objects: list[EntityPath],
    *,
    start: Optional[str] = None,
    stop: Optional[str] = None,
    session: Optional[HTTPClient] = None,
) -> dict:
    """
    Returns:
        dict with fields:
            - IsSuccess: bool
            - Message: str
            - ComputedStrands: list[list[str]]
            - CompleteChainAccess: list[TimeIntervalData]
            - IndividualStrandAccess: dict[str, list]  # Untyped in spec
            - IndividualObjectAccess: dict[str, list]  # Untyped in spec
    """
```

We keep these as `dict` in the return type and document the limitation. Users will work with them as dicts.

## Conclusion

**One-layer flattening is sufficient for 99.5% of all fields** (360 out of 362 total fields).

The two problematic fields are:
1. In a single output model (`ChainOutput`)
2. Due to incomplete OpenAPI spec (missing item types)
3. Easy to handle - we just return them as `dict` and document the structure

## What This Means for Function Signatures

**We can confidently apply the flattening strategy:**

```python
# ✓ All parameter values are either native types, models, or lists
def grid_coverage(
    entities: list[EntityPath],          # List[Model]
    grid: CoverageGrid,                  # Model (union)
    start: str,                          # Native type
    stop: str,                           # Native type
    *,
    out_step: Optional[float] = None,    # Native type
    session: Optional[HTTPClient] = None,
) -> dict:
    """All inputs are properly typed - no nested dicts!"""
```

**Key domain models to expose in `models.py`:**
- Grid types: `GlobalGrid`, `LatitudeBoundsGrid`, `LatLonBoundsGrid`
- Position types: `Cartesian`, `Keplerian`, `Spherical`, `SGP4Position`, etc.
- Sensor types: `ConicSensor`, `RectangularSensor`
- Attitude types: `FiniteAttitude`, `ImpulsiveAttitude`
- Constraint types: Various constraint models
- And ~75 more models identified in the analysis

## Next Steps

1. **Update `models.py`** to export all domain models (not just the ~90 we initially planned, but expand as needed based on usage)

2. **Design function signatures** using these typed models instead of bare dicts

3. **Grid types specifically** (from earlier discussion):
   ```python
   # Instead of:
   def get_grid_points(grid: dict, ...) -> dict:

   # Use:
   def get_grid_points(grid: CoverageGrid, ...) -> dict:

   # Where CoverageGrid = Union[GlobalGrid, LatitudeBoundsGrid, LatLonBoundsGrid, ...]
   ```

4. **Document the `ChainOutput` limitation** in the `chain_compute()` docstring

## Full Details

See `docs/model_depth_analysis.md` for complete field-by-field breakdown of all 53 models.
