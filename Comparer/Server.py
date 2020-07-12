import socket
import cv2
import numpy as np
import imageCompare

class server:
    def __init__(self, PORT):
        self.serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serv_sock.bind(('', PORT))
        self.serv_sock.listen(10)

    def Receive(self):
        data = 0
        while data == 0:
            data = self.client_sock.recv(1024 * 1024)
            break
            # Клиент отключился
        self.Image = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_GRAYSCALE)
        return self.Image

    def Close_Socket(self):
        self.client_sock.close()

    def Start_Socket(self):
        self.client_sock, self.client_addr = self.serv_sock.accept()
        print('Connected by', self.client_addr)


while True:
    image_server = server(33210)
    image_server.Start_Socket()


    while True:

        image = image_server.Receive()
        imageDif = image_server.Receive()

        Distance = imageCompare.Work(image, imageDif)
        print(Distance.HammingDistance())

image_server.Close_Socket()

