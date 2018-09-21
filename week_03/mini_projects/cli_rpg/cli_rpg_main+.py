import cli_rpg_base+ as base
import time, random

def main():
    setup()
    play(my_hero, enemies)

    time.sleep(2)
    base.cs()


def setup():
    # Instanciate a new hero
    my_hero = hero(input("Halt! Who stands before me? "))
    print("Behold...", my_hero.name, "a level", my_hero.level, "warrior with", my_hero.life, "life arises!!\n"

    my_enemies = base.make_enemies()



def play(hero, enemies):

    # Clear the screen
    base.cs()

    print("After long travels, you have finally arrived at the fabled caverns of Chu'k'ooo. A magnificent portal opens before you and you enter the caverns\n\n")

    time.sleep(1)

    while True:

        # Clear the screen
        base.cs()

        # Move the player
        move = base.move()
        print("You move", move[1], "steps,", move[0], "degrees towards the", move[2], "\n")
        time.sleep(1)

        # Present player with new enemy
        try:
            enemy = random.choice(enemies)
        except:
            print("All enemies have been vanquished - you are victorious")
            exit()
            exit()

        print("Before you stands", enemy.name, "- a formidable level", enemy.level, "warrior with", enemy.life, "lifepoints\n\n" )
        print("\"Halt! - Thou shall not pass!!\"", enemy.name, "exclaims - \"at least not without a fight!\"\n")
        print("Do you chose to fight[y/n]", enemy.name, "?", end="")

        # Ask the user if they want to fight the enemy
        while True:
            battle = input()
            if battle == "y":
                print("Oh, bravest of the brave - may the goddess of war be with you!n\n")
                fight = base.fight(hero, enemy, enemies)
                break
            elif battle == "n":
                print("Before: Level", hero.level, "life", hero.life)
                hero.set_level(0)
                print("You flee the battle. This shameful act torments you and you feel your spirit suffer")
                print("After: Level", hero.level, "life", hero.life, "\n")
                break
            else:
                print("input error - try again")
                continue




if __name__ == "__main__":
    main()
