from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import uniform


class Automata(webdriver.Chrome):

    def __init__(self, driver_path=r'/usr/local/bin/'):
        self.driver_path = driver_path
        self.usr = '' #specify the username
        self.pw = '' #specify the password
        self.randType = uniform(0.55, 0.61)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        super(Automata, self).__init__(options=options)
        self.implicitly_wait(15)

    def open(self):
        self.get("https://play.typeracer.com/")

    def cookies_disagree(self):
        disagree = self.find_element(By.XPATH, "//span[contains(., 'DISAGREE')]")
        disagree.click()

    def sign_in(self):
        signin = self.find_element(By.XPATH, "//a[contains(., 'Sign In')]")
        signin.click()

        usr_textbox = self.find_element(By.CLASS_NAME, "gwt-TextBox")
        usr_textbox.send_keys(self.usr)

        pw_textbox = self.find_element(By.CLASS_NAME, "gwt-PasswordTextBox")
        pw_textbox.send_keys(self.pw)

        pw_textbox.send_keys(Keys.ENTER)
        sleep(3) #although using sleep is not ideal, it seems to be the best solution here

        close_popup = self.find_element(By.CSS_SELECTOR, 'g[class="xShape"]')
        close_popup.click()

    def start_race(self):
        start = self.find_element(By.XPATH, "//a[contains(., 'Enter a Typing Race')]")
        start.click()
        sleep(2)

    def type_race(self):

        for _ in range(10):
            sleep(2)
            print("starting")

            text_ = self.find_element(By.CLASS_NAME, "txtInput")
            state = self.find_element(By.CLASS_NAME, "gameStatusLabel")
            text_full = self.find_element(By.CLASS_NAME, "inputPanel").text
            wordlist = text_full.split()
            wordlist = wordlist[:-3]

            while True:
                if "The race is on!" in state.text or "Go!" in state.text:
                    for word in wordlist:
                        print(word, wordlist)
                        text_.send_keys(word + " ")
                        sleep(self.randType)

                    print("continuing")
                    race_again = self.find_element(By.XPATH, "//a[contains(., 'Race again')]")
                    race_again.click()
                    return False


