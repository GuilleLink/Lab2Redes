#Universidad del Valle de Guatemala
#Redes
#Juan Guillermo Sandoval Lacayo - 17577
#Otto Alexander Trujillo Contreras - 17189
#Laboratorio 2

import socket
import pickle

HOST = '127.0.0.1'
PORT = 4000



def BinaryToDecimal(binary):  
         
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)   

#Receptor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = s.recv(1024)
    while msg:
        mensaje = pickle.loads(msg)
        print(mensaje) 
        msg = s.recv(1024) 
        
    # initializing a empty string for  
    # storing the string data 
    str_data =' '
    print(len(mensaje))
    # slicing the input and converting it  
    # in decimal and then converting it in string 
    for i in range(0, len(mensaje), 7): 
        
        # slicing the bin_data from index range [0, 6] 
        # and storing it as integer in temp_data 
        temp_data = int(mensaje[i:i + 7]) 
        
        # passing temp_data in BinarytoDecimal() fuction 
        # to get decimal value of corresponding temp_data 
        decimal_data = BinaryToDecimal(temp_data) 
        
        # Deccoding the decimal value returned by  
        # BinarytoDecimal() function, using chr()  
        # function which return the string corresponding  
        # character for given ASCII value, and store it  
        # in str_data 
        str_data = str_data + chr(decimal_data)  
    
    # printing the result 
    print("El mensaje es: \n",  str_data) 

    s.close()