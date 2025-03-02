from hero import Hero
from monster import Monster


def main():
    hero_obj = Hero("Hero")
    monster_obj = Monster("manst", hero_obj.level)
    while hero_obj.hp > 0:
        choose_action(hero_obj, monster_obj)
        print(
            f"Hero health: {hero_obj.hp} \n Monster health: {monster_obj.hp} \n Coins: {hero_obj.coins}"
        )
        if monster_obj.hp == 0:
            hero_obj.coins += monster_obj.level
            print(f"Monster defeated! You have {hero_obj.coins} coins")
            monster_obj = Monster("manst", hero_obj.level)

    print("Game over")


def choose_action(hero, monster):
    hero.coins += 1
    action = input(
        """Welcome to the game! 
        You are a hero and you have to defeat the monsters that are attacking the city. 
        enter 1 to attack the monster 
        2 to defend 
        3 to heal 
        4 to level up """
    )
    if action == "1":
        hero.attack(monster)
    elif action == "2":
        hero.defend()
    elif action == "3":
        hero.heal()
    elif action == "4":
        hero.levelup()


if __name__ == "__main__":
    main()
