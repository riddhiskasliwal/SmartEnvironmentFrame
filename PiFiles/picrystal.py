from sense_hat import SenseHat 
import time

sense = SenseHat()

violet = (148, 0, 211)
indigo = (75, 0, 130)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (255, 127, 0)
red = (255, 0, 0)

while True:
	freq = input("Current Frequency: ")
	time.sleep(2)
	if(freq > = 20 && freq < = 500){
		sense.show_message("", back_colour = violet)
	} else if (freq > = 501 && freq < = 1500){
		sense.show_message("", back_colour = indigo)
	} else if (freq > = 1501 && freq < = 1000){
		sense.show_message("", back_colour = blue)
	} else if (freq > = 1001 && freq < = 10000){
		sense.show_message("", back_colour = green)
	} else if (freq > = 10001 && freq < = 12000){
		sense.show_message("", back_colour = yellow)
	} else if (freq > = 12001 && freq < = 15000){
		sense.show_message("", back_colour = orange)
	} else if (freq > = 15001 && freq < = 20000){
		sense.show_message("", back_colour = red)
	}
