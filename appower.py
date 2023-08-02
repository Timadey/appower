#!/usr/bin/env python3
import sys
import time
import os
from appower.worker import Worker, Energy
# import shlex
# from settings import RAPL_ENERGY_INTERVAL, RAPL_GET_ENERGY_PERIOD
# from prettier_printer import pprint

# Usage: `python3 main.py [path to program or app]`
if __name__ == "__main__":
    print("[INFO] Appower uses Intel RAPL technology which requires elevated permission")
    # Get application name
    if len(sys.argv) < 2:
        print("Usage: ./appower /path/to/executable [arguments for executable]")
        sys.exit(1)
    else:
        sys.argv[1] = os.path.abspath(sys.argv[1])
        app_cmd = sys.argv[1:]


    rapl = Energy()
    # print(f"Getting normal RAPL energy consumption before running application for {RAPL_GET_ENERGY_PERIOD} secs")

    # Get energy on normal case scenerio in RAPL_ENERGY_INTERVAL interval
    # normal_energy_metrics = rapl.get_rapl_energy_in(RAPL_GET_ENERGY_PERIOD)

    # print("normal energy metrics", normal_energy_metrics)

    initial_energy = rapl.get_rapl_energy()
    start_time = time.time()
    print(f"{time.strftime('%H:%M:%S')}: Running application/executable")
    app_output = Worker.run_subprocess(app_cmd)

    print(f"{time.strftime('%H:%M:%S')}: Finished running application/executable")
    energy_after = rapl.get_rapl_energy()
    end_time = time.time()
    time_taken = float(end_time - start_time)

    # Convert energy from microjoules (μJ) to joules (J).
    # RAPL gives energy in microjoules
    energy_consumed = (energy_after - initial_energy) / 1e6

    # Power consumed by RAPL while app is running
    power_consumed = energy_consumed/time_taken
    print(f'\n\nTime taken to execute program:{time_taken}')
    print(f'RAPL Energy consumption reading at application start: {initial_energy}')
    print(f'RAPL Energy consumption reading at application finsh: {energy_after}')
    print(f'Power consumed during application runtime: {power_consumed} W')

    # Calculating baseline power
    # baseline_start = normal_energy_metrics[0]

    # if int(time_taken) > RAPL_GET_ENERGY_PERIOD:
    #     # use predictive model to get remaining energy metrics
    #     print("Using prediction model")
    #     remaining_time = int(time_taken - RAPL_GET_ENERGY_PERIOD)
    #     print(Energy.predict_energy_metrics(normal_energy_metrics, remaining_time))
    #     baseline_end = Energy.predict_energy_metrics(normal_energy_metrics, remaining_time)[-1]
    # else:
    #     baseline_end = normal_energy_metrics[int(time_taken)]

    # baseline_energy_consumed = (float(baseline_end) - float(baseline_start)) / 1e6
    # baseline_power_consumed = baseline_energy_consumed/time_taken

    # appower = power_consumed - baseline_power_consumed
    # print("\n\nEnergy consumption if application was not running during application runtime")
    # print(f'Start Baseline RAPL Energy consumption: {baseline_start}')
    # print(f'End Baseline RAPL Energy consumption: {baseline_end}')
    # print(f'Baseline power consumed: {baseline_power_consumed}')

    # print(f'Power consumed by application: {appower}')

