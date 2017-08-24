import RPi.GPIO as GPIO
import dht11
import time
import datetime
import urllib.request

myurl1 = 'https://api.thingspeak.com/update?api_key=0NIYQ2V14Y9BBY7T&field1='
myurl2 = 'https://api.thingspeak.com/update?api_key=0NIYQ2V14Y9BBY7T&field2='
f1 = urllib.request.urlopen(myurl1)
f2 = urllib.request.urlopen(myurl2)


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 2
instance = dht11.DHT11(pin=2)

cnt = 0
success = 0
fail = 0
errorrate = 0.0
while(1):
    cnt += 1
    result = instance.read()
    if result.is_valid():
        print('*'*26)
        success += 1
        errorrate = ((cnt-success)/cnt)*100
        print('* Total :', cnt, '/ Error rate :', errorrate, '% *')
        print('*'*26)
        print("Last valid input: " + str(datetime.datetime.now()))
        temperature = result.temperature
        humidity = result.humidity
        print("Temperature:", temperature, 'C')
        print("Humidity:", humidity, '%')

        url1 = myurl1 + str(temperature)
        url2 = myurl2 + str(humidity)
        f2 = urllib.request.urlopen(url2)
        f1 = urllib.request.urlopen(url1)
        
    time.sleep(5)

fail = cnt - success
print('Total :', cnt, ' / success :', success, ' / fail :', fail)
