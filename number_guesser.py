import random

top_range = input('Entre un nombre: ')
if top_range.isdigit():
    top_range = int(top_range)

if top_range <= 0:
    print('Veuillez entrer un nombre positif')
else:
    print('Veuillez entrer un nombre')

num_guess = 0

r = random.randint(0, top_range)

while True:
    num_guess +=1
    guess = input('Trouve le bon nombre: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Veuillez entrer un nombre')
        continue

    if guess == r:
        print('Bonne réponse')
        break
    elif guess < r:
        print('Plus grand')
    else:
       print('Plus petit')
    
print('Vous avez gagné en %s essais' %num_guess )

