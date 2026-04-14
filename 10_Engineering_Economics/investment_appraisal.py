"""
💰 Industrial-Engineering-Hub: Financial Engineering Tool
Investment Appraisal (NPV and Payback Period)
"""

class InvestmentAppraisal:
    def __init__(self, initial_investment, cash_flows, discount_rate):
        """
        initial_investment: Initial cost (negative value)
        cash_flows: List of annual cash flows (years 1 to n)
        discount_rate: Annual discount rate (MARR - Minimum Attractive Rate of Return)
        """
        self.p0 = initial_investment 
        self.flows = cash_flows
        self.r = discount_rate

    def calculate_npv(self):
        npv = self.p0
        for i, f in enumerate(self.flows):
            npv += f / (1 + self.r)**(i + 1)
        return npv

    def calculate_payback(self):
        cumulative_cash = self.p0
        for i, f in enumerate(self.flows):
            cumulative_cash += f
            if cumulative_cash >= 0:
                # Basic linear interpolation for the month
                prev_cash = cumulative_cash - f
                fraction = abs(prev_cash) / f
                return i + fraction
        return None # Never pays back

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: Yatırım Değerlendirme ---")
    
    try:
        p0 = -float(input("Başlangıç Yatırım Tutarı (₺): "))
        flows_input = input("Yıllık nakit akışlarını virgülle ayırarak giriniz (₺): ")
        flows = [float(f.strip()) for f in flows_input.split(',')]
        rate = float(input("İskonto Oranı / Sermaye Maliyeti (Ör: %12 için 0.12): "))
        
        calc = InvestmentAppraisal(p0, flows, rate)
        npv = calc.calculate_npv()
        payback = calc.calculate_payback()
        
        print("\n" + "="*50)
        print(f"📊 FİNANSAL ANALİZ SONUÇLARI:")
        print(f"🔹 Net Bugünkü Değer (NPV): {npv:,.2f} ₺")
        
        if npv > 0:
            print("✅ Sonuç: Proje EKONOMİK OLARAK UYGUNDUR (NPV > 0).")
        else:
            print("🛑 Sonuç: Proje EKONOMİK DEĞİLDİR (NPV < 0).")
            
        if payback:
            print(f"🔹 Geri Ödeme Süresi (Payback): {payback:.2f} Yıl")
        else:
            print("🔹 Geri Ödeme Süresi: Proje yatırımı geri ödemiyor.")
        print("="*50)
        
    except ValueError:
        print("🛑 Hata: Lütfen geçerli sayısal değerler giriniz.")

if __name__ == "__main__":
    main()
