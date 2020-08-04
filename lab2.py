#Universidad del Valle de Guatemala
#Redes
#Juan Guillermo Sandoval Lacayo - 17577
#Otto Alexander Trujillo Contreras - 17189
#Laboratorio 2

#Importacion de librerias
from bitarray import bitarray
import socket

#Hola en ASCII es:
#0100 1000    0110 1111    0110 1100    0110 0001
#Todo junto
#01001000011011110110110001100001

'''
#Conexion
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT =  4000        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))

'''


#parte 1
def strToBinary(s):
    st = s
    return(' '.join(format(x, 'b') for x in bytearray(st, 'utf-8')))

def countTotalBits(num):
    TotalNumberBits = 0
    TotalBinary = []
    for a in num:
        if a == ' ':
            pass
        else:
            binary = bin(int(a))[2:]
            TotalNumberBits = TotalNumberBits + len(binary)
    print('Numero total de bits: ', TotalNumberBits)
     
final_message = []
key = True
while key == True:
    MessageA = str(input("Ingrese un texto a enviar: "))
    MessageA = strToBinary(MessageA)
    BinaryNumber = MessageA
    for a in MessageA:
        if a == ' ':
            pass
        else:
            final_message.append(int(a))
    MessageA = bitarray(final_message)
    key = False
    try:
        valor = str(MessageA)
    except:
        print('Mensaje Invalido')
        key = True
        pass

countTotalBits(BinaryNumber)
print(MessageA)

