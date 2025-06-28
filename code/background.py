from entity import Entity

class Background(Entity):
    def move(self):
        print(f"{self.name} (Background) se moveu.")
