print('Bienvenue sur mon quizz')

playing = input('Voulez-vous jouer? (oui/non) ')

if playing.lower() !='oui':
    print("Alright bye bye now!")
    quit()
else: print("Alright let's do this !!!")

points = 0





answer = input('Quel est le dinosaure préféré de Marvin ? ')
if answer.lower() == 'spinosaure' or answer.lower() =='spino':
    print('Bonne réponse')
    points = points + 1
    print('Tu as actuellement %s point !'% points)
else:
    print('Mauvaise réponse')
    print('Tu as actuellement %s points'% points)

answer = input('Quel est le dinosaure préféré de Marvin ? ')
if answer.lower() == 'spinosaure' or 'spino':
    print('Bonne réponse')
    points = points + 1
    print('Tu as actuellement %s points !'% points)
else:
    print('Mauvaise réponse')
    print('Tu as actuellement %s points!'% points)





