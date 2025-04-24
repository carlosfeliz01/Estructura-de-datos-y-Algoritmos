import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Hola Mundo", "¡Hola, mundo!")


# Hey there! This is a simple GUI application that displays a message box with "¡Hola, mundo!" 
# when run. It uses the tkinter library to create the GUI elements. 
# The function `mostrar_mensaje` is called to show the message box when the script is executed. 
# You can customize the message and title as needed. Enjoy coding!

# Crear la ventana principal
ventana = tk.Tk()# Crear una instancia de Tk
ventana.title("Hola Mundo")# Titulo de la ventana
ventana.geometry("300x200")# Tamaño de la ventana
ventana.configure(bg="lightblue")# Color de fondo de la ventana


# Crear un botón que muestre el mensaje al hacer clic
boton_saludos = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton_saludos.pack(pady=20)  # Añadir el botón a la ventana y centrarlo

# Iniciar el bucle principal de la aplicación
ventana.mainloop()# Mantener la ventana abierta hasta que el usuario la cierre

