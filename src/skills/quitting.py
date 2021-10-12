from skills.action import Action
from skills.skill import Skill
from colorama import Fore
import sys


skill = Skill("Quitting", "Commands to stop Helena")

def sys_quit():
    print(Fore.RED + "Helena: See you next time!")
    sys.exit()

class Quit(Action):
    def __init__(self):
        self.name = "Quit"
        self.description = "Stops Helena"
        self.command = "quit"


    def run(self):
        sys_quit()


class Exit(Action):
    def __init__(self):
        self.name = "Exit"
        self.description = "Stops Helena"
        self.command = "exit"


    def run(self):
        sys_quit()


quit = Quit()
exit = Exit()


skill.add_action(quit)
skill.add_action(exit)
