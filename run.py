from bot_func import Automata
from time import sleep
from random import randint

sleep_before_quit = randint(5, 23) #can be set a constant -- does not matter
iter = 10000 #number of races to bot

try:
    for i in range(iter):
        with Automata() as bot:
                bot.open()
                sleep(4)
                bot.cookies_disagree()
                bot.sign_in()
                bot.start_race()
                bot.type_race()
                sleep(sleep_before_quit) #sleep before closing the window
except: raise
