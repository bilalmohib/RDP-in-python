#Code for the server

from vidstream import StreamingServer
import threading

#Can find this using IPConfig in CMD
myPrivateIPv4Address = '192.168.43.168'
my_generated_port = 9999
#Sending the data as parameters and saving them in receiver variable
receiver = StreamingServer(myPrivateIPv4Address,my_generated_port)

t = threading.Thread(target=receiver.start_server)

t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()