"""
📦 Industrial-Engineering-Hub: Production Planning Tool
Material Requirements Planning (MRP) Engine using Pandas
"""

import pandas as pd
import math

class MRPEngine:
    def __init__(self, bom, master_production_schedule, initial_inventory):
        """
        bom: dict reflecting product structure {item: {component: qty}}
        mps: dict {period: qty} for final product
        initial_inventory: dict {item: qty}
        """
        self.bom = bom
        self.mps = master_production_schedule
        self.inventory = initial_inventory
        self.periods = list(master_production_schedule.keys())

    def run_mrp(self, final_product):
        results = {}
        
        # Start with final product
        results[final_product] = self.calculate_item_requirements(final_product, self.mps)
        
        # Calculate for components recursively (simplified for this model)
        if final_product in self.bom:
            components = self.bom[final_product]
            for comp, qty_per in components.items():
                comp_gross_requirements = {p: results[final_product][p]['Planned_Order_Releases'] * qty_per 
                                          for p in self.periods}
                results[comp] = self.calculate_item_requirements(comp, comp_gross_requirements)
                
        return results

    def calculate_item_requirements(self, item, gross_requirements):
        df = pd.DataFrame(index=self.periods)
        df['Gross_Requirements'] = pd.Series(gross_requirements)
        df['Scheduled_Receipts'] = 0
        df['Projected_Available'] = 0
        df['Net_Requirements'] = 0
        df['Planned_Order_Receipts'] = 0
        df['Planned_Order_Releases'] = 0
        
        current_inv = self.inventory.get(item, 0)
        
        for p in self.periods:
            # Projected available balance
            net = df.at[p, 'Gross_Requirements'] - current_inv - df.at[p, 'Scheduled_Receipts']
            
            if net > 0:
                df.at[p, 'Net_Requirements'] = net
                df.at[p, 'Planned_Order_Receipts'] = net
                df.at[p, 'Planned_Order_Releases'] = net # Assuming lead time 0 for simplicity
                current_inv = 0
            else:
                df.at[p, 'Net_Requirements'] = 0
                current_inv = abs(net)
            
            df.at[p, 'Projected_Available'] = current_inv
            
        return df

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: MRP Motoru ---")
    
    # Example BOM: 1 Table = 1 Top + 4 Legs
    bom = {
        'Masa': {'Tabla': 1, 'Ayak': 4}
    }
    
    # Master Production Schedule (10 weeks)
    mps = {w: 0 for w in range(1, 11)}
    mps[5] = 50  # 50 tables needed in week 5
    mps[8] = 30  # 30 tables needed in week 8
    
    initial_inv = {'Masa': 10, 'Tabla': 5, 'Ayak': 20}
    
    engine = MRPEngine(bom, mps, initial_inv)
    mrp_results = engine.run_mrp('Masa')
    
    for item, report in mrp_results.items():
        print(f"\n📦 MRP RAPORU: {item}")
        print("="*60)
        print(report[['Gross_Requirements', 'Projected_Available', 'Net_Requirements', 'Planned_Order_Releases']])
        print("="*60)

if __name__ == "__main__":
    main()
