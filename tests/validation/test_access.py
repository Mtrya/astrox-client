"""Validation tests for access computation accuracy.

Reference values computed with STK 12 and brahe v0.9.0.
"""

import pytest

from astrox.access import compute_access
from astrox.models import EntityPath, J2Position, SitePosition


# Reference: STK 12
# ISS pass over Beijing on 2024-01-01
# Max elevation approximately 45 degrees
# Pass duration approximately 8-10 minutes
ISS_PASS_DURATION_MIN = 480  # seconds (8 minutes)
ISS_PASS_DURATION_MAX = 600  # seconds (10 minutes)


def test_access_iss_beijing(session):
    """Access computation for ISS over Beijing.

    Reference: STK 12 (approximate values)
    ISS at 400 km altitude should have passes of 8-10 minutes over Beijing.
    """
    # ISS-like orbit
    satellite = EntityPath(
        Name="ISS",
        Position=J2Position(
            field_type="J2",
            CentralBody="Earth",
            J2NormalizedValue=0.000484165143790815,
            RefDistance=6378137.0,
            OrbitEpoch="2024-01-01T00:00:00Z",
            CoordType="Classical",
            OrbitalElements=[
                6778137.0,  # 400 km altitude
                0.0005,
                51.6,  # ISS inclination
                0.0,
                0.0,
                0.0,
            ],
        ),
    )

    # Beijing ground station
    ground_station = EntityPath(
        Name="Beijing",
        Position=SitePosition(
            field_type="Site",
            CentralBody="Earth",
            LocationType="LatLonAlt",
            Location=[39.9042, 116.4074, 0.0],
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

    intervals = result["Intervals"]

    # Should have at least one access interval in 24 hours
    assert len(intervals) > 0

    # Verify pass durations are reasonable (8-10 minutes for LEO)
    for interval in intervals:
        duration = interval["Duration"]
        assert ISS_PASS_DURATION_MIN <= duration <= ISS_PASS_DURATION_MAX, \
            f"Pass duration {duration}s outside expected range"
