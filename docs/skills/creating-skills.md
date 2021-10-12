# Creating new skills
Creating new skills for Helena is quick and easy.

## Skills overview

Creating new commands for Helena comes in two parts: skills and actions.
Skills have a name, description and list of actions attached to them. They basically easily categoriser actions.
Actions have a name, description, command and run function. When someone enters a command into Helena, if it corresponds with an action, the action's run function will be called. This is where you put all of the action's code, from looking up the weather to minigames.

## Example code

Here is the code for the greetings skill

```python
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
```

## Code breakdown

Here is a breakdown of how the code works.

```python
from skills.action import Action
from skills.skill import Skill
from colorama import Fore
```
We are importing the Action and Skill classes so that we can create our own. The Fore class from colorama is used to create coloured text in the terminal later on.

```python
skill = Skill("Greetings", "Greetings in different languages")
```
Here the skill class is created. The name and description are passed as arguments.

```python
class Hello(Action):
    def __init__(self):
        self.name = "Hello"
        self.description = "Replies 'hello'"
        self.command = "hello"


    def run(self):
        print(Fore.RED + "Helena: Hello!")
```
The Hello class has been created. It extends from the Action class so the name, description and command can be set easily. It also contains a run function, which simply prints a message. This can be replaced with more complex code to do pretty much anything. All actions will look like a variant of this code.

```python
hello = Hello()
bonjour = Bonjour()
salut = Salut()


skill.add_action(hello)
skill.add_action(bonjour)
skill.add_action(salut)
```
Here the Actions are created and then added to the skill. There is just one more thing that needs to be done before the skill can be used.

## Installing the skill

The skill file must be placed in the 'skills' directory. Then the file must be imported into the skillsImporter file and appended to the list of skills.
This, however, is clunky to do so may be changed in a future release.