import re


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


def surroundingsDigitsPart2(content, line_number, line_position, number):
    # Loop back from position j to the start of the string
    # Intermediate lines
    if line_number != len(content) - 1 and line_number != 0:
        for pos in range(line_position - 1, (line_position - 1) - len(number), -1):
            # Coordenadas de las coincidencias
            coordenadas = [
                list((line_number + 1, pos)) if findIter(content, line_number + 1, pos) else None,
                list((line_number + 1, pos + 1)) if findIter(content, line_number + 1, pos + 1) else None,
                list((line_number + 1, pos - 1)) if findIter(content, line_number + 1, pos - 1) else None,
                list((line_number, pos + 1)) if findIter(content, line_number, pos + 1) else None,
                list((line_number, pos - 1)) if findIter(content, line_number, pos - 1) else None,
                list((line_number - 1, pos)) if findIter(content, line_number - 1, pos) else None,
                list((line_number - 1, pos + 1)) if findIter(content, line_number - 1, pos + 1) else None,
                list((line_number - 1, pos - 1)) if findIter(content, line_number - 1, pos - 1) else None,
            ]
            for coord in coordenadas:
                if coord is not None:
                    return coord

        return False

    # First line
    elif line_number == 0:
        for pos in range(line_position - 1, (line_position - 1) - len(number), -1):

            coordenadas = [
                list((line_number + 1, pos)) if findIter(content, line_number + 1, pos) else None,
                list((line_number + 1, pos + 1)) if findIter(content, line_number + 1, pos + 1) else None,
                list((line_number + 1, pos - 1)) if findIter(content, line_number + 1, pos - 1) else None,
                list((line_number, pos + 1)) if findIter(content, line_number, pos + 1) else None,
                list((line_number, pos - 1)) if findIter(content, line_number, pos - 1) else None
            ]
            for coord in coordenadas:
                if coord is not None:
                    return coord

        return False
    # Final line
    elif line_number == len(content) - 1:
        for pos in range(line_position - 1, (line_position - 1) - len(number), -1):
            coordenadas = [
                list((line_number - 1, pos)) if findIter(content, line_number - 1, pos) else None,
                list((line_number - 1, pos + 1)) if findIter(content, line_number - 1, pos + 1) else None,
                list((line_number - 1, pos - 1)) if findIter(content, line_number - 1, pos - 1) else None,
                list((line_number, pos + 1)) if findIter(content, line_number, pos + 1) else None,
                list((line_number, pos - 1)) if findIter(content, line_number, pos - 1) else None
            ]
            for coord in coordenadas:
                if coord is not None:
                    return coord

        return False


def findIter(content, line_number, pos):
    return re.findall(r'\*', content[line_number][pos])


def first_part(filename):
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


def second_part(filename):
    try:
        errors = set()
        with open(filename, 'r') as file:
            content = file.readlines()
            numbers_converted = []
            gear_subtracted = {}
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
                            result_surroundings = surroundingsDigitsPart2(content, i, j, entire_number)
                            if result_surroundings:
                                coordinate_key = tuple(result_surroundings)
                                if coordinate_key not in gear_subtracted:
                                    # If the coordinates are not in the dictionary, add a new list
                                    gear_subtracted[coordinate_key] = [entire_number]
                                elif len(gear_subtracted[coordinate_key]) == 0:
                                    # If the associated list is empty, add the value of entire_number
                                    gear_subtracted[coordinate_key] = [entire_number]
                                elif len(gear_subtracted[coordinate_key]) <= 2:
                                    # If the list has up to 2 elements, add the value of entire_number
                                    gear_subtracted[coordinate_key].append(entire_number)
                            entire_number = ''
                        previous_char_number = False

        # Filter keys that have exactly two values in the list
        keys_with_2_values = {k: values for k, values in gear_subtracted.items() if
                              len(values) == 2}
        # Multiply the values among themselves and add them all
        final_result = sum(int(values[0]) * int(values[1]) for values in keys_with_2_values.values())
        print(f"Second part sum result of gear couples: {final_result}")
    except FileNotFoundError:
        print("The file does not exist.")


if __name__ == '__main__':
    first_part('thirdDecember.txt')
    second_part('thirdDecember.txt')
