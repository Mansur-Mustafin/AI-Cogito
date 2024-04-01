from settings import *
import os
from AI.aiAlgorithms import *
from AI.ai import *
import csv
import time 
import threading
import numpy as np
import matplotlib.pyplot as plt

global start_time
global state
global curr_level

RESULST_DIR = 'analitics/'

algorithms = [AIS.DFS,AIS.BFS, AIS.IDS, AIS.GREDDY, AIS.ASTAR, AIS.ASTARW]
heuristics = [H.MISS, H.LINECOLUMN, H.PATTERN, H.MANHATTAN, H.MANHATTAN_PATTERN]

time_labels = {
    "file_name": "time_plot.png",
    "y_label": "Time (s)",
    "title": "Time execution per algorithm"
}

memory_labels = {
    "file_name": "memory_plot.png",
    "y_label": "Memory (MB)",
    "title": "Memory usage per algorithm"
}

moves_labels = {
    "file_name": "moves_plot.png",
    "y_label": "Number of moves",
    "title": "Numer of moves of solution per algorithm"
}

labels = [time_labels, memory_labels, moves_labels]

def write_to_csv(file_path, data, headers=None):
    """
    Write data to a CSV file.

    Args:
    - file_path (str): The path to the CSV file.
    - data (list of lists): The data to be written to the CSV file.
    - headers (list): Optional. The headers for the CSV file.
    """
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)
        
        
def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_time():
    """Print the current time."""
    while True:
        clear_screen()
        current_time = time.time()
        print(f"Running: ({str(state)} - Level {curr_level}) {int(current_time - start_time)}s")
        time.sleep(1)


def test_ai(algorithm , levels, heuristic, weight=1):
    global start_time
    global curr_level

    data = []

    for level in levels:
        curr_level = level.level
        start_time = time.time()

        ai: AI = AI(level, algorithm, heuristic, weight)
        data.append([level.level, round(ai.state.time, 4), ai.memory, len(ai.moves)])
    return data

def draw_plot(data, measure):
    bars = {}
    n_levels = len(data[0])
    for i in range(n_levels):
        bars["Level " + str(i + 1)] = [algo_data[i][measure] for algo_data in data]

    max_measure = 0
    for measures in bars.values():
        max_measure = max(np.max(measures), max_measure)

    x = np.arange(len(algorithms))
    width = 0.9 / n_levels
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in bars.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(labels[measure - 1]["y_label"])
    ax.set_title(labels[measure - 1]["title"])
    ax.set_xticks(x + (0.5 * (n_levels - 1))*width, algorithms)
    ax.legend(loc='upper right', prop={'size': 9})
    ax.set_ylim(0, max_measure * 1.1)
    ax.set_xlim(-0.3, len(algorithms) + 0.6)
    
    plt.savefig("./analitics/plots/" + labels[measure - 1]["file_name"])

def main():     

    global state
    levels =[]
    headers = ['Level', 'Time', 'Memory', 'Moves']
    data = []

    for filename in sorted(os.listdir('levels/')):  
        if filename.startswith("level") and filename.endswith(".yaml"):
            level_number = filename[5:-5]
            level = Level(level_number)
            if( level.difficulty == 0): levels.append(level)

    for ai_algorithm in algorithms:
        state = ai_algorithm
        if (ai_algorithm == AIS.ASTARW):
            data.append(test_ai(ai_algorithm,  levels, H.MANHATTAN_PATTERN, 1))
        elif(ai_algorithm == AIS.ASTAR):
            data.append(test_ai(ai_algorithm, levels, H.MANHATTAN_PATTERN))
            write_to_csv(RESULST_DIR + str(state) + '.csv', data[-1], headers)
    
    draw_plot(data, 1) # Time plot
    draw_plot(data, 2) # Space plot
    draw_plot(data, 3) # Moves plot

state = ""
start_time = time.time()
curr_level = 0

time_thread = threading.Thread(target=print_time)
time_thread.daemon = True
time_thread.start()


main()
        
       
