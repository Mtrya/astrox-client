"""
Close Approach Analysis Example

Demonstrates collision detection between satellites using both v3 (TLE-based)
and v4 (trajectory-based) methods.
"""

from astrox.conjunction_analysis import compute_close_approach
from astrox.models import TleInfo, CzmlPosition


# Example 1: V3 - TLE-based close approach (satellite vs catalog)
print("=" * 70)
print("Example 1: Close Approach Analysis V3 (TLE-based)")
print("=" * 70)

# ISS TLE data (epoch 2021-04-30)
iss_tle = TleInfo(
    SAT_Name="ISS (ZARYA)",
    SAT_Number="25544",
    TLE_Line1="1 25544U 98067A   21120.75712704  .00001608  00000-0  37381-4 0  9990",
    TLE_Line2="2 25544  51.6441 217.3237 0002714 302.6679 206.5255 15.48964989281240",
)

# Compute close approaches over 7 days
result_v3 = compute_close_approach(
    start_utcg="2021-04-30T00:00:00.000Z",
    stop_utcg="2021-05-07T00:00:00.000Z",
    sat1=iss_tle,
    version="v3",
    tol_max_distance=50.0,  # Detect approaches within 50 km
    tol_theta=5.0,  # Orbital plane angle threshold (deg)
    tol_dh=100.0,  # Altitude filtering error (km)
)

# Verified data structure: result keys include 'IsSuccess', 'Message', 'TotalNumber',
# 'AfterApoPeriFilterNumber', 'AfterCrossPlaneNumber', 'CA_Results'
# CA_Results items have keys: SAT1_Name, SAT2_Name, SAT1_Number, SAT2_Number,
# CA_MinRange_Time, CA_MinRange, CA_Theta, CA_DeltaV, CA_Probability
print(f"\nTotal events detected: {result_v3['TotalNumber']}")  # should be 31344
print(f"Filtered to {len(result_v3['CA_Results'])} events after plane/altitude filters")  # should be 2

print("\nFirst 3 close approaches:")
for i, ca in enumerate(result_v3["CA_Results"][:3], 1):
    print(f"\n  Event {i}:")
    print(f"    Time: {ca['CA_MinRange_Time']}")  # e.g., 2021-05-03T05:10:08.082Z
    print(f"    Miss Distance: {ca['CA_MinRange']:.3f} km")  # e.g., 0.927 km
    print(f"    Target: {ca['SAT2_Name']} (SSC: {ca['SAT2_Number']})")  # e.g., STARLINK-34029 (63805)
    print(f"    Relative Velocity: {ca['CA_DeltaV']:.3f} m/s")  # e.g., 11.227 m/s
    print(f"    Plane Angle: {ca['CA_Theta']:.3f}°")  # e.g., 94.294°
    print(f"    Collision Probability: {ca['CA_Probability']:.6f}")  # e.g., 0.000000

# Example 2: V3 with specific target list
print("\n" + "=" * 70)
print("Example 2: Close Approach with Specific Targets")
print("=" * 70)

# Define specific debris targets to check
target1 = TleInfo(
    SAT_Name="COSMOS 2251 DEB",
    SAT_Number="34454",
    TLE_Line1="1 34454U 93036SX  21120.50000000  .00000100  00000-0  10000-3 0  9999",
    TLE_Line2="2 34454  74.0400 180.0000 0050000 270.0000  90.0000 14.00000000100000",
)

target2 = TleInfo(
    SAT_Name="IRIDIUM 33 DEB",
    SAT_Number="33442",
    TLE_Line1="1 33442U 97051C   21120.50000000  .00000050  00000-0  10000-3 0  9999",
    TLE_Line2="2 33442  86.4000 200.0000 0010000  90.0000 270.0000 14.34000000150000",
)

result_v3_targeted = compute_close_approach(
    start_utcg="2021-04-30T00:00:00.000Z",
    stop_utcg="2021-05-02T00:00:00.000Z",
    sat1=iss_tle,
    version="v3",
    tol_max_distance=100.0,
    targets=[target1, target2],  # Only check these specific objects
)

print(f"\nFound {len(result_v3_targeted['CA_Results'])} close approaches with specified targets")  # should be 0

# Note: Specified targets (COSMOS 2251 DEB, IRIDIUM 33 DEB) have orbital planes
# too dissimilar to the ISS for close approach within the 2-day window

# Example 3: V4 - Trajectory-based close approach (for rockets)
print("\n" + "=" * 70)
print("Example 3: Close Approach Analysis V4 (Trajectory-based)")
print("=" * 70)

# Define rocket trajectory using CZML positions
rocket_position = CzmlPosition(
    **{"$type": "CzmlPosition"},
    CentralBody="Earth",
    referenceFrame="INERTIAL",
    interpolationAlgorithm="LAGRANGE",
    interpolationDegree=5,
    epoch="2021-04-30T12:00:00.000Z",
    cartesian=[
        # Time (seconds from epoch), X, Y, Z (meters)
        # Sample trajectory points for a rocket ascending to GTO
        0.0,
        -2.0e6,
        5.0e6,
        3.0e6,
        300.0,
        -1.8e6,
        5.2e6,
        3.5e6,
        600.0,
        -1.5e6,
        5.5e6,
        4.0e6,
        900.0,
        -1.0e6,
        6.0e6,
        5.0e6,
        1200.0,
        -0.5e6,
        6.5e6,
        6.0e6,
    ],
)

result_v4 = compute_close_approach(
    start_utcg="2021-04-30T12:00:00.000Z",
    stop_utcg="2021-04-30T12:30:00.000Z",
    sat1=rocket_position,
    version="v4",
    tol_max_distance=30.0,  # Stricter threshold for active rocket
    tol_cross_dt=10.0,  # Time error tolerance (seconds)
)

print(f"\nFound {result_v4['TotalNumber']} close approaches for rocket trajectory")  # should be 0
print(f"Filtered to {len(result_v4['CA_Results'])} events after plane/altitude filters")  # Note: Example trajectory uses synthetic data; real trajectories should use actual ephemeris
if result_v4["CA_Results"]:
    print("\nClose approach details:")
    for i, ca in enumerate(result_v4["CA_Results"][:5], 1):
        print(f"\n  Event {i}:")
        print(f"    TCA: {ca['CA_MinRange_Time']}")
        print(f"    Miss Distance: {ca['CA_MinRange']:.3f} km")
        print(f"    Target: {ca['SAT2_Name']}")

# Example 4: Fine-tuned sensitivity parameters
print("\n" + "=" * 70)
print("Example 4: Fine-tuned Detection Parameters")
print("=" * 70)

result_sensitive = compute_close_approach(
    start_utcg="2021-04-30T00:00:00.000Z",
    stop_utcg="2021-05-01T00:00:00.000Z",
    sat1=iss_tle,
    version="v3",
    tol_max_distance=20.0,  # Very close approaches only (20 km)
    tol_cross_dt=5.0,  # Tight time tolerance (5 seconds)
    tol_theta=2.0,  # Similar orbital planes (2 deg)
    tol_dh=50.0,  # Similar altitudes (50 km)
)

print(f"\nHigh-sensitivity search found {len(result_sensitive['CA_Results'])} events")  # should be 0
print("(Narrower thresholds reduce false positives)")

print("\n" + "=" * 70)
print("Close Approach Analysis Complete")
print("=" * 70)
print("\nKey takeaways:")
print("  - V3: Use TLE data for satellite-to-catalog collision screening")
print("  - V4: Use CZML trajectories for rocket/maneuver collision analysis")
print("  - Adjust tol_* parameters based on mission risk tolerance")
print("  - tol_max_distance: Primary collision threshold (km)")
print("  - tol_theta: Filter by orbital plane similarity (deg)")
print("  - tol_dh: Filter by altitude similarity (km)")

"""
>>> ======================================================================
>>> Example 1: Close Approach Analysis V3 (TLE-based)
>>> ======================================================================
>>>
>>> Found 2 close approach events
>>>
>>> First 3 close approaches:
>>>
>>>   Event 1:
>>>     Time: N/A
>>>     Distance: N/A
>>>     Target: N/A (SSC: N/A)
>>>     Relative Velocity: N/A
>>>
>>>   Event 2:
>>>     Time: N/A
>>>     Distance: N/A
>>>     Target: N/A (SSC: N/A)
>>>     Relative Velocity: N/A
>>>
>>> ======================================================================
>>> Example 2: Close Approach with Specific Targets
>>> ======================================================================
>>>
>>> Found 0 close approaches with specified targets
>>>
>>> ======================================================================
>>> Example 3: Close Approach Analysis V4 (Trajectory-based)
>>> ======================================================================
>>>
>>> Found 0 close approaches for rocket trajectory
>>>
>>> ======================================================================
>>> Example 4: Fine-tuned Detection Parameters
>>> ======================================================================
>>>
>>> High-sensitivity search found 0 events
>>> (Narrower thresholds reduce false positives)
>>>
"""
