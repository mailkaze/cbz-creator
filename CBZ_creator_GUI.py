from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import zipfile

class App:
    def __init__(self, ventana):
        #constructor de la ventana
        self.ventana = ventana
        self.ventana.title('Crear archivo CBZ')

        ventana = LabelFrame(self.ventana)
        ventana.grid(row=0, column=0, columnspan=3, pady=5)

        Label(ventana, text='Ruta de la carpeta contenedora:                                         ').grid(
            row=0, column=0)
        self.ruta = Entry(ventana)
        self.ruta.focus()
        self.ruta.grid(row=1,column=0, sticky=W + E)
        ttk.Button(ventana, text='Buscar', command=self.buscar_carpeta).grid(
            row=1, column=1)
        ttk.Button(ventana, text='Empaquetar', command=self.crear_lista).grid(
            row=2, column=0, columnspan=2, sticky=W + E)
        self.mensaje = Label(ventana, text='', fg='green')
        self.mensaje.grid(row=3, column=0, columnspan=2, sticky=W + E)
        self.lista = []

    def buscar_carpeta(self):
        ruta_carpeta = filedialog.askdirectory()
        self.ruta.delete(0, END)
        self.ruta.insert(END, ruta_carpeta)

    def crear_lista(self):
        """Busca todos los archivos en la carpeta
        especificada y almacena en una lista 
        los nombres de los que sean imágenes."""
        self.mensaje['text'] = ''
        if self.ruta.get() == '':
            self.mensaje['text'] = 'Debes escribir la ruta de la \ncarpeta que contiene las imágenes.'
            return
        try:
            for archivo in os.listdir(self.ruta.get()):
                if archivo.endswith(".jpg") or archivo.endswith(".png"):
                    self.lista.append(archivo)
            self.addZeros()
        except:
            self.mensaje['text'] = "No se ha encontrado esa carpeta."

    def addZeros(self):
        #TODO arreglar con regular expressions
        self.mensaje['text'] = ''
        renombrados = []
        numeros = "1234567890"
        for file in self.lista:
            nuevo_nombre = ""
            nom, ext = file.split(".")
            for char in nom:
                if char in numeros:
                    nuevo_nombre += char
                else:
                    break
            nuevo_nombre = "0" * (4 - len(nuevo_nombre)) + nuevo_nombre + "." + ext
            renombrados.append(nuevo_nombre)
        try:
            os.chdir(self.ruta.get())
            for i in range(len(self.lista)):
                os.rename(self.lista[i], renombrados[i])
            self.mensaje['text'] = "Los archivos se renombraron con éxito."
            self.crear_cbz(renombrados)
        except:
            self.mensaje['text'] = "No se pudieron renombrar los archivos."

    def crear_cbz(self, renombrados):
        self.mensaje['text'] = ''
        nombre = self.ruta.get().split("\\")[-1] + ".cbz"
        zip = zipfile.ZipFile(nombre, "w", zipfile.ZIP_DEFLATED)
        for file in renombrados:
            zip.write(file)
        self.mensaje['text'] = "El archivo CBZ fue creado con éxito."

if __name__ == '__main__':
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()