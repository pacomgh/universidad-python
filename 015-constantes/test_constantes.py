from constantes import CONSTANTE
#importamos por separado las constantes si queremos renombrar el nombre de la clase
from constantes import Matematicas as mate

print(CONSTANTE)
#para acceder una constante definida en una clase debemos acceder a ella
#a traves del nombre de la clase
#print(Matematicas.PI)
print(mate.PI)

#modificamos el valor de la constante
CONSTANTE = "nuevo valor de la constante"
mate.PI=3.14
print(CONSTANTE)
print(mate.PI)