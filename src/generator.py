from random import randint
from entities import Entity
from careers import *

def create_player():
    # Pick race
    # Pick class & career
    # Roll attributes
    # 
    this_char = {}
    pick_race(this_char)
    pick_class(this_char)
    
    return this_char

def pick_race(this_char: dict):
    choice = input("Do you want to randomise race or pick yourself?\nChoice: ")
    race = ""
    if "randomise" in choice.lower():
        race_random = randint(0, 100)
        if race_random > 0 and race_random < 91: race = "human"
        elif race_random > 90 and race_random < 95: race = "halfling"
        elif race_random > 94 and race_random < 99: race = "dwarf"
        elif race_random == 99: race = "high elf"
        elif race_random == 0: race = "wood elf"
    else:
        print("Pick a race: Human, Halfling, Dwarf, High Elf or Wood Elf")
        race = input("Pick one: ").lower()

    this_char["race"] = race
    
def pick_class(this_char: dict):
    choice = input("Do you want to randomise class and career, or pick yourself?\nChoice: ")
    class_var = ""
    career_var = ""
    
    if "randomise" in choice.lower():
        class_random = randint(0, 100)
        
        # check race, different races get different classes
        if this_char["race"] == "human": class_var = human_careers[class_random]
        elif this_char["race"] == "halfling": class_var = halfling_careers[class_random]
        elif this_char["race"] == "dwarf": class_var = dwarf_careers[class_random]
        elif this_char["race"] == "high elf": class_var = highelf_careers[class_random]
        elif this_char["race"] == "wood elf": class_var = woodelf_careers[class_random]
        
    else:
        loop_dict: dict
        if this_char["race"] == "human": loop_dict = human_careers
        elif this_char["race"] == "halfling": loop_dict = halfling_careers
        elif this_char["race"] == "dwarf": loop_dict = dwarf_careers
        elif this_char["race"] == "high elf": loop_dict = highelf_careers
        elif this_char["race"] == "wood elf": loop_dict = woodelf_careers
        
        print("You have the following careers to choose from for your race: ")
        loop_set = set(loop_dict.values())
        for career in loop_set:
                print(career)
        while True:
            class_var = input("Which of these careers do you pick?").lower()
            if class_var in loop_dict.values():
                break
        
    if class_var in academics: career_var = "academic"
    elif class_var in burghers: career_var = "burgher"
    elif class_var in courtiers: career_var = "courtier"
    elif class_var in peasants: career_var = "peasant"
    elif class_var in rangers: career_var = "ranger"
    elif class_var in riverfolk: career_var = "riverfolk"
    elif class_var in rogues: career_var = "rogue"
    elif class_var in warriors: career_var = "warrior"
    this_char["class"] = class_var
    this_char["career"] = career_var

if __name__ == "__main__":
    #random_person = Entity(True)
    #fixed_person = Entity(False)
    
    x = create_player()
    for y in x.values():
        print(y)
    