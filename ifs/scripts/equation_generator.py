from ifs.generators.midpoint import EquationGenerator
import json

params = ["A", "B", "x", "y"]
bias = [0.3, 0.3, 0.2, 0.2]
layers = [4, 2, 1]
n = 100_000

eg = EquationGenerator(params, bias, layers, n)

equations = eg.run()

equation_file = {
    "params": params,
    "bias": bias,
    "layers": layers,
    "n": n,
    "equations": equations,
}

with open("../data/equations/ABxy_421_100k.json", "w") as json_file:
    json.dump(equation_file, json_file)
json_file.close()
