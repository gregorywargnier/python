import random

#1.
age = input("nombre ? ")
age = int(age)
if age < 0:
    print ("negatif")
elif age == 0:
    print ("null")
else:
    print ("positif")

#2.
a = int(input("Tapez la valeur du nombre a : "))
b = int(input("Tapez la valeur du nombre b : "))

# Faire un test de comparaison pour trouver le plus grand
if a > b:
    print("Le maximum  de a et de b est : a = ", a)
else:
    print("Le maximum  de a et de b est : b = ", b)

#3.
birth = input("Quel est ton age ? ")
age = int(age)
if age < 18:
    print ("mineur")
else:
    print ("majeur")

#4
is_senior = input("Esct-ce que que tu as plus de 60 ans ? (o/n)").lower() == 'o'
is_student = input("etudiant ? (o/n)").lower() == 'o'
price = 50
student_discount = 20
senior_discount = 30
if is_student:
        price = price * ((100 - student_discount) / 100)
        print(f' Le prix du train est de {price} euros')
else:
        price = price * ((100 - senior_discount) / 100)
        print(f' Le prix du train est de {price} euros')


#5
nombre_inconnu = random.randint(1, 100)
proposition = int(input("Entrez un nombre entier entre 1 et 100 -> "))
while proposition != nombre_inconnu:
    if proposition > nombre_inconnu or proposition < nombre_inconnu:
        proposition = int(input("Entrez un nombre entier entre 1 et 100 -> "))
    else:
        print ('ok')
#6
mdp = input("saississez votre pot de passe ? ")
if len(mdp) >= 8:
    print ("votre mot de passe est valide")
else:
    print ("votre mot de passe n'est pas valide")