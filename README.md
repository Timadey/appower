<!-- cmake .. -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=../.venv ../raplcap/
make
make install
gcc -o energy energy.c -I./.venv/include/raplcap -L./.venv/lib -lraplcap-msr -Wl,-rpath,./.venv/lib -std=c99

chmood +x energy


pip install --upgrade requests urllib3 chardet
pip install psutil numpy scikit-learn

Also remember to set intervals -->


# Power Consumption Measurement Mini-Program (Appower)

## Overview
Appower uses the Intel Running Application Power Limit (RAPL) through the [`raplcap`](https://github.com/powercap/raplcap) library, which provides a C interface for interacting with RAPL. However, RAPL only provides the energy consumption of the entire CPU. Appower is developed to measure the specific power consumption of a single software application running on a Linux computer with an Intel processor.

## Prerequisites

Before using Appower, ensure you have the following prerequisites installed on your Linux environment (Ubuntu focal):

- Linux environment (Ubuntu focal) with Intel processor
- Python 3
- Pip
- CMake

## Installation

To install Appower on your system, follow change to project root and run installation script
```
cd appower
source ./install
```

Always activate virtual environment with `source .venv/bin/activate` before using, because required libraries were installed there



## Usage

To use Appower, you can run it from the terminal and specify the path to the executable and its arguments:

```
./appower /path/to/executable arg1 arg2 arg3
```
**Note**: Appower uses RAPL, which requires elevated permissions (sudo). Therefore, root user permission will be required.

## Example

An example program has been provided at the project level directory to demonstrate how to use Appower:

```
(.venv)$: ./appower
Please enter the full path of the application/program (must be an executable):
/home/your_username/projects/test_appower 30
```

## Implementation Details

### TL;DR (Too Long; Didn't Read)
- Power consumed by the CPU while the application is not running: x
- Power consumed by the CPU while the application is running: x + a
(where a is the additional power consumed by the application)
- Power consumed by the application alone: a (obtained by subtracting x from x + a)

### Steps to Measure Application Power Consumption

1. **CPU Selection**: The application process and its children processes' CPU affinity are set to a single processor to ensure proper energy reading from a specific CPU.

2. **Energy Monitoring**: The initial energy reading (before application execution) of the RAPL PACKAGE ZONE is recorded.

3. **Application Execution**: The target application is executed with the provided arguments.

4. **Energy Monitoring (After Execution)**: The final energy reading is obtained after the application completes.

5. **Power Consumption Calculation**: The energy consumed by the application is calculated as the difference between the final and initial energy readings.

6. **Baseline Power Consumption**: To exclude background application data, the power consumption of the CPU during normal operation is measured over a specific period (default: 60 seconds).

7. **Final Power Consumption**: The power consumed by the application alone is obtained by subtracting the baseline power consumption from the total power consumption.

<!-- ### Predictive Model (Optional)

If the energy metrics collected during the baseline power consumption measurement are not sufficient for the application's runtime, a predictive model can be used to estimate the energy consumption for the remaining time. This allows accurate calculation of the baseline power consumption for the application's runtime. -->

<!-- ## Limitations

- Appower currently supports Linux environments (Ubuntu focal) with Intel processors only.
- The accuracy of power consumption measurements may vary depending on the system's hardware and energy monitoring capabilities.

## Future Enhancements

- Extend support for other Linux distributions and processor types.
- Improve predictive model# Power Consumption Measurement Mini-Program (Appower)

---
References
[Intel RAPL](https://www.intel.com/content/dam/www/public/us/en/documents/manuals/64-ia-32-architectures-software-developer-vol-3b-part-2-manual.pdf)
[raplcap github repo](https://github.com/powercap/raplcap)
[psutil documentation](https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_num)

Written by Timothy Adeleke -->