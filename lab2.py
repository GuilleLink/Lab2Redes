#Universidad del Valle de Guatemala
#Redes
#Juan Guillermo Sandoval Lacayo - 17577
#Otto Alexander Trujillo Contreras - 17189
#Laboratorio 2

#Importacion de librerias
from bitarray import bitarray
import matplotlib.pyplot as plt 
import random
import socket
import pickle

#Para las gráficas
DetList = []
CorList = []
ErrList = []
msgSize = []

def graficar(lista1, lista2, lista1T, lista2T, titulo):
    plt.plot(lista1, lista2)
    plt.xlabel(lista1T)
    plt.ylabel(lista2T)
    plt.title(titulo)
    plt.show()

#Recibe el mensaje y la cantidad de errores a introducir
def  insertErrorMessage(mensaje, Errors):
    for bit in len(mensaje):
        if (Errors > 0):
            randomBitChanged = random.randint(0, 2)
            #Si es 1 cambia el bit si todavia hay bits por cambiar
            if (randomBitChanged == 1):
                if (bit == 0):
                    bit = 1
                elif (bit == 1):
                    bit = 0
            else:
                pass
        else:
            break

    return mensaje

def strToBinary2(msg):
    msgB = bin(int.from_bytes(msg.encode(), 'big'))
    msgB = msgB.replace("b","")
    msgB = bitarray(msgB)
    msgB = pickle.dumps(msgB)
    return msgB


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
#Algoritmo de Fletcher Sumcheck


def FletcherSumCheck(mensajeB):

    sumabin = int("0b00000000", 2)

    for letra in mensajeB:
        binarioActual = int(letra, 2)
        integer_sum = int(sumabin, 2) + int(binarioActual, 2)
        sumabin = bin(integer_sum)

    print(sumabin)
    print(~sumabin)


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


#-----------------------------------------------------

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
#Conexion y envio de mensaje entre sockets (corregido/no server)
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT =  4000        # The port used by the server

cont = True

while cont == True:
    print('Seleccione una opcion \n')
    print('1. Enviar mensaje')
    #print('2. Hacer graficos')
    print('2. salir')
    try:
        opt = input()
        opt = int(opt)
    except:
        print('No escribio un numero')
    if(opt == 1):
        mensaje = str(input("Ingrese su mensaje: \n"))
        try:
            #noise = int(input('Ingrese cuanto ruido desea ingresar en numeros \n'))
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', PORT))
                s.listen()
                conn, addr = s.accept()
                mensajeB = strToBinary2(mensaje)
                #mensajeE = insertErrorMessage(mensajeB, noise)

                conn.send(mensajeB)
                print('Message Sent')
                msgSize.append(len(mensaje))
                ErrList.append(noise)
                conn.close()

        except:
            #print(noise)
            print('Ha cometido un error, el ruido solo puede ser numeros')

    #elif(opt == 2):
    #    graficar(msgSize, ErrList, 'Size Message', 'Errors included', 'Message/Errors')
    #    graficar(ErrList, DetList, 'Errores', 'Errores detectados', 'Errors/Detected')
    #    graficar(ErrList, CorList, 'Errores', 'Errores corregidos', 'Errors/Corrected')
#
    elif(opt == 2):
        cont = False
        break

    else:
        print('No escribio una opcion valida')




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




