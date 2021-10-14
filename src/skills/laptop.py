from skills.skill import Skill
from skills.action import Action
from psutil import sensors_battery
from colorama import Fore


skill = Skill("Laptop", "Actions to help laptop user")


class Battery(Action):
    def __init__(self):
        self.name = "Battery"
        self.description = "Check your laptop's battery"
        self.command = "battery"


    def run(self):
        battery = sensors_battery()
        print(Fore.BLUE + "Helena: Current battery is at " + str(battery.percent) + "%.")
        if battery.power_plugged:
            print(Fore.BLUE + "Helena: The battery is charging" + ".")
        else:
            print(Fore.BLUE + "Helena: The battery is discharging" + ".")

        minutes, seconds = divmod(battery.secsleft, 60)
        hours, minutes = divmod(minutes, 60)
        formatted_time = "%dhr %02dm %02ds" % (hours, minutes, seconds)
        
        print(Fore.BLUE + "Helena: The battery will last " + formatted_time + ".")


battery = Battery()


skill.add_action(battery)
