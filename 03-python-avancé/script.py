import os
with open('file.txt', 'a+') as file:
    file.seek(0)
    content = file.read(3)
    print(content)


    file.seek(0)
    for lines in file:
        print(lines.strip())

    #recuperer le chemin ou on situe
    current_path = os.getcwd()

    file.write('\nLigne ajoutée.')
    file.write(f'on va ajouter {current_path}\n')