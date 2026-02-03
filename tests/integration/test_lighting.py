"""Integration tests for lighting endpoints."""

import pytest

from astrox.lighting import lighting_times
from astrox.models import J2Position


def test_lighting_times_returns_success(session):
    """Lighting times computation should return success with interval data."""
    position = J2Position(
        field_type="J2",
        CentralBody="Earth",
        J2NormalizedValue=0.000484165143790815,
        RefDistance=6378137.0,
        OrbitEpoch="2024-03-20T00:00:00Z",
        CoordType="Classical",
        OrbitalElements=[
            42164137.0,  # GEO
            0.0001,
            0.1,
            0.0,
            0.0,
            0.0,
        ],
    )

    result = lighting_times(
        start="2024-03-20T00:00:00Z",
        stop="2024-03-21T00:00:00Z",
        position=position,
        occultation_bodies=["Earth"],
        session=session,
    )

    assert result["IsSuccess"] is True
    assert "SunLight" in result
    assert "Penumbra" in result
    assert "Umbra" in result
