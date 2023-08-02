# from statsmodels.tsa.arima.model import ARIMA
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
import psutil
import os
import subprocess
import time
from settings import BASE_DIR, RAPL_ENERGY_INTERVAL
from typing import Dict


class Worker:
    """The Worker that collects that and does all the calculations of the metrics"""

    def __init__(self, app_name) -> None:
        self.app_name = app_name

    def get_all_process(self) -> Dict[int, psutil.Process]:
        """Get all the processes started by this application"""
        processes = {}
        for proc in psutil.process_iter(["pid", "name", "ppid"]):
            if proc.info["name"].lower() in self.app_name.lower():
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
    @staticmethod
    def run_subprocess(cmd):
        try:
            # result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            proc = subprocess.Popen(cmd)
            proc_pid = proc.pid

            # set cpu affinity of the process and its children to cpu core 0
            # to check for worst case scenerio and for focused measurement
            print("Setting cpu affinity of application to core 0 for worst case scenerio and focus measurement")
            print("Outputs from application may start displaying now")
            os.sched_setaffinity(proc_pid, {0})
            proc.wait()
        except subprocess.CalledProcessError as e:
            print(f"Application stopped abruptly: {e}")
   
    @staticmethod
    def countdown(seconds):
        for i in range(seconds, 0, -1):
            print(f"Time left: {i} seconds", end="\r")

class Energy:
    """Uses RAPL technology to get the energy consumed by the RAPL package zone
    It is assumed the program to get the energy consumption has been compiled
    and it is readily available in the project directory.
    This is done automaticatly done during installation of project.
    Default program name is `energy`

    Note: RAPL requires elevated permissions. Root permission might be required
    """


    def __init__(self) -> None:
        self.program_name = 'energy'
        self.cmd = f'{os.path.join(BASE_DIR, self.program_name)}'
        # self.cmd = '/home/joshua/timothy/projects/appower/energy'

    def get_rapl_energy(self):
        """Get the current total energy consumed by the RAPL package zone"""

        try:
            # Run the compiled C program and capture the output
            result = subprocess.run(f'sudo {self.cmd}', capture_output=True, text=True, check=True, shell=True)

            if result.returncode == 0:
                output = result.stdout.strip()
                return float(output)
            else:
                print(f"Error {result.returncode}: {result.stderr.strip()}")
                return None

        except FileNotFoundError:
            print("Error: The C program checking RAPL energy was not found.")
            return None

        except subprocess.CalledProcessError as e:
            print(f"Error encountered while fetching energy: {e.stderr}")
            return None
    

    def get_rapl_energy_in(self, sec):
        """Get the RAPL energy in a period in an interval of `RAPL_ENERGY_INTERVAL"""
        interval = RAPL_ENERGY_INTERVAL
        energy_metrics = []
        start = time.time()
        finish = start + sec
        # print(f"{time.strftime('%H:%M:%S')}: Getting the RAPL energy")
        while time.time() <= finish:
            energy_metrics.append(self.get_rapl_energy())
            print(f"Time left: {finish - time.time()} seconds", end="\r")
            time.sleep(interval)
        # print(f"{time.strftime('%H:%M:%S')}: Finished getting the RAPL energy")
        return energy_metrics
    
    # @staticmethod
    # def predict_energy_metrics(normal_metrics:list, num_predictions:float):
    #     """Predict the enery cosumption metrics the RAPL would be consuming for `sec` seconds"""

        # import numpy as np
        # import pandas as pd
        # from sklearn.model_selection import train_test_split
        # from sklearn.linear_model import LinearRegression
        # from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

        # Load data from list
        # data = normal_metrics # example list of energy consumption in uJ
        # data = np.array(data) # convert list to numpy array
        # data = data.reshape(-1,1) # reshape array to have one column

        # # Create time column from data length
        # time = np.arange(len(data)) # create array of time values from 0 to data length
        # time = time.reshape(-1,1) # reshape array to have one column

        # # Combine time and data columns into a dataframe
        # df = pd.DataFrame(np.concatenate((time,data), axis=1), columns=["time","energy"]) # create dataframe from time and data arrays
        # df.head()

        # # Split data
        # X = df["time"].values.reshape(-1,1)
        # y = df["energy"].values.reshape(-1,1)
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # # Define model
        # model = LinearRegression()

        # # Train model
        # model.fit(X_train, y_train)

        # # Test model
        # y_pred = model.predict(X_test)

        # # Evaluate model
        # mae = mean_absolute_error(y_test, y_pred)
        # rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        # r2 = r2_score(y_test, y_pred)
        # print(f"MAE: {mae:.2f}")
        # print(f"RMSE: {rmse:.2f}")
        # print(f"R2: {r2:.2f}")

        # # Predict for next remaining time(num_prediction) seconds
        # x = normal_metrics[-1] # current consumption in uJ
        # print("X start point = ", x)
        # predictions = [] # list to store predictions
        # for i in range(num_predictions): # loop for num predictionseconds
        #     y = model.predict([[x]]) # predict output y
        #     predictions.append(y[0][0]) # append output y to predictions list
        #     x += 1 # increment input x by one second

        # return predictions