"""
🧠 Industrial-Engineering-Hub: Decision Science Tool
Analytic Hierarchy Process (AHP) Weight Calculator
"""

import numpy as np

class AHPCalculator:
    def __init__(self, matrix):
        """
        matrix: A square n x n pairwise comparison matrix (numpy array)
        """
        self.matrix = np.array(matrix)
        self.n = self.matrix.shape[0]

    def calculate_weights(self):
        # Normalize the matrix
        column_sums = np.sum(self.matrix, axis=0)
        normalized_matrix = self.matrix / column_sums
        
        # Calculate weights (average of each row)
        weights = np.mean(normalized_matrix, axis=1)
        
        # Calculate consistency ratio (CR)
        weighted_sum_vector = np.dot(self.matrix, weights)
        lambda_max = np.mean(weighted_sum_vector / weights)
        
        ci = (lambda_max - self.n) / (self.n - 1)
        
        # Random Consistency Index (RI) table for 1-10
        ri_table = {1:0, 2:0, 3:0.58, 4:0.90, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45, 10:1.49}
        ri = ri_table.get(self.n, 1.49)
        
        cr = ci / ri if ri > 0 else 0
        
        return weights, cr

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: AHP Ağırlık Hesaplama ---")
    
    # Example Matrix for 3 criteria: Cost, Quality, Reliability
    # 1: Equal, 3: Moderate, 5: Strong, 7: Very Strong, 9: Extreme
    # Diagonal must be 1. Reciprocal below diagonal.
    pairwise_matrix = [
        [1,   1/3, 1/5], # Cost vs others
        [3,   1,   1/3], # Quality vs others
        [5,   3,   1]    # Reliability vs others
    ]
    
    calc = AHPCalculator(pairwise_matrix)
    weights, cr = calc.calculate_weights()
    
    print("\n📊 AHP SONUÇLARI:")
    print("-" * 50)
    criteria = ["Maliyet", "Kalite", "Güvenilirlik"]
    for i, w in enumerate(weights):
        print(f"🔹 {criteria[i]}: %{w*100:.2f}")
    
    print("-" * 50)
    print(f"📉 Tutarlılık Oranı (CR): {cr:.4f}")
    if cr < 0.1:
        print("✅ Karar mantıksal olarak tutarlıdır.")
    else:
        print("⚠️ Uyarı: Karar tutarsız olabilir (CR > 0.1). Lütfen puanları gözden geçirin.")

if __name__ == "__main__":
    main()
