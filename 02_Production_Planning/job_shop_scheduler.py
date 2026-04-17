"""
Production Job Scheduler
Applies dispatching rules like Shortest Processing Time (SPT) and Earliest Due Date (EDD).
"""

def schedule_spt(jobs):
    """
    Shortest Processing Time minimizes average flow time.
    jobs: list of dicts [{'id': str, 'processing_time': int, 'due_date': int}]
    """
    scheduled = sorted(jobs, key=lambda x: x['processing_time'])
    return calculate_metrics(scheduled)

def calculate_metrics(scheduled_jobs):
    current_time = 0
    total_flow_time = 0
    total_tardiness = 0
    
    for job in scheduled_jobs:
        current_time += job['processing_time']
        flow_time = current_time
        tardiness = max(0, current_time - job['due_date'])
        
        total_flow_time += flow_time
        total_tardiness += tardiness
        
        job['completion_time'] = current_time
        job['tardiness'] = tardiness
        
    avg_flow_time = total_flow_time / len(scheduled_jobs)
    return scheduled_jobs, avg_flow_time, total_tardiness

if __name__ == "__main__":
    job_queue = [
        {'id': 'J1', 'processing_time': 4, 'due_date': 10},
        {'id': 'J2', 'processing_time': 2, 'due_date': 5},
        {'id': 'J3', 'processing_time': 7, 'due_date': 12},
        {'id': 'J4', 'processing_time': 3, 'due_date': 8}
    ]
    
    print("Scheduling using SPT (Shortest Processing Time):")
    schedule, avg_flow, tardiness = schedule_spt(job_queue)
    
    for j in schedule:
        print(f"Job {j['id']} - Completed At: {j['completion_time']}, Tardiness: {j['tardiness']}")
    print(f"Average Flow Time: {avg_flow}, Total Tardiness: {tardiness}")
