
class CinepolisFlaskMetodos():
    
    numeroCompradores=0
    numeroBoletos=0
    tarjeta=""
    total=0.0
    resultado=""
    
    def calculo(self):
        if self.numeroBoletos > (self.numeroCompradores*7):
            self.resultado= "Error, el limite de boletos son {}".format(self.numeroCompradores*7)
        else:
            if self.numeroBoletos > 5:
                descuento= 0.15
            elif self.numeroBoletos <=5 and self.numeroBoletos > 2:
                descuento=0.10
            elif self.numeroBoletos <=2:
                descuento=0.0
            self.total=(self.numeroBoletos*12)-((self.numeroBoletos*12)*descuento)  
            if self.tarjeta =="Si":
                self.total=self.total-(self.total*0.10)
            self.resultado="{}".format(self.total)
               


