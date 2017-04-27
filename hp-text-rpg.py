from Character import Character
from Character import Hero
from Character import Opponent
from Character import Dobby
from Potions import Potions
from random import randint

hero = Hero()
dobby = Dobby()
potions = Potions()

print "Welcome to Hogwarts Dueling Club!"
print "What is your name?"
hero.name = raw_input("> ")
print "How many duels will you complete today?"
num_of_duels = int(raw_input("> "))

avail_opponents = []
avail_opponents.append(Opponent())
avail_opponents.append(Opponent())

opponents = []
for i in range(0, num_of_duels):
	rand_num = randint(0, len(avail_opponents) - 1)
	opponents.append(avail_opponents[rand_num])
	# if (avail_opponents[rand_num] == Opponent()):
	# 	opponents.append(Opponent())

for opponent in opponents: 
	opponent.health = opponent.max_health
	if hero.alive():
		print "\n*****NEW DUEL!*****"
	while opponent.alive() and hero.alive():
		rand_bool = randint(0,1)
		print "\nYou have %s health and %s power." % (hero.health, hero.power)
		print "Your opponent has %s health and %s power.\n" % (opponent.health, opponent.power)
		print "%s, what is your next action?" % hero.name
		print "1. Expelliarmus"
		print "2. Stupify"
		print "3. Jelly-Legs Jinx"
		print "4. Slug-Vomiting Charm"
		print "5. Crucio!"
		print "6. Episkey!"
		print "7. Raid Potions Storeroom"
		print "8. Do nothing"
		print "X. Flee"
		user_input = raw_input("> ")
		if user_input == "1": #Expelliarmus
			hero.attack(opponent)
			if rand_bool == 1:
				print "You have disarmed your opponent!"
				opponent.health = 0
			else:
				print "You missed!"
		elif user_input == "2": #Stupify
			hero.attack(opponent)
			if rand_bool == 1:
				print "You have stupified your opponent!"
				opponent.health = 0
			else:
				print "You missed!"
		elif user_input == "3": #Jelly-Legs Jinx
			hero.attack(opponent)
			if rand_bool == 1:
				print "You have jinxed your opponent!"
				opponent.receive_damage(hero.power)
				# opponent.health -= 2
			else:
				print "You missed!"
		elif user_input == "4": #Slug-Vomiting Charm
			hero.attack(opponent)
			if rand_bool == 1:
				print "Your opponent is vomiting slugs!"
				opponent.receive_damage(hero.power)
				# opponent.health -= 2
			else:
				print "You missed!"
		elif user_input == "5": #Crucio
			print "You are expelled!"
			hero.health = 0
			break
		elif user_input == "6": #Episkey
			hero.health += 10
		elif user_input == "7": #Potions room
			potions.take_potions(hero)
		elif user_input == "8": #Do nothing
			pass
		elif user_input == "X" or user_input == "x":
			print "10 points from Gryffindor!"
			hero.health = 0
			break
		else:
			print "Invalid input %s" % user_input

		if user_input != "7":
			if opponent.health > 0:
				if rand_bool == 1:
					hero.health -= opponent.power
					print "The %s hits you for %d damage." % (opponent.name, opponent.power)
				else:
					print "The %s missed!" % opponent.name
				if hero.health <= 0:
					print "You have been defeated by the %s." % opponent.name

		if hero.health > 0 and hero.health < 5:
			dobby.help(hero)
			print "Dobby has helped increase your health to %d!" % hero.health