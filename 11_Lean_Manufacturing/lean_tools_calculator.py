"""
Lean Manufacturing Tools Calculator
Calculates Kanban board requirements and Overall Equipment Effectiveness (OEE).
"""

def calculate_kanban_cards(daily_demand, lead_time_days, safety_stock_factor, container_capacity):
    """
    Calculates the number of Kanban cards needed for a system.
    """
    total_demand = daily_demand * lead_time_days
    safety_stock = total_demand * safety_stock_factor
    number_of_cards = (total_demand + safety_stock) / container_capacity
    import math
    return math.ceil(number_of_cards)

def calculate_oee(availability, performance, quality):
    """
    Overall Equipment Effectiveness (OEE) calculation.
    Values should be given as decimals between 0 and 1.
    """
    oee = availability * performance * quality
    return oee

if __name__ == "__main__":
    print(f"Kanban Cards Required: {calculate_kanban_cards(100, 2, 0.1, 20)}")
    print(f"OEE Score: {calculate_oee(0.9, 0.95, 0.99):.2%}")
