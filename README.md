# Warhammer Fantasy RPG Generator

## Description

This project was born from the need to quickly generate non-playable characters in the RPG Warhammer Fantasy Role Play.

Within the 4th edition core rulebook we can find informationf or how one should go about creating characters, but doing this takes quite a lot of time. Thus, this project was born.

## Future implementations

I plan currently to just create human NPCs since they are the backbone of this setting. However, I plan to add generators for all playable races, monster generator and other things. This will be update throughout the project.

# Character creation

## From the rulebook

When a character is created, you go through a recipe that looks something like this:

1. Choose on of the five species:
    - Human
    - Halfling
    - Dwarf
    - High Elf
    - Wood Elf
2. Pick a class and career.
3. Roll your attributes.
4. Pick Skills and Talents
5. Pick your trappings.
6. Add details
    - Name
    - Age
    - Eye Colour
    - Hair Colour
    - Height
    - Ambitions

After these steps, one may bring their character to life with the ten following questions:
1. Where are you from?
2. What is your family like?
3. What was your childhood like?
4. Why did you leave home?
5. Who are your best friends?
6. What is your greatest desire?
7. What are your best and worst memories?
8. What are your religious beliefs?
9. To whom, or what, are you loyal?
10. Why are you adventuring?

## Code Implementation

I am thinking that as a user of this program, you get to decide whether you want to go through with each step or if you want that step randomised for you. The WHFRP system rewards you XP if you decide randomise, so of course you would be awarded this.

That means that we will go through all the six steps of the creation, and with each step ask if the user wants to randomise or not.