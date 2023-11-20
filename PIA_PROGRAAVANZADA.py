class Tres_programas:
    def __init__(self, compra):
        self.compra = compra
        self.pagar = 0

    def descuento_clientes(self):
        if self.compra <= 500:
            self.pagar = self.compra
        elif 500 < self.compra <= 1000:
            self.pagar = self.compra * 0.95
        elif 1000 < self.compra <= 7000:
            self.pagar = self.compra * 0.89
        elif 7000 < self.compra <= 15000:
            self.pagar = self.compra * 0.82
        else:
            self.pagar = self.compra * 0.75
        return self.pagar

    def dinosaurio(self, nom, pes, lon):
        tonelada_a_kilogramos = 1000
        pie_a_metros = 0.3047
        self.nom = nom
        self.pes = pes
        self.lon = lon
        self.peskil = pes * tonelada_a_kilogramos
        self.lonmet = lon * pie_a_metros
        return f"Nombre: {self.nom}, Peso en Kilogramos: {self.peskil}, Longitud en Metros: {self.lonmet}"

    def gasolina(self, gal):
        galon_a_litros = 3.785
        precio_litro = 8.20
        self.gal = gal
        self.total = gal * galon_a_litros * precio_litro
        return self.total

    def archivos_texto(self):
        #pendiente xq no se que poner
        pass

#BLOQUE PRINCIPAAAAAAAAAAAAAAL
compra_objeto = Tres_programas(12550.00)
print(f"Resultado descuento_clientes: {compra_objeto.descuento_clientes()}")

dino_objeto = Tres_programas(0)  # El valor no es relevante aquí
print(dino_objeto.dinosaurio("TYRANNOSAURUS", 9, 40))

gasolina_objeto = Tres_programas(19.90)
print(f"Resultado gasolina: {gasolina_objeto.gasolina(20.90)}")
