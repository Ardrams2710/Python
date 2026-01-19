import random
import math
hide_and_seek=["Anupama","Anjali","Ardra","Sreejith","Aromal"]
new_game=list(set(hide_and_seek))
print("list of names after removing duplicates:",new_game)
name=random.choice(new_game)
print("Randomly choose a name for playing game:",name)
def reverse(g):
    game=""
    for i in g:
        game=i+game
    return game
print("reverse the name:",reverse(name))
num=len(new_game)
print("total number of unique names:",num)
print("squre root",math.ceil(math.sqrt(num)))



