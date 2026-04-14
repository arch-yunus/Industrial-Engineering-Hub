"""
🚚 Industrial-Engineering-Hub: Supply Chain Tool
Logistics Transportation Problem Optimizer using PuLP
"""

from pulp import *

class LogisticsOptimizer:
    def __init__(self, warehouses, customers, supply, demand, costs):
        """
        warehouses: list of origin names
        customers: list of destination names
        supply: dict {warehouse: capacity}
        demand: dict {customer: requirement}
        costs: dict {(warehouse, customer): unit_cost}
        """
        self.warehouses = warehouses
        self.customers = customers
        self.supply = supply
        self.demand = demand
        self.costs = costs

    def solve(self):
        # Create the LP Problem
        prob = LpProblem("Transportation_Problem", LpMinimize)

        # Decision Variables
        routes = [(w, c) for w in self.warehouses for c in self.customers]
        vars = LpVariable.dicts("Route", (self.warehouses, self.customers), 0, None, LpInteger)

        # Objective Function
        prob += lpSum([vars[w][c] * self.costs[(w, c)] for (w, c) in routes]), "Total_Logistics_Cost"

        # Supply Constraints
        for w in self.warehouses:
            prob += lpSum([vars[w][c] for c in self.customers]) <= self.supply[w], f"Supply_Constraint_{w}"

        # Demand Constraints
        for c in self.customers:
            prob += lpSum([vars[w][c] for w in self.warehouses]) >= self.demand[c], f"Demand_Constraint_{c}"

        # Solve
        prob.solve(PULP_CBC_CMD(msg=0))
        
        status = LpStatus[prob.status]
        total_cost = value(prob.objective)
        
        results = {}
        for w in self.warehouses:
            for c in self.customers:
                if vars[w][c].varValue > 0:
                    results[(w, c)] = vars[w][c].varValue
                    
        return status, total_cost, results

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Lojistik Optimizasyonu ---")
    
    # Simple Dataset
    sources = ["Fabrika-A", "Fabrika-B"]
    destinations = ["Depo-1", "Depo-2", "Depo-3"]
    
    supply = {"Fabrika-A": 500, "Fabrika-B": 400}
    demand = {"Depo-1": 200, "Depo-2": 300, "Depo-3": 250}
    
    # Unit transportation costs
    costs = {
        ("Fabrika-A", "Depo-1"): 4, ("Fabrika-A", "Depo-2"): 2, ("Fabrika-A", "Depo-3"): 5,
        ("Fabrika-B", "Depo-1"): 3, ("Fabrika-B", "Depo-2"): 6, ("Fabrika-B", "Depo-3"): 1
    }
    
    optimizer = LogisticsOptimizer(sources, destinations, supply, demand, costs)
    status, total_cost, flow = optimizer.solve()
    
    print(f"\n✅ Optimizasyon Durumu: {status}")
    print(f"💰 Minimum Toplam Lojistik Maliyeti: {total_cost:.2f} ₺")
    print("\n📦 OPTİMUM SEVKIYAT PLANI:")
    print("-" * 50)
    for (w, c), val in flow.items():
        print(f"🚛 {w} ----> {c}: {val} birim")
    print("-" * 50)

if __name__ == "__main__":
    main()
