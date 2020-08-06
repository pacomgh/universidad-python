#clase con las operaciones basicas
#si comentamos con triple comllas el comentario forma parte de la documentacion
"""Clase aritmetica para realizar las operaciones sumar, restar, etc"""
class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    #definimos metodo, inici minuscula, primer parametro = self
    #debe ir dentro de la clase
    #no le mandamos parametros al metodo porque usamos los atributos de la clase
    def sumar(self):
        #usamos los atibutos de la clase llamandolos con self
        """ realizamos la opreacion con los atributos de la clase """
        return self.operando1 + self.operando2
    
    def restar(self):
        """realiza la operacion de resta"""
        return self.operando1 - self.operando2
    
    def dividir(self):
        """realiza la operacion de division"""
        return self.operando1 / self.operando2
    
    def multiplicar(self):
        """realiza la operacion de multiplicacion"""
        return self.operando1 * self.operando2
    
#creamos objeto de la clase
#self es pasado de manera automatica
aritmetica = Aritmetica(2,4)
print("resultado de la suma:", aritmetica.sumar())
print("resultado de la resta:", aritmetica.restar())
print("resultado de la multiplicacion:", aritmetica.multiplicar())
print("resultado de la division:", aritmetica.dividir())
        
