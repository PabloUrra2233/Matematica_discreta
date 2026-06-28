import customtkinter

ventana = customtkinter.CTk()
ventana.title("Ruta óptima entre ciudades")
ventana.geometry("500x300")

titulo = customtkinter.CTkLabel(
    ventana,
    text="Ruta óptima entre ciudades"
)
titulo.pack(pady=20)

boton = customtkinter.CTkButton(
    ventana,
    text="Calcular ruta"
)
boton.pack(pady=10)

ventana.mainloop()