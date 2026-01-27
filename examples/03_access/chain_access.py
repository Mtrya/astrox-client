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
    """Compute multi-hop access chains between ground stations via relay satellites."""
    print("=" * 70)
    print("Access Chain Computation: Ground → Relay Satellites → Ground")
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
    print(f"  Transmitter: {transmitter.Name} (Florida)")  # Name='Transmitter'
    print(f"  Relay 1: {relay1.Name} (LEO)")              # Name='Relay_1'
    print(f"  Relay 2: {relay2.Name} (LEO)")              # Name='Relay_2'
    print(f"  Receiver: {receiver.Name} (Europe)")        # Name='Receiver'
    print(f"  Total Links: {len(connections)}")           # 5
    print()

    # Compute access chain
    print("Computing access chains from Transmitter to Receiver...")
    # Endpoint: POST /access/ChainCompute
    # The API returns ChainOutput structure (see OpenAPI spec)
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

    # Expected structure based on OpenAPI spec:
    # ChainOutput: {IsSuccess: bool, Message: str, ComputedStrands: list[list[str]],
    #               CompleteChainAccess: list[TimeIntervalData], IndividualStrandAccess: dict,
    #               IndividualObjectAccess: dict}
    # TimeIntervalData: {Start: str, Stop: str, Duration: float}

    # Access result fields directly - HTTPClient handles IsSuccess flag checks
    # and raises AstroxAPIError if IsSuccess is false
    chain_intervals = result["CompleteChainAccess"]

    if not chain_intervals:
        print("No complete access chains found.")
        print("Note: Complete chains require simultaneous access across all links.")
        print("Try adjusting time window, orbits, or sensor angles.")
    else:
        print(f"Complete Chain Access Intervals: {len(chain_intervals)}")

        for i, interval in enumerate(chain_intervals, 1):
            print(f"Chain Access Window {i}:")
            print(f"  Start: {interval['Start']}")
            print(f"  Stop:  {interval['Stop']}")
            print(f"  Duration: {interval['Duration']:.2f} seconds")
            print()

    print()
    print("Access chain computation completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
