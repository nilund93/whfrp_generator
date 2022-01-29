from random import randint

# Superclass assumes character is human and is an NPC
# For other races, animals or monsters, remake the attributes-methods. 

class Entity:
    weapon_skill: int
    ballistic_skill: int
    strength: int
    toughness: int
    initative: int
    agility: int
    dexterity: int
    intelligence: int
    willpower: int
    fellowship: int
    wounds: int
    movement: int
    
    def __init__(self, rand = True):
        self.name = input("Name: ")
        if rand: self.randomize_attributes()
        else: 
            self.create_attributes()

    def __str__(self) -> str:
        return f"{self.name}\nWS: {self.weapon_skill}\nBS: {self.ballistic_skill}\nS: {self.strength}\
            \nT:{self.toughness}\nI: {self.initative}\nA: {self.agility}\nDex: {self.dexterity}\nInt: {self.intelligence}\
                \nWP: {self.willpower}\nFel: {self.fellowship}\nW: {self.wounds}\nMovement: {self.movement}"

    def randomize_attributes(self):
        pass

    def create_attributes(self):
        self.weapon_skill = int(input("Weapon skill: "))
        self.ballistic_skill = int(input("Ballistic Skill: "))
        self.strength = int(input("Strength: "))
        self.toughness = int(input("Toughness: "))
        self.initative = int(input("Initiative: "))
        self.agility = int(input("Agility: "))
        self.dexterity = int(input("Dexterity: "))
        self.intelligence = int(input("Intelligence: "))
        self.willpower = int(input("Willpower: "))
        self.fellowship = int(input("Fellowship: "))
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        print(f"Wounds: {self.wounds}")
        self.movement = int(input("Movement: "))


class Human(Entity):
    def __init__(self, rand = True):
        self.name = input("Name: ")
        if rand: self.randomize_attributes()
        else: 
            super().create_attributes()
    
    def randomize_attributes(self):
        self.weapon_skill = randint(20, 40)
        self.ballistic_skill = randint(20, 40)
        self.strength = randint(20, 40)
        self.toughness = randint(20, 40)
        self.initative = randint(20, 40)
        self.agility = randint(20, 40)
        self.dexterity = randint(20, 40)
        self.intelligence = randint(20, 40)
        self.willpower = randint(20, 40)
        self.fellowship = randint(20, 40)
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        self.movement = 4
    
class Halfling(Entity):
    def __init__(self, rand = True):
        self.name = input("Name: ")
        if rand: self.randomize_attributes()
        else: 
            super().create_attributes()
    
    def randomize_attributes(self):
        self.weapon_skill = randint(10, 30)
        self.ballistic_skill = randint(30, 50)
        self.strength = randint(10, 30)
        self.toughness = randint(20, 40)
        self.initative = randint(20, 40)
        self.agility = randint(20, 40)
        self.dexterity = randint(30, 50)
        self.intelligence = randint(20, 40)
        self.willpower = randint(30, 50)
        self.fellowship = randint(30, 50)
        self.wounds = 2*(self.toughness//10) + self.willpower//10
        self.movement = 3

class Dwarf(Entity):
    def __init__(self, rand = True):
        self.name = input("Name: ")
        if rand: self.randomize_attributes()
        else: 
            super().create_attributes()
    
    def randomize_attributes(self):
        self.weapon_skill = randint(30, 50)
        self.ballistic_skill = randint(20, 40)
        self.strength = randint(20, 40)
        self.toughness = randint(30, 50)
        self.initative = randint(20, 40)
        self.agility = randint(10, 30)
        self.dexterity = randint(30, 50)
        self.intelligence = randint(20, 40)
        self.willpower = randint(40, 60)
        self.fellowship = randint(10, 30)
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        self.movement = 3

class HighElf(Entity):
    def __init__(self, rand = True):
        self.name = input("Name: ")
        if rand: self.randomize_attributes()
        else: 
            super().create_attributes()
    
    def randomize_attributes(self):
        self.weapon_skill = randint(30, 50)
        self.ballistic_skill = randint(30, 50)
        self.strength = randint(20, 40)
        self.toughness = randint(20, 40)
        self.initative = randint(20, 40)
        self.agility = randint(20, 40)
        self.dexterity = randint(20, 40)
        self.intelligence = randint(20, 40)
        self.willpower = randint(20, 40)
        self.fellowship = randint(20, 40)
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        self.movement = 4

class WoodElf(Entity):
    def __init__(self, rand = True):
        self.name = input("Name: ")
        if rand: self.randomize_attributes()
        else: 
            super().create_attributes()
    
    def randomize_attributes(self):
        self.weapon_skill = randint(20, 40)
        self.ballistic_skill = randint(20, 40)
        self.strength = randint(20, 40)
        self.toughness = randint(20, 40)
        self.initative = randint(30, 50)
        self.agility = randint(30, 50)
        self.dexterity = randint(30, 50)
        self.intelligence = randint(30, 50)
        self.willpower = randint(30, 50)
        self.fellowship = randint(20, 40)
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        self.movement = 5