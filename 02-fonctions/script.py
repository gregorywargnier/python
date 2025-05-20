#fonctions
def say_hello(name: str = None):


    if name is None:
        name = 'World'


    print(f'hello', name)
    #return f'Hello, {name}!'


say_hello('greg')

#retourner valeur
def square(x):
    return x * x

result = square(5)
print(result)

#arguments variable
def addition(*numbers):
    return sum(numbers)

print(addition(1, 2) + addition(3))
print(addition(1, 2, 3)) # Affiche 6

#OU
def display_informations(**informations):
    for key, value in informations.items():
        print(f"{key} : {value}")

display_informations(name='Fiorella', age=5)
# Affiche :
# nom : Fiorella
# age : 5

#portée de variable
y = 5 # y est une variable globale

def my_function():
    x = 10 # x est locale à ma_fonction
    print(x)
    print(y)

my_function()
# print(x) # Cela provoquerait une erreur, car x n'est pas définie ici
print(y)

#Fonctions anonymes
square = lambda x: x * x
print(square(4)) # Affiche 16

#Argument nommés
def greet(name, age):
    print(f'Bonjour {name}, tu as {age} ans.')

greet(name='Fiorella', age=5)
greet(age=5, name='Fiorella') # L'ordre n'a pas d'importance