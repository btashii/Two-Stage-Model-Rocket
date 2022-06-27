import os
import socket
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#setting up the plot graph

plt.style.use('fivethirtyeight')
fig = plt.figure(frameon=False)
plt.rc('axes', labelsize=10)   
plt.rc('xtick', labelsize=5)
plt.rc('ytick', labelsize=5)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.0.0.5', 12345))
yaxis = []
#time  = -1
xaxis = []

#connection succesful?
os.system("say 'Succesful client connection with server established. Welcome!'")


#count starts from -1 and increments by 1
index = count(-1)
indexstring = str(index)
#animation function for live graph
def animate(i):
	xaxis.append(next(index))
	msg = s.recv(1024)
	yaxis.append(msg.decode("utf-8"))
	plt.cla()
	plt.plot(xaxis, yaxis, label = 'Fahrenheit/Second')
	plt.ylabel('Temperature in Fahrenheit')
	plt.xlabel('Time in seconds')
	#os.popen('sh /Users/tashi/Desktop/Space\ Club\ /countdownspeech.sh')
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()


#console log of client-server connection
while True:
	msg = s.recv(1024)
	print(msg.decode("utf-8"))
	#yaxis.append(msg)
	#time += 1
	print(yaxis)
