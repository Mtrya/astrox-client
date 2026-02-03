"""Integration tests for access endpoints."""

import pytest

from astrox.access import compute_access
from astrox.models import EntityPath, J2Position, SitePosition


def test_access_returns_success(session):
    """Access computation should return success with interval data."""
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

    ground_station = EntityPath(
        Name="Beijing",
        Position=SitePosition(
            field_type="Site",
            CentralBody="Earth",
            LocationType="LatLonAlt",
            Location=[39.9042, 116.4074, 0.0],  # Beijing
        ),
    )

    result = compute_access(
        start="2024-01-01T00:00:00Z",
        stop="2024-01-02T00:00:00Z",
        entities=[satellite, ground_station],
        session=session,
    )

    assert result["IsSuccess"] is True
    assert "Intervals" in result
