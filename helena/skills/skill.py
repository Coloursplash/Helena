class Skill:
    def __init__(self, name: str, description: str):
        self.active = True
        self.name = name
        self.description = description
        self.actions = []


    def set_active(self, active: bool):
        self.active = active


    def add_action(self, action):
        self.actions.append(action)


    def remove_action(self, action):
        if action in self.actions:
            self.action.remove(action)
        else:
            print("ERROR: Action '" + action.name + "' not in actions of skill '" + self.name + "'")
