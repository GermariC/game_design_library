# Dice Roll library, Germari Cull, Febraury 18, 2021, 12:29, v0.0

# d4 simulator 
def roll_d4(num_roll): # num_roll is an ARGUMENT
    import random

    rolls = 0 
    while rolls <= num_roll:
        result = random.randint(1,4)
        print(f"You rolled a {result} on the da!\n")
        rolls += 1