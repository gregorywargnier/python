#try catch
try:
    x = 10 / 0
except ZeroDivisionError:
    print('Erreur : Division par zéro !')

try:
    result = 10 / 2
except ZeroDivisionError:
    print('Erreur : Division par zéro !')
else:
    print('Résultat:', result)
finally:
    print('Opération terminée.')