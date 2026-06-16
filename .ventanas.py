import tkinter as tk
from tkinter import messagebox
from servicios import *
import random

pregunta_actual = random.choice(preguntas)

texto_pregunta = pregunta_actual["pregunta"]
opciones = pregunta_actual["opciones"]
respuesta_correcta = pregunta_actual["respuesta_correcta"]

def abrir_ventana_login():
    
    def ingresar():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()
        respuesta = respuesta_usuario.get()

        resultado = validaciones_login(
            usuario, 
            contrasena, 
            respuesta, 
            pregunta_actual
            )

        if resultado == True:
            ventana.destroy()
            abrir_ventana_principal()
        else:
            messagebox.showerror("Errores", "\n".join(resultado))
            return

    def registrarse():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()
        respuesta = respuesta_usuario.get()

        resultado = validaciones_registro(
            usuario,
            contrasena,
            respuesta, 
            pregunta_actual
            )

        if resultado == True:
            ventana.destroy()
            abrir_ventana_principal()
        else:
            messagebox.showerror("Errores", "\n".join(resultado))
            return

    ventana = tk.Tk()
    ventana.title("Login")
    ventana.geometry("600x500")

    etiqueta_usuario = tk.Label(
        ventana,
        text="Usuario"
        )
    etiqueta_usuario.pack()

    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.pack()

    etiqueta_contrasena = tk.Label(
        ventana,
        text="Contraseña"
        )
    etiqueta_contrasena.pack()

    entrada_contrasena = tk.Entry(
        ventana, 
        show="*")

    entrada_contrasena.pack()

    etiqueta_usuario = tk.Label(
        ventana, 
        text=texto_pregunta
        )
    etiqueta_usuario.pack()

    respuesta_usuario = tk.StringVar()

    etiqueta_pregunta = tk.Label(
        ventana,
        text=pregunta_actual["pregunta"]
    )
    etiqueta_pregunta.pack()

    for opcion in pregunta_actual["opciones"]:
        boton_opcion = tk.Radiobutton(
            ventana,
            text=opcion,
            variable=respuesta_usuario,
            value=opcion[0]
        )
        boton_opcion.pack(anchor="w")

    boton_ingresar = tk.Button(
        ventana,
        text="Ingresar",
        command=ingresar
)
    boton_ingresar.pack()

    boton_registro = tk.Button(
        ventana,
        text="Registrarse",
        command=registrarse
    )
    boton_registro.pack()

    ventana.mainloop()

def abrir_ventana_principal():
    ventana = tk.Tk()
    ventana.title("Chatbot")
    ventana.geometry("400x500")

    ventana.mainloop()




