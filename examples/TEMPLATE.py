# /// script
# dependencies = ["astrox-client"]
# requires-python = ">=3.10"
# ///
"""
Brief description of what this example demonstrates.

This should be 1-2 sentences explaining the purpose and what the user will learn.

API: POST /api/Module/Endpoint
"""

from astrox.<module> import <function>
from astrox.models import <Model1>, <Model2>


def main():
    # Setup - define inputs, models, configuration
    print("=" * 70)
    print("Example Title")
    print("=" * 70)
    print()

    # Define parameters
    param1 = "value1"
    param2 = "value2"

    # Create models
    model = <Model1>(...)

    # Action - call the API function
    print("Executing API call...")
    result = <function>(
        param1=param1,
        param2=param2,
        model=model,
    )

    # Output - display results using direct field access
    print()
    print("Results:")
    print("-" * 70)

    # Direct field access - no .get() or "if in" checks
    print(f"Success: {result['IsSuccess']}")
    print(f"Message: {result['Message']}")

    # Access nested data directly
    data = result["Data"]
    print(f"Data: {data}")

    # Iterate without emptiness checks
    for item in result["Items"]:
        print(f"  - {item}")


if __name__ == "__main__":
    main()
