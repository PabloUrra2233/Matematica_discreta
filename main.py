import customtkinter as ctk
from tkinter import Canvas, PhotoImage

from datos_grafo import cargar_grafo
from algoritmo_dijkstra import dijkstra

def dibujar_grafo(camino=None):
    canvas.delete("all")

    if imagen_fondo is not None:
        canvas.create_image(0, 0, image=imagen_fondo, anchor="nw")

    if camino is None:
        camino = []
    aristas_camino = []

    for i in range(len(camino) - 1):
        aristas_camino.append((camino[i], camino[i + 1]))
        aristas_camino.append((camino[i + 1], camino[i]))

    dibujadas = set()

    for origen in grafo:
        for destino in grafo[origen]:
            if (destino, origen) in dibujadas:
                continue

            x1, y1 = posiciones[origen]
            x2, y2 = posiciones[destino]

            if (origen, destino) in aristas_camino:
                color = "#ff1f1f"
                grosor = 5
            else:
                color = "#303030"
                grosor = 2

            canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                width=grosor
            )
            if (origen, destino) in aristas_camino:
                peso = grafo[origen][destino]
                x_medio = (x1 + x2) // 2
                y_medio = ((y1 + y2) // 2) - 12

                canvas.create_text(
                    x_medio,
                    y_medio,
                    text=f"{peso} km",
                    fill="black",
                    font=("Arial", 10, "bold")
                )
            dibujadas.add((origen, destino))

    for ciudad in posiciones:
        x, y = posiciones[ciudad]

        if ciudad in camino:
            color_nodo = "#ff4d4d"
        else:
            color_nodo = "#ffffff"

        canvas.create_oval(
            x - 15,
            y - 15,
            x + 15,
            y + 15,
            fill=color_nodo,
            outline="#000000",
            width=2
        )

        nombre = ciudad

        canvas.create_text(
            x,
            y - 28,
            text=nombre,
            fill="#000000",
            font=("Arial", 9, "bold")
        )


def calcular_ruta():
    origen = combo_origen.get()
    destino = combo_destino.get()

    if origen == "" or destino == "":
        texto_resultado.configure(text="Selecciona origen y destino.")
        return

    if origen == destino:
        texto_resultado.configure(text="El origen y destino son iguales.")
        dibujar_grafo([origen])
        return

    camino, distancia = dijkstra(grafo, origen, destino)

    ruta_texto = " → ".join(camino)

    texto_resultado.configure(
        text=f"Ruta óptima:\n{ruta_texto}\n\nDistancia total: {distancia} km"
    )

    dibujar_grafo(camino)


grafo, posiciones = cargar_grafo()
ciudades = sorted(grafo.keys())

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Ruta óptima entre ciudades")
ventana.geometry("1000x820")

titulo = ctk.CTkLabel(
    ventana,
    text="Ruta óptima entre ciudades mediante grafos ponderados",
    font=("Arial", 22, "bold")
)
titulo.pack(pady=15)

panel = ctk.CTkFrame(ventana)
panel.pack(pady=10)

label_origen = ctk.CTkLabel(panel, text="Origen:")
label_origen.grid(row=0, column=0, padx=10, pady=10)

combo_origen = ctk.CTkComboBox(panel, values=ciudades, width=220)
combo_origen.grid(row=0, column=1, padx=10, pady=10)

label_destino = ctk.CTkLabel(panel, text="Destino:")
label_destino.grid(row=0, column=2, padx=10, pady=10)

combo_destino = ctk.CTkComboBox(panel, values=ciudades, width=220)
combo_destino.grid(row=0, column=3, padx=10, pady=10)

boton = ctk.CTkButton(
    panel,
    text="Calcular ruta",
    command=calcular_ruta
)
boton.grid(row=0, column=4, padx=10, pady=10)

texto_resultado = ctk.CTkLabel(
    ventana,
    text="Selecciona una ciudad de origen y una ciudad de destino.",
    font=("Arial", 15),
    wraplength=900
)
texto_resultado.pack(pady=10)

canvas = Canvas(
    ventana,
    width=1448,
    height=939,
)
canvas.pack(pady=10)

try:
    imagen_fondo = PhotoImage(file="assets/mapa_us.png")
except:
    imagen_fondo = None

dibujar_grafo()

ventana.mainloop()