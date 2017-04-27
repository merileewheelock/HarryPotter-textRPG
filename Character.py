from random import randint

class Character(object):
    def __init__(self):
        self.name = hero
        self.health = 10
        self.magical_knowledge = 4

    def alive(self):
        return self.health > 0

    def attack(self, opponent):
        if not self.alive():
            return

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is defeated." % self.name

    def print_status(self):
        print "%s has %d health and %d magical knowledge." % (self.name, self.health, self.magical_knowledge)

class Hero(Character):
    def __init__(self):
        # super(Hero, self).__init__()
        self.name = "hero"
        self.health = 10
        self.magical_knowledge = 4
        self.location = 15

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health

class Dobby(Character):
    def __init__(self):
        # super(Dobby, self).__init__()
        self.name = "Dobby"
        self.health = 5

    def help(self, who_to_help):
        who_to_help.health += self.health

class Opponent(Character):
    def __init__(self):
        # super(Opponent, self).__init__()
        self.name = "Opposing Student"
        self.health = randint(8,10)
        self.magical_knowledge = randint(3,6)
        self.max_health = 10
