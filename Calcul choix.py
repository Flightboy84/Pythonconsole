
lolo = int(input("Quel age avez-vous?"))
if lolo < 18:
    print("Le prix sera de 7 euros")
    prix= 7
else:
    print("Le prix sera de 12 euros")
    prix=12

popcorn = input("Voulez-vous du popcorn: ")
if popcorn=="oui":
    prixtotal=prix+5
else:
    prixtotal=prix

print("Vous devez payer : "+str(prixtotal))



