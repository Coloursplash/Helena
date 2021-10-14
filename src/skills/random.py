from skills.skill import Skill
from skills.action import Action
from colorama import Fore
from random import choice


skill = Skill("Random", "Actions related to random numbers")


class SpinWheel(Action):
    def __init__(self):
        self.name = "Spin wheel"
        self.description = "Spin a wheel with elements on it"
        self.command = "spinwheel"


    def run(self):
        elements = []

        print(Fore.RED + "Helena: Enter elements on the wheel")
        print(Fore.RED + "Heena: Enter an empty line once done")
        while True:
            element = input(Fore.WHITE + "==> ")

            if element == "":
                break
            else:
                elements.append(element)

        print(Fore.BLUE + "Spinning the wheel...")

        print(Fore.CYAN + choice(elements))


class Dice(Action):
    def __init__(self):
        self.name = "Dice"
        self.description = "Roll a 6 sided die"
        self.command = "dice"


    def run(self):
        base   = '\n+-------+'
        blank  = '\n|       |'
        left   = '\n| *     |'
        middle = '\n|   *   |'
        right  = '\n|     * |'
        both   = '\n| *   * |'
        sides = [
                base + blank + middle + blank + base,
                base + left + blank + right + base,
                base + left + middle + right + base,
                base + both + blank + both + base,
                base + both + middle + both + base,
                base + both + both + both + base
        ]

        print(Fore.BLUE + "Rolling the die...")

        print(Fore.CYAN + choice(sides))


class CoinFlip(Action):
    def __init__(self):
        self.name = "Coin flip"
        self.description = "Flip a two sided coin"
        self.command = "coinflip"


    def run(self):
        sides = ["HEADS", "TAILS"]

        print(Fore.BLUE + "Flipping the coin..")

        print(Fore.CYAN + choice(sides))


spinWheel = SpinWheel()
dice = Dice()


skill.add_action(spinWheel)
skill.add_action(dice)
