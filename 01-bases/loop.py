print(range(5))
for i in range(5):
    print(i)

numberA = input("saisir un nombre entre 1 et 18: ")
while not numberA.isnumeric() or int(numberA) < 1 or int(numberA) > 18:
    numberA = input("saisir un nombre entre 1 et 18: ")

for i in range(1, numberA + 1):
    print(i)


