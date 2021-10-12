from skills.action import Action
from skills.skill import Skill
from colorama import Fore


skill = Skill("Greetings", "Greetings in different languages")


class Hello(Action):
    def __init__(self):
        self.name = "Hello"
        self.description = "Replies 'hello'"
        self.command = "hello"


    def run(self):
        print(Fore.RED + "Helena: Hello!")


class Bonjour(Action):
    def __init__(self):
        self.name = "Bonjour"
        self.description = "Replies 'bonjour'"
        self.command = "bonjour"


    def run(self):
        print(Fore.RED + "Helena: Bonjour!")


class Salut(Action):
    def __init__(self):
        self.name = "Salut"
        self.description = "Replies 'salut'"
        self.command = "salut"


    def run(self):
        print(Fore.RED + "Helena: Salut!")


hello = Hello()
bonjour = Bonjour()
salut = Salut()


skill.add_action(hello)
skill.add_action(bonjour)
skill.add_action(salut)
