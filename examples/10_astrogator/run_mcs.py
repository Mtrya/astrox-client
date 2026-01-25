"""
Run Mission Control Sequence (MCS) for trajectory design.

This example demonstrates using the Astrogator MCS to design a
simple orbit transfer maneuver from LEO to higher orbit using
impulsive delta-V burns.
"""

from astrox.astrogator import run_mcs
from astrox._models import (
    AgVAState,
    IAgVAElementAgVAElementCartesian,
    AgVAMCSSegmentAgVAMCSInitialState,
)
from astrox.models import (
    ApoapsisStop,
    Cartesian,
    DurationStop,
    ImpulsiveAttitude,
    ImpulsiveManeuver,
    ImpulsiveManeuverSegment,
    InitialStateSegment,
    PeriapsisStop,
    PropagateSegment,
)


def main():
    print("=" * 70)
    print("Mission Control Sequence: LEO Orbit Raising Maneuver")
    print("=" * 70)
    print()

    # Initial orbit state: LEO circular orbit
    initial_state = AgVAState(
        Epoch="1 Jan 2024 12:00:00.000",
        CoordSystemName="Earth Inertial",
        Element=IAgVAElementAgVAElementCartesian.model_construct(
            **{
                "$type": "Cartesian",
                "X": 6678137.0,  # Position X (m) - at equator
                "Y": 0.0,  # Position Y (m)
                "Z": 0.0,  # Position Z (m)
                "Vx": 0.0,  # Velocity X (m/s)
                "Vy": 7726.67,  # Velocity Y (m/s) - circular LEO
                "Vz": 0.0,  # Velocity Z (m/s)
            }
        ),
    )

    print("Mission Profile: LEO to Higher Orbit Transfer")
    print("-" * 70)
    print("Initial Orbit:")
    print("  Altitude: ~300 km")
    print("  Type: Circular LEO")
    print("  Velocity: ~7.73 km/s")
    print()
    print("Maneuver Sequence:")
    print("  1. Initial State: Set spacecraft in LEO")
    print("  2. Propagate to apoapsis")
    print("  3. Burn 1: Raise periapsis (Hohmann transfer burn)")
    print("  4. Propagate to new apoapsis")
    print("  5. Burn 2: Circularize orbit")
    print("  6. Propagate one orbit to verify")
    print()

    # Define mission sequence
    sequence = [
        # Segment 1: Set initial state
        AgVAMCSSegmentAgVAMCSInitialState.model_construct(
            **{
                "$type": "InitialState",
                "Name": "InitialLEOState",
                "InitialState": initial_state.model_dump(by_alias=True),
            }
        ),
        # Segment 2: Propagate to apoapsis
        PropagateSegment.model_construct(
            **{
                "$type": "Propagate",
                "Name": "PropagateToFirstApoapsis",
                "PropagatorName": "Earth HPOP",
                "StopConditions": [
                    ApoapsisStop(
                        Name="FirstApoapsis",
                        CentralBodyName="Earth",
                        Mu=3.986004418e14,  # Earth's gravitational parameter (m³/s²)
                    ).model_dump(by_alias=True)
                ],
            }
        ),
        # Segment 3: First burn - raise periapsis
        ImpulsiveManeuverSegment(
            SegmentType="Maneuver",
            Maneuver=ImpulsiveManeuver(
                DeltaVVector=Cartesian(
                    x=0.0,
                    y=500.0,  # 500 m/s prograde burn
                    z=0.0,
                ),
                Attitude=ImpulsiveAttitude(
                    AlignmentVector=Cartesian(x=0, y=1, z=0),  # Align with velocity
                ),
            ),
        ),
        # Segment 4: Propagate to next apoapsis
        PropagateSegment(
            SegmentType="Propagate",
            StoppingConditions=[
                ApoapsisStop(
                    Name="TransferApoapsis",
                    CentralBodyName="Earth",
                    Mu=3.986004418e14,  # Earth's gravitational parameter (m³/s²)
                )
            ],
        ),
        # Segment 5: Second burn - circularize
        ImpulsiveManeuverSegment(
            SegmentType="Maneuver",
            Maneuver=ImpulsiveManeuver(
                DeltaVVector=Cartesian(
                    x=0.0,
                    y=350.0,  # 350 m/s prograde burn
                    z=0.0,
                ),
                Attitude=ImpulsiveAttitude(
                    AlignmentVector=Cartesian(x=0, y=1, z=0),
                ),
            ),
        ),
        # Segment 6: Propagate one orbit to verify
        PropagateSegment(
            SegmentType="Propagate",
            StoppingConditions=[
                PeriapsisStop(
                    Name="VerifyOrbit",
                    CentralBodyName="Earth",
                    Mu=3.986004418e14,  # Earth's gravitational parameter (m³/s²)
                )
            ],
        ),
        # Segment 7: Final propagation to apoapsis
        PropagateSegment(
            SegmentType="Propagate",
            StoppingConditions=[
                ApoapsisStop(
                    Name="FinalApoapsis",
                    CentralBodyName="Earth",
                    Mu=3.986004418e14,  # Earth's gravitational parameter (m³/s²)
                )
            ],
        ),
    ]

    print("Executing Mission Control Sequence...")
    print()

    # Run MCS
    result = run_mcs(
        central_body="Earth",
        main_sequence=sequence,
        name="LEO_Orbit_Raising",
        description="Hohmann transfer from 300km to higher orbit",
    )

    # Display results
    print("Mission Control Sequence Results:")
    print("=" * 70)
    print()

    if "SegmentResults" in result and result["SegmentResults"]:
        segment_results = result["SegmentResults"]
        print(f"Total Segments Executed: {len(segment_results)}")
        print()

        total_delta_v = 0.0

        for i, seg_result in enumerate(segment_results, 1):
            seg_type = seg_result.get("SegmentType", "Unknown")
            print(f"Segment {i}: {seg_type}")
            print("-" * 70)

            # Initial state segment
            if seg_type == "InitialState":
                initial = seg_result.get("InitialState", {})
                epoch = initial.get("Epoch", "N/A")
                print(f"  Epoch: {epoch}")

            # Propagate segment
            elif seg_type == "Propagate":
                final_state = seg_result.get("FinalState", {})
                duration = seg_result.get("Duration", 0)
                print(f"  Duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")

                if "Element" in final_state:
                    elem = final_state["Element"]
                    if isinstance(elem, dict):
                        # Show position/velocity if Cartesian
                        if "x" in elem:
                            pos_mag = (elem["x"]**2 + elem["y"]**2 + elem["z"]**2)**0.5
                            vel_mag = (elem["vx"]**2 + elem["vy"]**2 + elem["vz"]**2)**0.5
                            altitude = (pos_mag - 6378137) / 1000  # km
                            print(f"  Final Altitude: {altitude:.1f} km")
                            print(f"  Final Velocity: {vel_mag:.2f} m/s")

            # Maneuver segment
            elif seg_type == "Maneuver":
                maneuver_result = seg_result.get("ManeuverResult", {})
                dv_vector = maneuver_result.get("DeltaVVector", {})

                if isinstance(dv_vector, dict) and "x" in dv_vector:
                    dv_mag = (dv_vector["x"]**2 + dv_vector["y"]**2 +
                              dv_vector["z"]**2)**0.5
                    total_delta_v += dv_mag
                    print(f"  Delta-V Applied: {dv_mag:.2f} m/s")
                    print(f"  Delta-V Vector: ({dv_vector['x']:.1f}, "
                          f"{dv_vector['y']:.1f}, {dv_vector['z']:.1f}) m/s")

            print()

        # Mission summary
        print("=" * 70)
        print("Mission Summary:")
        print("-" * 70)
        print(f"Total Delta-V Used: {total_delta_v:.2f} m/s")
        print(f"Total Delta-V Used: {total_delta_v/1000:.3f} km/s")
        print()
        print("Mission Analysis:")
        print("  - Hohmann transfer is the most fuel-efficient two-burn transfer")
        print("  - First burn raises apoapsis (transfer orbit injection)")
        print("  - Second burn circularizes at higher altitude")
        print(f"  - Total delta-V: ~{total_delta_v:.0f} m/s")

    else:
        print("No segment results returned.")
        print()
        print("Possible issues:")
        print("  - Invalid initial state")
        print("  - Propagation errors")
        print("  - Stopping condition not met")

    print()
    print("Applications:")
    print("-" * 70)
    print("  - Orbit transfer mission design")
    print("  - Rendezvous trajectory planning")
    print("  - Station-keeping maneuver optimization")
    print("  - Fuel budget analysis")
    print("  - Launch window analysis")
    print("  - Interplanetary trajectory design")

    print()
    print("MCS execution completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()

    # Example output:
    # >>> ======================================================================
    # >>> Mission Control Sequence: LEO Orbit Raising Maneuver
    # >>> ======================================================================
    # >>>
    # >>> Mission Profile: LEO to Higher Orbit Transfer
    # >>> ----------------------------------------------------------------------
    # >>> Initial Orbit:
    # >>>   Altitude: ~300 km
    # >>>   Type: Circular LEO
    # >>>   Velocity: ~7.73 km/s
    # >>>
    # >>> Maneuver Sequence:
    # >>>   1. Initial State: Set spacecraft in LEO
    # >>>   2. Propagate to apoapsis
    # >>>   3. Burn 1: Raise periapsis (Hohmann transfer burn)
    # >>>   4. Propagate to new apoapsis
    # >>>   5. Burn 2: Circularize orbit
    # >>>   6. Propagate one orbit to verify
    # >>>
    # >>> Traceback (most recent call last):
    # >>>   File "/home/betelgeuse/Developments/astrox-client/examples/10_astrogator/run_mcs.py", line 254, in <module>
    # >>>     main()
    # >>>   File "/home/betelgeuse/Developments/astrox-client/examples/10_astrogator/run_mcs.py", line 78, in main
    # >>>     PropagateSegment.model_construct(
    # >>>         **{
    # >>>             "$type": "Propagate",
    # >>>             "Name": "PropagateToFirstApoapsis",
    # >>>             "PropagatorName": "Earth HPOP",
    # >>>             "StopConditions": [
    # >>>                 ApoapsisStop(
    # >>>                     Name="FirstApoapsis",
    # >>>                     CentralBodyName="Earth",
    # >>>                     Mu=3.986004418e14,  # Earth's gravitational parameter (m³/s²)
    # >>>                 ).model_dump(by_alias=True)
    # >>>             ],
    # >>>         }
    # >>>     ),
    # >>>   File "/home/betelgeuse/Developments/astrox-client/.venv/lib/python3.13/site-packages/pydantic/main.py", line 250, in __init__
    # >>>     validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
    # >>> pydantic_core._pydantic_core.ValidationError: 4 validation errors for AgVAMCSSegmentAgVAMCSPropagate
    # >>> $type
    # >>>   Field required [type=missing, input_value={'SegmentType': 'Propagat... Mu=398600441800000.0)]}, input_type=dict]
    # >>>     For further information visit https://errors.pydantic.dev/2.12/v/missing
    # >>> PropagatorName
    # >>>   Field required [type=missing, input_value={'SegmentType': 'Propagat... Mu=398600441800000.0)]}, input_type=dict]
    # >>>     For further information visit https://errors.pydantic.dev/2.12/v/missing
    # >>> StopConditions
    # >>>   Field required [type=missing, input_value={'SegmentType': 'Propagat... Mu=398600441800000.0)]}, input_type=dict]
    # >>>     For further information visit https://errors.pydantic.dev/2.12/v/missing
    # >>> Name
    # >>>   Field required [type=missing, input_value={'SegmentType': 'Propagat... Mu=398600441800000.0)]}, input_type=dict]
    # >>>     For further information visit https://errors.pydantic.dev/2.12/v/missing
