class Entity:
    def __init__(self, name, surf, rect):
        self.name = name
        self.surf = surf
        self.rect = rect

    def move(self):
        pass  # Método abstrato
