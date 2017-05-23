import MySQLdb
from PIL import Image
import webbrowser
import PIL.ImageEnhance
import sys
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM

port_number = 8880
size = 1024
hostname = gethostbyname('0.0.0.0')

try:
	db = MySQLdb.connect(host="192.168.1.9", port=3306, user="pi", passwd="pi",db="piframe")
except:
	print("cannot connect")

cursor = db.cursor()

sql = "SELECT * FROM images"

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((hostname, port_number))

while True:
	(data, addr) = sock.recvfrom(size)
	print(data)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			image = open("frame.jpg", 'wb')
			image.write(row[1].decode('base64'))
			image.close()
		print("file saved")
	except:
		print("cannot read file")

	img = Image.open("frame.jpg")
	
	enhancer = PIL.ImageEnhance.Color(img)
	
	enhancer.enhance(4.0).save("frame_filter.jpg", "jpeg")
	webbrowser.open("frame_filter.jpg")
sys.ext()
db.close()
