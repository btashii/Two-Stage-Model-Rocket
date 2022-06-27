# MPL3115A2
# This code is designed to work with the MPL3115A2_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus
import time
import datetime
import os
import socket

# Declare document to write on
f = open("sensorlog.txt", "a")

# Get I2C bus
bus = smbus.SMBus(1)

# MPL3115A2 address, 0x60(96)
# Select control register, 0x26(38)
#   0xB9(185) Active mode, OSR = 128, Altimeter mode
bus.write_byte_data(0x60, 0x26, 0xB9)
# MPL3115A2 address, 0x60(96)
# Select data configuration register, 0x13(19)
#   0x07(07)  Data ready event enabled for altitude, pressure, temperature
bus.write_byte_data(0x60, 0x13, 0x07)
# MPL3115A2 address, 0x60(96)
# Select control register, 0x26(38)
#   0xB9(185) Active mode, OSR = 128, Altimeter mode
bus.write_byte_data(0x60, 0x26, 0xB9)

time.sleep(1)

# MPL3115A2 address, 0x60(96)
# Read data back from 0x00(00), 6 bytes
# status, tHeight MSB1, tHeight MSB, tHeight LSB, temp MSB, temp LSB
data = bus.read_i2c_block_data(0x60, 0x00, 6)

# Convert the data to 20-bits
tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
altitude = tHeight / 16.0
cTemp = temp / 16.0
fTemp = cTemp * 1.8 + 32

# MPL3115A2 address, 0x60(96)
# Select control register, 0x26(38)
#   0x39(57)  Active mode, OSR = 128, Barometer mode
bus.write_byte_data(0x60, 0x26, 0x39)

time.sleep(1)

# MPL3115A2 address, 0x60(96)
# Read data back from 0x00(00), 4 bytes
# status, pres MSB1, pres MSB, pres LSB
data = bus.read_i2c_block_data(0x60, 0x00, 4)

# Convert the data to 20-bits
pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
pressure = (pres / 4.0) / 1000.0






#socket.AF_INET is IPV4 address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#hostname that you get by doing "hostname -I"
hostname = '10.0.0.5'
#Designated Port
port = 12345
s.bind((hostname, port))
print("Awaiting client connection...")
s.listen(5)
clientsocket, address = s.accept()
print("Client connection from" + " " + str(address) + " " + "has been established.")
time.sleep(3)



# Output data to screen

a = 1
t = -31
temperature = fTemp
if (temperature < 100):
  print("System temperature is nominal at:" + " " + str(temperature) + " " + "degrees Fahrenheit.  Proceeding with countdown.")
  f.write("System temperature is nominal. Proceeding with countdown." + "\n")
  time.sleep(2)
  while (a == 1):
    time.sleep(1)
    clientsocket.send(bytes(temperature))
    t += 1
    print "Pressure : %.2f kPa" %pressure
    print "Altitude : %.2f m" %altitude
    print "Temperature in Celsius  : %.2f C" %cTemp
    print "Temperature in Fahrenheit  : %.2f F" %fTemp
    if (t < 0):
      timemagnitude = str(t*-1)
      timenomagnitude = str(t)
      print("T-Minus:" + " " + timemagnitude + " " + "seconds")
      #clientsocket.send(bytes("T-Minus:" + " " + timemagnitude + " " + "seconds"))
    elif (t>0):
      print("T-Plus:" + " " + str(t) + " " + "seconds")
      f.write(str(datetime.datetime.now()) + ":" + "\n" + str("Pressure : %.2f kPa" %pressure) + "\n" + str("Altitude : %.2f m" %altitude) + "\n" + str("Temperature in Celsius  : %.2f C" %cTemp) + "\n" + str("Temperature in Fahrenheit  : %.2f F" %fTemp) + "\n")
    elif (t == 0):
      print("Rocket Launched at:" + " " + str(datetime.datetime.now()))

else:
  print("Temperature has exceeded 100 degrees Fahrenheit. Launch is not advised. Check environmental temperature or interior of rocket.")
