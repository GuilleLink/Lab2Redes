
import bitarray
import random



#def strToBinary(s):
#    st = s
#    return(' '.join(format(x, 'b') for x in bytearray(st, 'utf-8')))
#
#mensaje = str('hola')
#Errors = 2
#
#mensaje = bin(int.from_bytes(mensaje.encode(), 'big'))
#
#print(mensaje)
#for bit in range(0, len(mensaje)):
#    if (Errors > 0):
#        randomBitChanged = random.randint(0, 1)
#        #Si es 1 cambia el bit si todavia hay bits por cambiar
#        if (randomBitChanged == 1):     
#            print(mensaje[bit])       
#            if (mensaje[bit] == '0'):
#                Errors -= 1
#                mensaje[bit] = '1'
#            elif (mensaje[bit] == '1'):
#                Errors -= 1
#                #print(mensaje[bit])
#                mensaje[bit] = '0'
#                #sprint(mensaje[bit])
#        else:
#            pass
#
#print(mensaje)


s = 'Hello'.encode('UTF-8')
print(s)



