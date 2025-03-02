class Hero:
    difend = False
    HEALTH = 60
    LEVEL_UP = 30
    MIN_COINS = 1.75

    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0

    def heal(self):
        self.hp = self.hp * self.HEALTH / 100
        return self.hp

    def levelup(self):
        if self.coins < self.MIN_COINS * self.level:
            return "Not enough coins"
        else:
            self.level += int(self.level * self.LEVEL_UP / 100)
            self.damage += int(self.damage * self.LEVEL_UP / 100)
            self.hp = 10

    def attack(self, monster):
        monster.reduce_health(self)
        if monster.hp == 0:
            self.coins += monster.level
            return f"Monster defeated! You have {self.coins} coins"

    def defend(self):
        self.defend = True

    def reduce_health(self, monster):

        if self.defend:
            self.hp -= monster.damage * 0.2
            self.defend = False
            print("You defended the attack your hp is now: ", self.hp)
        else:
            self.hp -= monster.damage
            print("You didn't defend the attack your hp is now: ", self.hp)
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def increase_coins(self, coins):
        self.coins += coins
        print(f"You have {self.coins} coins")
