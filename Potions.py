class Potions(object):
    def take_potions(self, hero):
        while True:
            print "============================"
            print "Welcome to the potions room!"
            print "============================"
            print "What do you want to take?"
            print "1. Felix Felicis (power up!)"
            print "2. Pepper Up Potion (to your health!)"
            print "X. Nothing, return to duel"
            user_input = raw_input("> ")
            if user_input == "1":
                hero.power += 5
                print "%s's power increased to %d." % (hero.name, hero.power)
            if user_input == "2":
                hero.health += 5
                print "%s's health increased to %d." % (hero.name, hero.health)
            if user_input == "X" or "x":
                break
            # else:
            #     break