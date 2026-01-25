"""
Orbital Lifetime Calculation

Demonstrates calculation of satellite orbital decay time based on TLE data,
atmospheric drag, and satellite physical properties.
"""

from astrox.conjunction_analysis import compute_lifetime
from astrox.models import TleInfo

# Example 1: Low Earth Orbit satellite (LEO)
print("=" * 70)
print("Example 1: LEO Satellite Lifetime (~400 km)")
print("=" * 70)

# ISS-like orbit
leo_tle = TleInfo(
    SAT_Name="LEO-SAT-400KM",
    SAT_Number="99001",
    TLE_Line1="1 99001U 21001A   21120.50000000  .00001608  00000-0  37381-4 0  9999",
    TLE_Line2="2 99001  51.6400 217.3000 0003000 302.0000 206.0000 15.48964989000010",
)

# Satellite properties
mass_leo = 5000.0  # kg
surface_area_leo = 25.0  # m² (approximate cross-sectional area)

result_leo = compute_lifetime(
    epoch="2021-04-30T12:00:00.000Z",
    tles=leo_tle,
    sm=surface_area_leo,
    mass=mass_leo,
)

print(f"\nSatellite: {leo_tle.SAT_Name}")
print(f"Mass: {mass_leo} kg")
print(f"Surface area: {surface_area_leo} m²")
print(f"Area-to-mass ratio: {surface_area_leo / mass_leo:.4f} m²/kg")
lifetime = result_leo.get('Lifetime') or result_leo.get('LifeYears', 'N/A')
print(f"\nEstimated orbital lifetime: {lifetime:.2f} years" if isinstance(lifetime, (int, float)) else f"\nEstimated orbital lifetime: {lifetime}")

# Example 2: Different altitudes comparison
print("\n" + "=" * 70)
print("Example 2: Altitude Impact on Lifetime")
print("=" * 70)

altitudes = [
    ("300 km", "1 99002U 21002A   21120.50000000  .00010000  00000-0  50000-4 0  9999", "2 99002  51.6400 217.3000 0003000 302.0000 206.0000 15.72000000000010"),
    ("500 km", "1 99003U 21003A   21120.50000000  .00000500  00000-0  10000-4 0  9999", "2 99003  51.6400 217.3000 0003000 302.0000 206.0000 15.22000000000010"),
    ("700 km", "1 99004U 21004A   21120.50000000  .00000100  00000-0  30000-5 0  9999", "2 99004  51.6400 217.3000 0003000 302.0000 206.0000 14.98000000000010"),
    ("900 km", "1 99005U 21005A   21120.50000000  .00000010  00000-0  10000-5 0  9999", "2 99005  51.6400 217.3000 0003000 302.0000 206.0000 14.76000000000010"),
]

print(f"\nLifetime vs altitude (constant mass={mass_leo} kg, area={surface_area_leo} m²):")
print(f"{'Altitude':<15} {'Lifetime (years)':<20}")
print("-" * 35)

for alt_name, line1, line2 in altitudes:
    tle = TleInfo(
        SAT_Name=f"SAT-{alt_name}",
        SAT_Number=line1.split()[1],
        TLE_Line1=line1,
        TLE_Line2=line2,
    )

    result = compute_lifetime(
        epoch="2021-04-30T12:00:00.000Z",
        tles=tle,
        sm=surface_area_leo,
        mass=mass_leo,
    )

    lifetime = result.get("Lifetime") or result.get("LifeYears", "N/A")
    if isinstance(lifetime, (int, float)):
        print(f"{alt_name:<15} {lifetime:.2f}")
    else:
        print(f"{alt_name:<15} {lifetime}")

# Example 3: Area-to-mass ratio impact
print("\n" + "=" * 70)
print("Example 3: Area-to-Mass Ratio Impact")
print("=" * 70)

# 600 km orbit TLE
base_tle = TleInfo(
    SAT_Name="SAT-600KM",
    SAT_Number="99006",
    TLE_Line1="1 99006U 21006A   21120.50000000  .00000200  00000-0  50000-5 0  9999",
    TLE_Line2="2 99006  51.6400 217.3000 0003000 302.0000 206.0000 15.16000000000010",
)

configurations = [
    ("Small dense", 5000.0, 10.0),  # Low A/M ratio (heavy, compact)
    ("Standard", 5000.0, 25.0),  # Medium A/M ratio
    ("Large light", 1000.0, 25.0),  # High A/M ratio (light, large)
    ("Debris fragment", 50.0, 2.0),  # Very high A/M ratio
]

print(f"\nLifetime at 600 km altitude with different configurations:")
print(f"{'Configuration':<20} {'Mass (kg)':<12} {'Area (m²)':<12} {'A/M Ratio':<12} {'Lifetime (yrs)'}")
print("-" * 75)

for config_name, mass, area in configurations:
    result = compute_lifetime(
        epoch="2021-04-30T12:00:00.000Z",
        tles=base_tle,
        sm=area,
        mass=mass,
    )

    a_to_m = area / mass
    lifetime = result.get("Lifetime") or result.get("LifeYears", "N/A")
    lifetime_str = f"{lifetime:.2f}" if isinstance(lifetime, (int, float)) else lifetime
    print(f"{config_name:<20} {mass:<12.1f} {area:<12.1f} {a_to_m:<12.5f} {lifetime_str}")

# Example 4: Debris cloud lifetime analysis
print("\n" + "=" * 70)
print("Example 4: Debris Cloud Lifetime Analysis")
print("=" * 70)

# Simulate debris at various altitudes with different A/M ratios
debris_scenarios = [
    ("Large fragment", 400, 100.0, 5.0, "1 99100U 21100A   21120.50000000  .00003000  00000-0  80000-4 0  9999", "2 99100  51.6400 217.3000 0003000 302.0000 206.0000 15.48000000000010"),
    ("Medium fragment", 500, 50.0, 5.0, "1 99101U 21101A   21120.50000000  .00001000  00000-0  30000-4 0  9999", "2 99101  51.6400 217.3000 0003000 302.0000 206.0000 15.22000000000010"),
    ("Small fragment", 600, 10.0, 2.0, "1 99102U 21102A   21120.50000000  .00000500  00000-0  15000-4 0  9999", "2 99102  51.6400 217.3000 0003000 302.0000 206.0000 15.16000000000010"),
    ("Tiny flake", 700, 0.5, 0.05, "1 99103U 21103A   21120.50000000  .00000100  00000-0  30000-5 0  9999", "2 99103  51.6400 217.3000 0003000 302.0000 206.0000 14.98000000000010"),
]

print(f"\nDebris lifetime analysis:")
print(f"{'Type':<18} {'Alt (km)':<10} {'Mass (kg)':<12} {'Area (m²)':<12} {'Lifetime (yrs)'}")
print("-" * 70)

for debris_type, altitude, mass, area, line1, line2 in debris_scenarios:
    tle = TleInfo(
        SAT_Name=debris_type,
        SAT_Number=line1.split()[1],
        TLE_Line1=line1,
        TLE_Line2=line2,
    )

    result = compute_lifetime(
        epoch="2021-04-30T12:00:00.000Z",
        tles=tle,
        sm=area,
        mass=mass,
    )

    lifetime = result.get("Lifetime") or result.get("LifeYears", "N/A")
    lifetime_str = f"{lifetime:.2f}" if isinstance(lifetime, (int, float)) else lifetime
    print(f"{debris_type:<18} {altitude:<10} {mass:<12.1f} {area:<12.2f} {lifetime_str}")

# Example 5: High-drag satellite (deliberate de-orbit)
print("\n" + "=" * 70)
print("Example 5: De-orbit Scenarios")
print("=" * 70)

# Standard satellite
standard_tle = TleInfo(
    SAT_Name="STANDARD-SAT",
    SAT_Number="99200",
    TLE_Line1="1 99200U 21200A   21120.50000000  .00000500  00000-0  15000-4 0  9999",
    TLE_Line2="2 99200  51.6400 217.3000 0003000 302.0000 206.0000 15.22000000000010",
)

# Same satellite with deployed drag sail
drag_sail_tle = TleInfo(
    SAT_Name="DRAG-SAIL-SAT",
    SAT_Number="99201",
    TLE_Line1="1 99201U 21201A   21120.50000000  .00020000  00000-0  10000-3 0  9999",
    TLE_Line2="2 99201  51.6400 217.3000 0003000 302.0000 206.0000 15.22000000000010",
)

print("\nComparing de-orbit methods (500 km altitude):")

# Standard configuration
result_standard = compute_lifetime(
    epoch="2021-04-30T12:00:00.000Z",
    tles=standard_tle,
    sm=20.0,
    mass=1000.0,
)

# With drag sail deployed (100 m² sail)
result_drag_sail = compute_lifetime(
    epoch="2021-04-30T12:00:00.000Z",
    tles=drag_sail_tle,
    sm=120.0,  # 20 m² body + 100 m² drag sail
    mass=1000.0,
)

lifetime_std = result_standard.get("Lifetime") or result_standard.get("LifeYears", "N/A")
lifetime_sail = result_drag_sail.get("Lifetime") or result_drag_sail.get("LifeYears", "N/A")

print(f"\nStandard configuration:")
print(f"  Area: 20 m², Mass: 1000 kg")
print(f"  Lifetime: {lifetime_std:.2f} years" if isinstance(lifetime_std, (int, float)) else f"  Lifetime: {lifetime_std}")

print(f"\nWith drag sail deployed:")
print(f"  Area: 120 m², Mass: 1000 kg")
print(f"  Lifetime: {lifetime_sail:.2f} years" if isinstance(lifetime_sail, (int, float)) else f"  Lifetime: {lifetime_sail}")

if isinstance(lifetime_std, (int, float)) and isinstance(lifetime_sail, (int, float)) and lifetime_sail > 0:
    reduction_factor = lifetime_std / lifetime_sail
    print(f"  De-orbit time reduced by factor of {reduction_factor:.1f}")

print("\n" + "=" * 70)
print("Orbital Lifetime Analysis Complete")
print("=" * 70)
print("\nKey Factors Affecting Lifetime:")
print("  1. Altitude: Higher altitude = longer lifetime (exponential)")
print("  2. Area-to-Mass Ratio: Higher A/M = shorter lifetime")
print("  3. Solar Activity: Increased atmospheric density during solar max")
print("  4. Inclination: Affects atmospheric density encounters")
print("\nTypical Lifetimes:")
print("  - 200-300 km: Days to weeks")
print("  - 400-500 km: Months to few years")
print("  - 600-700 km: Several years to decades")
print("  - 800+ km: Decades to centuries")
print("  - 1000+ km: Centuries (debris problem)")
print("\nDe-orbit Mitigation:")
print("  - Deploy drag sails to increase area")
print("  - Lower perigee with propulsive maneuver")
print("  - 25-year rule: Remove from LEO within 25 years post-mission")

"""
>>> ======================================================================
>>> Example 1: LEO Satellite Lifetime (~400 km)
>>> ======================================================================
>>>
>>> Satellite: LEO-SAT-400KM
>>> Mass: 5000.0 kg
>>> Surface area: 25.0 m²
>>> Area-to-mass ratio: 0.0050 m²/kg
>>>
>>> Estimated orbital lifetime: 1.13 years
>>>
>>> ======================================================================
>>> Example 2: Altitude Impact on Lifetime
>>> ======================================================================
>>>
>>> Lifetime vs altitude (constant mass=5000.0 kg, area=25.0 m²):
>>> Altitude        Lifetime (years)
>>> -----------------------------------
>>> 300 km          0.40
>>> 500 km          3.98
>>> 700 km          25.00
>>> 900 km          25.00
>>>
>>> ======================================================================
>>> Example 3: Area-to-Mass Ratio Impact
>>> ======================================================================
>>>
>>> Lifetime at 600 km altitude with different configurations:
>>> Configuration        Mass (kg)    Area (m²)    A/M Ratio    Lifetime (yrs)
>>> ---------------------------------------------------------------------------
>>> Small dense          5000.0       10.0         0.00200      25.00
>>> Standard             5000.0       25.0         0.00500      5.19
>>> Large light          1000.0       25.0         0.02500      1.14
>>> Debris fragment      50.0         2.0          0.04000      0.75
>>>
>>> ======================================================================
>>> Example 4: Debris Cloud Lifetime Analysis
>>> ======================================================================
>>>
>>> Debris lifetime analysis:
>>> Type               Alt (km)   Mass (kg)    Area (m²)    Lifetime (yrs)
>>> ----------------------------------------------------------------------
>>> Large fragment     400        100.0        5.00         0.16
>>> Medium fragment    500        50.0         5.00         0.28
>>> Small fragment     600        10.0         2.00         0.18
>>> Tiny flake         700        0.5          0.05         0.70
>>>
>>> ======================================================================
>>> Example 5: De-orbit Scenarios
>>> ======================================================================
>>>
>>> Comparing de-orbit methods (500 km altitude):
>>>
>>> Standard configuration:
>>>   Area: 20 m², Mass: 1000 kg
>>>   Lifetime: 1.06 years
>>>
>>> With drag sail deployed:
>>>   Area: 120 m², Mass: 1000 kg
>>>   Lifetime: 0.23 years
>>>   De-orbit time reduced by factor of 4.6
>>>
>>> ======================================================================
>>> Orbital Lifetime Analysis Complete
>>> ======================================================================
>>>
>>> Key Factors Affecting Lifetime:
>>>   1. Altitude: Higher altitude = longer lifetime (exponential)
>>>   2. Area-to-Mass Ratio: Higher A/M = shorter lifetime
>>>   3. Solar Activity: Increased atmospheric density during solar max
>>>   4. Inclination: Affects atmospheric density encounters
>>>
>>> Typical Lifetimes:
>>>   - 200-300 km: Days to weeks
>>>   - 400-500 km: Months to few years
>>>   - 600-700 km: Several years to decades
>>>   - 800+ km: Decades to centuries
>>>   - 1000+ km: Centuries (debris problem)
>>>
>>> De-orbit Mitigation:
>>>   - Deploy drag sails to increase area
>>>   - Lower perigee with propulsive maneuver
>>>   - 25-year rule: Remove from LEO within 25 years post-mission
"""
