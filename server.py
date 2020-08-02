#Universidad del Valle de Guatemala
#Redes
#Juan Guillermo Sandoval Lacayo - 17577
#Otto Alexander Trujillo Contreras - 17189
#Laboratorio 2

#Server

#Importacion de librerias
import socket


Host = '127.0.0.1'
Port = 4000
while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((Host, Port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
        exit()
