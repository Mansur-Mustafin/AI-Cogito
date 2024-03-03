import pygame
import sys
from settings import *
from model.mainMenu import MainMenu
from service.controller.controller import Command
from service.controller.gameController import GameController
from service.controller.menuController import LevelMenuController
from service.controller.menuController import MainMenuController, EndMenuController
from view.viewMainMenu import ViewMainMenu
import os
from AI.aiAlgorithms import *
from AI.ai import *
import csv
import time 
import threading

global start_time
global state
global curr_level

RESULST_DIR = 'analitics/'

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
        print(f"Running: ({state} - Level {curr_level}) {int(current_time - start_time)}s")
        time.sleep(1)

def test_ai(algorithm , levels):
    global start_time

    global curr_level


    data = []

    for level in levels:
        curr_level =level
        start_time = time.time()
        ai: AI = AI(level, algorithm)
        data.append( [level, round(ai.state.time, 4), ai.memory, len(ai.moves)])
    return data


def main():     

    global state
    easy_levels= []
    medium_levels= []
    hard_levels= []
    headers = ['Level', 'Time', 'Memory', 'Moves']

    for filename in os.listdir('levels/'):
        if filename.startswith("level") and filename.endswith(".yaml"):
            level_number = filename[5:-5]
            level = Level(level_number)
            if( level.difficulty == 1): easy_levels.append(level_number)
            elif ( level.difficulty == 2): medium_levels.append(level_number)
            else:  hard_levels.append(level_number)

    state = "BFS"
    data = test_ai(AIS.BFS, easy_levels + medium_levels)
    write_to_csv(RESULST_DIR +'bfs.csv', data, headers)

state = ""
start_time = time.time()
curr_level = 0

time_thread = threading.Thread(target=print_time)
time_thread.daemon = True
time_thread.start()


main()
        
       
