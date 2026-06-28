import customtkinter

Grafo = customtkinter.CTk()
def button_callback():
    print("button pressed")

def button_callback2():
    print("button pressed")

Grafo.title("Grafo")
self.checkbox_frame (self, values=["value 1", "value 2", "value 3"])

button = customtkinter.CTkButton(Grafo, text="my button", command=button_callback)
boton_Mostrar = customtkinter.CTkButton(Grafo, text="Mostrar Grafo", command=button_callback2)
boton_Mostrar.grid(row=1, column=0, padx=15, pady=(0,5))

Grafo.mainloop()