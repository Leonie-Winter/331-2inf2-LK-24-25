import time
from datetime import datetime
import os

class Ampel:
    def __init__(self, anfangszustand: bool):
        self.zustand = anfangszustand
    
    def is_night(self):
        now = datetime.now()
        current_hour = int(now.strftime("%H"))
        return current_hour >= 18 or current_hour < 5

    def schalten(self):
            self.zustand = not self.zustand
            print(f"{self.print_the_thing()}")
            
    def print_the_thing(self):
        night = self.is_night()
        if self.zustand == True and night == False:
                return "####\n""#""\033[42m  \033[0m""#\n" "####\n" 
        elif self.zustand == False and night == False:
                return "####\n""#""\033[41m  \033[0m""#\n" "####\n"
        elif self.zustand == True and night == True:
                return "####\n""#""\033[43m  \033[0m""#\n" "####\n"
        else: 
                return "####\n""#""  ""#\n" "#### \n"

if __name__ == "__main__":
    ampel = Ampel(False) 
    for _ in range(5): 
        ampel.schalten()
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')