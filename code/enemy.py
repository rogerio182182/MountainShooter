from entity import Entity

class Enemy(Entity):
    def move(self):
        print(f"{self.name} (Enemy) se moveu.")
