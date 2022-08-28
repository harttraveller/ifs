"""
For the random generation of midpoint functions, selection functions, and associated parameters
"""

from typing import List, Dict
from math import log
from numpy import sin, cos, tan
import numpy as np


class OperationGenerate:
    def __init__(self, params: List[str], bias: List[float] = None) -> None:
        if bias is not None:
            assert len(params) == len(bias)
        self.params = params
        self.bias = bias
        self.operations = {
            "add": lambda params, bias: f"({' + '.join([np.random.choice(params, p=bias), np.random.choice(params, p=bias)])})",
            "subtract": lambda params, bias: f"({' - '.join([np.random.choice(params, p=bias), np.random.choice(params, p=bias)])})",
            "multiply": lambda params, bias: f"({' * '.join([np.random.choice(params, p=bias), np.random.choice(params, p=bias)])})",
            "divide": lambda params, bias: f"({' / '.join([np.random.choice(params, p=bias), np.random.choice(params, p=bias)])})",
            "exponent": lambda params, bias: f"({' ** '.join([np.random.choice(params, p=bias), np.random.choice(params, p=bias)])})",
            "logarithm": lambda params, bias: f"(log({np.random.choice(params, p=bias)}, {np.random.choice(params, p=bias)}))",
            "sin": lambda params, bias: f"(sin({np.random.choice(params, p=bias)}))",
            "cos": lambda params, bias: f"(cos({np.random.choice(params, p=bias)}))",
            "tan": lambda params, bias: f"(tan({np.random.choice(params, p=bias)}))",
        }

    def add(self):
        return self.operations["add"](self.params, self.bias)

    def subtract(self):
        return self.operations["subtract"](self.params, self.bias)

    def multiply(self):
        return self.operations["multiply"](self.params, self.bias)

    def divide(self):
        return self.operations["divide"](self.params, self.bias)

    def exponent(self):
        return self.operations["exponent"](self.params, self.bias)

    def logarithm(self):
        return self.operations["logarithm"](self.params, self.bias)

    def sin(self):
        return self.operations["sin"](self.params, self.bias)

    def cos(self):
        return self.operations["cos"](self.params, self.bias)

    def tan(self):
        return self.operations["tan"](self.params, self.bias)

    def random(self):
        return self.operations[np.random.choice(list(self.operations.keys()))](
            self.params, self.bias
        )


def generate_list_of_components(
    params: List[str], bias: List[float], n: int
) -> List[str]:
    op = OperationGenerate(params, bias)
    return [op.random() for _ in range(n)]


def generate_equation(params: List[str], bias: List[float], layers: List[int]):
    if layers[-1] != 1:
        layers.append(1)
    for i in layers:
        params = generate_list_of_components(params, bias, i)
        bias = None  # bias can only be applied on first round
    return params[0]


def generate_equations(params, bias, layers, n):
    return [generate_equation(params, bias, layers) for _ in range(n)]


def generate_functions(params, bias, layers, n):
    string_params = ", ".join(params)
    function = "".join(["lambda ", string_params, ": "])
    equations = generate_equations(params, bias, layers, n)
    functions = list()
    for equation in equations:
        function_dictionary = dict()
        function_dictionary["parameters"] = params
        function_dictionary["equation"] = f"(f{string_params}) = {equation}"
        function_dictionary["function"] = eval(f"{function}{equation}")
        functions.append(function_dictionary)
    return functions


class Midpoint:
    def __init__(self, funcdict: Dict) -> None:
        self.funcdict = funcdict
        self.function = funcdict["function"]

    @property
    def equation(self):
        return self.funcdict["equation"]

    def set_params(self, **kwargs):
        self.params = kwargs

    def execute(self, A, B):
        return self.function(A, B, **self.params)
