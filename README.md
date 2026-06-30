# Ruta óptima entre ciudades mediante grafos ponderados

Proyecto final de **Matemática Discreta** desarrollado en Python. El programa modela una red de ciudades de Estados Unidos como un **grafo ponderado, no dirigido y conexo**, donde cada ciudad corresponde a un vértice y cada conexión corresponde a una arista con peso positivo.

El objetivo principal es calcular la **ruta de menor distancia** entre dos ciudades seleccionadas por el usuario, utilizando una implementación manual del **algoritmo de Dijkstra**. La aplicación incluye una interfaz gráfica que permite seleccionar origen y destino, visualizar el grafo sobre un mapa y destacar claramente la ruta óptima encontrada.

---

## Funcionalidades principales

- Carga de datos desde un archivo CSV.
- Modelamiento de una red de **15 ciudades no chilenas**.
- Uso de más de **20 conexiones reales** entre ciudades.
- Representación del grafo mediante diccionarios en Python.
- Implementación manual del algoritmo de Dijkstra.
- Selección de ciudad de origen y ciudad de destino.
- Visualización del grafo en una interfaz gráfica.
- Resaltado de la ruta óptima en color rojo.
- Visualización de los pesos de los tramos que forman parte de la ruta seleccionada.
- Presentación de la secuencia de ciudades y de la distancia total acumulada.

---

## Cumplimiento de requerimientos

| Requerimiento | Cumplimiento en el proyecto |
|---|---|
| 15 ciudades no chilenas | Se utilizan 15 ciudades de Estados Unidos. |
| Mínimo 20 conexiones reales | El archivo `datos.csv` contiene 29 conexiones entre ciudades. |
| Grafo conexo | Todas las ciudades están conectadas mediante al menos un camino. |
| Pesos positivos | Todos los pesos corresponden a distancias positivas en kilómetros. |
| Criterio único de ponderación | Todos los pesos representan distancia aproximada por carretera. |
| Datos organizados | Las conexiones, pesos, coordenadas y fuentes están almacenadas en `datos.csv`. |
| Interfaz gráfica | La aplicación permite interactuar mediante una ventana gráfica. |
| Selección de origen y destino | El usuario puede elegir ambas ciudades mediante menús desplegables. |
| Cálculo de ruta óptima | La ruta se calcula mediante el algoritmo de Dijkstra. |
| Secuencia de ciudades | La aplicación muestra el recorrido obtenido como una secuencia ordenada. |
| Costo total estimado | La aplicación muestra la distancia total acumulada en kilómetros. |
| Visualización del grafo | Las ciudades se muestran como nodos y las conexiones como aristas. |
| Ruta óptima distinguida | El camino calculado se resalta en rojo sobre el grafo. |
| Repositorio ejecutable | El repositorio incluye código fuente, datos, imagen del mapa, dependencias e instrucciones de ejecución. |

---

## Modelamiento del grafo

El proyecto utiliza un grafo ponderado definido como:

```text
G = (V, E, w)
```

Donde:

- `V` es el conjunto de vértices, representado por las ciudades.
- `E` es el conjunto de aristas, representado por las conexiones entre ciudades.
- `w` es la función de peso, que asigna una distancia positiva a cada conexión.

En este caso, el peso de cada arista representa la **distancia aproximada por carretera en kilómetros** entre dos ciudades conectadas. Por lo tanto, la distancia total de una ruta corresponde a la suma de los pesos de las aristas que forman ese camino.

El grafo se trabaja como **no dirigido**, ya que una conexión entre dos ciudades puede recorrerse en ambos sentidos. Por ejemplo, si existe una conexión entre `Seattle` y `San Francisco`, también se considera válida la conexión entre `San Francisco` y `Seattle`.

---

## Ciudades utilizadas

El grafo considera las siguientes 15 ciudades de Estados Unidos:

```text
Seattle, San Francisco, Los Angeles, Las Vegas, Phoenix,
Salt Lake City, Denver, Minneapolis, Chicago, Dallas,
Houston, New Orleans, Atlanta, Washington, New York
```

Estas ciudades fueron escogidas para cubrir distintas zonas geográficas del país: costa oeste, suroeste, centro, sur, medio oeste y costa este.

---

## Datos y fuentes

Los datos del grafo están almacenados en el archivo:

```text
datos.csv
```

Cada fila del archivo representa una conexión entre dos ciudades. El archivo contiene las siguientes columnas:

```text
origen,destino,peso,x_origen,y_origen,x_destino,y_destino,fuente
```

Significado de cada columna:

- `origen`: ciudad inicial de la conexión.
- `destino`: ciudad final de la conexión.
- `peso`: distancia aproximada en kilómetros.
- `x_origen`, `y_origen`: coordenadas visuales de la ciudad de origen en el mapa.
- `x_destino`, `y_destino`: coordenadas visuales de la ciudad de destino en el mapa.
- `fuente`: referencia usada para respaldar la distancia.

Las distancias fueron consultadas usando **Google Maps**, considerando rutas en automóvil entre las ciudades conectadas. Los valores se registraron como distancias aproximadas en kilómetros y fueron consultados el **29-06-2026**.

Referencia general utilizada:

```text
Google. (2026). Google Maps: rutas en automóvil entre ciudades de Estados Unidos.
Consultado el 29 de junio de 2026, en https://www.google.com/maps
```

---

## Algoritmo utilizado

El proyecto utiliza el **algoritmo de Dijkstra** para encontrar el camino de menor distancia entre una ciudad de origen y una ciudad de destino.

La implementación se encuentra en:

```text
algoritmo_dijkstra.py
```

El algoritmo trabaja con tres estructuras principales:

- `distancias`: guarda la menor distancia conocida desde el origen hasta cada ciudad.
- `anteriores`: guarda la ciudad previa desde donde se llegó a cada vértice, para reconstruir el camino final.
- `visitados`: guarda las ciudades que ya fueron procesadas.

Proceso general:

1. Todas las distancias comienzan en infinito, excepto la ciudad de origen, que comienza en 0.
2. Se selecciona la ciudad no visitada con menor distancia acumulada.
3. Se revisan sus vecinos y se actualizan las distancias si se encuentra una ruta más corta.
4. El proceso se repite hasta llegar al destino.
5. Finalmente, se reconstruye el camino usando el diccionario `anteriores`.

La implementación no utiliza librerías externas de grafos ni cola de prioridad, para que el funcionamiento del algoritmo sea directo y explicable.

---

## Interfaz gráfica

La interfaz gráfica está desarrollada con **CustomTkinter** y utiliza un `Canvas` de Tkinter para dibujar el grafo.

Desde la interfaz, el usuario puede:

1. Seleccionar una ciudad de origen.
2. Seleccionar una ciudad de destino.
3. Presionar el botón **Calcular ruta**.
4. Ver la ruta óptima como secuencia de ciudades.
5. Ver la distancia total acumulada.
6. Observar el grafo en el mapa, con la ruta óptima resaltada en rojo.

La visualización permite distinguir entre:

- Aristas normales: conexiones disponibles del grafo.
- Aristas rojas: conexiones que forman parte de la ruta óptima calculada.
- Nodos rojos: ciudades que pertenecen al camino encontrado.

---

## Estructura del proyecto

```text
Matematica_discreta/
├── main.py
├── datos_grafo.py
├── algoritmo_dijkstra.py
├── datos.csv
├── requirements.txt
├── README.md
└── assets/
    └── mapa_us.png
```

Descripción de archivos principales:

- `main.py`: contiene la interfaz gráfica, la visualización del grafo y la interacción con el usuario.
- `datos_grafo.py`: lee el archivo CSV y construye el grafo junto con las posiciones visuales de las ciudades.
- `algoritmo_dijkstra.py`: contiene la implementación manual del algoritmo de Dijkstra.
- `datos.csv`: contiene las conexiones, pesos, coordenadas visuales y fuentes.
- `requirements.txt`: indica las dependencias necesarias para ejecutar el programa.
- `assets/mapa_us.png`: imagen del mapa usada como fondo para la visualización.

---

## Requisitos

Para ejecutar el proyecto se necesita tener instalado Python 3 y la dependencia indicada en `requirements.txt`:

```text
customtkinter
```

---

## Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/PabloUrra2233/Matematica_discreta.git
```

Entrar a la carpeta del proyecto:

```bash
cd Matematica_discreta
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python main.py
```

---

## Ejemplo de uso

1. Seleccionar una ciudad de origen, por ejemplo `Las Vegas`.
2. Seleccionar una ciudad de destino, por ejemplo `Atlanta`.
3. Presionar **Calcular ruta**.
4. El programa muestra la secuencia de ciudades que forman la ruta óptima.
5. El programa muestra la distancia total en kilómetros.
6. La ruta se resalta visualmente en rojo sobre el grafo.

---

## Pruebas sugeridas para la demostración

Para verificar el funcionamiento de la aplicación se pueden realizar pruebas seleccionando distintas ciudades de origen y destino. En cada caso, la aplicación debe mostrar la ruta óptima, la distancia total y el recorrido resaltado en rojo sobre el grafo.

Ejemplos recomendados para la demostración:

- `Las Vegas` → `Atlanta`
- `Seattle` → `New York`
- `Houston` → `Washington`

---

## Relación con Matemática Discreta

Este proyecto aplica contenidos de grafos vistos en Matemática Discreta:

- Representación de grafos mediante vértices y aristas.
- Uso de grafos ponderados.
- Modelamiento de una red real mediante un grafo.
- Búsqueda de caminos mínimos.
- Aplicación del algoritmo de Dijkstra.
- Interpretación de pesos como distancias positivas.

---

## Integrante

- Pablo Urra

Proyecto final de Matemática Discreta.
