# Model Depth Analysis

Analysis of whether one-layer flattening is sufficient for all Input/Output models.

## Problematic Models

These models have fields that are untyped dicts or inline objects:

### ChainOutput

- `IndividualStrandAccess`: `Dict[str, List[Any]]`
- `IndividualObjectAccess`: `Dict[str, List[Any]]`

## All Models

### AccessInput2

- `ComputeAER`: `bool`
- `Description`: `str`
- `FromObjectPath`: `Model(EntityPath)`
- `OutStep`: `float`
- `Start`: `str`
- `Stop`: `str`
- `ToObjectPath`: `Model(EntityPath2)`
- `UseLightTimeDelay`: `bool`

### AccessOutput

- `IsSuccess`: `bool`
- `Message`: `str`
- `Passes`: `None`

### AzimuthElevationMaskInput

- `TerrainMaskPara`: `Model(TerrainMaskConfig)`
- `Text`: `str`
- `sitePosition`: `Model(EntityPositionSite4)`

### BallisticInput

- `BallisticType`: `str`
- `BallisticTypeValue`: `float`
- `CentralBody`: `str`
- `GravitationalParameter`: `float`
- `ImpactAltitude`: `float`
- `ImpactLatitude`: `float`
- `ImpactLongitude`: `float`
- `LaunchAltitude`: `float`
- `LaunchLatitude`: `float`
- `LaunchLongitude`: `float`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `Union[str, None]`

### CAInput

- `SAT1`: `Model(TleInfo)`
- `Start_UTCG`: `str`
- `Stop_UTCG`: `str`
- `Targets`: `List[Model(TleInfo2)]`
- `TolCrossDt`: `float`
- `TolDh`: `float`
- `TolMaxDistance`: `float`
- `TolTheta`: `float`

### CAInput4

- `SAT1`: `Model(EntityPositionCzml)`
- `Start_UTCG`: `str`
- `Stop_UTCG`: `str`
- `Targets`: `List[Model(TleInfo2)]`
- `TolCrossDt`: `float`
- `TolDh`: `float`
- `TolMaxDistance`: `float`
- `TolTheta`: `float`

### CAOutput

- `AfterApoPeriFilterNumber`: `int`
- `AfterCrossPlaneNumber`: `int`
- `CA_Results`: `List[Model(CAResultInfo)]`
- `IsSuccess`: `bool`
- `Message`: `str`
- `TotalNumber`: `int`

### CAOutput4

- `AfterApoPeriFilterNumber`: `int`
- `AfterCrossPlaneNumber`: `int`
- `CA_Results`: `List[Model(CAResultInfo4)]`
- `IsSuccess`: `bool`
- `Message`: `str`
- `TotalNumber`: `int`

### ChainInput

- `AllObjects`: `List[Model(IEntityObject)]`
- `Connections`: `None`
- `Description`: `str`
- `EndObject`: `str`
- `Start`: `str`
- `StartObject`: `str`
- `Stop`: `str`
- `UseLightTimeDelay`: `bool`

### ChainOutput

- `CompleteChainAccess`: `List[Model(TimeIntervalData)]`
- `ComputedStrands`: `List[List[str]]`
- `IndividualObjectAccess`: `Dict[str, List[Any]]`
- `IndividualStrandAccess`: `Dict[str, List[Any]]`
- `IsSuccess`: `bool`
- `Message`: `str`

### CityDataBaseOutput

- `Cities`: `None`
- `IsSuccess`: `bool`
- `Message`: `str`

### CoverageGridInput

- `Grid`: `Model(ICoverageGrid)`
- `Text`: `str`

### CoverageInput

- `Assets`: `List[Model(EntityPath3)]`
- `ContainAssetAccessResults`: `bool`
- `ContainCoveragePoints`: `bool`
- `Description`: `str`
- `FilterType`: `Union[str, None]`
- `Grid`: `Model(ICoverageGrid)`
- `GridPointConstraints`: `None`
- `GridPointSensor`: `Model(ISensor2)`
- `NumberOfAssets`: `int`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `str`

### CoverageOutput

- `AccessDurationDatas`: `List[Model(AccessDurationData)]`
- `AssetAccessResults`: `List[List[List[Model(CvTimeInterval)]]]`
- `GapDurationDatas`: `List[Model(GapDurationData)]`
- `GlobalCoverageDatas`: `List[Model(GlobalCoverageData)]`
- `IsSuccess`: `bool`
- `Message`: `str`
- `PercentCovered`: `float`
- `Points`: `Model(CoverageGridPoints2)`
- `SatisfactionIntervalsWithNumberOfAssets`: `List[List[Model(CvTimeInterval)]]`

### FOMInput_TimeValueByGridPoint

- `Assets`: `List[Model(EntityPath3)]`
- `ContainAssetAccessResults`: `bool`
- `ContainCoveragePoints`: `bool`
- `Description`: `str`
- `FilterType`: `Union[str, None]`
- `Grid`: `Model(ICoverageGrid)`
- `GridPointConstraints`: `None`
- `GridPointSensor`: `Model(ISensor2)`
- `NumberOfAssets`: `int`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `str`
- `Time`: `str`

### FOMInput_ValueByGridPoint

- `Assets`: `List[Model(EntityPath3)]`
- `ComputeType`: `str`
- `ContainAssetAccessResults`: `bool`
- `ContainCoveragePoints`: `bool`
- `Description`: `str`
- `FilterType`: `Union[str, None]`
- `Grid`: `Model(ICoverageGrid)`
- `GridPointConstraints`: `None`
- `GridPointSensor`: `Model(ISensor2)`
- `NumberOfAssets`: `int`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `str`

### FacilityDataBaseOutput

- `Facilities`: `None`
- `IsSuccess`: `bool`
- `Message`: `str`

### GEOYMLambertInput

- `keplerMb`: `Model(KeplerElements3)`
- `keplerPt`: `Model(KeplerElements2)`
- `tof`: `float`

### GEO_Input

- `Description`: `str`
- `Inclination`: `float`
- `OrbitEpoch`: `str`
- `SubSatellitePoint`: `float`

### GEO_Output

- `Elements_Inertial`: `Model(KeplerElements5)`
- `Elements_TOD`: `Model(KeplerElements4)`
- `IsSuccess`: `bool`
- `Message`: `str`

### HpopInput

- `AreaMassRatioDrag`: `float`
- `AreaMassRatioSRP`: `float`
- `CoefficientOfDrag`: `float`
- `CoefficientOfSRP`: `float`
- `CoordEpoch`: `str`
- `CoordSystem`: `str`
- `CoordType`: `str`
- `Description`: `str`
- `GravitationalParameter`: `float`
- `HpopPropagator`: `Model(Propagator2)`
- `OrbitEpoch`: `str`
- `OrbitalElements`: `List[float]`
- `Start`: `str`
- `Stop`: `str`

### InterfaceInput

- `AgVAAttitudeControlFiniteAttitude`: `Model(AgVAAttitudeControlFiniteAttitude)`
- `AgVAAttitudeControlFiniteThrustVector`: `Model(AgVAAttitudeControlFiniteThrustVector)`
- `AgVAAttitudeControlFiniteVelocityVector`: `Model(AgVAAttitudeControlFiniteVelocityVector)`
- `AgVAAttitudeControlImpulsiveAntiVelocityVector`: `Model(AgVAAttitudeControlImpulsiveAntiVelocityVector)`
- `AgVAAttitudeControlImpulsiveAttitude`: `Model(AgVAAttitudeControlImpulsiveAttitude)`
- `AgVAAttitudeControlImpulsiveThrustVector`: `Model(AgVAAttitudeControlImpulsiveThrustVector)`
- `AgVAAttitudeControlImpulsiveVelocityVector`: `Model(AgVAAttitudeControlImpulsiveVelocityVector)`
- `CalcScalarSphericalElement`: `Model(CalcScalarSphericalElement)`
- `CentralBodyPosition`: `Model(EntityPositionCentralBody)`
- `CoverageGridGlobal`: `Model(CoverageGridGlobal)`
- `CzmlOrientation`: `Model(CzmlOrientation)`
- `CzmlPosition`: `Model(EntityPositionCzml2)`
- `GravityFieldFunction`: `Model(GravityFieldFunction)`
- `OrientationVNC`: `Model(OrientationVNC)`
- `PropagatorJ2`: `Model(EntityPositionJ2)`
- `PropagatorSGP4`: `Model(EntityPositionSGP4)`
- `SitePosition`: `Model(EntityPositionSite)`
- `TwoBodyFunction`: `Model(TwoBodyFunction)`
- `agVAApoapsisStoppingCondition`: `Model(AgVAApoapsisStoppingCondition)`
- `agVAAttitudeControlFiniteAntiVelocityVector`: `Model(AgVAAttitudeControlFiniteAntiVelocityVector)`
- `agVADurationStoppingCondition`: `Model(AgVADurationStoppingCondition)`
- `agVAElementCartesian`: `Model(AgVAElementCartesian)`
- `agVAElementKeplerian`: `Model(AgVAElementKeplerian)`
- `agVAElementSpherical`: `Model(AgVAElementSpherical)`
- `agVAEngineConstAcc`: `Model(AgVAEngineConstAcc)`
- `agVAEngineConstIsp`: `Model(AgVAEngineConstant)`
- `agVAEpochStoppingCondition`: `Model(AgVAEpochStoppingCondition)`
- `agVAMCSInitialState`: `Model(AgVAMCSInitialState)`
- `agVAMCSManeuverFinite`: `Model(AgVAMCSManeuverFinite)`
- `agVAMCSManeuverImpulsive`: `Model(AgVAMCSManeuverImpulsive)`
- `agVAMCSPropagate`: `Model(AgVAMCSPropagate)`
- `agVAPeriapsisStoppingCondition`: `Model(AgVAPeriapsisStoppingCondition)`
- `agVAScalarStoppingCondition`: `Model(AgVAScalarStoppingCondition)`
- `calcScalarCartographic`: `Model(CalcScalarCartographic)`
- `calcScalarDeltaSpherical`: `Model(CalcScalarDeltaSphericalElement)`
- `calcScalarDuration`: `Model(CalcScalarDuration)`
- `calcScalarEpoch`: `Model(CalcScalarEpoch)`
- `calcScalarModifiedKeplerianElement`: `Model(CalcScalarModifiedKeplerianElement)`
- `calcScalarPointElement`: `Model(CalcScalarPointElement)`
- `conicSensor`: `Model(ConicSensor)`
- `constraintAzElMask`: `Model(ConstraintAzElMask)`
- `constraintElevationAngle`: `Model(ConstraintElevationAngle)`
- `constraintRange`: `Model(ConstraintRange)`
- `covGridLatLonBounds`: `Model(CovGridLatLonBounds)`
- `cvLatLonBoundsCoverageGrid`: `Model(CoverageGridLatLonBounds)`
- `cvLatitudeBoundsCoverageGrid`: `Model(CoverageGridLatitudeBounds)`
- `jacchiaRoberts`: `Model(JacchiaRoberts)`
- `orientationLVLH`: `Model(OrientationLVLH)`
- `orientationVVLH`: `Model(OrientationVVLH)`
- `propagatorTwoBody`: `Model(EntityPositionTwoBody)`
- `rKF7th8th`: `Model(RKF7th8th)`
- `rectangularSensor`: `Model(RectangularSensor)`
- `sRPSpherical`: `Model(SRPSpherical)`

### J2Input

- `CentralBody`: `str`
- `CoordSystem`: `str`
- `CoordType`: `str`
- `GravitationalParameter`: `float`
- `J2NormalizedValue`: `float`
- `OrbitEpoch`: `str`
- `OrbitalElements`: `List[float]`
- `RefDistance`: `float`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `str`

### LandingZoneInput

- `FaSheDian`: `List[float]`
- `LuoDian`: `List[float]`
- `ZoneXYs`: `List[float]`

### LifeTimeTLE_Input

- `Epoch`: `str`
- `Mass`: `float`
- `Sm`: `float`
- `TLEs`: `Model(TleInfo2)`

### LifeTimeTLE_Output

- `IsSuccess`: `bool`
- `LifeYears`: `float`
- `Message`: `str`

### LightingTimesInput

- `AzElMaskData`: `None`
- `Description`: `str`
- `OccultationBodies`: `None`
- `Position`: `Model(IEntityPosition2)`
- `Start`: `str`
- `Stop`: `str`

### MCSOutput

- `IsSuccess`: `bool`
- `MainSequenceResults`: `None`
- `Message`: `str`
- `Positions`: `Model(EntityPositionCzmlPositions)`

### Molniya_Input

- `ApogeeLongitude`: `float`
- `ArgumentOfPeriapsis`: `float`
- `Description`: `str`
- `OrbitEpoch`: `Union[str, None]`
- `PerigeeAltitude`: `float`

### Molniya_Output

- `Elements_Inertial`: `Model(KeplerElements7)`
- `Elements_TOD`: `Model(KeplerElements6)`
- `IsSuccess`: `bool`
- `Message`: `str`

### MultiSatesInput

- `AllSateElements`: `List[Model(KeplerElementsWithEpoch)]`
- `Epoch`: `str`

### MultiSatesOutput

- `AllElementsAtEpoch`: `List[Model(KeplerElements)]`
- `IsSuccess`: `bool`
- `Message`: `str`

### MultiSgp4Input

- `Epoch`: `str`
- `TLEs`: `List[str]`

### MultiSgp4Output

- `AllElementsAtEpoch`: `List[Model(KeplerElements)]`
- `IsSuccess`: `bool`
- `Message`: `str`

### RocketGuid_Output2

- `Delta_Elm32k`: `None`
- `Delta_Elm3k`: `None`
- `Delta_Sma1`: `float`
- `Delta_Sma2`: `float`
- `Delta_Va`: `float`
- `Delta_dL`: `float`
- `DicAllData`: `None`
- `DicAllDataZJ`: `None`
- `DicKeyData`: `None`
- `DicKeyData2`: `None`
- `GuanJiFangCheng`: `None`
- `IsSuccess`: `bool`
- `Message`: `Union[str, None]`
- `ZJLD`: `None`

### RocketLandingInput

- `A0`: `float`
- `Cons_B`: `float`
- `Cons_H`: `float`
- `Cons_Lambda`: `float`
- `Cons_V`: `float`
- `Dt1`: `float`
- `Dt2`: `float`
- `FaSheDianLLA`: `None`
- `Force2`: `float`
- `Force4`: `float`
- `Height4`: `float`
- `Ips2`: `float`
- `Ips4`: `float`
- `IsOptimize`: `bool`
- `Name`: `Union[str, None]`
- `Phicx0`: `float`
- `Phicx20`: `float`
- `Psicx0`: `float`
- `Psicx20`: `float`
- `Sa4`: `float`
- `Sm`: `float`
- `T0`: `float`
- `Text`: `Union[str, None]`
- `VariableLowerBound`: `None`
- `VariableUpperBound`: `None`
- `VariableX0`: `None`
- `X0`: `None`

### RocketLanding_Output

- `DicAllData`: `None`
- `DicKeyData`: `None`
- `DicShiXu`: `None`
- `IsSuccess`: `bool`
- `Message`: `Union[str, None]`
- `Optim_VariableX0`: `None`

### RocketSegmentFA_Input

- `A0`: `float`
- `AeroParamsFileName`: `Union[str, None]`
- `Alpham`: `float`
- `FaSheDianLLA`: `None`
- `Gw`: `float`
- `McsProfiles`: `None`
- `Name`: `Union[str, None]`
- `Name_FaSheDian`: `Union[str, None]`
- `Natmos`: `int`
- `ProfileOptim`: `Model(VAMCSProfileDEOptimizer)`
- `RocketSegments`: `None`
- `RocketType`: `Union[str, None]`
- `T1`: `float`
- `Text`: `Union[str, None]`
- `UseMcsProfile`: `bool`
- `ecc0`: `float`
- `inc0`: `float`
- `omg0`: `float`
- `sma0`: `float`

### RocketSegmentFA_Input2

- `A0`: `float`
- `AeroParamsFileName`: `Union[str, None]`
- `Alpham`: `float`
- `FaSheDianLLA`: `None`
- `Gw`: `float`
- `McsProfiles`: `None`
- `Name`: `Union[str, None]`
- `Name_FaSheDian`: `Union[str, None]`
- `Natmos`: `int`
- `ProfileOptim`: `Model(VAMCSProfileDEOptimizer)`
- `RocketSegments`: `None`
- `RocketType`: `Union[str, None]`
- `T1`: `float`
- `Text`: `Union[str, None]`
- `UseMcsProfile`: `bool`
- `ecc0`: `float`
- `inc0`: `float`
- `omg0`: `float`
- `sma0`: `float`

### RocketSegmentFA_Output

- `DicAllData`: `None`
- `DicAllDataZJ`: `None`
- `DicGuidanceParams`: `None`
- `DicKeyData`: `None`
- `DicKeyData2`: `None`
- `DicShiXu`: `None`
- `Input_New`: `Model(RocketSegmentFA_Input)`
- `IsSuccess`: `bool`
- `Message`: `Union[str, None]`
- `ZJLD`: `None`

### SSO_Input

- `Altitude`: `float`
- `Description`: `str`
- `LocalTimeOfDescendingNode`: `float`
- `OrbitEpoch`: `Union[str, None]`

### SSO_Output

- `Elements_Inertial`: `Model(KeplerElements7)`
- `Elements_TOD`: `Model(KeplerElements6)`
- `IsSuccess`: `bool`
- `Message`: `str`

### SatelliteDatabaseOutput

- `IsSuccess`: `bool`
- `Message`: `str`
- `TLEs`: `None`
- `TotalCount`: `int`

### Sgp4Input

- `SatelliteNumber`: `Union[str, None]`
- `Start`: `str`
- `Step`: `Union[float, None]`
- `Stop`: `str`
- `TLEs`: `List[str]`

### SimpleAscentInput

- `BurnoutAltitude`: `float`
- `BurnoutLatitude`: `float`
- `BurnoutLongitude`: `float`
- `BurnoutVelocity`: `float`
- `CentralBody`: `str`
- `LaunchAltitude`: `float`
- `LaunchLatitude`: `float`
- `LaunchLongitude`: `float`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `str`

### SolarAERInput

- `Start`: `str`
- `Stop`: `str`
- `Text`: `str`
- `TimeStepSec`: `int`
- `sitePosition`: `Model(EntityPositionSite2)`

### SolarIntensityInput

- `AzElMaskData`: `None`
- `Description`: `str`
- `OccultationBodies`: `None`
- `Position`: `Model(IEntityPosition2)`
- `Start`: `str`
- `Stop`: `str`
- `TimeStepSec`: `float`

### TLE_Input

- `BStar`: `float`
- `Ecc`: `float`
- `Epoch`: `str`
- `Inc`: `float`
- `IsMeanElements`: `bool`
- `Name`: `str`
- `RAAN`: `float`
- `SSC`: `str`
- `Sma`: `float`
- `TA`: `float`
- `W`: `float`

### TwoBodyInput

- `CentralBody`: `str`
- `CoordSystem`: `str`
- `CoordType`: `str`
- `GravitationalParameter`: `float`
- `OrbitEpoch`: `str`
- `OrbitalElements`: `List[float]`
- `Start`: `str`
- `Step`: `float`
- `Stop`: `str`

### Walker_Input

- `InterPlanePhaseIncrement`: `int`
- `InterPlaneTrueAnomalyIncrement`: `float`
- `NumPlanes`: `int`
- `NumSatsPerPlane`: `int`
- `RAANIncrement`: `float`
- `SeedKepler`: `Model(KeplerElements8)`
- `WalkerType`: `str`

### Walker_Output

- `IsSuccess`: `bool`
- `Message`: `str`
- `WalkerSatellites`: `None`

### ZiyouInput

- `RV_J2000`: `List[float]`
- `Start`: `str`
- `Type`: `str`

### ZiyouOutput

- `IsSuccess`: `bool`
- `Message`: `str`
- `Target_StkEpheFile`: `str`
- `Ziyou_StkAttiFile`: `str`
- `Ziyou_StkEpheFile`: `str`

