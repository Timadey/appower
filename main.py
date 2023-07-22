import time
import sys
from prettier_printer import pprint
from appower.worker import Worker

# Usage: `python3 main.py [app_name]`
if __name__ == "__main__":
    # Get application name
    if not len(sys.argv) > 1:
        app_name = input("Please enter the application name: ")
    else:
        app_name = sys.argv[1]

    """Since an application can have many processes,
    get all the processes by this application
    """
    consumption = Worker(app_name)
    all_processes = consumption.get_all_process()
    pprint(all_processes)
    if len(all_processes) < 1:
        print(f"This application {app_name}, does not have any open process")
        sys.exit()
    metrics = []
    while len(all_processes) > 0:
        try:
            for proc in all_processes.values():
                proc_metrics = consumption.get_process_metrics(proc)
                metrics.append(proc_metrics)
                pprint(proc_metrics)
        except Exception:
            print("Metrics collection has stopped")
            break
        time.sleep(1)
        all_processes = consumption.get_all_process()

    """Calculate average from all the metrics collected"""
    
