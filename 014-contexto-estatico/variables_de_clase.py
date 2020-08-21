class MiClase:
    #esta variable se asocia con la clase y no con el objeto
    variableClase = "variable de clase"
    #definimos un atributo de instancia, se asocia a objeto y no clase
    def __init__(self, nombre):
        #se asocia con los objetos a crear, variable de clase fuera de cualquier metodo
        #pero dentro de la clase
        self.nombre = nombre
        
#para acceder a las variables de clase no es necesario crear objetos
print(MiClase.variableClase)
objeto1 = MiClase("variable de instancia")
MiClase.nombre = "modificando variable instancia"
#podemos acceder a variables de instacia con el nombre de la clase u objetos
#solo aplica cuando se hizo alguna modificacion, asi es que se asocia
print(MiClase.nombre)
print(objeto1.nombre)
#podemos acceder a variables de clase a traves de los objetos
print(objeto1.variableClase)
#podemos acceder a las variables de la clase con el nombre de la clase
print(MiClase.variableClase)
objeto1.variableClase = "modificando variable de clase"
#esta modificacion solo se asocia a este objeto
print(objeto1.variableClase)
#el valor sigue siendo el mismo
print(MiClase.variableClase)
#usa el mismo valor de la clase
objeto2 = MiClase("Nuevo valor de variable de instancia")
print(objeto2.variableClase)

objeto3 = MiClase("valor de tercer objeto")

#todos los objetos veran este cambio excepto los que cambiaron el valor original
MiClase.variableClase = "Cambio desde la clase"
#consulta el valir de su propio objeto
print(objeto1.variableClase)
#consultan el valir de la variable de la clase
print(objeto2.variableClase)
print(objeto3.variableClase)