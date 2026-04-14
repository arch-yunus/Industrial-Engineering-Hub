"""
🚚 Industrial-Engineering-Hub: Facility Planning Tool
Activity Relationship Chart (ARC) Analyzer - SLP Foundation
"""

class RelationshipSolver:
    def __init__(self, departments, relationships):
        """
        departments: list of department names
        relationships: dict {(dep1, dep2): rating}
        Rating values: A=6, E=5, I=4, O=3, U=2, X=1
        """
        self.departments = departments
        self.relationships = relationships
        self.scores = {'A': 6, 'E': 5, 'I': 4, 'O': 3, 'U': 2, 'X': 1}

    def calculate_total_closeness_scores(self):
        tcs = {dep: 0 for dep in self.departments}
        
        for (d1, d2), rating in self.relationships.items():
            score = self.scores.get(rating, 0)
            tcs[d1] += score
            tcs[d2] += score
            
        return tcs

def main():
    print("--- ⚙️ Endüstri Mühendisliği Karar Destek Sistemi: İlişki Diyagramı Analizi ---")
    
    deps = ["Depo", "Kesim", "Montaj", "Boyama", "Paketleme", "Ofis"]
    
    # Example Relationship Ratings:
    # A: Absolutely Necessary, E: Especially Important, I: Important, O: Ordinary, U: Unimportant, X: Undesirable
    rels = {
        ("Depo", "Kesim"): 'A',
        ("Kesim", "Montaj"): 'A',
        ("Montaj", "Boyama"): 'E',
        ("Boyama", "Paketleme"): 'A',
        ("Paketleme", "Depo"): 'I',
        ("Ofis", "Paketleme"): 'U',
        ("Ofis", "Depo"): 'X',
        ("Montaj", "Paketleme"): 'O'
    }
    
    solver = RelationshipSolver(deps, rels)
    tcs = solver.calculate_total_closeness_scores()
    
    # Sort departments by Total Closeness Score (TCS)
    sorted_tcs = sorted(tcs.items(), key=lambda x: x[1], reverse=True)
    
    print("\n📊 TOPLAM YAKINLIK SKORLARI (TCS):")
    print("-" * 50)
    print("Bölüm             | Skor | Yerleşim Önceliği")
    print("-" * 50)
    for i, (dep, score) in enumerate(sorted_tcs):
        priority = "Yüksek" if i < 2 else ("Orta" if i < 4 else "Düşük")
        print(f"{dep:<17} | {score:<4} | {priority}")
    print("-" * 50)
    print("✅ Not: TCS puanı en yüksek olan bölümler (Ör: Kesim, Montaj), yerleşimin merkezine konulmalıdır.")

if __name__ == "__main__":
    main()
