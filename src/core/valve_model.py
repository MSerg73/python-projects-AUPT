class Valve:
    def __init__(self, name):
        self.name = name
        self.opened = True

    def toggle(self):
        self.opened = not self.opened
