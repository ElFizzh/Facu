#PROBLEMA COMPUESTO 2
class Operaciones:
    def __init__(self):
        self.valor = int(input("ingrese el primer valor"))
        self.valor2 = int(input("ingrese el segundo valor"))

    def sumar(self):
        suma = self.valor + self.valor2
        print("La suma es", suma)
    
    def restar(self):
        resta = self.valor - self.valor2
        print("la resta es", resta)
    
    def multiplicar(self):
        multi = self.valor * self.valor2
        print("La mutliplicacion es", multi)
   
    def dividir(self):
        divi = self.valor / self.valor2
        print("La division es", divi)

# Bloque principal
operacion1 = Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.dividir()
    
