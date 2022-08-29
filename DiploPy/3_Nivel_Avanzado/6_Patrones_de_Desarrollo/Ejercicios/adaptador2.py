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

class ImposibleTransformaVoltage(Exception):
    pass

class MotorAdapter(Motor, Fuente):

    @classmethod
    def convertir_voltaje(cls, voltage_entrada):
        if voltage_entrada == cls.voltaje_salida: #Se está fijango en las fuentes
            return ((cls.voltaje_maximo + cls.voltaje_minimo)/2)

        else:
            raise ImposibleTransformaVoltage(
                "No se puede transformar {0} en {1}V. Este adaptador transforma:  {2} en {1}V.".format(
                    voltage_entrada, ((cls.voltaje_maximo + cls.voltaje_minimo)/2), cls.voltaje_salida
                )
            )

    @classmethod
    def prender(cls, voltage_entrada):
        try:
            voltage = cls.convertir_voltaje(voltage_entrada)
            #print(voltage)
            cls.salida(voltage)
        except ImposibleTransformaVoltage as e:
            print(e)

class FuenteArAdapter(MotorAdapter, FuenteAr):
    pass

class FuenteVateria9VAdapter(MotorAdapter, FuenteVateria9V):
    pass

if __name__ == "__main__":    
 
    print('---'*25)
    motor_220 = FuenteArAdapter()
    print(motor_220.prender(FuenteAr.voltaje_salida) )       
    print(motor_220.prender(FuenteVateria9V.voltaje_salida))
