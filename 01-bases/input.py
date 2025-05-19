name = input("c'est quoi ton nom ?")

#print('Bonjour' + name + ' !')
#print(f'Bonjour {name} !')

age = input("C'est quoi ton age ?")

if age.isnumeric():
    age = int(age)
else:
    exit('Veuillez entrer un nombre entier')
age = int(age)
print(f'tu as {age} ans. Dans 2 ans tu aura {int(age) + 2}')

if age < 10: 
    print('vous avez moins de 10 ans')
elif age == 15:
    print('vous etes mineur')
else: 
    print('vous avez plus de 18 ans')    