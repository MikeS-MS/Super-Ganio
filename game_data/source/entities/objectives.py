from game_data.source.collisions.customcollisions import ObjectiveBox
from game_data.engine.item import Item
from game_data.engine.base.entity import Entity


class Rose(Entity):
    def __init__(self, hp, x, y, level_instance, images: dict):
        super().__init__(hp, x, y, level_instance, images, images['idle'], 0)
        self.enable_gravity = False
        self.can_jump = False
        self.items.append(Item('rose'))
        self.collision = ObjectiveBox(self, self.current_image.get_rect(topleft=(self.x, self.y)))
        self.level_instance.collisions.append(self.collision)
