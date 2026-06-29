import csv


def cargar_grafo():
    grafo = {}
    posiciones = {}

    with open("datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            origen = fila["origen"]
            destino = fila["destino"]
            peso = int(fila["peso"])

            x_origen = int(fila["x_origen"])
            y_origen = int(fila["y_origen"])
            x_destino = int(fila["x_destino"])
            y_destino = int(fila["y_destino"])

            if origen not in grafo:
                grafo[origen] = {}

            if destino not in grafo:
                grafo[destino] = {}

            grafo[origen][destino] = peso
            grafo[destino][origen] = peso

            posiciones[origen] = (x_origen, y_origen)
            posiciones[destino] = (x_destino, y_destino)

    return grafo, posiciones