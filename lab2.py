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
#parte 1 - STRING -> BINARY -> BITARRAY // Buscar ruido 
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
    return TotalNumberBits

#parte 2 - Algoritmo de deteccion y correcion
#Algoritmo de Hamming
def Calcular_Reduccion_Bits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def Redundancia_Bits(data, r): 
    j = 0
    k = 1
    m = len(data) 
    res = ''  
    for i in range(1, m + r+1): 
        if(i == 2**j): 
            res = res + '0'
            j += 1
        else: 
            res = res + data[-1 * k] 
            k += 1
    return res[::-1]

def Calcular_Paridad_Bits(arr, r): 
    n = len(arr) 
    for i in range(r): 
        val = 0
        for j in range(1, n + 1):  
            if(j & (2**i) == (2**i)): 
                val = val ^ int(arr[-1 * j]) 
        arr = arr[:n-(2**i)] + str(val) + arr[n-(2**i)+1:] 
    return arr 

def Detectar_Error(arr, nr): 
    n = len(arr) 
    res = 0
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
        res = res + val*(10**i)
    return int(str(res), 2) 

# Parte Final - Poner todo a funcionar  
final_message = []
BinaryNumberString = ''
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
for u in BinaryNumber:
    if u == ' ':
        pass
    else:
        BinaryNumberString = BinaryNumberString + u

TotalBits = countTotalBits(BinaryNumber)
print('Numero de bits: ', TotalBits, '\n')
print('Bitarray: ', MessageA, '\n')
print('Numero binario: ', BinaryNumber, '\n')

#Aplicar Hamming
r = Calcular_Reduccion_Bits(TotalBits)
arr = Redundancia_Bits(BinaryNumberString, r)
arr = Calcular_Paridad_Bits(arr, r)
print("La Data transferida es " + arr, '\n')
correction = Detectar_Error(arr, r) 
print("La posicion del error es " + str(correction))

