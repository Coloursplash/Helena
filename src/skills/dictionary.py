from skills.skill import Skill
from skills.action import Action
from colorama import Fore
import nltk
from nltk.corpus import wordnet

nltk.data.path.append("data/nltk")

skill = Skill("Dictionary", "Dictionary definitions for any word")


class Dictionary(Action):
    def __init__(self):
        self.name = "Dictionary"
        self.description = "Definition, synonyms and antonyms for inputed word"
        self.command = "dictionary"#


    def run(self):
        print(Fore.RED + "Helena: Enter a word:")
        word = input(Fore.WHITE + "==> ")

        syns = wordnet.synsets(word)
        if len(syns) == 0:
            print(Fore.MAGENTA + "Helena: I don't recogonise that word.")
            return

        synonyms = set()
        antonyms = set()

        count = 0
        for meaning in syns:
            count += 1
            print(Fore.BLUE + "{:>3}. {}".format(count, meaning.definition()))

            for synonym in meaning.lemmas():
                if synonym.name() != word:
                    name = " ".join(synonym.name().split("_"))
                    synonyms.add(name)
                for antonym in synonym.antonyms():
                    name = " ".join(antonym.name().split("_"))
                    antonyms.add(name)

        print("\nSynonyms:\n" + ", ".join(synonyms))
        print("\nAntonyms:\n" + ",".join(antonyms))


dictionary = Dictionary()


skill.add_action(dictionary)
