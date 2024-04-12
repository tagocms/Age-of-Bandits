# Age of Bandits: A text-based role-playing game
#### Video Demo:  <URL HERE>
#### Description:

##### Overview:

This project is a text-based role-playing game - played exclusively on the terminal -, based on the popular Dungeons & Dragons tabletop games. It functions in a pretty simple manner: the user creates a character with its own vocation and abilities and faces three combat encounters against different types of bandits to liberate a fort. 

##### Functionality:

The first lines of code are designated for the creation of two classes: `Player` and `Enemy`. Both of these classes have a number of instance variables and properties, such as attack rolls, maximum hit points, damage, level etc. The only properties (with "getter" and "setter" functions) created were for the instance variables: vocation, level, hit_points and max_hit_points. This was done to ensure that these values had validations within the "setter" functions and prevent bugs in the code. One example is the hit_points "setter", which checks if the new value for the hit_points property is less than or equal to 0 or if the new value surpasses the max_hit_points property - both of which have their respective conditional actions in response.

The `main()` function calls all of the other functions used to create the game, beginning with a function that prints an "Age of Bandits" text using the `pyfiglet` module to the terminal. After that, it allows the user to choose between playing, accessing the tutorial, accessing the leaderboard or exiting the program. If the option to access the leaderboard is chosen, a table containing previous successful attempts at the game is shown, with columns for the name of the player character, their vocation, number of total combat turns and the date of the playing session, ordered by the number of combat turns in ascending order.

If the user chooses to start the game, the `main()` functions calls functions to start the game, create the player character (which is an object of the `Player` class) and start the combat encounters with enemies (which are objects of the `Enemy` class). The combat encounter work the same way: the function responsible for it receives the player object, number of each type of enemy and a final argument that defines one of the enemy vocations as a level 2 enemy as parameters. With this, a list containing all of the enemies with their respective vocations is created and used in the rest of the function. 

Then, the "game loop" starts, with the beginning of the first turn of combat, in which the player has the option to attack one of the enemies, use a skill, dring a potion or simply skip their turn. Both the attack and the skill actions utilize a loop to iterate over the list of enemies and the dictionary of skills (each instance variable "vocation" has different skills) and their abilities, printing them on the terminal, respectively. If the player chooses to attack, they have to choose the specific position of the enemy on the list, and the enemy's instance variable "alive" must be "True" for the attack to be executed - if the enemy is not alive or if the position (or even "string") inputted does not exist, there is an exception and "while loop" that will only break if the inputted value is valid. The same goes for the choice of skill.

When the player attacks an enemy, a function called `attack_hit()` is called to check if the attack hits or not. The arguments passed into the function are the player's "attack_roll" instance variable, the number of sides on the "virtual die" that going to be cast and the enemy's "armor_class" instance variable. Then, this function calls `random.randint(1, number of sides on the die)` to randomly choose a number bewteen 1 and the number of sides on the die (in this case, 20). If the sum of the player's attack roll and the result of the cast die are equal to or greater than the enemy's armor class, the attack hits and the enemy's "hit_points" instance variable is reduced by the same amount of the value of the player's "damage" instance variable. If the attack misses, nothing happens.

When the player uses a skill, they can have one of three effects, depending on their choice of skill (which are dependant on their vocation):
- Healing skill: replenishes the player's "hit_points" instance variable by a determined value, up to the player's "max_hit_points" instance variable;
- Block skill: increases the player's "armor_class" instance variable by a determined value, until the end of the next enemy turn;
- Damage skill (Poison or Firestaff): increases the player's "damage" instance variable by a determined value, which resets after their next attack.

After the player's turn, there is a check to see if every enemy in the enemies list has their "alive" instance variable set to "True". If it's "False", they will not perform any actions and cannot be targeted by the player on subsequent turns. If it's "True", they will perform actions, limited to attacking and using a skill, both of which work almost identically to when the player performs them, with the difference being that the objects are inverted (for example: the enemy's attack targets the player's armor class, not the other way around). 

For every enemy in the enemies list to perform an action, the list is iterated over in a "for loop", in which each enemy attacks or executes a skill on their turn - the choice between using a skill or attacking is based on the `random.choice()` function. Additionally, if the enemy has used a skill on their previous turn, then their choice is automatically set to attack. If the enemy is of the "Witch" vocation, there is another random choice of which skill to use ("Firestaff" or "Heal") - but, if the enemy's "hit_points" are equal to their "max_hit_points", the choice is automatically set to the "Firestaff" skill. 

If the player's "hit_points" instance variable is reduced to 0 or less during the enemy turn, a "Game Over" text using the `pyfiglet` module will be printed to the terminal and the program will exit via `sys.exit()`.

After the enemy turn, the "game loop" begins again, until all the enemies' "alive" instance variable are set to "False" or the player's "alive" instance variable is set to "False". 

After each combat encounter, there is a brief text printed to the terminal detailing the story and setting the scene for the next battle - also, the player's "level" instance variable is increased by 1, which increases some of their other attributes and properties, such as "hit_points", "damage" etc. The last battle also contains an enemy of the "Brute" vocation, whose "level" instance variable is set to 2. 

After the last combat encounter, the `leaderboard.csv` file is updated, using the `csv` library with the value of the total turns, between all combat encounters, it took for the game to be finished, along with the player object's name, vocation and the date in which the game was played. Also, a "Thanks for playing" text using the `pyfiglet` module is printed to the terminal, as the program finishes its execution.

##### Takeaways:
I learned a lot about Object-Oriented Programming (OOP) from the way I had to implement the `Player` and `Enemy` classes and their respective attributes, properties and methods. 

I also got better at using "loops" and catching exceptions, making the program cleaner and less vulnerable to unexpected inputs. 

Finally, I got into the habit of using functions more often, compartmentalizing my code so it's easier to test and fix. 

##### Libraries and packages:
For this project, the libraries in the **`requirements.txt`** file were used. 

They are:
- random,
- pyfiglet,
- sys,
- time,
- datetime,
- csv,
- tabulate,
- pytest.
