"""
Advanced Critical Path Method (CPM) Calculator
Calculates ES, EF, LS, LF, Slack, and determines the Critical Path.
"""
import sys

def calculate_cpm(tasks):
    """
    Kapsamlı CPM Ağ Analizi Hesaplayıcısı.
    ES, EF, LS, LF ve Bolluk (Slack) değerlerini hesaplar.
    
    Beklenen 'tasks' formatı:
    {
        'A': {'duration': 3, 'predecessors': []},
        'B': {'duration': 4, 'predecessors': ['A']},
        ...
    }
    """
    # 1. Forward Pass (İleri Hesaplama) - ES and EF
    es = {}
    ef = {}
    
    computed = set()
    while len(computed) < len(tasks):
        progress = False
        for task_id, info in tasks.items():
            if task_id not in computed:
                preds = info.get('predecessors', [])
                if all(p in computed for p in preds):
                    if not preds:
                        es[task_id] = 0
                    else:
                        es[task_id] = max(ef[p] for p in preds)
                    
                    ef[task_id] = es[task_id] + info['duration']
                    computed.add(task_id)
                    progress = True
        
        if not progress:
            raise ValueError("Döngü tespit edildi veya eksik öncül aktivite var!")

    project_duration = max(ef.values()) if ef else 0

    # 2. Backward Pass (Geri Hesaplama) - LS and LF
    ls = {}
    lf = {}
    
    # Sonrakileri (successors) bul
    successors = {task_id: [] for task_id in tasks}
    for task_id, info in tasks.items():
        for p in info.get('predecessors', []):
            if p in successors:
                successors[p].append(task_id)

    computed_backward = set()
    while len(computed_backward) < len(tasks):
        progress = False
        for task_id in list(tasks.keys()):
            if task_id not in computed_backward:
                succs = successors[task_id]
                if all(s in computed_backward for s in succs):
                    if not succs:
                        lf[task_id] = project_duration
                    else:
                        lf[task_id] = min(ls[s] for s in succs)
                    
                    ls[task_id] = lf[task_id] - tasks[task_id]['duration']
                    computed_backward.add(task_id)
                    progress = True

    # 3. Bolluk (Slack) ve Kritik Yol
    results = {}
    critical_path = []
    
    for task_id in tasks:
        slack = ls[task_id] - es[task_id]
        is_critical = slack == 0
        if is_critical:
            critical_path.append(task_id)
            
        results[task_id] = {
            'ES': es[task_id],
            'EF': ef[task_id],
            'LS': ls[task_id],
            'LF': lf[task_id],
            'Slack': slack,
            'Critical': is_critical,
            'Duration': tasks[task_id]['duration']
        }
        
    # Kritik yolu kronolojik olarak sırala (ES'ye göre)
    critical_path.sort(key=lambda x: results[x]['ES'])
    
    return results, project_duration, critical_path

def main():
    print("="*65)
    print("🏗️  KRİTİK YOL YÖNTEMİ (CPM) GELİŞMİŞ ANALİZÖRÜ")
    print("="*65)
    print("Proje aktivitelerinin erken/geç başlama zamanlarını, kesintilerini")
    print("hesaplar ve projeyi geciktirmeyecek 'Kritik Yolu' belirler.\n")
    
    # Standart bir ağ modeli (README'de belirtilen özellikleri test etmek için)
    tasks_data = {
        'A': {'duration': 3, 'predecessors': []},
        'B': {'duration': 4, 'predecessors': ['A']},
        'C': {'duration': 2, 'predecessors': ['A']},
        'D': {'duration': 5, 'predecessors': ['B', 'C']},
        'E': {'duration': 1, 'predecessors': ['D']},
        'F': {'duration': 2, 'predecessors': ['C']},
        'G': {'duration': 4, 'predecessors': ['E', 'F']}
    }
    
    print("[Örnek Proje Ağı Üzerinde CPM Çalıştırılıyor...]\n")
    
    try:
        results, duration, cp = calculate_cpm(tasks_data)
        
        # Terminal için formatlı çıktı
        print(f"{'Görev':<6} | {'Süre':<6} | {'ES':<4} | {'EF':<4} | {'LS':<4} | {'LF':<4} | {'Bolluk':<6} | {'Kritik Mi?'}")
        print("-" * 65)
        for t_id, r in sorted(results.items()):
            crit_marker = "🌟 Evet" if r['Critical'] else "   Hayır"
            print(f"{t_id:<6} | {r['Duration']:<6} | {r['ES']:<4} | {r['EF']:<4} | {r['LS']:<4} | {r['LF']:<4} | {r['Slack']:<6} | {crit_marker}")
            
        print("\n" + "="*65)
        print(f"🎯 Toplam Proje Süresi : {duration} birim")
        print(f"🚨 Kritik Yol         : {' -> '.join(cp)}")
        print("="*65)
        
    except Exception as e:
        print(f"Sistem Hatası: {e}")

if __name__ == "__main__":
    main()
