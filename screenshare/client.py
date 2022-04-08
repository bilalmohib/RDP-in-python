####################################### Code For Screen Share #######################################
#This is the code for the client
from vidstream import ScreenShareClient
#Importing the thread
import threading

#Can find this using IPConfig in CMD
myPrivateIPv4Address = '192.168.43.168'
my_generated_port = 9999
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