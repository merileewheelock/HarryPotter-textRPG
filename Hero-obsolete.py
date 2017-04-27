import time
import time

class Hero(object):
	def __init__(self, name = "Student"):
		self.name = name
		self.health = 20
		self.power = 5
		self.max_health = self.health

		#This class method returns a boolean. True if hero alive, False if hero dead.
	def is_alive(self):
		#return self.health > 0 (Another way to write the code below)
		if(self.health > 0):
			return True
		else:
			return False

	def attack(self, who_to_attack):
		who_to_attack.health -= self.power	#who_to_attack is effectively the_goblin

	def increase_health(self, amount):
		self.health += amount
		if self.health > self.max_health:
			self.health = self.max_health

	def print_status(self):
		print "%s has %d health and %d power." % (self.name, self.health, self.power)

	def receive_damage(self, points):
		self.health -= points
		print "%s received %d damage." % (self.name, points)
		if self.health <= 0:
			print "%s is defeated." % self.name

	def attack(self, opponent):
		if not self.is_alive():
			return
		print "%s attacks %s" % (self.name, opponent.name)
		enemy.receive_damage(self.power)
		time.sleep(1.5)

	def restore(self):
		self.health = 10
		print "Hero's heath is restored to %d!" % self.health
		time.sleep(1)