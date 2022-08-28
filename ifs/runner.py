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
    def __init__(
        self,
        edges: np.array,
        midpoint: FunctionType,
        midpoint_params: Dict,
        ruleset: FunctionType,
        ruleset_params: Dict,
        start_point: np.array = None,
    ) -> None:
        self.edges = edges
        self.dimensions = self.__resolve_dimensionality(edges)
        self.midpoint = midpoint
        self.midpoint_params = midpoint_params
        self.ruleset = ruleset
        self.ruleset_params = ruleset_params
        self.start_point = self.__set_default_start(start_point, self.dimensions)

    # Private Methods
    def __resolve_dimensionality(self, edges: np.array) -> int:
        """
        Resolves the number of dimensions the vertices are expressed in.
        ? Surely a better way to articulate.
        """
        return len(edges)

    def __set_default_start(self, start_point: np.array, dimensions: int) -> Dict:
        if start_point is None:
            return np.zeros(dimensions)
        else:
            return start_point

    # Run IFS
    def run(self, n: int) -> np.array:
        """
        Runs the IFS system.

        Params:
            n (int): The number of iterations to run the IFS system.
        """
        pass
        # get the number of dimensions
        # create the point list with the first point at the origin if start is None
