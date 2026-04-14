"""
⚙️ Industrial-Engineering-Hub: Facility Planning Tool
Assembly Line Balancing (Largest Candidate Rule Heuristic)
"""

def balance_line(tasks, task_times, cycle_time):
    """
    Simple heuristic to balance an assembly line.
    tasks: list of task names
    task_times: dict of task names to their processing times
    cycle_time: the maximum allowed time per station
    """
    stations = []
    current_station_tasks = []
    current_station_time = 0
    
    # Sort tasks by time (Largest Candidate Rule)
    sorted_tasks = sorted(tasks, key=lambda x: task_times[x], reverse=True)
    
    for task in sorted_tasks:
        time = task_times[task]
        if current_station_time + time <= cycle_time:
            current_station_tasks.append(task)
            current_station_time += time
        else:
            # Close current station and open a new one
            stations.append((current_station_tasks, current_station_time))
            current_station_tasks = [task]
            current_station_time = time
            
    # Add the last station
    if current_station_tasks:
        stations.append((current_station_tasks, current_station_time))
        
    return stations

def main():
    print("--- 🏭 Endüstri Mühendisliği Karar Destek Sistemi: Montaj Hattı Dengeleme ---")
    
    # Example Dataset
    example_tasks = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    example_times = {
        'A': 4, 'B': 3, 'C': 2, 'D': 5, 'E': 1, 'F': 4, 'G': 3
    }
    
    print(f"Örnek Görevler ve Süreleri: {example_times}")
    
    try:
        user_cycle_time = float(input("Çevrim Süresi (Cycle Time) değerini giriniz: "))
        
        result_stations = balance_line(example_tasks, example_times, user_cycle_time)
        
        print("\n" + "="*50)
        print(f"📊 HAT DENGELEME SONUÇLARI (Largest Candidate Rule):")
        total_time = sum(example_times.values())
        
        for i, (sts, t) in enumerate(result_stations):
            print(f"📍 İstasyon {i+1}: Görevler {sts} | Toplam Süre: {t}")
            
        n_stations = len(result_stations)
        efficiency = (total_time / (n_stations * user_cycle_time)) * 100
        
        print(f"\n✅ İstasyon Sayısı: {n_stations}")
        print(f"✅ Hat Verimliliği: %{efficiency:.2f}")
        print("="*50)
        
    except ValueError:
        print("❌ Hata: Lütfen geçerli bir sayısal değer giriniz.")

if __name__ == "__main__":
    main()
