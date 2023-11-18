Datos=[]
# Se lee el archivo de forma secuencial, y se agregan los elementos
# a la lista.
with open("agenda.csv","r") as f:
 # Se lee secuencialmente el archivo de texto.
 for linea in f:
 # Se toma el texto de la línea leída, y se divide tomando como separador
 # el caracter pipe. La función retorna una lista, donde cada parte del
 # texto es un elemento.
    lista=linea.split("|")
 # El último elemento contiene \n como salto de linea. Se remplaza por nada.
 lista[2]=lista[2].replace("\n","")
 Datos.append(lista)

# Se revisa el contenido de la lista
print(">> Contenido de la nueva lista.\n")
print(Datos)