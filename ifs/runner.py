"""
This is the class to generate an IFS fractal. It requires:

* a set of verticies in n dimensions
* a function that accepts two points from n dimensional space, along with several parameters
* a ruleset for the application of the function
* some arbitrary starting point

"""

import numpy as np
from types import FunctionType
from typing import Dict


class IFS:
    def __init__(self) -> None:
        pass

    # Private Methods
    def __resolve_dimensionality(self, vertices: np.array) -> int:
        """
        Resolves the number of dimensions the vertices are expressed in.
        ? Surely a better way to articulate.
        """
        pass

    # Public Methods

    def reset(self) -> None:
        pass

    def add_vertices(self, vertices: np.array):
        """
        Adds the edge vertices.
        """
        pass

    def add_midpoint_function(self, midpoint: FunctionType, params: Dict) -> None:
        """
        A midpoint function and the parameters for the functions execution.
        """
        pass

    def add_ruleset_function(self, ruleset: FunctionType, params: Dict) -> None:
        """
        A ruleset function and the parameters for the functions execution.
        """
        pass

    def run(self):
        """
        Runs the IFS system.
        """
        pass
