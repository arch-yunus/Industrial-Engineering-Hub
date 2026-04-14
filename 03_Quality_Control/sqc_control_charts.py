"""
📉 Industrial-Engineering-Hub: Quality Control Tool
Statistical Process Control (SPC) - X-bar and R Charts
"""

import matplotlib.pyplot as plt
import numpy as np

class ControlChartGenerator:
    # Standard factors for Control Charts (for n=2 to n=10)
    A2 = {2: 1.880, 3: 1.023, 4: 0.729, 5: 0.577, 6: 0.483, 7: 0.419, 8: 0.373, 9: 0.337, 10: 0.308}
    D3 = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0.076, 8: 0.136, 9: 0.184, 10: 0.223}
    D4 = {2: 3.267, 3: 2.574, 4: 2.282, 5: 2.114, 6: 2.004, 7: 1.924, 8: 1.864, 9: 1.816, 10: 1.777}

    def __init__(self, data):
        """
        data: Use a 2D numpy array or list of lists where each sublist is a sample (subgroup).
        """
        self.data = np.array(data)
        self.subgroup_size = self.data.shape[1]
        self.means = np.mean(self.data, axis=1)
        self.ranges = np.max(self.data, axis=1) - np.min(self.data, axis=1)
        
        self.grand_mean = np.mean(self.means)
        self.average_range = np.mean(self.ranges)

    def calculate_limits(self):
        n = self.subgroup_size
        a2, d3, d4 = self.A2[n], self.D3[n], self.D4[n]
        
        # X-bar Chart Limits
        ucl_x = self.grand_mean + (a2 * self.average_range)
        lcl_x = self.grand_mean - (a2 * self.average_range)
        
        # R-Chart Limits
        ucl_r = d4 * self.average_range
        lcl_r = d3 * self.average_range
        
        return (ucl_x, lcl_x), (ucl_r, lcl_r)

    def plot_charts(self):
        (ucl_x, lcl_x), (ucl_r, lcl_r) = self.calculate_limits()
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
        
        # X-bar Chart
        ax1.plot(self.means, marker='o', color='b', label='Sample Mean')
        ax1.axhline(ucl_x, color='r', linestyle='--', label=f'UCL: {ucl_x:.2f}')
        ax1.axhline(lcl_x, color='r', linestyle='--', label=f'LCL: {lcl_x:.2f}')
        ax1.axhline(self.grand_mean, color='g', label=f'CL: {self.grand_mean:.2f}')
        ax1.set_title(f'X-Bar Control Chart (n={self.subgroup_size})')
        ax1.legend()
        
        # R Chart
        ax2.plot(self.ranges, marker='o', color='orange', label='Sample Range')
        ax2.axhline(ucl_r, color='r', linestyle='--', label=f'UCL: {ucl_r:.2f}')
        ax2.axhline(lcl_r, color='r', linestyle='--', label=f'LCL: {lcl_r:.2f}')
        ax2.axhline(self.average_range, color='g', label=f'CL: {self.average_range:.2f}')
        ax2.set_title('R Control Chart')
        ax2.legend()
        
        plt.tight_layout()
        plt.show()

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: SPC Kontrol Grafikleri ---")
    
    # Sample Data: 10 subgroups of size 5
    sample_data = np.random.normal(loc=10.0, scale=0.5, size=(10, 5))
    
    generator = ControlChartGenerator(sample_data)
    print(f"🔹 Grand Mean (X-double-bar): {generator.grand_mean:.4f}")
    print(f"🔹 Average Range (R-bar): {generator.average_range:.4f}")
    
    generator.plot_charts()

if __name__ == "__main__":
    main()
