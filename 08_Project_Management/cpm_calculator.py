"""
Critical Path Method (CPM) simplified calculator.
"""

def calculate_cpm(tasks):
    """
    Basic forward pass for CPM.
    Tasks: dictionary of 'task_id': {'duration': int, 'precedence': ['task_id', ...]}
    """
    ef = {} # Early Finish
    es = {} # Early Start
    
    for task_id, info in tasks.items():
        if not info['precedence']:
            es[task_id] = 0
            ef[task_id] = info['duration']
        else:
            max_precedence_ef = max([ef.get(p, 0) for p in info['precedence']])
            es[task_id] = max_precedence_ef
            ef[task_id] = es[task_id] + info['duration']
            
    return ef, max(ef.values())

if __name__ == "__main__":
    tasks_data = {
        'A': {'duration': 3, 'precedence': []},
        'B': {'duration': 4, 'precedence': ['A']},
        'C': {'duration': 2, 'precedence': ['A']},
        'D': {'duration': 5, 'precedence': ['B', 'C']}
    }
    _, duration = calculate_cpm(tasks_data)
    print(f"Project Total Completion Time: {duration} periods")
