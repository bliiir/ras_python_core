# class Character():

# class Protagonist(Character):

# class Antagonist(Character):

import random
import time

###############
### Classes ###
###############

# Trolls, goblins, werewolves, orcs, vampire

class Character(object):

    def __init__(self, name):
        self.name = name
        self.level = random.randint(50,100)
        self.life = random.randint(50,100)
        self.kills = 0

    def __str__(self):
        return(f"{self.name}, lvl: {self.level}")

    # Tracks how many kills the hero has done
    def kills(self):
        self.kills +=1
        return(self.kills)

    # Removes lifepoints equivalent to damage from character
    def take_damage(self, damage):
        self.life -= damage
        return(self.life)

    # Random damage generator
    def do_damage(self, opponent):
        damage_done = random.randint(1,20) + self.level/5
        return(damage_done)

    # Levels hero up or down
    def set_level(self, direction):
        if direction == 1:
            self.level += 1
        if direction == 0:
            self.level -= 1


    def status(self, opponent):
        print("Name:", self.name, "level:", self.level, "life:", self.life)
        print("Name:", opponent.name, "level:", opponent.level, "life:", opponent.life)
        print("\n")


#################
### Functions ###
#################

# Create the protagonist
class hero(Character):
    def make(name):
        hero = Character(name)
    return(hero)




# Create the antagonists
class enemy(Character):

    # List of names to use for opponents
    names = ["Caitlin Comeau", "France Frakes", "Kimber Kellison", "Mila Mirelez", "Mindy Marcellus", "Jacklyn Josephs", "Jacquline Jury", "Leonie Laguardia", "Kortney Knobel", "Lauren Larkin", "Carlene Chace", "Alycia Alan", "Myrle Marks", "Alva Avalos", "Melisa Martinson", "Hugo Hellen", "Diann Dicarlo", "Aurea Allain", "Rudy Rohloff", "Douglass Duggan"]

    # names = ["Caitlin Comeau", "France Frakes"]

    # Make enemies (!)
    print("Summoning enemies...\n")
    enemies = []
    for name in names:
        enemy = Character(name)
        enemies.append(enemy)

    # Inject suspense
    time.sleep(0.1)

    # List enemies
    # print("Visions of an army of foes roll before your eyes: \n")
    # for each in enemies:
    #     print("Enemy name: {:20s} Level: {:5d} Life: {:5d}".format(each.name, each.level, each.life))
    #     time.sleep(0.01)

    return(enemies)




# Fight to the death. Remove enemy from the enemies list if hero wins. End the game if the hero loses
def fight(hero, enemy, enemies):

    old_life = hero.life

    while True:

        cs()

        hero.status(enemy)

        # Hero's turn
        damage_done_hero = int(hero.do_damage(enemy))
        enemy.take_damage(damage_done_hero)
        print(hero.name, "deals", damage_done_hero, "to ", enemy.name)

        # Enemy vanquished
        if enemy.life <= 0:

            # Update hero attributes
            hero.level += 1
            hero.kills += 1
            hero.life = old_life + 5

            # Notify the user
            print("\nPraise the gods!", enemy.name, "died in agony by your sword, oh lord!\nOur lord,", hero.name, "has vanquished", hero.kills, "enemies, and has levelled up to", hero.level, "\n")

            # Remove the killed enemy
            try:
                enemies.remove(enemy)
            except:
                print("All enemies have been vanquished - you are victorious")
                exit()
            break

        #
        else:
            print(enemy.name, "has", enemy.life, "left\n")

        # Enemy's turn ()
        damage_done_enemy = int(enemy.do_damage(hero)/10*8) # Give the hero a little edge
        life_left_hero = hero.take_damage(damage_done_enemy)
        print(enemy.name, "deals", damage_done_enemy, "damage to", hero.name)

        # Hero vanquished
        if hero.life <=0:
            print("Oh, no", hero.name, "has died")
            print("Ending game...")
            time.sleep(1)
            exit()

        # Hero hurt
        else:
            print(hero.name, "has", hero.life, "life left\n")

        time.sleep(2)

        # Status
    hero.status(enemy)

def move():
    angle = random.randint(0,46)
    steps = random.randint(0,100)
    direction = random.choice(["North", "East", "West", "South"])
    return(angle, steps, direction)

def cs():
    print(chr(27) + "[2J")

def main():
    print("Welcome to the game - please execute cli_rpg_main.py rather than this file")

# Execute if this file is used directly rather than as an import
if __name__ == "__main__":
    main()
