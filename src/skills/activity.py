from skills.skill import Skill
from skills.action import Action
from colorama import Fore
import requests


skill = Skill("Activity", "Activity related actions to pass the time")


class Activity(Action):
    def __init__(self):
        self.name = "Activity"
        self.description = "Suggests a random activity"
        self.command = "activity"


    def run(self):
        req = requests.get("https://www.boredapi.com/api/activity")
        data = req.json()
        response = ""

        if data == "":
            print(Fore.MAGENTA + "Helena: Sorry, an error occured")
            return

        if (data.get('accessibility') < 0.4):
            response += "I can propose something interesting but it's not easy"
        elif (data.get('accessibility') < 0.6):
            response += "I have something easy for you"

        if (data.get('price') == 0):
            response += " and it's free."
        elif (data.get('price') <= 0.3):
            response += " and it's quite cheap."
        elif (data.get('price') > 0.3 and data.get('price') < 0.6):
            response += " and it cost a few."
        elif (data.get('price') >= 0.6):
            response += " but it's expensive."

        if (data.get('participants') > 1):
            response += " It's a group activity for " + str(data.get('participants')) + " people."

        response += "\n" + data.get('activity')
        print(Fore.BLUE + response)


activity = Activity()


skill.add_action(activity)
