class Potions(object):
    def take_potions(self, hero):
        while True:
            print "================================"
            print "You snuck into the potions room!"
            print "================================"
            print "What do you want to take?"
            print "1. Felix Felicis (power up!)"
            print "2. Pepper Up Potion (to your health!)"
            print "X. Nothing, return to duel"
            user_input = raw_input("> ")
            if user_input == "1":
                hero.magical_knowledge += 5
                print "%s's magical knowledge increased to %d." % (hero.name, hero.magical_knowledge)
            if user_input == "2":
                hero.health += 5
                print "%s's health increased to %d." % (hero.name, hero.health)
            if user_input == "X" or "x":
                break
            # else:
            #     break