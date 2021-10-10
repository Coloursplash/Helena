from skills.skill import Skill
from skills.action import Action
from colorama import Fore
import termdown
from os import system
from time import ctime


skill = Skill("Time", "Clocks, stopwatches and other time related actions")


class Clock(Action):
    def __init__(self):
        self.name = "Clock"
        self.description = "Displays the time"
        self.command = "clock"


    def run(self):
        print(Fore.BLUE + ctime())


class Timer(Action):
    def __init__(self):
        self.name = "Timer"
        self.description = "Starts a timer for the specified time"
        self.command = "timer"

    def run(self):
        print(Fore.RED + "Helena: SPACE = play/pause")
        print("Helena: R = reset")
        print("Helena: Q = quit")
        while True:
            time = input(Fore.RED + "Helena: How long for: ")
            if time.isdigit():
                time = int(time)
                if time > 0:
                    command = "python -m termdown " + str(time)
                    system(command)
                    break
                else:
                    print(Fore.MAGENTA + "Helena: The timer must last at 1 second")
            else:
                print(Fore.MAGENTA + "Helena: Please enter a number!")


class Stopwatch(Action):
    def __init__(self):
        self.name = "Stopwatch"
        self.description = "Starts a stopwatch"
        self.command = "stopwatch"


    def run(self):
        print(Fore.RED + "Helena: SPACE = play/pause")
        print("Helena: L = lap")
        print("Helena: R = reset")
        print("Helena: Q = quit")
        print()
        command = "python -m termdown"
        system(command)


clock = Clock()
timer = Timer()
stopwatch = Stopwatch()


skill.add_action(clock)
skill.add_action(timer)
skill.add_action(stopwatch)
