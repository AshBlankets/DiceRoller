import os
class DiceRoller():
    def startup(self):
    	ESCAPE = u"\u001B"
    	os.system("echo {}[31mHello World{}[0m".format(ESCAPE, ESCAPE))



d = DiceRoller()
d.startup()