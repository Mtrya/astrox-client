"""
TLE Generation from Orbital Elements

Demonstrates conversion from Keplerian orbital elements to Two-Line Element (TLE)
format for satellite catalog operations and SGP4 propagation.
"""

from astrox.conjunction_analysis import get_tle

# Example 1: Generate TLE for LEO satellite
print("=" * 70)
print("Example 1: LEO Satellite TLE Generation")
print("=" * 70)

# ISS-like orbit parameters
iss_tle = get_tle(
    name="ISS-LIKE",
    ssc="99001",  # NORAD catalog number (5 digits)
    epoch="2021-04-30T12:00:00.000Z",
    b_star=0.000037381,  # Atmospheric drag coefficient (1/Earth radii)
    sma=6778.0,  # Semi-major axis (km) - ~400 km altitude
    ecc=0.0002714,  # Eccentricity
    inc=51.6441,  # Inclination (deg, TEME frame)
    w=302.6679,  # Argument of perigee (deg, TEME)
    raan=217.3237,  # Right ascension of ascending node (deg, TEME)
    ta=206.5255,  # True anomaly (deg, TEME)
    is_mean_elements=False,  # Using osculating elements
)

print("\nGenerated TLE for LEO satellite:")
print(f"Name: {iss_tle.get('SAT_Name', 'N/A')}")
print(f"SSC: {iss_tle.get('SAT_Number', 'N/A')}")
print(f"\nTLE Line 1: {iss_tle.get('TLE_Line1', 'N/A')}")
print(f"TLE Line 2: {iss_tle.get('TLE_Line2', 'N/A')}")

# Example 2: GEO satellite TLE
print("\n" + "=" * 70)
print("Example 2: Geostationary Satellite TLE")
print("=" * 70)

geo_tle = get_tle(
    name="GEO-COMSAT",
    ssc="99002",
    epoch="2021-04-30T00:00:00.000Z",
    b_star=0.0,  # Negligible drag at GEO altitude
    sma=42164.0,  # GEO semi-major axis (km)
    ecc=0.0001,  # Near-circular
    inc=0.05,  # Near-equatorial (deg)
    w=0.0,  # Argument of perigee
    raan=75.0,  # RAAN for specific longitude
    ta=0.0,  # True anomaly
    is_mean_elements=True,  # Mean elements more common for GEO
)

print("\nGenerated TLE for GEO satellite:")
print(f"Name: {geo_tle.get('SAT_Name', 'N/A')}")
print(f"TLE Line 1: {geo_tle.get('TLE_Line1', 'N/A')}")
print(f"TLE Line 2: {geo_tle.get('TLE_Line2', 'N/A')}")

altitude_geo = 42164.0 - 6378.137  # km above Earth surface
print(f"\nOrbital parameters:")
print(f"  Altitude: {altitude_geo:.1f} km")
print(f"  Inclination: {0.05} deg (near-equatorial)")
print(f"  Eccentricity: {0.0001} (near-circular)")

# Example 3: Sun-Synchronous Orbit (SSO) TLE
print("\n" + "=" * 70)
print("Example 3: Sun-Synchronous Orbit TLE")
print("=" * 70)

sso_tle = get_tle(
    name="SSO-EARTH-OBS",
    ssc="99003",
    epoch="2021-04-30T06:00:00.000Z",
    b_star=0.00005,  # Moderate drag
    sma=7078.0,  # ~700 km altitude
    ecc=0.001,  # Nearly circular
    inc=98.2,  # Sun-synchronous inclination (deg)
    w=90.0,  # Argument of perigee
    raan=120.0,  # RAAN
    ta=0.0,  # True anomaly at epoch
    is_mean_elements=False,
)

print("\nGenerated TLE for SSO satellite:")
print(f"Name: {sso_tle.get('SAT_Name', 'N/A')}")
print(f"TLE Line 1: {sso_tle.get('TLE_Line1', 'N/A')}")
print(f"TLE Line 2: {sso_tle.get('TLE_Line2', 'N/A')}")

altitude_sso = 7078.0 - 6378.137
print(f"\nOrbital parameters:")
print(f"  Altitude: {altitude_sso:.1f} km")
print(f"  Inclination: {98.2} deg (sun-synchronous)")
print(f"  Period: ~99 minutes")

# Example 4: Molniya orbit TLE
print("\n" + "=" * 70)
print("Example 4: Molniya Orbit TLE")
print("=" * 70)

molniya_tle = get_tle(
    name="MOLNIYA-COM",
    ssc="99004",
    epoch="2021-04-30T00:00:00.000Z",
    b_star=0.00001,  # Low drag (high apogee)
    sma=26554.0,  # Semi-major axis for 12-hour period (km)
    ecc=0.74,  # Highly eccentric
    inc=63.4,  # Critical inclination (minimizes argument of perigee drift)
    w=270.0,  # Argument of perigee (deg)
    raan=180.0,  # RAAN
    ta=0.0,  # At perigee
    is_mean_elements=True,
)

print("\nGenerated TLE for Molniya satellite:")
print(f"Name: {molniya_tle.get('SAT_Name', 'N/A')}")
print(f"TLE Line 1: {molniya_tle.get('TLE_Line1', 'N/A')}")
print(f"TLE Line 2: {molniya_tle.get('TLE_Line2', 'N/A')}")

perigee_alt = 26554.0 * (1 - 0.74) - 6378.137
apogee_alt = 26554.0 * (1 + 0.74) - 6378.137
print(f"\nOrbital parameters:")
print(f"  Perigee altitude: {perigee_alt:.1f} km")
print(f"  Apogee altitude: {apogee_alt:.1f} km")
print(f"  Inclination: {63.4} deg (critical)")
print(f"  Period: ~12 hours")

# Example 5: Debris object with high drag
print("\n" + "=" * 70)
print("Example 5: Space Debris with High Drag")
print("=" * 70)

debris_tle = get_tle(
    name="DEBRIS-FRAG",
    ssc="99005",
    epoch="2021-04-30T12:00:00.000Z",
    b_star=0.001,  # Very high drag coefficient
    sma=6678.0,  # Low altitude (~300 km)
    ecc=0.01,  # Slightly eccentric
    inc=45.0,  # Moderate inclination
    w=180.0,
    raan=90.0,
    ta=45.0,
    is_mean_elements=False,
)

print("\nGenerated TLE for high-drag debris:")
print(f"Name: {debris_tle.get('SAT_Name', 'N/A')}")
print(f"TLE Line 1: {debris_tle.get('TLE_Line1', 'N/A')}")
print(f"TLE Line 2: {debris_tle.get('TLE_Line2', 'N/A')}")

altitude_debris = 6678.0 - 6378.137
print(f"\nOrbital parameters:")
print(f"  Altitude: {altitude_debris:.1f} km (low)")
print(f"  B*: {0.001} (high drag - rapid decay expected)")

# Example 6: Batch generation for constellation
print("\n" + "=" * 70)
print("Example 6: Constellation TLE Generation")
print("=" * 70)

print("\nGenerating TLEs for 4-satellite constellation:")

constellation_tles = []
for i in range(4):
    tle = get_tle(
        name=f"CONST-SAT-{i + 1}",
        ssc=f"9901{i}",
        epoch="2021-04-30T00:00:00.000Z",
        b_star=0.00005,
        sma=7178.0,  # 800 km altitude
        ecc=0.001,
        inc=55.0,
        w=0.0,
        raan=i * 90.0,  # Evenly spaced RAANs (0, 90, 180, 270 deg)
        ta=0.0,
        is_mean_elements=True,
    )
    constellation_tles.append(tle)

for i, tle in enumerate(constellation_tles, 1):
    print(f"\nSatellite {i}:")
    print(f"  {tle.get('TLE_Line1', 'N/A')}")
    print(f"  {tle.get('TLE_Line2', 'N/A')}")

print("\n" + "=" * 70)
print("TLE Generation Complete")
print("=" * 70)
print("\nKey Parameters:")
print("  - ssc: NORAD catalog number (5-digit string)")
print("  - epoch: Element epoch in UTC (YYYY-MM-DDTHH:MM:SS.fffZ)")
print("  - b_star: Drag coefficient (1/Earth radii)")
print("    * LEO: 0.00001-0.0001 (typical)")
print("    * High drag debris: 0.001+")
print("    * GEO: ~0 (negligible)")
print("  - sma: Semi-major axis in km")
print("  - All angles in degrees, TEME reference frame")
print("  - is_mean_elements:")
print("    * True: Mean elements (removes short-period variations)")
print("    * False: Osculating elements (instantaneous state)")
print("\nUse Cases:")
print("  - Generate TLEs from propagated states")
print("  - Create synthetic satellite catalogs")
print("  - Convert between orbital element formats")
print("  - Feed TLEs to SGP4 propagator")

"""
>>> ======================================================================
>>> Example 1: LEO Satellite TLE Generation
>>> ======================================================================
>>>
>>> Generated TLE for LEO satellite:
>>> Name: ISS-LIKE
>>> SSC: 99001
>>>
>>> TLE Line 1: 1 99001U 99999A   21120.50000000  .00000000  00000-0  00000-0 0  9995
>>> TLE Line 2: 2 99001  51.6346 217.3462 0016077 284.8260 224.4008 15.56945662    01
>>>
>>> ======================================================================
>>> Example 2: Geostationary Satellite TLE
>>> ======================================================================
>>>
>>> Generated TLE for GEO satellite:
>>> Name: GEO-COMSAT
>>> TLE Line 1: 1 99002U 99999A   21120.00000000  .00000000  00000-0  00000-0 0  9991
>>> TLE Line 2: 2 99002   0.0727  79.1489 0000989 356.0137 359.8399  1.00278301    05
>>>
>>> Orbital parameters:
>>>   Altitude: 35785.9 km
>>>   Inclination: 0.05 deg (near-equatorial)
>>>   Eccentricity: 0.0001 (near-circular)
>>>
>>> ======================================================================
>>> Example 3: Sun-Synchronous Orbit TLE
>>> ======================================================================
>>>
>>> Generated TLE for SSO satellite:
>>> Name: SSO-EARTH-OBS
>>> TLE Line 1: 1 99003U 99999A   21120.25000000  .00000000  00000-0  00000-0 0  9999
>>> TLE Line 2: 2 99003  98.1947 120.0000 0016452  90.0000   0.0000 14.54214189    00
>>>
>>> Orbital parameters:
>>>   Altitude: 699.9 km
>>>   Inclination: 98.2 deg (sun-synchronous)
>>>   Period: ~99 minutes
>>>
>>> ======================================================================
>>> Example 4: Molniya Orbit TLE
>>> ======================================================================
>>>
>>> Generated TLE for Molniya satellite:
>>> Name: MOLNIYA-COM
>>> TLE Line 1: 1 99004U 99999A   21120.00000000  .00000000  00000-0  00000-0 0  9993
>>> TLE Line 2: 2 99004  63.3929 179.9934 7394860 270.0278 359.9940  2.01855099    09
>>>
>>> Orbital parameters:
>>>   Perigee altitude: 525.9 km
>>>   Apogee altitude: 39825.8 km
>>>   Inclination: 63.4 deg (critical)
>>>   Period: ~12 hours
>>>
>>> ======================================================================
>>> Example 5: Space Debris with High Drag
>>> ======================================================================
>>>
>>> Generated TLE for high-drag debris:
>>> Name: DEBRIS-FRAG
>>> TLE Line 1: 1 99005U 99999A   21120.50000000  .00000000  00000-0  00000-0 0  9999
>>> TLE Line 2: 2 99005  45.0000  89.9700 0099209 182.0798  42.1044 15.91446793    05
>>>
>>> Orbital parameters:
>>>   Altitude: 299.9 km (low)
>>>   B*: 0.001 (high drag - rapid decay expected)
>>>
>>> ======================================================================
>>> Example 6: Constellation TLE Generation
>>> ======================================================================
>>>
>>> Generating TLEs for 4-satellite constellation:
>>>
>>> Satellite 1:
>>>   1 99010U 99999A   21120.00000000  .00000000  00000-0  00000-0 0  9990
>>>   2 99010  55.0000 360.0000 0013149 319.5279  40.4720 14.27558710    01
>>>
>>> Satellite 2:
>>>   1 99011U 99999A   21120.00000000  .00000000  00000-0  00000-0 0  9991
>>>   2 99011  55.0000  90.0000 0013149 319.5279  40.4720 14.27558710    02
>>>
>>> Satellite 3:
>>>   1 99012U 99999A   21120.00000000  .00000000  00000-0  00000-0 0  9992
>>>   2 99012  55.0000 180.0000 0013149 319.5279  40.4720 14.27558710    03
>>>
>>> Satellite 4:
>>>   1 99013U 99999A   21120.00000000  .00000000  00000-0  00000-0 0  9993
>>>   2 99013  55.0000 270.0000 0013149 319.5279  40.4720 14.27558710    04
>>>
>>> ======================================================================
>>> TLE Generation Complete
>>> ======================================================================
>>>
>>> Key Parameters:
>>>   - ssc: NORAD catalog number (5-digit string)
>>>   - epoch: Element epoch in UTC (YYYY-MM-DDTHH:MM:SS.fffZ)
>>>   - b_star: Drag coefficient (1/Earth radii)
>>>     * LEO: 0.00001-0.0001 (typical)
>>>     * High drag debris: 0.001+
>>>     * GEO: ~0 (negligible)
>>>   - sma: Semi-major axis in km
>>>   - All angles in degrees, TEME reference frame
>>>   - is_mean_elements:
>>>     * True: Mean elements (removes short-period variations)
>>>     * False: Osculating elements (instantaneous state)
>>>
>>> Use Cases:
>>>   - Generate TLEs from propagated states
>>>   - Create synthetic satellite catalogs
>>>   - Convert between orbital element formats
>>>   - Feed TLEs to SGP4 propagator
"""
