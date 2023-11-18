class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        print("coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrante")
        else:
            if self.x<0 and self.y>0:
                print("segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("cuarto cuadrante")

#Bloque principal

punto1=Punto(100,2)
punto1.imprimir()
punto1.imprimir_cuadrante()