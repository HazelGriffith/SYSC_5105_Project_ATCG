import json
import random, math, os
from Quadratic_Equation_Solver.quadratic_equation_solver import Quadratic, NotEnoughPrecisionException





test_frames = [
    ("TF1", 1, 5, 6),
    ("TF2", 1, 2, 1),
    ("TF3", 1, 1, 2),
    ("TF4", 0, 4, 8),
    ("TF5", 1e-12, 3, 2),
    ("TF6", 1e308, 1e308, 1),
    ("TF7", 1, -1e6, 1),
    ("TF8", 1, 0, -4),
    ("TF9", 1, 0, 4),
    ("TF10", 2, 4, 2),
]

results = []

for ID,a,b,c in test_frames:
    try:
        output = Quadratic.solveQuadratic(a,b,c)
        results.append({"id":ID, "input":(a,b,c), "output":output, "status":"PASS"})
    except Exception as e:
        results.append({"id":ID, "input":(a,b,c), "error":str(e), "status":"EXCEPTION"})

with open("quadratic_test_results.json","w") as f:
    json.dump(results,f,indent=4)
    
with open("quadratic_test_results.json", "r") as f:
    data = json.load(f)              # Python dict / list

with open("quadratic_test_results.txt", "w") as f:
    f.write(json.dumps(data, indent=2))   # nicely formatted text

print("Saved → quadratic_test_results.json")
print("Saved → quadratic_test_results.txt")