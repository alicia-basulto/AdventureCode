import re
from math import factorial


def second_part(counter, id, total, scratchcards ):
    id= int(id)
    for i in range(counter):
            # If the list has up to 2 elements, add the value of entire_number
            scratchcards[id+i+1] += scratchcards[id]


def fourth_challenge(filename):

    try:
        dict_second_part = {}
        errors = set()
        total = 0
        total_first_part = 0
        sum = 0
        with open(filename, 'r') as file:
            content = file.readlines()
            for i in range(len(content)):
                dict_second_part[i+1] = 1
        for line in content:
            counter = 0

            division_id = line.split(':')
            id = division_id[0].strip("Card")
            line_content = division_id[1].split('|')
            winning_numbers =[int(x) for x in (remove(line_content[0].strip()).split(',')) ]
            game_numbers =[int(x) for x in (remove(line_content[1].strip()).split(',')) ]

            for c in game_numbers :
                if c in winning_numbers:
                    counter +=1

            total_first_part += first_part(counter, id)
            second_part(counter, id, total,dict_second_part)

        for i in dict_second_part.values():
            sum += i

        print(f"First part 4th December: {total_first_part}")
        print(f"Second part 4th December: {sum}")


    except FileNotFoundError:
        print("The file does not exist.")


def first_part(counter):
    total = 0
    a = 1  # Primer término de la progresión
    r = 2  # Razón de la progresión
    n = counter  # Número de términos que quieres calcular
    progresion = []  # Lista para almacenar los términos de la progresión
    for i in range(n):
        progresion.append( a * r ** i)
    if counter == 0:
        progresion.append(0)
    else:
        total += progresion[-1]
    return total


def remove(string):
    return string.replace("  "," ").replace(" ", ",")

if __name__ == '__main__':
    fourth_challenge('fourthDecember.txt')

