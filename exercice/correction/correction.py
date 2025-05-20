#1
# Vérifier si un nombre est positif, négatif ou nul
def input_int(prompt):
    n = input(prompt)

    if n.lstrip('-').isnumeric():
        return int(n)
    else:
        print('Veuillez entrer un nombre entier')
        return input_int(prompt)

# n = input_int('Saisir un nombre: ')

# if n > 0:
#     print('Le nombre est positif')
# elif n == 0:
#     print('Le nombre est nul')
# else:
#     print('Le nombre est négatif')

# Alternative moins lisible
# print('Le nombre est positif') if n > 0 else print('Le nombre est nul') if n == 0 else print('Le nombre est négatif')

#2
n1 = input_int('Saisir le premier nombre: ')
n2 = input_int('Saisir le deuxieme nombre: ')

if n1 > n2:
    print(n1)
else:
    print(n2)

# Alternative moins lisible
print(n1 if n1 > n2 else n2)

#3
# Vérifier si un utilisateur est majeur


age = input_int('Quel est votre âge? ')

if age >= 18:
    print('Vous êtes majeur')
else:
    print('Vous avez moins de 18 ans')
#4
# Calculer le prix d'un billet avec réduction
is_senior = input('Est-ce que vous avez plus de 60 ans ? (o/n) ').lower() == 'o'
is_student = input('Est-ce que vous etes etudiant ? (o/n) ').lower() == 'o'

price = 50
student_discount = 20
senior_discount = 30

if is_student and not is_senior:
    price = price * ((100 - student_discount) / 100)
    print(f'Le prix du train est de {price} euros')
elif is_senior:
    discount = price * senior_discount / 100
    price = price - discount
    print(f'Le prix du train est de {price} euros avec une remise de {discount}')
else:
    print(f'Le prix du train est de {price} euros')
#5
# Jeu de devinette


import random

guess = random.randint(1, 100)
n = input_int('Devinez un nombre: ')

while n != guess:
    if n > guess:
        print('Le nombre est plus petit')
    else:
        print('Le nombre est plus grand')

    n = input_int('Devinez un nombre: ')

print(f'Bravo tu as trouvé {guess} !')
#6
# Système de validation de mot de passe
password = input('Saisir un mot de passe: ')
is_valid = len(password) >= 8 and any(c.isupper() for c in password) and any(c.isnumeric() for c in password)

while not is_valid:
    print('Le mot de passe doit contenir au moins 8 caractères, une lettre majuscule et un chiffre')
    password = input('Saisir un mot de passe: ')
    is_valid = len(password) >= 8 and any(c.isupper() for c in password) and any(c.isnumeric() for c in password)

print(f'Mot de passe valide: {password}')