"""
⚙️ Industrial-Engineering-Hub: Operations Research Tool
Workforce Shift Scheduling Optimizer (Integer Programming)
"""

from pulp import *

class WorkforceOptimizer:
    def __init__(self, hourly_requirements, shifts):
        """
        hourly_requirements: list of 24 integers (demand per hour)
        shifts: dict {shift_name: list_of_hours_covered}
        """
        self.requirements = hourly_requirements
        self.shifts = shifts

    def solve(self):
        # Create the LP Problem (Minimize total staff)
        prob = LpProblem("Workforce_Scheduling", LpMinimize)

        # Decision Variables: Number of people assigned to each shift
        shift_vars = LpVariable.dicts("Shift", self.shifts.keys(), 0, None, LpInteger)

        # Objective Function: Minimize total personnel
        prob += lpSum([shift_vars[s] for s in self.shifts.keys()]), "Total_Staff"

        # Constraints: For each hour, total staff must meet requirements
        for hour in range(24):
            # Find shifts that cover this hour
            covering_shifts = [s for s, hours in self.shifts.items() if hour in hours]
            prob += lpSum([shift_vars[s] for s in covering_shifts]) >= self.requirements[hour], f"Hour_Constraint_{hour}"

        # Solve
        prob.solve(PULP_CBC_CMD(msg=0))
        
        status = LpStatus[prob.status]
        total_staff = value(prob.objective)
        
        results = {s: shift_vars[s].varValue for s in self.shifts.keys() if shift_vars[s].varValue > 0}
        
        return status, total_staff, results

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Personel Vardiya Optimizasyonu ---")
    
    # Example Hourly Demand (24 hours) - High in morning and evening
    demand = [
        2, 2, 1, 1, 3, 5, 8, 10, 12, 10, 8, 8, # 00:00 - 11:00
        10, 12, 14, 15, 12, 10, 8, 6, 4, 3, 2, 2 # 12:00 - 23:00
    ]

    # Typical 8-hour shifts starting every 4 hours
    shifts = {
        "Gece-1 (00-08)": list(range(0, 8)),
        "Sabah (04-12)": list(range(4, 12)),
        "Gündüz (08-16)": list(range(8, 16)),
        "Akşam (12-20)": list(range(12, 20)),
        "Gece-2 (16-00)": list(range(16, 24)),
        "Gece-V3 (20-04)": list(range(20, 24)) + list(range(0, 4))
    }

    optimizer = WorkforceOptimizer(demand, shifts)
    status, total, plan = optimizer.solve()

    print(f"\n✅ Optimizasyon Durumu: {status}")
    print(f"👥 Minimum Gereken Toplam Personel: {int(total)}")
    print("\n📅 OPTİMUM VARDİYA ÇİZELGESİ:")
    print("-" * 50)
    for shift, count in plan.items():
        print(f"🔹 {shift}: {int(count)} personel")
    print("-" * 50)

if __name__ == "__main__":
    main()
