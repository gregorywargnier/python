#Definition (Tableau (php))
fruits = ['pomme', 'banane', 'cerise']
print(fruits[0]) # Affiche 'pomme'
print(fruits[-1]) # Affiche 'cerise'. liste à l'envers
print(fruits[1:3]) # Affiche ['banane', 'cerise']
fruits_copy = fruits.copy() # Créer une copie de la liste

fruits.sort()
print(fruits) # Affiche ['banane', 'cerise', 'pomme']

fruits.append('orange') # Ajoute un élément
print(fruits)

fruits.remove('banane') # Supprime un élément
print(fruits)

#Boucl list
for fruit in fruits:
    print(fruit)

#tuples
my_tuple = (1,)
print(my_tuple[0]) # Affiche 1

a, b = (1, 2)
print(a)  # Affiche 1
print(b)  # Affiche 2

#dictionnaires key value
person = {'name': 'Fiorella', 'age': 5}
print(person['name']) # Affiche Fiorella

person['city'] = 'Lens' # Ajoute une clé
print(person)

age = person.get('age', 'Non spécifié')
print(age)

for key, value in person.items():
    print(f"{key} : {value}")

#ensembles
numbers = {1, 2, 3, 3, 4} # Les doublons sont supprimés
print(numbers) # Affiche {1, 2, 3, 4}

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b) # Union: {1, 2, 3, 4, 5}
print(a & b) # Intersection: {3}
print(a - b) # Différence: {1, 2}

a.add(6)
a.remove(2)