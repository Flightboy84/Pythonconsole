#Excercice Graven vidéo n°4

from random import shuffle

mots = input("Entrer les mots en suivant cette logique : mot1/mot2/mots3/... :").split("/")
shuffle(mots)
print(mots)
comptemots = len(mots)
if comptemots < 10:
    print(mots[0], mots[1])
else:
    print(mots[comptemots-1],mots[comptemots-2],mots[comptemots-3])

