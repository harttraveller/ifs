"""
This is the class to generate an IFS fractal. It requires:

* a set of verticies in n dimensions
* a function that accepts two points from n dimensional space, along with several parameters
* a ruleset for the application of the function
* some arbitrary starting point

"""


class IFS:
    def __init__(self) -> None:
        pass

    def reset(self) -> None:
        pass

    def add_vertices(self, vertices):
        pass

    def add_midpoint_function(self, midpoint):
        """
        The name is deceiving. While this should accept a "function" in mathematical terms,
        actually, an instantiated class should be passed.

        Args:
            midpoint (_type_): _description_
        """
        pass

    def add_ruleset_function(self, ruleset):
        pass
