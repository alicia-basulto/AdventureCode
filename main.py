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


if __name__ == '__main__':
    first_challenge('firstDecember.txt')
