marcas=["Audi\n","Alfa Romeo\n","BMW\n","Mercedes Benz\n"]
#Se abre en modo Write Extended, que permite lectura.
with open("marcas.txt","w+") as f:
 # Escribe cada elemento de la lista como una línea
 f.writelines(marcas)
 # Se va al inicio del archivo.
 f.seek(0,0)
 # Lee secuencialmente el archivo, desde el inicio.
 for linea in f:
    print(linea)