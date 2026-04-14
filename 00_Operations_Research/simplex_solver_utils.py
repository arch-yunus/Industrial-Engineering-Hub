"""
⚙️ Industrial-Engineering-Hub: Operations Research Utils
Linear Programming Solver using SciPy
"""

from scipy.optimize import linprog

def solve_production_mix(profits, resource_usage, resource_limits):
    """
    Solves a production mix problem using Linear Programming.
    profits: List of coefficients for the objective function (maximized)
    resource_usage: Matrix of resource requirements per product
    resource_limits: List of total available resources
    """
    # SciPy minimize, so we negate profits for maximization
    c = [-p for p in profits]
    
    # Linear constraints: A_ub * x <= b_ub
    res = linprog(c, A_ub=resource_usage, b_ub=resource_limits, method='highs')
    
    if res.success:
        return {
            'Optimal Value': -res.fun,
            'Optimal Solution': res.x,
            'Status': 'Success'
        }
    else:
        return {'Status': 'Failed', 'Message': res.message}

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Üretim Karması Optimizasyonu ---")
    
    # Example: 2 Products, 3 Resources (Labor, Machine, Material)
    # Max z = 40x1 + 30x2
    profits = [40, 30]
    
    # Constraints:
    # 2x1 + 1x2 <= 100 (Labor)
    # 1x1 + 2x2 <= 80  (Machine)
    # 1x1 + 1x2 <= 60  (Material)
    usage = [
        [2, 1],
        [1, 2],
        [1, 1]
    ]
    limits = [100, 80, 60]
    
    result = solve_production_mix(profits, usage, limits)
    
    if result['Status'] == 'Success':
        print("\n✅ Optimal Çözüm Bulundu:")
        print(f"💰 Maksimum Kar: {result['Optimal Value']:.2f} ₺")
        for i, val in enumerate(result['Optimal Solution']):
            print(f"📦 Ürün {i+1} Miktarı: {val:.2f} adet")
    else:
        print(f"🛑 Çözüm Başarısız: {result['Message']}")

if __name__ == "__main__":
    main()
