# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Brief description of what this example demonstrates.

API: POST /api/Module/Endpoint
"""

from astrox.<module> import <function>
from astrox.models import <Model1>, <Model2>


def main():
    # Setup
    entity = <Model1>(...)

    # Execute
    result = <function>(
        param1=value1,
        param2=value2,
        entity=entity,
    )

    # Output - direct field access, no defensive checks
    print(f"Success: {result['IsSuccess']}")
    print(f"Data: {result['Data']}")


if __name__ == "__main__":
    main()
