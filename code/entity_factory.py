from player import Player
from enemy import Enemy
from background import Background

class EntityFactory:
    def get_entity(self, entity_type: str, name, surf, rect):
        if entity_type == "player":
            return Player(name, surf, rect)
        elif entity_type == "enemy":
            return Enemy(name, surf, rect)
        elif entity_type == "background":
            return Background(name, surf, rect)
        else:
            raise ValueError("Tipo de entidade inválido")
