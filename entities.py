from random import randint

# Superclass assumes character is human and is an NPC
# For other races, animals or monsters, remake the attributes-methods. 

class Entity:
    weapon_skill: int
    ballistic_skill: int
    strength: int
    toughness: int
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
            \nT:{self.toughness}\nA: {self.agility}\nDex: {self.dexterity}\nInt: {self.intelligence}\
                \nWP: {self.willpower}\nFel: {self.fellowship}\nW: {self.wounds}\nMovement: {self.movement}"

    def randomize_attributes(self):
        self.weapon_skill = randint(20, 40)
        self.ballistic_skill = randint(20, 40)
        self.strength = randint(20, 40)
        self.toughness = randint(20, 40)
        self.agility = randint(20, 40)
        self.dexterity = randint(20, 40)
        self.intelligence = randint(20, 40)
        self.willpower = randint(20, 40)
        self.fellowship = randint(20, 40)
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        self.movement = 4

    def create_attributes(self):
        self.weapon_skill = int(input("Weapon skill: "))
        self.ballistic_skill = int(input("Ballistic Skill: "))
        self.strength = int(input("Strength: "))
        self.toughness = int(input("Toughness: "))
        self.agility = int(input("Agility: "))
        self.dexterity = int(input("Dexterity: "))
        self.intelligence = int(input("Intelligence: "))
        self.willpower = int(input("Willpower: "))
        self.fellowship = int(input("Fellowship: "))
        self.wounds = self.strength//10 + 2*(self.toughness//10) + self.willpower//10
        print(f"Wounds: {self.wounds}")
        self.movement = int(input("Movement: "))
    