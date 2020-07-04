#!/usr/bin/env python
#
# GrovePi Example for using the Grove - LCD RGB Backlight (http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time 
import grovepi
import math
import json

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D7
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 7  # The Sensor goes on digital port 4.

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
greenLed = 4

# Connect the LED to digital port D3
# SIG,NC,VCC,GND
blueLed = 3

# Connect the LED to digital port D2
# SIG,NC,VCC,GND
redLed = 2

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0



#threshold value was increased to match the darkness value of the room when the light was switched off
threshold = 500

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

from grove_rgb_lcd import *

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

data = []
dataTemp = []

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value
        
        #changed it so that if resitance was > threshold, the light would turn on, so that way it trigged when the light was off. 
        if resistance > threshold:
        
            # This example uses the blue colored sensor. 
            # The first parameter is the port, the second parameter is the type of sensor.
            [temp,humidity] = grovepi.dht(sensor,blue)  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                print("Temp = %.02f C Humidity =%.02f%%"%(temp, humidity))
                setRGB(0,128,64)
                setText("Temp = %.02f F\nHumidity =%.02f%%"%((temp *9/5 + 32), humidity))
                dataTemp.append([
                    (temp *9/5 +32),humidity]
                    )
            
            #green LED conditions
            if temp > 60 and if humidity < 80
                grovepi.digitalWrite(greenLed,1)
                grovepi.digitalWrite(blueLed, 0)
                grovepi.digitalWrite(redLed, 0)
            
            #Blue LED conditions
            else if temp > 85 and if humidity is < 80
                grovepi.digitalWrite(greenLed,0)
                grovepi.digitalWrite(blueLed, 1)
                grovepi.digitalWrite(redLed, 0)
            
            #red LED conditons 
            else if temp > 95
                grovepi.digitalWrite(redLed, 1)
            
            #green and blue LED conditions
            else if humidity > 80
                grovepi.digitalWrite(greenLed,1)
                grovepi.digitalWrite(blueLed, 1)
        
            
            with open('data.json', 'w') as outfile:
                json.dump(dataTemp, outfile)
            
            #only take readings once every 60 seconds.     
            time.sleep(1800)
            

        except IOError:
            print ("Error")
