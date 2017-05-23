from sense_hat import SenseHat
import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time

server_ip = "192.168.1.1"
port_number = 8880
size = 1024

sock = socket(AF_INET, SOCK_DGRAM)

sense = SenseHat()

while True:
	time.sleep(1800)
	temperature = sense.get_temperature()
	humidity = sense.get_humidity()
	print("lawn pi sending packet")
	sock.sendto(str(temperature), (server_ip, port_number))
	time.sleep(3600)

