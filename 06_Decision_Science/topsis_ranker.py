"""
🧠 Industrial-Engineering-Hub: Decision Science Tool
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
"""

import numpy as np

class TOPSISRanker:
    def __init__(self, decision_matrix, weights, impacts):
        """
        decision_matrix: Alternatives (rows) x Criteria (cols)
        weights: array of criteria weights (sums to 1)
        impacts: array of '+' or '-' indicating benefit or cost criteria
        """
        self.matrix = np.array(decision_matrix, dtype=float)
        self.weights = np.array(weights)
        self.impacts = impacts

    def calculate(self):
        # 1. Normalize the matrix
        norm_matrix = self.matrix / np.sqrt((self.matrix**2).sum(axis=0))
        
        # 2. Weighted normalized matrix
        weighted_matrix = norm_matrix * self.weights
        
        # 3. Determine ideal (A+) and anti-ideal (A-) solutions
        a_plus = []
        a_minus = []
        for i, imp in enumerate(self.impacts):
            col = weighted_matrix[:, i]
            if imp == '+':
                a_plus.append(np.max(col))
                a_minus.append(np.min(col))
            else:
                a_plus.append(np.min(col))
                a_minus.append(np.max(col))
        
        a_plus = np.array(a_plus)
        a_minus = np.array(a_minus)
        
        # 4. Calculate distances to ideal and anti-ideal
        s_plus = np.sqrt(((weighted_matrix - a_plus)**2).sum(axis=1))
        s_minus = np.sqrt(((weighted_matrix - a_minus)**2).sum(axis=1))
        
        # 5. Calculation of performance score (Si*)
        scores = s_minus / (s_plus + s_minus)
        
        return scores

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: TOPSIS Sıralama ---")
    
    # 3 Alternatives (Supplier A, B, C) and 3 Criteria (Price, Quality, Delivery Time)
    # Price is cost (-), Quality is benefit (+), Delivery is benefit (+)
    dataset = [
        [200, 7, 5], # Supplier A
        [150, 6, 8], # Supplier B
        [250, 9, 7]  # Supplier C
    ]
    
    weights = [0.4, 0.4, 0.2]
    impacts = ['-', '+', '+']
    
    ranker = TOPSISRanker(dataset, weights, impacts)
    scores = ranker.calculate()
    
    print("\n📊 TOPSIS PERFORMANS SKORLARI:")
    print("-" * 50)
    alternatives = ["Tedarikçi A", "Tedarikçi B", "Tedarikçi C"]
    for i, s in enumerate(scores):
        print(f"🔹 {alternatives[i]}: {s:.4f}")
    
    best_idx = np.argmax(scores)
    print("-" * 50)
    print(f"✅ Rapor: En iyi seçenek '{alternatives[best_idx]}' olarak belirlenmiştir.")

if __name__ == "__main__":
    main()
