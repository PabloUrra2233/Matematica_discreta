def dijkstra(grafo, origen, destino):
    distancias = {}
    anteriores = {}
    visitados = set()

    for ciudad in grafo:
        distancias[ciudad] = float("inf")
        anteriores[ciudad] = None

    distancias[origen] = 0

    while len(visitados) < len(grafo):
        ciudad_actual = None
        menor_distancia = float("inf")

        for ciudad in grafo:
            if ciudad not in visitados and distancias[ciudad] < menor_distancia:
                menor_distancia = distancias[ciudad]
                ciudad_actual = ciudad

        if ciudad_actual is None:
            break

        if ciudad_actual == destino:
            break

        visitados.add(ciudad_actual)

        for vecino in grafo[ciudad_actual]:
            peso = grafo[ciudad_actual][vecino]
            nueva_distancia = distancias[ciudad_actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = ciudad_actual

    camino = []
    ciudad = destino

    while ciudad is not None:
        camino.insert(0, ciudad)
        ciudad = anteriores[ciudad]

    return camino, distancias[destino]