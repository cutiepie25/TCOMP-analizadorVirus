import tkinter as tk
import os
from tkinter import filedialog, messagebox
from controladores.admin_archivo import AdminArchivo
from controladores.analizador import Analizador

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("App Práctica I")
        self.bytes = None

        # Widgets
        self.label_titulo = tk.Label(root, text="Práctica I")
        self.label_titulo.pack()

        self.textbox_ruta = tk.Entry(root, width=50, state="readonly")
        self.textbox_ruta.pack()

        self.button_buscar = tk.Button(root, text="Buscar", command=self.buscar_archivo)
        self.button_buscar.pack()

        self.textbox_bytes = tk.Text(root, width=60, height=15, state="normal")
        self.textbox_bytes.pack()

        self.button_analizar = tk.Button(root, text="Analizar", state="disabled", command=self.analizar)
        self.button_analizar.pack()


    def buscar_archivo(self):
        archivo = filedialog.askopenfilename()
        if archivo:
            admin = AdminArchivo(archivo)
            self.bytes = admin.leer_bytes()

            # Mostrar ruta
            self.textbox_ruta.config(state="disabled")
            self.textbox_ruta.delete(0, tk.END)
            self.textbox_ruta.insert(0, archivo)
            self.textbox_ruta.config(state="disabled")

            # Mostrar bytes
            self.textbox_bytes.delete("1.0", tk.END)
            self.textbox_bytes.insert(tk.END, " ".join(str(b) for b in self.bytes))
            self.textbox_bytes.config(state="disabled")
            self.button_analizar.config(state="normal")
        else:
            messagebox.showerror("Error", "Debe seleccionar un archivo!")

    def analizar(self):
        if self.bytes:
            analizador = Analizador(self.bytes)
            virus, estado = analizador.analizar()
            nombre_archivo = os.path.basename(self.textbox_ruta.get())

            if virus:
                mensaje = (
                    f"Nombre del archivo: {nombre_archivo}\n"
                    f"Contenido en bytes: {len(self.bytes)} bytes\n"
                    f"Virus detectado: {virus}\n"
                    f"Estado final alcanzado: q{estado}"
                )
            else:
                mensaje = (
                    f"Nombre del archivo: {nombre_archivo}\n"
                    f"Contenido en bytes: {len(self.bytes)} bytes\n"
                    f"Virus detectado: No encontrado\n"
                    f"Estado en el que se detuvo: q{estado}"
                )

            from tkinter import messagebox
            messagebox.showinfo("Resultado del análisis", mensaje)

