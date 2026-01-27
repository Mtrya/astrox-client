"""
Compute access chain through multiple objects.

This example demonstrates relay satellite access chain computation
from ground transmitter → relay satellites → ground receiver.

Known Issue: The /access/ChainCompute endpoint occasionally returns
HTTP 500 errors due to server-side instability. The client implementation
is correct, but the server may fail. See issues.md for details.
"""

from astrox.access import compute_chain
from astrox.models import (
    ConicSensor,
    EntityPath,
    EntityPositionJ2,
    EntityPositionSite,
)
from astrox._models import LinkConnection


def main():
    print("=" * 70)
    print("Access Chain Computation: Ground → Relay Satellites → Ground")
    print("=" * 70)
    print()

    print("WARNING: This example may fail with HTTP 500 (server-side error).")
    print("The /access/ChainCompute endpoint can be unstable on the server.")
    print("See examples/03_access/issues.md for details.")
    print()
    print("=" * 70)
    print()


    # Define analysis time window
    start = "2022-04-25T00:00:00Z"
    stop = "2022-04-25T12:00:00Z"

    # Transmitter: Ground station in Eastern US
    transmitter = EntityPath(
        Name="Transmitter",
        Position=EntityPositionSite(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[-75.5966, 30.0386, 0.0]  # lon, lat, alt
        ),
        Sensors=[
            ConicSensor(
                **{'$type': 'Conic'},
                Text="TX_Antenna",
                outerHalfAngle=60.0,  # Wide beam antenna
            )
        ],
    )

    # Relay 1: LEO satellite over Atlantic
    relay1 = EntityPath(
        Name="Relay_1",
        Position=EntityPositionJ2(
            **{'$type': 'J2'},
            J2NormalizedValue=0.000484165143790815,
            RefDistance=6378136.3,
            OrbitEpoch="25 Apr 2022 00:00:00.000000",
            CoordSystem="Inertial",
            CoordType="Classical",
            OrbitalElements=[
                6678137.0,  # ~300km altitude
                0.0,
                28.5,
                0.0,
                0.0,
                0.0,
            ],
        ),
        Sensors=[
            ConicSensor(
                **{'$type': 'Conic'},
                Text="Downlink",
                outerHalfAngle=45.0,
            )
        ],
    )

    # Relay 2: LEO satellite over Europe
    relay2 = EntityPath(
        Name="Relay_2",
        Position=EntityPositionJ2(
            **{'$type': 'J2'},
            J2NormalizedValue=0.000484165143790815,
            RefDistance=6378136.3,
            OrbitEpoch="25 Apr 2022 00:00:00.000000",
            CoordSystem="Inertial",
            CoordType="Classical",
            OrbitalElements=[
                6678137.0,
                0.0,
                28.5,
                45.0,  # Different RAAN
                0.0,
                90.0,  # Different true anomaly
            ],
        ),
        Sensors=[
            ConicSensor(
                **{'$type': 'Conic'},
                Text="Downlink",
                outerHalfAngle=45.0,
            )
        ],
    )

    # Receiver: Ground station in Europe
    receiver = EntityPath(
        Name="Receiver",
        Position=EntityPositionSite(
            **{'$type': 'SitePosition'},
            cartographicDegrees=[10.0, 48.0, 0.0]  # Munich area
        ),
        Sensors=[
            ConicSensor(
                **{'$type': 'Conic'},
                Text="RX_Antenna",
                outerHalfAngle=60.0,
            )
        ],
    )

    # Define all link objects
    all_objects = [transmitter, relay1, relay2, receiver]

    # Define connections (all possible links)
    connections = [
        # Transmitter to relay satellites
        LinkConnection(
            FromObject="Transmitter",
            ToObject="Relay_1",
        ),
        LinkConnection(
            FromObject="Transmitter",
            ToObject="Relay_2",
        ),
        # Relay satellites to receiver
        LinkConnection(
            FromObject="Relay_1",
            ToObject="Receiver",
        ),
        LinkConnection(
            FromObject="Relay_2",
            ToObject="Receiver",
        ),
        # Inter-satellite links (optional)
        LinkConnection(
            FromObject="Relay_1",
            ToObject="Relay_2",
        ),
    ]

    print(f"Analysis Period: {start} to {stop}")
    print()
    print("Network Topology:")
    print(f"  Transmitter: {transmitter.Name} (Florida)")
    print(f"  Relay 1: {relay1.Name} (LEO)")
    print(f"  Relay 2: {relay2.Name} (LEO)")
    print(f"  Receiver: {receiver.Name} (Europe)")
    print(f"  Total Links: {len(connections)}")
    print()

    # Compute access chain
    print("Computing access chains from Transmitter to Receiver...")
    result = compute_chain(
        start=start,
        stop=stop,
        all_objects=all_objects,
        start_object="Transmitter",
        end_object="Receiver",
        connections=connections,
        description="Relay satellite communication chain",
    )

    # Display results
    print()
    print("Access Chain Results:")
    print("-" * 70)

    if "AccessData" in result and result["AccessData"]:
        chain_intervals = result["AccessData"]
        print(f"Total Complete Chain Intervals: {len(chain_intervals)}")
        print()

        for i, interval in enumerate(chain_intervals, 1):
            print(f"Chain Access Window {i}:")
            print(f"  Start: {interval.get('Start')}")
            print(f"  Stop:  {interval.get('Stop')}")
            print(f"  Duration: {interval.get('Duration', 0):.2f} seconds")

            # Show chain path if available
            if "ChainPath" in interval:
                path = interval["ChainPath"]
                print(f"  Path: {' → '.join(path)}")

            print()
    else:
        print("No complete access chains found during the analysis period.")
        print()
        print("Note: Complete chains require simultaneous access across all links.")
        print("Try adjusting:")
        print("  - Analysis time window (longer period)")
        print("  - Relay satellite orbits (different planes)")
        print("  - Sensor cone angles (wider coverage)")

    print()
    print("Access chain computation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
