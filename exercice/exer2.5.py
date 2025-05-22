# Distributeur de monnaie
#question 1
currency = [10, 20, 50]
piece = [5, 2, 1]

#print(piece[0])
x = min(currency)
y = min(piece)
print(x, y)

#question 2 et 3
money = [50, 20, 10, 5, 2, 1]
money.sort(reverse=True)
print(money)
def give_change(price, payment):

    rendered = {}
    difference = price - payment

    for m in money:
        if difference // m > 0:
            rendered[m] = int(difference // m)
            difference = difference % m
    return rendered

print(give_change(68, 0))

#question bonus
with open('dispenser.txt', 'a+') as file:
    file.seek(0)
    content = file.read(0)
    #print(content)

    file.seek(0)
    for lines in file:
        print(lines.strip())

    file.seek(0)
    file.write(str(give_change(60, 0)))

money.remove(10)
print(money)
def disqualification(price, payment):
    rendered = {}
    difference = price - payment

    for m in money:
        if difference // m > 1:
            rendered[m] = int(difference // m)
            difference = difference % m
    return rendered
print(disqualification(68, 0))

#convertisseur de temperatures
temp = float(input("Entrer votre température: "))
init =  input("Entrer votre valeur de départ (c/f/k): ")
arrive = input("Entrer votre valeur d'arrivé (c/f/k): ")

if init == 'c' or init == 'f'or init == 'k' or arrive == 'c' or arrive == 'f' or arrive == 'k':
    if init == "c":
        if arrive == "f":
            temp = round((temp * 9) / 5 + 32)
            print(f" votre température est de : {temp} Fahrenheit")
        elif arrive == "k":
            temp = round(temp + 273)
            print(f" votre température est de : {temp} Kelvin")
        else:
            print(f" votre température est de : {temp} Celsius")

    if init == "f":
        if arrive == "c":
            temp = round((temp - 32) * (5/9))
            print(f" votre température est de : {temp} Celsius")
        elif arrive == "k":
            temp = round((temp - 32) * 5/9 + 273,15)
            print(f" votre température est de : {temp} Kelvin")
        else:
            print(f" votre température est de : {temp} Fahrenheit")

    if init == "k":
        if arrive == "c":
            temp = round(temp - 273,15)
            print(f" votre température est de : {temp} Celsius")
        elif arrive == "f":
            temp = round((temp - 273) * 5/9 + 273,15)
            print(f" votre température est de : {temp} Fahrenheit")
        else:
            print(f" votre température est de : {temp} Kelvin")
else:
    print(f"Votre unité/valeur n'est pas reconnue")