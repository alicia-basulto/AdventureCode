import re


def first_challenge(filename):
    try:
        sum_total = 0
        with open(filename, 'r') as file:
            content = file.readlines()
        list_number = []
        number_regex = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        for line in content:
            map_number = {}
            word_to_number = {word: str(index + 1) for index, word in enumerate(number_regex)}
            # Replace words in the input string with their numeric representations
            for word, number in word_to_number.items():
                if word in line:
                    iter_matches = re.finditer(word, line)
                    indices_coincidences = [match.start() for match in iter_matches]
                    for match in indices_coincidences:
                        map_number[match] = number

            # Extract digits in order
            for char in line:
                if char.isdigit():
                    iter_matches = re.finditer(char, line)
                    indices_coincidences = [match.start() for match in iter_matches]

                    for match in indices_coincidences:
                        map_number[match] = char

            map_number_ordered = dict(sorted(map_number.items(), key=lambda item: item[0], reverse=True))
            num_reversed = ', '.join(map(str, list(map_number_ordered.values())))
            num = num_reversed[::-1]

            if len(num) == 1:
                num = num + num
            elif len(num) > 2:
                num = num[0] + num[len(num) - 1]
            list_number.append(int(num))
            sum_total += int(num)
        print("Sum total: " + str(sum(list_number)))
    except FileNotFoundError:
        print("The file does not exist.")


def second_challenge(filename):
    cubes_limit = {'red': 12, 'green': 13, 'blue': 14}
    try:
        errors = set()
        with open(filename, 'r') as file:
            content = file.readlines()
        for line in content:
            division_id = line.split(':')
            id = division_id[0].strip("Game")
            line_content = division_id[1].split(';')
            # Utilizar expresiones regulares para encontrar los pares color-valor
            for game in line_content:
                patron = re.compile(r'(\d+)\s+(\w+)')
                coincidencias = patron.findall(game)
                # Construir un diccionario con los valores encontrados
                mapa_colores = {color: int(valor) for valor, color in coincidencias}
                # Verificar que los valores no superen los límites
                for color, valor_actual in mapa_colores.items():
                    valor_limite = cubes_limit.get(color, float('inf'))
                    if valor_actual > valor_limite:
                        errors.add(id)
                        print(f"El valor para '{color}' ({valor_actual}) supera el límite de {valor_limite}")

        numeros = [int(cadena.strip()) for cadena in errors]

        todos_los_numeros = list(range(1, len(content) + 1))
        numeros_no_aparecen = [numero for numero in todos_los_numeros if numero not in numeros]

        print("Sum total:" + str(sum(numeros_no_aparecen)))

    except FileNotFoundError:
        print("The file does not exist.")


def surroundingsDigits(content, line_number, line_position, number):
    # Loop back from position j to the start of the string
    # Intermediate lines
    if line_number != len(content) - 1 and line_number != 0:
        for pos in range(line_position - 1, (line_position - 1) - len(number), -1):
            if (re.findall(r'[^a-zA-Z0-9.\n]', content[line_number + 1][pos])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number + 1][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number + 1][pos - 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number - 1][pos])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number - 1][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number - 1][pos - 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number][pos - 1])):
                return True
        return False
    # First line
    elif line_number == 0:
        for pos in range(line_position - 1, (line_position - 1) - len(number), -1):
            if (re.findall(r'[^a-zA-Z0-9.\n]', content[line_number + 1][pos])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number + 1][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number + 1][pos - 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number][pos - 1])):
                return True
        return False
    # Final line
    elif line_number == len(content) - 1:
        for pos in range(line_position - 1, (line_position - 1) - len(number), -1):
            if (re.findall(r'[^a-zA-Z0-9.\n]', content[line_number - 1][pos])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number - 1][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number - 1][pos - 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number][pos + 1])
                    or re.findall(r'[^a-zA-Z0-9.\n]', content[line_number][pos - 1])):
                return True
        return False


def third_challenge(filename):
    cubes_limit = {'red': 12, 'green': 13, 'blue': 14}
    try:
        errors = set()
        with open(filename, 'r') as file:
            content = file.readlines()
            numbers_subtracted = []
            numbers_converted = []
            previous_char_number = False
            for i, line in enumerate(content):
                entire_number = ''
                for j, character in enumerate(line):
                    if character.isdigit():
                        previous_char_number = True
                        entire_number += character
                    else:
                        if previous_char_number and entire_number:
                            numbers_converted.append(int(entire_number))
                            if not surroundingsDigits(content, i, j, entire_number):
                                numbers_subtracted.append(int(entire_number))
                            entire_number = ''
                        previous_char_number = False

            total = [int(x) for x in numbers_converted]
            total_subtraction = [int(x) for x in numbers_subtracted]

            print(f"Result: {sum(total) - sum(total_subtraction)}")














    except FileNotFoundError:
        print("The file does not exist.")


if __name__ == '__main__':
    # first_challenge('firstDecember.txt')
    # second_challenge('secondDecember.txt')
    third_challenge('thirdDecember.txt')
