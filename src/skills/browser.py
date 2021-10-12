from skills.skill import Skill
from skills.action import Action
from colorama import Fore
import webbrowser
from time import sleep


skill = Skill("Browser", "Actions relating to web browsers (not web scraping)")


class Website(Action):
    def __init__(self):
        self.name = "Website"
        self.description = "Open the specified website in a web browser"
        self.command = "website"


    def run(self):
        print(Fore.RED + "Helena: Enter a URL:")
        url = input(Fore.WHITE + "==> ")
        if "https://" not in url:
            url = "https://" + url

        webbrowser.open_new_tab(url)

        sleep(2)


website = Website()


skill.add_action(website)
