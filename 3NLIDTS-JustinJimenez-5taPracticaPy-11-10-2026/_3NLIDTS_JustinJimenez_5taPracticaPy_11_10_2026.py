import tkinter as tk
from tkinter import messagebox
import re

ventana = tk.Tk()
ventana.configure(bg="pink")
ventana.geometry("350x550")
ventana.title("Actividad 04 - Formulario de Registro Vr. 001")

rbSeleccionGenero = tk.IntVar()

tk.Label(ventana, text="Nombre:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack()

tk.Label(ventana, text="Apellidos:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbApellidos = tk.Entry(ventana, width=35, justify="center")
tbApellidos.pack()

tk.Label(ventana, text="Edad:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbEdad = tk.Entry(ventana, width=10, justify="center")
tbEdad.pack()

tk.Label(ventana, text="Estatura:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbEstatura = tk.Entry(ventana, width=15, justify="center")
tbEstatura.pack()

tk.Label(ventana, text="Telefono:", font=("Segoe UI", 14, "bold")).pack(padx=10, pady=8)
tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack()

gb = tk.LabelFrame(ventana, text="Selecione un Genero", padx=10, pady=8)
gb.pack(padx=10, pady=8)
rbMasculino = tk.Radiobutton(gb, text="Masculino", value=1, variable=rbSeleccionGenero)
rbMasculino.grid(column=1, row=1)
rbFemenino = tk.Radiobutton(gb, text="Femenino", value=2, variable=rbSeleccionGenero)
rbFemenino.grid(column=2, row=1)
rbNoDefinido = tk.Radiobutton(gb, text="No Definido", value=3, variable=rbSeleccionGenero)
rbNoDefinido.grid(column=3, row=1)

gb2 = tk.LabelFrame(ventana, text="")
gb2.pack(padx=10, pady=8)
btnGuardar = tk.Button(gb2, text="Guardar", width=10, padx=10, pady=8)
btnGuardar.grid(column=1, row=1)
btnBorrar = tk.Button(gb2, text="Borrar", width=10, padx=10, pady=8)
btnBorrar.grid(column=2, row=1)

ventana.mainloop()

