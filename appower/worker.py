import psutil
from typing import Dict


class Worker:
    """The Worker that collects that and does all the calculations of the metrics"""

    def __init__(self, app_name) -> None:
        self.app_name = app_name

    def get_all_process(self) -> Dict[int, psutil.Process]:
        """Get all the processes started by this application"""
        processes = {}
        for proc in psutil.process_iter(["pid", "name", "ppid"]):
            if proc.info["name"].lower() in self.app_name.lower() and proc.status() == psutil.STATUS_RUNNING:
                processes[proc.pid] = proc
        return processes

    def get_process_metrics(self, proc: psutil.Process) -> Dict:
        """This method gets the metrics on the system resources used by this process
        The following metrics are retrieved
        """
        with proc.oneshot():
            return {
                "pid": proc.pid,
                "cpu_percent": proc.cpu_percent(interval=0.5),
                "cpu_times": proc.cpu_times(),
                "memory_info": proc.memory_info(),
                "memory_percent": proc.memory_percent(),
                "io_counters": proc.io_counters(),
                "num_ctx_switches": proc.num_ctx_switches(),
                "num_interrupts": proc.num_threads(),
                "create_time": proc.create_time(),
            }
