import re
from math import factorial

limits = {}
result = {}
new_seeds = []
solution= []
location_dict_2={}



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


def second_challenge(seeds):
    # Split the list into pairs

    pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for individual_pair in pairs:
        for i in range (individual_pair[0], (individual_pair[0]-1) + individual_pair[1]):
            new_seeds.append(i)
    for pair in pairs:
        pair = [pair[0], (pair[0]-1) + pair[1]]
        new_range = pair
        for key, section in limits.items():
            intersection_range = find_range(new_range, section)
            if not intersection_range:
                result_in_map_2(new_range, key)
                break
            new_range = [(new_range[0]-intersection_range[0]) + intersection_range[2], (new_range[0]-intersection_range[0]) + intersection_range[2] + (new_range[1]-new_range[0])]
    print(f"Second part:The minimum value of the location is '{min(solution)}'.")

def find_range(rango_a_verificar, lista_de_rangos):
    for rango in lista_de_rangos:
        inicio_interseccion = max(rango_a_verificar[0], rango[0])
        fin_interseccion = min(rango_a_verificar[1], rango[1])
        # Verificar si hay intersección
        if inicio_interseccion <= fin_interseccion:
            return rango # Hay intersección con al menos un rango
    return False  # No hay intersección con ninguno de los rangos



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
        second_challenge(seeds)

    except FileNotFoundError:
        print("The file does not exist.")


def first_challenge(location_dict, seeds):
    result_in_map(seeds)
    for key, results in result.items():
        location = results[len(results) - 1][1]
        location_dict[key] = location
    if location_dict:
        min_value_location = min(location_dict.values())
        print(f"First part: the minimum value of the location is '{min_value_location}'.")
    else:
        print(f"No coincidence found")


def result_in_map_2(seeds, id_key):
    loop_execution = False
    min_value = float('inf')  # Initialize min_value with positive infinity

    for seed in range(seeds[0], seeds[1]):
        next_seed = seed
        for key, value in limits.items():
            if key == id_key:
                loop_execution = True
            if loop_execution:
                next_seed = location_calculator(next_seed, value)
                if key == 'humidity,location':
                    min_value = min(min_value, next_seed)

    solution.append(min_value)


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

