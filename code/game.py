from level import Level

class Game:
    def __init__(self, window):
        self.window = window
        self.levels = []

    def run(self):
        for level in self.levels:
            level.run()
