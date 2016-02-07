import time
from threading import Thread
import boto3
import mraa
from math import log
import pyupm_i2clcd as lcd

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('TemperatureSensor')
# Initialize lcd
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

# Clear
myLcd.clear()

# Green
myLcd.setColor(255, 255, 0)

# Zero the cursor
myLcd.setCursor(0,0)

# Define which analog pin the temp sensor is connected to
temp_pin_number=1

# Initialize temp sensor
tempSensor = mraa.Aio(temp_pin_number)
# Initialize temp sensor
tempSensor = mraa.Aio(temp_pin_number)

# Define ISR
def interr_test(i):
        global tempSensor
        global myLcd

        # Define constants
        B = 4275
        R0 = 100000.0

        # Get raw value
        raw = tempSensor.read()
	time.sleep(5)
        # Calculate
        R = 1023.0/raw - 1.0
        R = R0*R
	
  	temp = 1.0/(log(R/R0)/B+1/298.15)-273.15
	myLcd.setCursor(0,0)
        myLcd.write("Temperature is:")
        myLcd.setCursor(1,0)
        myLcd.write("%2.1f C" % temp)
	table.put_item(
        Item={
                'Time': str(time.time()),
                
                
                
                'Temperature': str(temp),
                }
        )

        # Display

# Define what DIO the switch is connected to
for i in range(10):
    t = Thread(target=interr_test, args=(i,))
    t.start()




print(table.creation_date_time)



# Passively poll
try:
    	while(1):
                pass
except KeyboardInterrupt:
        exit
