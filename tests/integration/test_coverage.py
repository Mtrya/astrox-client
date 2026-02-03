"""Integration tests for coverage endpoints."""

import pytest

from astrox.coverage import compute_coverage
from astrox._models import CoverageGridGlobal
from astrox.models import EntityPath, J2Position


def test_coverage_returns_success(session):
    """Coverage computation should return success with interval data."""
    satellite = EntityPath(
        Name="TestSat",
        Position=J2Position(
            field_type="J2",
            CentralBody="Earth",
            J2NormalizedValue=0.000484165143790815,
            RefDistance=6378137.0,
            OrbitEpoch="2024-01-01T00:00:00Z",
            CoordType="Classical",
            OrbitalElements=[
                6878137.0,  # 500 km altitude
                0.001,
                45.0,
                0.0,
                0.0,
                0.0,
            ],
        ),
    )

    grid = CoverageGridGlobal(
        CentralBodyName="Earth",
        Resolution=10.0,
        Height=0.0,
    )

    result = compute_coverage(
        start="2024-01-01T00:00:00Z",
        stop="2024-01-01T01:00:00Z",
        grid=grid,
        assets=[satellite],
        step=60.0,
        session=session,
    )

    assert result["IsSuccess"] is True
    assert "SatisfactionIntervalsWithNumberOfAssets" in result
