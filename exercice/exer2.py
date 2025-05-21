#1
def show_message(name):

    print(name)

show_message("Bienvenue en python")

#2
def good_bye(name):
    print(f'Au revoir,',name,'!')

good_bye("greg")

#3
def addition(*numbers):
    return sum(numbers)

print(addition(5) * addition(2))

#4
def is_even(n, a):
    if n % a == 0:
        return True
    else:
        return False
print(is_even(4, 2))
print(is_even(7, 2))

#5
numbers = [10, 20, 30, 40]
print(numbers)

numbers.append(50)
print(numbers)

numbers.remove(20)
print(numbers)

for number in numbers:
    print(number)

#6
student = {'name': 'gregory', 'age': 37, 'average_note':15}
print(student)

student['average_note'] = 12
print(student)

student['classroom'] = '5A'
print(student)

print(student)

student2 = ({
    'person2': {
        'name': 'sylvain',
        'age': 30,
        'average_note':7
    },
    'person3': {
        'name': 'john',
        'age': 32,
        'average_note': 10
    }
})
print((student2.get('person2')['average_note'] + student2.get('person3')['average_note'])/2)

#7
stats = ([10, 20, 30, 40])
def average(stats):
    return sum(stats)/len(stats)
print(average(stats))

x = max(stats)
print(x)

y = min(stats)
print(y)

print(len(stats))

#8
text = 'bonjour le monde bonjour'

word = text.split()

word_frequency = []
for words in word:
    word_frequency.append(word.count(words))
print(str(list(zip(word_frequency))))

#9
def merge_dicts(dict1, dict2):
    merged = dict1.copy()

    for key, value in dict2.items():
        if key in merged:

            if isinstance(merged[key], (int, float)) and isinstance(value, (int, float)):
                merged[key] += value

            elif isinstance(merged[key], str) and isinstance(value, str):
                merged[key] += value
            else:
                raise ValueError(f"Conflit de type entre les valeurs pour la clé '{key}'")
        else:
            merged[key] = value

    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

result = merge_dicts(dict1, dict2)
print(result)

#10
list_of_dicts = ([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}])

def sort_by_key(list_of_dicts):
    list_of_dicts.sort(key=lambda x: x['age'])
    return list_of_dicts
print(sort_by_key(list_of_dicts))

#11


def generate_matrix(n):
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(i + j)
        matrix.append(row)

    return matrix


n = 3
matrix = generate_matrix(n)
for row in matrix:
    print(row)