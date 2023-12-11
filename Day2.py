import re


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



if __name__ == '__main__':
    second_challenge('secondDecember.txt')

