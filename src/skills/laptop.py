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
        print(Fore.RED + "Helena: Current battery is at " + str(battery.percent) + "%")
        if battery.power_plugged:
            print(Fore.RED + "Helena: The battery is charging")
        else:
            print(Fore.RED + "Helena: The battery is discharging")
        print(Fore.RED + "Helena: The battery will last" + str(battery.secsleft))


battery = Battery()


skill.add_action(battery)
