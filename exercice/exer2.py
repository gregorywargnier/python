"""""
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
"""
#9
dist1 = {'a': 1, 'b': 2}
dist2 = {'b': 3, 'c': 4}
dist_list = [dist1, dist2]
#print(dist_list)
def merge_conflits(**dist_list):
    for key, value in dist_list.items():
        print(f"{key} : {value}")

#10