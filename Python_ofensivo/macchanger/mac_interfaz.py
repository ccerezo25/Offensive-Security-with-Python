import tkinter as tk
from tkinter import messagebox
import subprocess
import re

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^[e][n][t][s][h]\d{1,2}$', interface)
    is_valid_mac_address = re.match(r'^[0-9A-Fa-f]{2}([-:])[0-9A-Fa-f]{2}(\1[0-9A-Fa-f]{2}){4}$', mac_address)
    return is_valid_interface and is_valid_mac_address

def change_mac_address():
    interface = interface_entry.get()
    mac_address = mac_entry.get()
    
    if is_valid_input(interface, mac_address):
        try:
            subprocess.run(["ifconfig", interface, "down"])  # Comandos en Linux
            subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])  # Comandos en Linux
            subprocess.run(["ifconfig", interface, "up"])
            messagebox.showinfo("Éxito", "Dirección MAC cambiada exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cambiar la dirección MAC: {str(e)}")
    else:
        messagebox.showerror("Error", "Datos inválidos. Verifique la interfaz y la dirección MAC.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cambiar Dirección MAC")
root.geometry("400x200")

# Etiquetas y entradas
interface_label = tk.Label(root, text="Interfaz de red:")
interface_label.pack()
interface_entry = tk.Entry(root)
interface_entry.pack()

mac_label = tk.Label(root, text="Nueva dirección MAC:")
mac_label.pack()
mac_entry = tk.Entry(root)
mac_entry.pack()

# Botón para cambiar la MAC
change_button = tk.Button(root, text="Cambiar MAC", command=change_mac_address)
change_button.pack()

# Iniciar la interfaz gráfica
root.mainloop()
