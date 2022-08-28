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


class Midpoint:
    def __init__(self, function, params):
        pass


class Ruleset:
    def __init__(self, function, params):
        pass


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
        points = [self.start_point]
        selected_edges = list()
        for _ in range(n):
            selected_edge = self.ruleset(
                points, selected_edges, self.edges, **self.ruleset_params
            )
            computed_midpoint = self.midpoint(
                self.points[-1], selected_edge, **self.midpoint_params
            )
            points.append(computed_midpoint)
        return points
