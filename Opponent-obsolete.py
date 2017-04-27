import time

class Opponent(object):
	def __init__(self, name):
		self.name = name
		self.health = 10
		self.max_health = 10
		self.power = 10

	def take_damage(self, damage):
		self.health -= damage

	def is_alive(self):
		return self.health > 0

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

	def attack(self, hero):
		if not self.is_alive():
			return
		print "%s attacks %s" % (self.name, opponent.name)
		enemy.receive_damage(self.power)
		time.sleep(1.5)