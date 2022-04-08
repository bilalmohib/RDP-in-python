#!/usr/bin/env python
# Client.py of 'Remote Desktop'

import pyautogui as pg
import socket

host = input('Host: ')  # as both code is running on same pc
port = int(input('Port: '))  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

####################################### Code For Screen Share #######################################
#This is the code for the client
from vidstream import ScreenShareClient
#Importing the thread
import threading

#Can find this using IPConfig in CMD
myPrivateIPv4Address = '192.168.43.168'
my_generated_port = port
#Sending the data as parameters and saving them in sender variable
sender = ScreenShareClient(myPrivateIPv4Address,my_generated_port)

#Send the stream thread to start sharing
t = threading.Thread(target=sender.start_stream)
t.start()

#If STOP is the call then break the loop and connection with the server
while input("") != 'STOP':
    continue

#To stop the client stream connected to the server
sender.stop_stream()
####################################### Code For Screen Share #######################################

message = 'done'
while True:
    try:
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response
            if data == 'click':
                pg.click(x, y)
            elif data == 'del':
                pg.typewrite(['backspace'])
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
            elif data=='rclick':
                pg.click(button='right')
            elif data=='dclick':
                pg.click(clicks=2)
            elif data=='nl':
                pg.typewrite(['enter'])
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)  # show in terminal
            message = 'done' # again take input

        client_socket.close()  # close the connection
    except:
        pass
# Created by vismodo: https://github.com/vismodo/
# Email: vismaya.atreya@outlook.com
# Repository: https://github.com/vismodo/Remote-Desktop (Remote Desktop)
# Python Version: 3.9