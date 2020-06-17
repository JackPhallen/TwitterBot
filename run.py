from TwitterBot import TwitterBot
import os
import sys

BASE = os.path.dirname(os.path.realpath(sys.argv[0]))
RESOURCES = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"resources/")
PROPS = os.path.join(RESOURCES, "properties.ini")


props_path = os.path.join(BASE, PROPS)
bot = TwitterBot(props_path)
bot.run()




