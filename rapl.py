data = [
    {
        'pid': 3118,
        'cpu_percent': 0.0,
        'memory_percent': 0.08988926713225968,
        'io_counters': (9810787, 9774863, 177446912, 91275264, 364211064, 169382519),
        'num_ctx_switches': {'voluntary': 1580, 'involuntary': 486},
        'num_interrupts': 1,
        'create_time': 1689920712.85
    },
    {
        'pid': 3155,
        'cpu_percent': 0.0,
        'memory_percent': 0.9086600103325557,
        'io_counters': (1081902, 2383249, 123637760, 655360, 1896043, 33634934),
        'num_ctx_switches': {'voluntary': 1188299, 'involuntary': 498106},
        'num_interrupts': 13,
        'create_time': 1689920725.97
    },
    {
        'pid': 3519,
        'cpu_percent': 0.0,
        'memory_percent': 0.5194042815651144,
        'io_counters': (814, 637, 2863104, 311296, 182922, 313050),
        'num_ctx_switches': {'voluntary': 1773, 'involuntary': 97},
        'num_interrupts': 10,
        'create_time': 1689920757.49
    }
    # Add more data points here if needed
]

num_data_points = len(data)

# Initialize sums for each metric
total_cpu_percent = 0.0
total_memory_percent = 0.0
total_io_counters = [0, 0, 0, 0, 0, 0]
total_num_ctx_switches_voluntary = 0
total_num_ctx_switches_involuntary = 0
total_num_interrupts = 0

# Calculate sums for each metric
for entry in data:
    total_cpu_percent += entry['cpu_percent']
    total_memory_percent += entry['memory_percent']
    total_io_counters = [total + entry_io for total, entry_io in zip(total_io_counters, entry['io_counters'])]
    total_num_ctx_switches_voluntary += entry['num_ctx_switches']['voluntary']
    total_num_ctx_switches_involuntary += entry['num_ctx_switches']['involuntary']
    total_num_interrupts += entry['num_interrupts']

# Calculate averages for each metric
average_cpu_percent = total_cpu_percent / num_data_points
average_memory_percent = total_memory_percent / num_data_points
average_io_counters = [total // num_data_points for total in total_io_counters]
average_num_ctx_switches_voluntary = total_num_ctx_switches_voluntary / num_data_points
average_num_ctx_switches_involuntary = total_num_ctx_switches_involuntary / num_data_points
average_num_interrupts = total_num_interrupts / num_data_points

print("Average CPU Percent:", average_cpu_percent)
print("Average Memory Percent:", average_memory_percent)
print("Average I/O Counters:", average_io_counters)
print("Average Number of Voluntary Context Switches:", average_num_ctx_switches_voluntary)
print("Average Number of Involuntary Context Switches:", average_num_ctx_switches_involuntary)
print("Average Number of Interrupts:", average_num_interrupts)
