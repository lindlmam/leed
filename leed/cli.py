"""Main program defining command line interface."""
import argparse

from . import example


def python_template():
    """Entry point for the minimal example."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--radius",
        required=True,
        type=float,
        help="Radius of circle.",
    )
    parser.add_argument(
        "--print-data",
        required=False,
        action="store_true",
        help="Print info from data file.",
    )
    parser.add_argument(
    	"-e",
    	"--elias",
    	action="store_true",
    	help="Tells you the truth about elias",
    )

    args = parser.parse_args()

    example.print_something(args.radius)
    if args.print_data:
        example.print_some_data()
    if args.elias:
    	print("elias is bigger as an egg")
