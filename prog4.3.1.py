Datos=[]
with open("agenda.csv","r+") as f:
 for linea in f:
    lista=linea.split("|")
    lista[2]=lista[2].replace