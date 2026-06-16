"""Do something."""
import os

import numpy as np
import yaml
from pkg_resources import resource_filename

some_data = resource_filename(__name__, os.path.join("data", "some_data.yml"))


def print_something(radius):
    """Print circumference of circle.

    Args:
        radius (float): Radius of circle.
    """
    print(f"Circle with radius {radius} has circumference {2 * np.pi * radius}")


def print_some_data():
    """Use useful data."""
    with open(some_data, encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.Loader)
        for k, v in data.items():
            print(f"{k}: {v}")
