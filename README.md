# AMMM_MIRI-Project
This repository contains tools for generating problem instances, solving them using heuristic algorithms, and evaluating an ILP formulation implemented in CPLEX.

Project Structure:
.
├── InstanceGenerator/
│   ├── config.dat
│   └── instanceGenerator.py
│
├── algorithms/
│   ├── heuristics/
│   │   ├── aux_functions.py
│   │   ├── grasp.py
│   │   ├── greedy.py
│   │   ├── greedy_solver.py
│   │   └── localsearch.py
│   │
│   ├── instances/      # input data files (auto-generated or custom)
│   ├── solutions/      # output solution files
│   │
│   ├── Main.py         # Main
│   ├── config.dat
│   └── logger.py
│
├── cplex/
│   ├── project.mod
│   ├── test.dat
│   └── README
│
└── README.md

1. Instance Generation
  The folder InstanceGenerator contains the tools used to generate synthetic problem instances.

Configuration
- The file InstanceGenerator/config.dat allows the user to define the instances size.

The generator automatically stores the resulting .dat files under:
  algorithms/instances/

This location can be changed inside the instance generator code or configuration file.

Running the instance generator:
  python InstanceGenerator/instanceGenerator.py

2. Algorithms

All heuristic algorithms are located under algorithms/heuristics/.

The implemented heuristics include:
- Greedy constructive heuristic,
- Local Search (First Improvement or Best Improvement),
- GRASP (with configurable alpha parameter).


3. Solver Configuration (Main config)
The file algorithms/config.dat contains the main parameters used when running the solver:
selection of the algorithm (Greedy, Local Search, GRASP),

input/output file name and path,

Local Search policy (FI or BI),

GRASP-specific settings (alpha, maximum iterations),

paths for instances and solutions.

Running the solver
python algorithms/Main.py


The solver reads all relevant settings from algorithms/config.dat.

4. ILP Model (CPLEX)

The folder cplex/ contains the exact ILP formulation of the problem:

project.mod is the ILP model,

test.dat is an example instance for testing.

These files can be loaded and solved with IBM CPLEX Studio or via the command-line CPLEX tools.

Summary
Component	Purpose	How to run
InstanceGenerator	Creates synthetic problem instances	python InstanceGenerator/instanceGenerator.py
Heuristic solvers	Solves the optimization problem using Greedy, LS, or GRASP	python algorithms/Main.py
CPLEX ILP model	Exact integer linear programming formulation	Load project.mod and .dat in CPLEX

Si quieres, te hago una versión más corta para entregable, o una versión con ejemplos de uso.
