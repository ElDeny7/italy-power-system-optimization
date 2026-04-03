from pyomo.environ import *


def build_model(config):
    model = ConcreteModel()

    # -------------------
    # SETS
    # -------------------
    model.T = RangeSet(1, 24)  # time (hours)
    model.Z = Set(initialize=["NORD", "CNORD", "CSUD"])  # zones
    model.G = Set(initialize=["gas", "solar"])  # technologies

    # -------------------
    # PARAMETERS
    # -------------------
    # Demand per zone (simplified constant)
    demand_dict = {(z, t): 100 for z in model.Z for t in model.T}
    model.demand = Param(model.Z, model.T, initialize=demand_dict)

    # Generation costs
    model.cost = Param(model.G, initialize={"gas": 50, "solar": 0})

    # Capacity limits
    model.capacity = Param(
        model.G,
        model.Z,
        initialize={(g, z): 150 for g in model.G for z in model.Z}
    )

    # -------------------
    # VARIABLES
    # -------------------
    model.P = Var(model.G, model.Z, model.T, domain=NonNegativeReals)

    # -------------------
    # OBJECTIVE
    # -------------------
    def obj_rule(m):
        return sum(
            m.cost[g] * m.P[g, z, t]
            for g in m.G for z in m.Z for t in m.T
        )

    model.obj = Objective(rule=obj_rule, sense=minimize)

    # -------------------
    # CONSTRAINTS
    # -------------------

    # Power balance
    def balance_rule(m, z, t):
        return sum(m.P[g, z, t] for g in m.G) >= m.demand[z, t]

    model.balance = Constraint(model.Z, model.T, rule=balance_rule)

    # Capacity constraint
    def capacity_rule(m, g, z, t):
        return m.P[g, z, t] <= m.capacity[g, z]

    model.capacity_limit = Constraint(model.G, model.Z, model.T, rule=capacity_rule)

    return model
