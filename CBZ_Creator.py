import os
import zipfile

archivos = []
ruta = ""

def crear_lista(ru, li):
    """Busca todos los archivos en la carpeta
       especificada y almacena en una lista 
       los nombres de los que sean imágenes."""
    try:
        for archivo in os.listdir(ru):
            if archivo.endswith(".jpg") or archivo.endswith(".png"):
                li.append(archivo)
    except:
        print("No se ha encontrado la carpeta especificada.")

def addZeros(arch, ru):
    renombrados = []
    numeros = "1234567890"
    for file in arch:
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
        os.chdir(ru)
        for i in range(len(arch)):
            os.rename(arch[i], renombrados[i])
        print("Los archivos se renombraron con éxito.")
        crear_cbz(renombrados, ruta)
    except:
        print("No se pudieron renombrar los archivos.")

def crear_cbz(arch, ru):
    nombre = ru.split("\\")[-1] + ".cbz"
    zip = zipfile.ZipFile(nombre, "w", zipfile.ZIP_DEFLATED)
    for file in arch:
        zip.write(file)
    print("El archivo CBZ fue creado con éxito.")

ruta = input("Pega aquí la ruta de la carpeta contenedora: ")
crear_lista(ruta, archivos)
addZeros(archivos, ruta)