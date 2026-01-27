# Known Issues - Access Examples

## HTTP 500 Errors (Server-Side Issues)

### 1. `/access/ChainCompute` - Returns HTTP 500

**Status**: Server-side error (not a client issue)

**Affected Examples**:
- `chain_access.py` - `compute_chain()` function

**Error**: `astrox.exceptions.AstroxHTTPError: HTTP 500: Internal Server Error`

**Verified Behavior** (tested 2026-01-27):
- The endpoint `/access/ChainCompute` exists in the OpenAPI spec
- The payload format is correct (includes all required discriminators: `$type` fields)
- The HTTPClient correctly raises `AstroxHTTPError` for HTTP 500 responses
- The example code now accesses fields directly without defensive `IsSuccess` checks
- When the server returns HTTP 500, the code fails naturally, revealing the server-side issue

**Expected Response Structure** (from OpenAPI spec):
```json
{
  "IsSuccess": bool,
  "Message": str,
  "ComputedStrands": list[list[str]] | null,
  "CompleteChainAccess": list[TimeIntervalData] | null,
  "IndividualStrandAccess": dict | null,
  "IndividualObjectAccess": dict | null
}
```
where `TimeIntervalData` has: `{Start: str, Stop: str, Duration: float}`

**Notes**:
- This is a server-side bug in chain computation (returns HTTP 500 instead of HTTP 200 with `IsSuccess: false`)
- The client implementation is correct
- The HTTPClient already checks for `IsSuccess` flag and raises `AstroxAPIError` if false
- Examples should not duplicate this check - let errors propagate naturally

**Recommendation**: Skip `compute_chain()` examples until server-side issue is resolved.

---

## Successfully Working Endpoints

### 1. `/access/AccessComputeV2` - Working

**Status**: Working correctly

**Affected Examples**:
- `compute_access.py` - `compute_access()` function

**API Response Structure**:
```json
{
  "IsSuccess": true,
  "Message": "OK",
  "Passes": [
    {
      "AccessStart": "2022-04-25T16:07:55.725Z",
      "AccessStop": "2022-04-25T16:07:59.021Z",
      "Duration": 3.295902494017355,
      "MinElevationData": {
        "Time": "2022-04-25T16:07:55.725Z",
        "Azimuth": 170.65866937163312,
        "Elevation": -0.10167640918707362,
        "Range": 1988285.214916554,
        "RangeDot": 0
      },
      "MaxElevationData": { ... },
      "MinRangeData": { ... },
      "MaxRangeData": { ... },
      "AccessBeginData": { ... },
      "AccessEndData": { ... },
      "AllDatas": [
        {
          "Time": "2022-04-25T16:07:55.725Z",
          "Azimuth": 170.65866937163352,
          "Elevation": -0.10167640918714721,
          "Range": 1988285.214916558,
          "RangeDot": 0
        },
        ...
      ]
    }
  ]
}
```

**Notes**:
- Function works correctly after fixing endpoint path from `/Access/V2` to `/access/AccessComputeV2`
- Properly handles all required fields: `FromObjectPath`, `ToObjectPath`
- Successfully returns access computation results (even when no access windows are found)
- Example code uses correct schema fields: `Passes`, `AllDatas`, `AccessStart`, `AccessStop`, `Duration`, `Time`, `Azimuth`, `Elevation`, `Range`
