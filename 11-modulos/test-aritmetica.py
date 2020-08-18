#import modulo_aritmetica as aritmetica
#No usar numero en nombres de archivos, ni "-"
#aritmetica = __import__('modulo-aritmetica')
#importar desde otro directorio
#from modules import modulo_aritmetica as aritmetica
import modules.modulo_aritmetica as aritmetica

resultado = aritmetica.sumar(1,2)
print(resultado)

resultado = aritmetica.restar(4, 6)
print(resultado)
