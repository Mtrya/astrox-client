"""Integration tests for propagation endpoints."""

import pytest

from astrox.propagator import propagate_two_body
from astrox.models import EntityPath, Keplerian


def test_two_body_returns_success(session):
    """Two-body propagation should return success with position data."""
    entity = EntityPath(
        Position=Keplerian(
            field_type="Keplerian",
            CentralBody="Earth",
            SemimajorAxis=6678137.0,  # 300 km altitude
            Eccentricity=0.0,
            Inclination=45.0,
            ArgOfPeriapsis=0.0,
            RAAN=0.0,
            TrueAnomaly=0.0,
        )
    )

    result = propagate_two_body(
        start="2024-01-01T00:00:00Z",
        stop="2024-01-01T01:00:00Z",
        entity=entity,
        step=300.0,
        session=session,
    )

    assert result["IsSuccess"] is True
    assert "Position" in result
    assert "Velocity" in result
