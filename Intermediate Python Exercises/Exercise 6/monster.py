import random
from colorama import init


class Monster:
    def __init__(self, name, levelHero):
        self.name = name
        self.level = random.randint(levelHero - 1, levelHero + 1)
        self.hp = self.level + 45
        self.damage = self.level + 2

    def reduce_health(self, hero):
        self.hp -= hero.damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
