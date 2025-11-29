# Main.py
from pathlib import Path
import time

from logger import (
    read_instance,
    print_solution,
    print_covered_matrix,
    read_config, 
    write_solution,    
)

from greedy.greedy_solver import greedy
# If we add more solvers add them here


# ------------------- CONFIG -------------------
BASE_DIR = Path(__file__).resolve().parent

# Read from config.dat
config = read_config(BASE_DIR / "config.dat")

# PARAMETERS FROM CONFIG.DAT
instance_path   = BASE_DIR / config["instancePath"]
solver          = config.get("solver", "Greedy")
solution_file   = BASE_DIR / config.get("solutionFile", "solutions/solution.sol")
localSearch     = config.get("localSearch", False)
max_exec_time   = config.get("maxExecTime", 60)


# ------------------- READ DATA -------------------
K, P, R, A, C, N, M = read_instance(instance_path)


# ------------------- SOLVERS EXECUTION -------------------
if solver == "Greedy" and not localSearch:

    start = time.perf_counter()      # START TIME
    S, covers, cost = greedy(K, P, R, A, C, N, M)
    end = time.perf_counter()        # END TIME

    # Execution time
    exec_time = end - start
    exec_time = exec_time * 1000 # ms
    
    # save solution (even if it is not feasible)
    write_solution(solution_file, S, covers, cost)

    if S is not None:
        print_solution(S)
        # print_covered_matrix(covers, N) # If is feasible this always print the same since eveything is covered, so it is not necessary
        print(f"Total cost: {cost}")
    else:
        print("Not feasible solution was faund for this data")

    print(f"\nExecution time: {exec_time:.6f} ms\n")

else:
    print("The selected solver is not implemented yet :( \nTry another configuration please")