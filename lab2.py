#Universidad del Valle de Guatemala
#Redes
#Juan Guillermo Sandoval Lacayo - 17577
#Otto Alexander Trujillo Contreras - 17189
#Laboratorio 2



#Importacion de librerias
from bitarray import bitarray


SentMessage = bitarray()

#Hola en ASCII es:
#0100 1000    0110 1111    0110 1100    0110 0001
#Todo junto
#01001000011011110110110001100001

#parte 1 

MessageA = input("Ingrese un texto a enviar")
try:
    valor = str(MessageA)
except ValueError:
    print('Mensaje invalido')
    negacion = 1
    pass
while negacion == 1:
    MessageA = input("Ingrese un texto a enviar")
    negacion = 2
    try:
        valor = str(MessageA)
    except ValueError:
        print('Mensaje invalido')
        negacion = 1
        pass

MessageABinary = bitarray(MessageA)

print(MessageABinary)
print("HOLAA")
