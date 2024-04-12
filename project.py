import random
from pyfiglet import Figlet
import sys
from time import sleep
from datetime import date
import csv
from tabulate import tabulate



class Player:
    def __init__(self, vocation, name, level=1, alive=True):
        self.hit_points = 0
        self.max_hit_points = 0
        self.weapon = ""
        self.skills = {}
        self.damage = 0
        self.attack_roll = 0
        self.armor_class = 0
        self.potions = 0

        self.vocation = vocation
        self.set_weapon()
        self.name = name
        self.level = level
        self.alive = alive


    @property
    def vocation(self):
        return self._vocation

    @vocation.setter
    def vocation(self, vocation):
        if vocation not in ("Mage", "Rogue", "Warrior"):
            raise ValueError("Class does not exist.")
        else:
            self._vocation = vocation


    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level not in (1, 2, 3):
            raise ValueError("Level does not exist")
        else:
            self._level = level
            self.set_max_hit_points()
            self.set_damage()
            self.set_attack_roll()
            self.set_armor_class()
            self.set_potions()
            self.set_skills()


    @property
    def hit_points(self):
        return self._hit_points


    @hit_points.setter
    def hit_points(self, hit_points):
        if hit_points <= 0:
            self._hit_points = 0
            self.alive = False
        elif hit_points >= self.max_hit_points:
            self._hit_points = self.max_hit_points
        else:
            self._hit_points = hit_points


    @property
    def max_hit_points(self):
        return self._max_hit_points


    @max_hit_points.setter
    def max_hit_points(self, max_hit_points):
        self._max_hit_points = max_hit_points


    def level_up(self):
        self.level += 1
        print(f"🪄  \033[1:32:40mYou have leveled up! Now at level {self.level}!\033[m")
        print(f"❤️  Max hit points now at {self.max_hit_points}!")
        print(f"🛡️  Armor class now at {self.armor_class} points!")
        print(f"🗡️  Damage now at {self.damage} points!")
        print(f"🎯 Bonus attack roll now at {self.attack_roll} points!")



    def set_max_hit_points(self):
        if self.vocation == "Warrior":
            self.max_hit_points = (10 * self.level)
        elif self.vocation == "Rogue":
            self.max_hit_points = (9 * self.level)
        elif self.vocation == "Mage":
            self.max_hit_points = (8 * self.level)
        self.hit_points = self.max_hit_points


    def set_weapon(self):
        if self.vocation == "Warrior":
            self.weapon = "Sword"
        elif self.vocation == "Rogue":
            self.weapon = "Dagger"
        elif self.vocation == "Mage":
            self.weapon = "Staff"


    def set_skills(self):
        if self.vocation == "Warrior":
            self.skills.update({"Block": 3 + self.level})
        elif self.vocation == "Rogue":
            self.skills.update({"Poison": 5 + self.level})
        elif self.vocation == "Mage":
            self.skills.update({"Firestaff": 7 + self.level, "Heal": 7 + self.level})


    def set_damage(self):
        weapons = {"Sword": 5, "Dagger": 5, "Staff": 4}
        self.damage = weapons[self.weapon] + self.level


    def set_potions(self):
        self.potions = 3


    def use_potion(self):
        if self.potions > 0:
            self.hit_points += 6
            self.potions -= 1
            print(f"🥛 Used potion, now there are only {self.potions} potions left.")
        else:
            print("No more potions!")


    def set_armor_class(self):
        armor_classes = {"Mage": 10, "Rogue": 11, "Warrior": 12}
        self.armor_class = armor_classes[self.vocation] + self.level


    def set_attack_roll(self):
        attack_rolls = {"Sword": 3, "Dagger": 3, "Staff": 3}
        self.attack_roll = attack_rolls[self.weapon] + self.level



class Enemy():
    def __init__(self, vocation, level=1, alive=True):
        self.hit_points = 0
        self.max_hit_points = 0
        self.weapon = ""
        self.skills = {}
        self.damage = 0
        self.attack_roll = 0
        self.armor_class = 0

        self.vocation = vocation
        self.set_weapon()
        self.level = level
        self.alive = alive


        self.set_skills()


    @property
    def vocation(self):
        return self._vocation

    @vocation.setter
    def vocation(self, vocation):
        if vocation not in ("Witch", "Brigand", "Brute"):
            raise ValueError("Class does not exist.")
        else:
            self._vocation = vocation


    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level not in (1, 2, 3):
            raise ValueError("Level does not exist")
        else:
            self._level = level
            self.set_max_hit_points()
            self.set_damage()
            self.set_attack_roll()
            self.set_armor_class()


    @property
    def hit_points(self):
        return self._hit_points


    @hit_points.setter
    def hit_points(self, hit_points):
        if hit_points <= 0:
            self._hit_points = 0
            self.alive = False
        elif hit_points >= self.max_hit_points:
            self._hit_points = self.max_hit_points
        else:
            self._hit_points = hit_points


    @property
    def max_hit_points(self):
        return self._max_hit_points

    @max_hit_points.setter
    def max_hit_points(self, max_hit_points):
        self._max_hit_points = max_hit_points


    def set_max_hit_points(self):
        if self.vocation == "Brute":
            self.max_hit_points = (10 * self.level)
        elif self.vocation == "Brigand":
            self.max_hit_points = (8 * self.level)
        elif self.vocation == "Witch":
            self.max_hit_points = (6 * self.level)
        self.hit_points = self.max_hit_points


    def set_skills(self):
        if self.vocation == "Brute":
            self.skills = {"Block": 1}
        elif self.vocation == "Brigand":
            self.skills = {"Poison": 1}
        elif self.vocation == "Witch":
            self.skills = {"Firestaff": 2, "Heal": 2}


    def set_weapon(self):
        if self.vocation == "Brute":
            self.weapon = "Sword"
        elif self.vocation == "Brigand":
            self.weapon = "Dagger"
        elif self.vocation == "Witch":
            self.weapon = "Staff"


    def set_damage(self):
        weapons = {"Sword": 3, "Dagger": 2, "Staff": 1}
        self.damage = weapons[self.weapon] + self.level


    def set_armor_class(self):
        armor_classes = {"Witch": 8, "Brigand": 9, "Brute": 10}
        self.armor_class = armor_classes[self.vocation] + self.level


    def set_attack_roll(self):
        attack_rolls = {"Sword": 2, "Dagger": 2, "Staff": 1}
        self.attack_roll = attack_rolls[self.weapon] + self.level




def main():
    menu_choice()
    start_game()
    player = character_creation()
    start_first_encounter(player)
    turn_first = combat_encounter(player, 2, 0, 0)
    player.level_up()
    start_second_encounter(player)
    turn_second = combat_encounter(player, 2, 2, 0)
    player.level_up()
    start_third_encounter(player)
    turn_third = combat_encounter(player, 3, 2, 1, boss=2)
    ending(player)
    total_turn = turn_first + turn_second + turn_third
    row = create_row_leaderboard(player.name, player.vocation, total_turn)
    update_leaderboard(row)
    text_renderer("Thanks for playing")



def text_renderer(text):
    figlet = Figlet()
    figlet.setFont(font="standard")
    print(figlet.renderText(text))

def menu_choice():
    MENU = ["👍 [0] - Play", "✋ [1] - Help", "📋 [2] - Leaderboard","👋 [3] - Exit"]
    text_renderer("Age of Bandits")
    while True:
        print(f"\033[1mMENU:\033[m")
        for option in MENU:
            print(option)
        print("Choose between 0, 1, 2 or 3.")
        print()
        try:
            choice = int(input("\033[4mWhat do you want to do?\033[m ").strip())
        except (UnboundLocalError, ValueError):
            print()
            pass
        else:
            print()
            if choice in (0, 1, 2, 3):
                if choice == 3:
                    sys.exit(text_renderer("Thank you for playing!"))
                elif choice == 2:
                    read_leaderboard()
                    print()
                elif choice == 1:
                    print("This is an adventure game, with light RPG elements.")
                    print("The goal of the game is for the player to beat the three combat encounters, each getting progressively harder.")
                    sleep(1)
                    print("The player can choose between three vocations: Mage, Rogue and Warrior.")
                    print("Each vocation has its own weapons, hit points and abilities which can be used.")
                    sleep(1)
                    print("Each turn, the player can perform an action and a bonus action, while enemies can only perform actions.")
                    print("Actions are reserved for attacks or skill usage and bonus actions are used for drinking potions to replenish Hit Points.")
                    sleep(1)
                    print("Attacks have a chance to hit based on a random number between 1 and 20 plus the bonus attack roll of the player's character, minus the enemy's armor class.")
                    print("If the sum of the random number and the bonus attack roll is greater than the enemy's armor class, the attack hits and deals damage.")
                    sleep(1)
                    print("All player properties (HP, weapon damage etc.) can be viewed during combat.")
                    sleep(1)
                    print("At the end of the first two combat encounters, the player will level up, granting them more damage and HP.")
                    sleep(1)
                    print("Now that you are ready, set forth on your journey!")
                    print()
                elif choice == 0:
                    break



def start_game():
    print("The world has seen troubling days... bandits roam the countryside and rob and kill anyone in sight!")
    sleep(2)
    print("You have been tasked with clearing a local fort of bandits, using whatever means necessary.")
    sleep(2)
    print("But first, you must create your character.")
    sleep(1)
    print()


def validate_vocation(vocation):
    return vocation in ("Mage", "m", "M", "Rogue", "r", "R", "Warrior", "w", "W")


def validate_name(name):
    return name.isalpha()


def character_creation():
    while True:
        vocation = input("\033[4mWhat's your vocation? [Mage, Rogue, Warrior]\033[m ").strip().capitalize()
        if validate_vocation(vocation):
            break
        print("Invalid vocation.")
    while True:
        name = input("\033[4mWhat's your name?\033[m ").strip()
        if validate_name(name):
            break
    return Player(vocation, name)


def start_first_encounter(player):
    print()
    print("You arrive at the fort as the night falls. It's a crumbling mess and crawling with cutthroats.")
    sleep(2)
    print("At the gate, there are two guards, both of them lightly armored brigands.")
    sleep(2)
    print("You know that this task is going to be difficult. But you prepare yourself and go ahead.")
    sleep(2)
    if player.vocation == "Mage":
        print("You hurl a spell at the unsuspecting bandits, but it doesn't hit them.")
    elif player.vocation == "Rogue":
        print("You try to sneak past the bandits, but they are able to notice you.")
    elif player.vocation == "Warrior":
        print("You charge at the bandits, but they are well ready to deal with a single attacker.")
    sleep(2)
    print("The fight begins.")
    sleep(3)


def combat_encounter(player, brigands_input=0, witches_input=0, brutes_input=0, boss=1):
    options = ["🗡️  [0] - Attack", "❇️  [1] - Use skill", "🥛 [2] - Use potion", "❌ [3] - Skip turn"]
    enemies = []
    enemies_choice = {}
    for e1 in range(brigands_input):
        enemies.append(Enemy("Brigand"))
    for e2 in range(witches_input):
        enemies.append(Enemy("Witch"))
    for e3 in range(brutes_input):
        enemies.append(Enemy("Brute", level=boss))
    for enemy in range(len(enemies)):
        enemies_choice.update({enemy: 0})
    turn = 0
    while True:
        action = True
        bonus_action = True
        turn += 1
        sleep(2)
        print()
        print(f"⚔️  \033[1mTurn {turn}!\033[m")
        print()
        print(f"🫡  \033[1mYour turn!\033[m")
        print()
        while True:
            sleep(2)
            print(f"There are {len([enemy for enemy in enemies if enemy.alive])} enemies still in the fight.")
            for enemy in range(len(enemies)):
                if enemies[enemy].alive:
                    print(f"😡 {enemies[enemy].vocation} [{enemy}] - has {enemies[enemy].hit_points} hit points.")

            print()
            sleep(1)
            print(f"\033[1mRESOURCES:\033[m")
            print(f"{'🟩' if action == True else '🟥'} Action = {str(action)}.")
            print(f"{'🟢' if bonus_action == True else '🔴'} Bonus Action = {str(bonus_action)}.")
            print(f"❤️  You have {player.hit_points} hit points.")
            print(f"🛡️  Your armor class is at {player.armor_class} points.")
            print(f"🗡️  You deal {player.damage} points of damage per hit.")
            print(f"🎯 You have {player.attack_roll} points of hit bonus.")
            print(f"🥛 You have {player.potions} potions left.")
            print()
            print(f"\033[1mOPTIONS:\033[m")
            for option in options:
                print(option)
            print()
            while True:
                try:
                    choice = int(input("\033[4mWhat do you wish to do?\033[m ").strip())
                except (UnboundLocalError, ValueError):
                    pass
                else:
                    if choice in (0, 1) and action == False:
                        print("Not enough actions.")
                    elif choice == 2 and bonus_action == False:
                        print("Not enough bonus actions.")
                    elif choice == 2 and player.potions <= 0:
                        print("Not enough potions.")
                    elif choice == 3:
                        break
                    else:
                        break
            print()
            if choice == 0:
                action = False
                while True:
                    for enemy in range(len(enemies)):
                        if enemies[enemy].alive:
                            print(f"😡 {enemies[enemy].vocation} [{enemy}]")
                    print()
                    try:
                        attack_choice = int(input("\033[4mWho do you wish to attack?\033[m ").strip())
                    except (UnboundLocalError, ValueError):
                        pass
                    else:
                        if 0 <= int(attack_choice) <= (int(len(enemies)) - 1):
                            if enemies[attack_choice].alive:
                                print()
                                break
                            else:
                                print(f"{enemies[attack_choice].vocation} [{attack_choice}] is already dead.")
                        else:
                            print(f"[{attack_choice}] is not a valid enemy.")
                hit = attack_hit(player.attack_roll, 20, enemies[attack_choice].armor_class)
                hit_total = hit['die rolled'] + player.attack_roll
                sleep(1)
                print(f"🎲 Player die rolled (d20) = {hit['die rolled']}.")
                print(f"🎯 Player attack bonus = {player.attack_roll}.")
                print(f"🛡️  Enemy armor class = {enemies[attack_choice].armor_class}.")
                sleep(2)
                print()
                print(f"🎲 {hit['die rolled']} + {player.attack_roll} = {hit_total}")
                sleep(1)
                print()
                if hit["hit"]:
                    enemies[attack_choice].hit_points -= player.damage
                    print(f"🎲 {hit_total} (hit total) >= {enemies[attack_choice].armor_class} (armor class)")
                    print()
                    sleep(1)
                    print(f"🎯 Hit for {player.damage} points of damage!")
                    print(f"🖤 {enemies[attack_choice].vocation} [{attack_choice}] now has {enemies[attack_choice].hit_points} hit points.")
                    if enemies[attack_choice].alive == False:
                        print(f"☠️  {enemies[attack_choice].vocation} [{attack_choice}] has died!")
                else:
                    print(f"🎲 {hit_total} (hit total) < {enemies[attack_choice].armor_class} (armor class)")
                    print()
                    sleep(1)
                    print(f"🌀 Attack missed!")
                player.set_damage() # Reset player damage
                sleep(1)
                print()
            elif choice == 1:
                action = False
                while True:
                    j = 0
                    for skill in player.skills:
                        if skill == "Block":
                            print(f"🛡️  [{j}] - {skill}: increases armor class by {player.skills[skill]} points.")
                        elif skill == "Poison":
                            print(f"✴️  [{j}] - {skill}: deals an additional {player.skills[skill]} points of damage on next turn.")
                        elif skill == "Firestaff":
                            print(f"✴️  [{j}] - {skill}: deals an additional {player.skills[skill]} points of damage on next turn.")
                        elif skill == "Heal":
                            print(f"✳️  [{j}] - {skill}: heals self for {player.skills[skill]} points.")
                        j += 1
                    print()
                    try:
                        skill_choice = int(input("\033[4mWhat skill do you wish to use?\033[m ").strip())
                    except (UnboundLocalError, ValueError):
                        print()
                        pass
                    else:
                        print()
                        if 0 <= int(skill_choice) <= (int(len(player.skills)) - 1):
                            break
                skills_list = []
                for key in player.skills.keys():
                    skills_list.append(key)
                skill_choice_key = skills_list[skill_choice]
                sleep(1)
                if skill_choice_key == "Block":
                    player.armor_class += player.skills[skill_choice_key]
                    print(f"🛡️  Used {skill_choice_key}! Armor class now at {player.armor_class} until next turn.")
                elif skill_choice_key == "Heal":
                    player.hit_points += player.skills[skill_choice_key]
                    print(f"✳️  Used {skill_choice_key}! Hit points now at {player.hit_points}.")
                else:
                    player.damage += player.skills[skill_choice_key]
                    print(f"✴️  Used {skill_choice_key}! Damage now at {player.damage} until the end of the next turn.")
                sleep(1)
                print()
            elif choice == 2:
                bonus_action = False
                player.use_potion()
                sleep(1)
                print(f"❤️  Player now has {player.hit_points} hit points!")
                print()

            if choice == 3 or (action == False and bonus_action == False):
                for enemy in enemies:
                    if enemy.alive:
                        enemy.set_armor_class() # Reset armor class enemy
                break


        if not [enemy for enemy in enemies if enemy.alive]:
            print("The enemies lie defeated.")
            sleep(1)
            print()
            print("🎉 \033[1mCombat ended!\033[m")
            print()
            break
        else:
            print("😡 \033[1mEnemy Turn!\033[m")
            sleep(1)


        for enemy in range(len(enemies)):
            if enemies[enemy].alive:
                print()
                print(f"😡 \033[1m{enemies[enemy].vocation} [{enemy}]'s turn!\033[m")
                sleep(1)
                print()
                if enemies_choice[enemy] == 1:
                    enemy_choice = 0
                else:
                    enemy_choice = random.choice([0, 1])
                enemies_choice.update({enemy: enemy_choice})
                if enemy_choice == 0:
                    print(f"🗡️  {enemies[enemy].vocation} [{enemy}] attempts to attack you.")
                    print()
                    enemy_hit = attack_hit(enemies[enemy].attack_roll, 20, player.armor_class)
                    enemy_hit_total = enemy_hit['die rolled'] + enemies[enemy].attack_roll
                    sleep(1)
                    print(f"🎲 Enemy die rolled (d20) = {enemy_hit['die rolled']}.")
                    print(f"🎯 Enemy attack bonus = {enemies[enemy].attack_roll}.")
                    print(f"🛡️  Player armor class = {player.armor_class}.")
                    sleep(2)
                    print()
                    print(f"🎲 {enemy_hit['die rolled']} + {enemies[enemy].attack_roll} = {enemy_hit_total}")
                    sleep(1)
                    print()
                    if enemy_hit["hit"]:
                        player.hit_points -= enemies[enemy].damage
                        print(f"🎲 {enemy_hit_total} (hit total) >= {player.armor_class} (armor class)")
                        print()
                        sleep(1)
                        print(f"🎯 Hit for {enemies[enemy].damage} points of damage!")
                        print(f"❤️  You now have {player.hit_points} hit points.")
                    else:
                        print(f"🎲 {enemy_hit_total} (hit total) < {player.armor_class} (armor class)")
                        print()
                        sleep(1)
                        print("🌀 Attack missed!")
                    enemies[enemy].set_damage() # Reset enemy damage
                elif enemy_choice == 1:
                    while True:
                        enemy_skill_choice = random.choice(range(len(enemies[enemy].skills)))
                        if (enemy_skill_choice == 1 and enemies[enemy].hit_points < enemies[enemy].max_hit_points) or enemy_skill_choice == 0:
                            break
                    enemy_skills_list = []
                    for key in enemies[enemy].skills.keys():
                        enemy_skills_list.append(key)
                    enemy_skill_choice_key = enemy_skills_list[enemy_skill_choice]
                    if enemy_skill_choice_key == "Block":
                        enemies[enemy].armor_class += enemies[enemy].skills[enemy_skill_choice_key]
                        print(f"🛡️  Used {enemy_skill_choice_key}! Armor class now at {enemies[enemy].armor_class} until next turn.")
                    elif enemy_skill_choice_key == "Heal":
                        enemies[enemy].hit_points += enemies[enemy].skills[enemy_skill_choice_key]
                        print(f"✳️  Used {enemy_skill_choice_key}! Hit points now at {enemies[enemy].hit_points}.")
                    else:
                        enemies[enemy].damage += enemies[enemy].skills[enemy_skill_choice_key]
                        print(f"✴️  Used {enemy_skill_choice_key}! Damage now at {enemies[enemy].damage} until the end of the next turn.")
                sleep(1)
                if player.alive == False:
                    print("💀 \033[1:31:40mHit points reached 0!\033[m")
                    text_renderer("Game Over")
                    sys.exit()
        player.set_armor_class() # Reset player armor class
    return turn


def attack_hit(attack, die, defense):
    die_rolled = random.randint(1, die)
    return {"hit": (attack + die_rolled) >= defense, "die rolled": die_rolled}

def start_second_encounter(player):
    print()
    print("You walk through the corpses of your recently fallen foes. You feel more experienced after that battle.")
    sleep(2)
    print("Entering the fort, you notice that there are two witches rushing at you, spells at the ready.")
    sleep(2)
    print("Behind you, two brigands sneak up to you and prepare to attack.")
    sleep(2)
    if player.vocation == "Mage":
        print("'Face me as honorable foes, one at a time!' you say, knowing it will not happen.")
    elif player.vocation == "Rogue":
        print("'You guys are good! I honestly didn't notice you creeping up like that.' you shout, smirking.")
    elif player.vocation == "Warrior":
        print("'Four of you? Good.' you say, resolute and unwavering.")
    sleep(2)
    print("The fight begins.")
    sleep(3)

def start_third_encounter(player):
    print()
    print("You feel extremely tired after the last confrontation. Four enemies felled is no easy task.")
    sleep(2)
    print("Finally, as you approach the main keep, you hear six different voices singing and shouting from the inside.")
    sleep(2)
    print("This is it. Your last challenge. 'Am I up for it?' you wonder.")
    sleep(2)
    print("It doesn't matter. You must push through. And that's exactly what you decide to do.")
    sleep(2)
    if player.vocation == "Mage":
        print("You blast open the keep doors and, through the smoke you see your enemies.")
    elif player.vocation == "Rogue":
        print("You pick the door's lock and sneak inside, noticing your enemies.")
    elif player.vocation == "Warrior":
        print("You kick down the doors and charge at your enemies.")
    sleep(2)
    print("There are three brigands, two witches and their brute leader - the largest man you've ever seen.")
    sleep(2)
    print("The brute notices you: 'Hah! Looks like we're about to have some fun, boys!'")
    sleep(2)
    print("The fight begins.")
    sleep(3)


def ending(player):
    print("As the last of your enemies are defeated, you collapse to the ground.")
    sleep(2)
    print("You feel accomplished for being able to complete this task. But also exhausted.")
    sleep(2)
    print("You're going to be OK. And so are the people in the lands around the fort, thanks to you.")
    if player.vocation == "Mage":
        print("You wonder what you'll do next: maybe finish your studies at university?")
    elif player.vocation == "Rogue":
        print("You wonder what you'll do next: maybe steal some noble's gold and give it to the people?")
    elif player.vocation == "Warrior":
        print("You wonder what you'll do next: maybe look for a mentor to hone your sword skills?")
    sleep(2)
    print("Whatever it is you do next, you deserve some rest...")
    sleep(3)
    print()


def create_row_leaderboard(player, vocation, turns):
    return {"Player": player, "Vocation": vocation, "Turns": turns, "Date": date.today()}


def update_leaderboard(row):
    with open("leaderboard.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["Player", "Vocation", "Turns", "Date"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(row)


def read_leaderboard():
    table = []
    leaderboard = []
    with open("leaderboard.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

    for row in sorted(table, key=lambda row: row["Turns"]):
        leaderboard.append(row)

    print(tabulate(leaderboard, headers="keys", tablefmt="grid", showindex=(i + 1 for i in range(len(leaderboard)))))


if __name__ == "__main__":
    main()
