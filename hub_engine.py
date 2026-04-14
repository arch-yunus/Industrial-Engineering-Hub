"""
🏗️ Industrial-Engineering-Hub: Master Decision Support Engine
Central CLI for all IE modules and tools.
"""

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
    ========================================================
    🏗️  INDUSTRIAL ENGINEERING MASTER HUB ENGINE v3.0
    ========================================================
    Sistem Mimarisi, AI ve İleri Optimizasyon Ekosistemi
    "Sadece sistemleri tasarlamaz, onları zekayla donatırız."
    ========================================================
    """)

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(" [0] 🎯 Yöneylem Araştırması & Optimizasyon ++")
        print(" [1] 🔬 İş Etüdü & Ergonomi")
        print(" [2] 🏭 Üretim Planlama & Stok Yönetimi (AI)")
        print(" [3] 📉 Kalite Kontrol & Altı Sigma")
        print(" [4] 🚚 Tesis Planlama & Lojistik ++")
        print(" [5] 🎲 Simülasyon & Sistem Modelleme")
        print(" [6] 🧠 Karar Bilimi (AHP/TOPSIS)")
        print(" [7] 🌀 Sistem Dinamiği & Karmaşıklık")
        print(" [8] 🛰️ Zeka & Veri Analitiği (AI)")
        print(" [Q] ❌ Çıkış")
        print("-" * 56)
        
        choice = input("Seçiminizi yapın: ").strip().upper()
        
        if choice == 'Q':
            print("Güle güle mühendis! Sistem optimize kalsın.")
            break
        elif choice == '0':
            sub_menu_or()
        elif choice == '1':
            run_tool('01_Work_Study_and_Ergonomics/time_study_standardizer.py')
        elif choice == '2':
            sub_menu_planning()
        elif choice == '3':
            run_tool('03_Quality_Control/sqc_control_charts.py')
        elif choice == '4':
            sub_menu_logistics()
        elif choice == '5':
            sub_menu_simulation()
        elif choice == '6':
            sub_menu_decision()
        elif choice == '7':
            run_tool('07_System_Dynamics_and_Complexity/bullwhip_simulator.py')
        elif choice == '8':
            run_tool('02_Production_Planning/ai_demand_forecaster.py')
        else:
            input("Geçersiz seçim. Devam etmek için Enter'a basın...")

def run_tool(path):
    clear_screen()
    print(f"🚀 Modül başlatılıyor: {path}\n")
    os.system(f"python \"{path}\"")
    input("\nAna menüye dönmek için Enter'a basın...")

def sub_menu_or():
    while True:
        clear_screen()
        print("🎯 Yöneylem Araştırması Araç Kutusu")
        print("[1] Üretim Karması (LP) Çözücü")
        print("[2] Personel Vardiya (ILP) Optimizasyonu")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('00_Operations_Research/simplex_solver_utils.py')
        elif c == '2': run_tool('00_Operations_Research/workforce_optimizer.py')
        elif c == 'B': break

def sub_menu_planning():
    while True:
        clear_screen()
        print("🏭 Üretim Planlama Araç Kutusu")
        print("[1] EOQ & ROP Hesaplayıcı")
        print("[2] MRP Motoru (Pandas tabanlı)")
        print("[3] AI Destekli Talep Tahmini")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('02_Production_Planning/inventory_eoq_calculator.py')
        elif c == '2': run_tool('02_Production_Planning/mrp_engine.py')
        elif c == '3': run_tool('02_Production_Planning/ai_demand_forecaster.py')
        elif c == 'B': break

def sub_menu_logistics():
    while True:
        clear_screen()
        print("🚚 Tesis ve Lojistik Araç Kutusu")
        print("[1] Montaj Hattı Dengeleme")
        print("[2] Lojistik Ulaştırma Optimizasyonu")
        print("[3] SLP İlişki Diyagramı Analizörü")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('04_Facility_and_Supply_Chain/assembly_line_balancing.py')
        elif c == '2': run_tool('04_Facility_and_Supply_Chain/logistics_optimizer.py')
        elif c == '3': run_tool('04_Facility_and_Supply_Chain/relationship_chart_solver.py')
        elif c == 'B': break

def sub_menu_simulation():
    while True:
        clear_screen()
        print("🎲 Simülasyon Araç Kutusu")
        print("[1] Fabrika Simülasyonu (SimPy)")
        print("[2] Monte Carlo Risk Analizi")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('05_Simulation/simpy_factory_model.py')
        elif c == '2': run_tool('05_Simulation/monte_carlo_risk.py')
        elif c == 'B': break

def sub_menu_decision():
    while True:
        clear_screen()
        print("🧠 Karar Bilimi Araç Kutusu")
        print("[1] AHP Ağırlık Hesaplayıcı")
        print("[2] TOPSIS Sıralama")
        print("[B] Geri")
        c = input("> ").upper()
        if c == '1': run_tool('06_Decision_Science/ahp_calculator.py')
        elif c == '2': run_tool('06_Decision_Science/topsis_ranker.py')
        elif c == 'B': break

if __name__ == "__main__":
    main_menu()
