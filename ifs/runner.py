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

    def add_edges(self, vertices: np.array):
        """
        Adds the edge vertices.
        """
        self.__edges = vertices
        self.__dim = self.__resolve_dimensionality(vertices)

    def add_midpoint_function(self, midpoint: FunctionType, params: Dict) -> None:
        """
        A midpoint function and the parameters for the functions execution.
        """
        self.__midpoint = midpoint
        self.__midpoint_params = params

    def add_ruleset_function(self, ruleset: FunctionType, params: Dict) -> None:
        """
        A ruleset function and the parameters for the functions execution.
        """
        self.__ruleset = ruleset
        self.__ruleset_params = params

    # Function Execution
    def midpoint(self, A: np.array, B: np.array, params: Dict = None) -> np.array:
        if params is None:
            return self.__midpoint(A, B, **self.__midpoint_params)
        else:
            return self.__midpoint(A, B, **params)

    def ruleset(self, A: np.array, B: np.array, params: Dict = None) -> np.array:
        if params is None:
            return self.__ruleset(A, B, **self.__ruleset_params)
        else:
            return self.__ruleset(A, B, **params)

    # Properties
    @property
    def edges(self) -> np.array:
        return self.__edges

    @property
    def midpoint_params(self) -> Dict:
        return self.__midpoint_params

    @property
    def ruleset_params(self) -> Dict:
        return self.__ruleset_params

    # Run IFS
    def run(self, n: int, start: np.array = None) -> np.array:
        """
        Runs the IFS system.

        Params:
            n (int): The number of iterations to run the IFS system.
        """
        pass
        # get the number of dimensions
        # create the point list with the first point at the origin if start is None
