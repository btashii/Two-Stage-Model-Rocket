import socket 

#socket.AF_INET is IPV4 address 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#hostname that you get by doing "hostname -I"
hostname = '10.0.0.5'
#Designated Port
port = 12345  
s.bind((hostname, port))
s.listen(5) 

while True: 
	clientsocket, address = s.accept() 
	print("Connection from" + " " + str(address) + " " + "has been established.")
	clientsocket.send(bytes(12))
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()