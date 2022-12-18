from bot_func import Automata
from time import sleep

try:
    with Automata() as bot:
        bot.open()
        sleep(4)
        bot.cookies_disagree()
        bot.sign_in()
        bot.start_race()
        bot.type_race()
        sleep(5) #sleep before ultimately quitting
except: raise
