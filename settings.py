import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Project root
# Interval at which to gather RAPL energy
RAPL_ENERGY_INTERVAL = 1 #sec
# Number of sceonds to gather RAPL energy while application is yet to run
RAPL_GET_ENERGY_PERIOD = 180 #secs
