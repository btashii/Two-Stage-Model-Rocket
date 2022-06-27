# Two-Stage-Model-Rocket
Project Developed from Jan 2020 - Aug 2020

Repository contains programming code for the onboard model rocket; telemetry data is streamed to the user's computer interface through a python pipeline locally connected by the Raspberry Pi WIFI network. 

Hardware:  
-Onboard Raspberry Pi Zero W (RPI) which connects to any laptop regardless of internet connection.  
-Rocket is 10 feet high, cardboard tubing and 3-D printed nosecone, fins and engine housing modeled in Fusion 360.  
-Nosecone has a opening that can be sealed with a screwing hatch; houses the electronics.  
-Adafruit Power Booster with a soldered switch allows the onboard lithium polymer battery to recharge and turn off/on.  
-Includes barometric pressure/temperature/altitude sensor. -Uses Estes D-12 engines for propulsion.   

Software:  
-Sensor data is fed through a python server to be sent to the software in the laptop, where the data is then displayed on a visual live graph using matplotlib.  
-Simulation software "OpenRocket" was used to model trajectory path.  
-Altitude: 1,200 feet high. 
