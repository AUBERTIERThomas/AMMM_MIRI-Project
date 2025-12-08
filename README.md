# AMMM_MIRI-Project

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

**1. Instance Generation**
  The folder InstanceGenerator contains the tools used to generate synthetic problem instances.
  Configuration:
    - The file InstanceGenerator/config.dat allows the user to define the instances size.

The generator automatically stores the resulting .dat files under:
  algorithms/instances/

This location can be changed inside the instance generator code.

Running the instance generator:
  **python InstanceGenerator/instanceGenerator.py**

**2. Algorithms**

All heuristic algorithms are located under algorithms/heuristics/.
The implemented heuristics include:
- Greedy constructive heuristic,
- Local Search,
- GRASP.


**3. Solver Configuration (Main config)**
The file algorithms/config.dat contains the main parameters used when running the solver:
selection of the algorithm (Greedy, Local Search, GRASP), input/output file name and path,
Local Search policy (FI or BI), GRASP-specific settings (alpha, maximum iterations),

Running the solver
**python algorithms/Main.py**

--> The solver reads all relevant settings from algorithms/config.dat.


**4. ILP Model (CPLEX)**

The folder cplex/ contains the exact ILP formulation of the problem:
project.mod is the ILP model,
test.dat is an example instance for testing.
