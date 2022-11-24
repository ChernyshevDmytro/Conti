import random

# e - exit; r - rock, s - scissors; p - paper
user_command = ["r", "s", "p", "e"]

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


class rock_scissors_paper:
    def __init__(self, rsp):
        self.coeff = protect_coeff[rsp]

    def __add__(self, other):
        if self.coeff[0] == other.coeff[0]:
            return "0, 0"
        else:
            for i in range(len(self.coeff)):
                if self.coeff[i] - other.coeff[i] == 2:
                    return "0,1", print("Computer win")

            return "1,0", print("You win")


while True:
    user_input_command = input("Please, choose r, s, p or e for exit :")
    if user_input_command == "e":
        break
    else:
        comp_choise = random.choice(user_command[:3])
        comp_choise_ins = rock_scissors_paper(comp_choise)
        print(f"Computer choose {comp_choise}")
        my_choice = rock_scissors_paper(user_input_command)
        print(my_choice + comp_choise_ins)


