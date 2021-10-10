from skills.action import Action
from skills.skill import Skill
from colorama import Fore
import skills.skillsImporter as skillsImporter
import sys

# so that the version number can be accessed
sys.path.append("../")
import __main__


skill = Skill("Helena information", "Commands related to information about Helena")

class Skills(Action):
    def __init__(self):
        self.name = "Active skills"
        self.description = "Print all active skills"
        self.command = "skills"


    def run(self):
        print(Fore.RED + "Helena: Current active skills are:\n")
        for skill in skillsImporter.get_skills():
            print(Fore.BLUE + skill.name)
            print(Fore.CYAN + skill.description + "\n")


class Actions(Action):
    def __init__(self):
        self.name = "Active actions"
        self.description = "Print all active action"
        self.command = "actions"


    def run(self):
        print(Fore.RED + "Helena: Current active actions are:\n")
        helena = __main__.get_helena()
        for action in helena.actions:
            print(Fore.BLUE + action.name)
            print(Fore.CYAN + action.description)
            print(Fore.RED + action.command + "\n")


class Version(Action):
    def __init__(self):
        self.name = "Version"
        self.description = "Get the version number of Helena"
        self.command = "version"


    def run(self):
        helena = __main__.get_helena()
        print(Fore.RED + "Helena: I am version " + helena.VERSION + ".")


skills = Skills()
version = Version()
actions = Actions()


skill.add_action(skills)
skill.add_action(version)
skill.add_action(actions)
