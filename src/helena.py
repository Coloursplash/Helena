# -*- coding: utf-8 -*-
from colorama import Fore
import skills.skillsImporter as skillsImporter


class Helena():
    def __init__(self):
        self.VERSION = "0.1"
        self.skills = []
        self.actions = []

        print(Fore.CYAN + "Loading skills")
        self.skills = skillsImporter.get_skills()
        print(Fore.BLUE + str(len(self.skills)) + " skills loaded")
        print(Fore.CYAN + "Loading actions")
        for skill in self.skills:
            for action in skill.actions:
                self.actions.append(action)
        print(Fore.BLUE + str(len(self.actions)) + " actions loaded")
        print("Initialised!")


    def find_action(self, action_command: str):
        '''
        Find if the action passed is valid.
        '''
        output = []
        # if command matches the command for an action, run the action
        for action in self.actions:
            if action_command == action.command:
                output.append(action)

        return output


    def check_action(self, action_command):
        '''
        Putting this into a function so that it can be reused if voice commands are added in the future.
        '''
        actions = self.find_action(action_command)
        if len(actions) > 0:
            if len(actions) > 1:
                print(Fore.MAGENTA + "Helena: More than one action uses this command:")
                for i in range(len((actions))):
                    print(Fore.BLUE + str(i+1) + ": " + actions[i].name)
                    print(Fore.CYAN + actions[i].description)
                while True:
                    selectedAction = input(Fore.RED + "Helena: Choose a number: ")
                    if selectedAction.isdigit():
                        selectedAction = int(selectedAction)
                        if 1 <= selectedAction <= len(actions):
                            action = actions[selectedAction -1]
                            break
                        else:
                            print(Fore.MAGENTA + "Helena: The number must be in the list above!")
                    else:
                        print(Fore.MAGENTA + "Helena: Please enter a number!")
            else:
                action = actions[0]
            return action
        else:
            print(Fore.MAGENTA + "Helena: That isn't a command!")
            return None



    def cmd_loop(self):
        '''
        Loop while getting a user's input, check and convert to an action, then run the action.
        '''
        notQuit = True

        while notQuit:
            print(Fore.RED + "Helena: What can I do for you?")
            userInput = input(Fore.WHITE + "==> ")
            # check if userInput contains non-empty characters
            userInput = userInput.strip(" \t\n")
            if userInput != "":
                action = self.check_action(userInput)
                if action != None:
                    action.run()
            else:
                print(Fore.MAGENTA + "Helena: Please enter a command!")


    def execute_once(self, userInput):
        userInput = userInput.strip(" \t\n")
        if userInput != "":
            action = self.check_action(userInput)
            if action != None:
                action.run()
        else:
            print(Fore.MAGENTA + "Helena: This isn't a command!")
