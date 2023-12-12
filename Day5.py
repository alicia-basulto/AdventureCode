import re
from math import factorial

limits = {}
result = {}
def second_part(counter, id, total, scratchcards ):
    id= int(id)
    for i in range(counter):
            # If the list has up to 2 elements, add the value of entire_number
            scratchcards[id+i+1] += scratchcards[id]


def map_generator(origin, destination, range, map_identifier):
    if map_identifier not in limits:
        limits[map_identifier] = []  # Create an empty list if the map_identifier doesn't exist
    limits[map_identifier].append([origin, (origin-1) + range, destination])


def location_calculator(seed,limits_list):
        result = seed
        for sublist in limits_list:
            min = sublist[0]
            max = sublist[1]
            destination = sublist[2]
            if seed >= min and seed <= max:
                result = destination + (seed - min)

        if result is None:
            result = seed

        return result



def fourth_challenge(filename):

    try:
        # Defines a dictionary to store the maps of each category
        input_parsed = {}
        location_dict = {}
        next_seed = 0

        #Read the input file
        with open(filename, 'r') as archivo:
            content = archivo.read()
        # Divide content into sections based on empty lines
        sections = [section.strip() for section in content.split('\n\n') if section.strip()]

        for section_part in sections:
            lines = section_part.split('\n')
            category = lines[0].strip().replace("-to-", ",").replace("map", "").replace(" :","")
            data = process_section('\n'.join(lines[1:]))  # Process the rest of the section
            input_parsed[category] = data

        seeds = input_parsed.pop('seeds:')[0]

        input_to_map(input_parsed)

        first_challenge(location_dict, seeds)

    except FileNotFoundError:
        print("The file does not exist.")


def first_challenge(location_dict, seeds):
    result_in_map(seeds)
    for key, results in result.items():
        location = results[len(results) - 1][1]
        location_dict[key] = location
    if location_dict:
        min_value_location = min(location_dict.values())
        print(f"The minimum value of the location is '{min_value_location}'.")
    else:
        print(f"No coincidence found")


def result_in_map(seeds):
    for seed in seeds:
        result[seed] = []
        next_seed = seed
        for key, value in limits.items():
            next_seed = location_calculator(next_seed, value)
            original_seed = seed
            result[original_seed].append([key, next_seed])


def input_to_map(input_parsed):
    for key, value in input_parsed.items():
        for sublist in value:
            map_generator(sublist[1], sublist[0], sublist[2], key)


def process_section(section):
    # Split the section lines into words and convert them to numbers
    mapa = [[int(num) for num in linea.split()] for linea in section.split('\n') if linea.strip()]
    return mapa

if __name__ == '__main__':
    fourth_challenge('fifthDecember.txt')

