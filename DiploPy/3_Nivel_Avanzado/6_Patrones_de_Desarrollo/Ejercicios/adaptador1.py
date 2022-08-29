# -------------- CLIENTE -----------------------------------
class Motor():
    voltaje_minimo = 1.5
    voltaje_maximo = 3

    @classmethod
    def salida(cls, voltage_entrada):
        if  voltage_entrada > cls.voltaje_maximo:
            print("Con voltaje de entrada de : %s V Se quema!" %(voltage_entrada))
        elif voltage_entrada < cls.voltaje_minimo:
            print("Con voltaje de entrada de : %s V el Voltage es insuficiente!!!" %(voltage_entrada))
        else:
            print("Con voltaje de entrada de : %s V está funcionando" %(voltage_entrada))

    def prender(self, voltage_entrada):
        self.salida(voltage_entrada)
        
# ---------------FUENTE-------------------------------
class Fuente():
    voltaje_salida = None

class FuenteAr(Fuente):
    voltaje_salida = 220      

class FuenteVateria9V(Fuente):
    voltaje_salida = 9 

#------- CLASES ADAPTADORAS -------------------
class FuenteArAdapter():
    
    voltage_entrada = FuenteAr.voltaje_salida
    voltaje_salida = (Motor.voltaje_maximo + Motor.voltaje_minimo)/2

class FuenteVateria9VAdapter():
    
    voltage_entrada = FuenteAr.voltaje_salida
    voltaje_salida = (Motor.voltaje_maximo + Motor.voltaje_minimo)/2 

if __name__ == "__main__":    
 
    motor = Motor()
    print(motor.prender(FuenteAr.voltaje_salida))
    print(motor.prender(FuenteVateria9V.voltaje_salida))
    print('---'*25)
        
    print(motor.prender(FuenteArAdapter.voltaje_salida))
    print(motor.prender(FuenteVateria9VAdapter.voltaje_salida))
