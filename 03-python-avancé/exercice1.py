""""

with open('exo.txt', 'a+') as file:
    file.seek(0)
    content = file.read(3)
    print(content)

file.seek(0)
for i in range(10):
    if i % 2 == 0:
        file.write(str(i))
        file.write("\n")
        file.seek(0)

file.close()
"""