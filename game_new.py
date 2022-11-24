import random
from datetime import datetime
import json
import os
# e - exit; r - rock, s - scissors; p - paper
user_command = ["r", "s", "p", "e"]
win_params = {0: " draw ", 2: "Computer win", -2: "You win", -1:"", 1:""}
"""
rock: 
defense_from_rock = 0
defense_from_paper = -1
defense_from_scissors = 1

scissors:
defense_from_rock = -1
defense_from_paper = 1
defense_from_scissors = 0

paper:
defense_from_rock = 1
defense_from_paper = 0
defense_from_scissors = -1
"""
protect_coeff = {"r": [0, -1, 1], "s": [-1, 1, 0], "p": [1, 0, -1]}

scores = {}
game_save_name = "game_paper_scissors_rock.json"

if os.path.getsize(game_save_name) > 0:
    with open(game_save_name, "r") as file:
        scores = json.load(file)
        comp_win=0
        you_win=0
        for k, v in scores.items():
          if v ==  'You win':
             you_win+=1
          elif v ==  'Computer win':
             comp_win+=1             
        print(f"Computer wins {comp_win} times\nYou win {you_win} times")

class rock_scissors_paper:
    def __init__(self, rsp):
        self.coeff = protect_coeff[rsp]

    def __add__(self, other):
        message = ""
        for i in range(len(self.coeff)):                
            message+= win_params[self.coeff[i]-other.coeff[i]]
        scores[str(datetime.now())] = message
        return (message)    


while True:
    user_input_command = input("Please, choose r, s, p or e for exit :")
    if user_input_command == "e":
        with open(game_save_name, 'w') as f:
            json.dump(scores, f)

        break
    else:
        comp_choise = random.choice(user_command[:3])
        comp_choise_ins = rock_scissors_paper(comp_choise)
        my_choice = rock_scissors_paper(user_input_command)        
        print(f"Computer choose {comp_choise}")
        print(my_choice + comp_choise_ins)
         

