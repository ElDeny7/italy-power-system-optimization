# italy-power-system-optimization
Pyomo-based multi-zonal optimization model of the Italian electricity system for dispatch and capacity planning under decarbonization scenarios.

## Description

This repository contains a Python-based optimization model of the Italian electricity system with a multi-zonal representation and hourly temporal resolution. The model is developed using Pyomo and solved with Gurobi, and is designed to support the analysis of generation dispatch, capacity planning, and cross-zonal power exchanges under different energy transition scenarios.

The model formulation follows a cost-minimization framework:

min ∑_{t ∈ T} ∑_{z ∈ Z} ∑_{g ∈ G} (C_var,g · P_{g,z,t}) + ∑_{g ∈ G} C_cap,g · K_g + ∑_{t ∈ T} ∑_{z ∈ Z} C_CO2 · E_{z,t}

subject to:

- Power balance constraints for each zone and time step
- Generation capacity limits and availability factors
- Ramping constraints and operational limits for thermal units
- Storage dynamics (state of charge evolution)
- Inter-zonal transmission constraints (NTC limits)
- Policy or scenario-specific constraints (e.g., RES targets)

where:
- P_{g,z,t} = power output of technology g in zone z at time t
- K_g = installed capacity of technology g
- C_var,g = variable generation cost
- C_cap,g = investment cost
- C_CO2 = carbon price

The model explicitly represents the Italian bidding zones (e.g., NORD, CNORD, CSUD, SUD, SICI, SARD) and captures spatial heterogeneity in demand, renewable resources, and transmission constraints.

---

## Objectives

The main objectives of the model are:

- Quantify optimal generation dispatch across zones and time
- Evaluate investment decisions in generation and storage capacity
- Analyze the impact of renewable penetration on system operation
- Assess congestion and cross-zonal power flows
- Support scenario analysis for decarbonization pathways

---

## Methodology

The model is formulated as a large-scale linear or mixed-integer linear programming (LP/MILP) problem using Pyomo, a widely adopted algebraic modeling language in Python for optimization. The problem is solved using Gurobi, a state-of-the-art commercial solver for large-scale mathematical programming.

- Pyomo is used to define sets, variables, constraints, and the objective function.
- Gurobi is used to efficiently solve the resulting optimization problem.

---

## Scope and Use Cases

This model can be used for:

- Academic research in power system optimization
- Scenario analysis for energy policy and planning
- Sensitivity analysis on fuel prices, CO₂ costs, and demand growth
- Evaluation of storage deployment and flexibility requirements

---

## References

- Hart, W.E., Laird, C.D., Watson, J.-P., Woodruff, D.L. (2017). *Pyomo – Optimization Modeling in Python*. Springer.
- Gurobi Optimization, LLC. (2024). *Gurobi Optimizer Reference Manual*.
- Pfenninger, S., DeCarolis, J., Hirth, L., Quoilin, S., Staffell, I. (2018). “The importance of open data and software in energy modeling.” *Energy Strategy Reviews*, 22, 149–159.
