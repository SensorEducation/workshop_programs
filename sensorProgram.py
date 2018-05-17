#SensorEd Workshop V0.1
#Author - Jacob Ulasevich
#Sensor Introduction

"""
Sensors can perform a variety of different tasks and each individual
sensor can perform differently depending on how you program it.

This workshop will be working with the Adafruit BME 680 sensor.  It can
collect pressure, temperature, humidity, ans gas resistance.
"""

#Imports
import bme680
import time
import datetime
import sqlite3
import os
from sqlite3 import Error

"""
You've seen most of these libraries before but the bme680 is the library
for our sensor. The datetime library allows for getting the specific date.
Finally, sqllite 3 will allow us to save our data in SQL format.
"""

"""
A good practice when working in a program that does alot is having a main
function that you can execute on the end.
"""
def main():

    #Number of times you want while loop to repeat
    repeat = 20
    #Seconds you want to wait between each reading
    wait_period = 1
    #Keep 0, incriment each time you take a reading
    count = 0
    
    #Create Sensor Variable
    sensor = bme680.BME680(i2c_addr=0x77)

    #Database
    #Creates/open a file called sensorData.db by defining the path
    db = sqlite3.connect("/home/pi/Pimoroni/bme680/examples/test2DB.db")
    cursor = db.cursor()
    
    #In order to get the MAC Adress we need to run another program
    try:
        cursor.execute('''
            CREATE TABLE b827eb06efa4(dateTime TEXT PRIMARY KEY,  temperature FLOAT,
                           pressure FLOAT, humidity FLOAT, gas FLOAST)
        ''')
    except Error as e:
        print("Error: " + str(e))
    
    #Set up the sensor to begin reading data
    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)


    #Print out the initial readings
    print("\n\nInitial reading:")
    for name in dir(sensor.data):
        value = getattr(sensor.data, name)

        if not name.startswith('_'):
            print("{}: {}".format(name, value))

    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile(0)

    
    #Begin reading 
    print("\n\nPolling:")
    try:
        #Set up a while loop given the variables a the begining
        while(repeat > count):
            """
            If else statements allow you to perform one block of code
            if the condition is true, if it itsn't it will perform
            the block of code after "else" or none at all.
            """
            if sensor.get_sensor_data():
                #The parameter for dates is %d/%m/%Y for day month year
                dateNow = time.strftime("%d/%m/%Y")
                #The parameter for time is %H/%M/%S for hour minute second
                timeNow = time.strftime("%H/%M/%S")
                #Combine the two strings above and put a "|" between them
                dateTime = dateNow + "|" + timeNow
                """
                By performing float("{0:.2f}".format() you can round whatever parameter is in
                format to whatever decimal place you idtentified before the f.  2f rounds the number
                to the nearest hundreth.

                Sensor.data.TERM will return the current reading from the sensor of whatever term
                you chose.
                """
                temperatureCelcius = float("{0:.2f}".format(sensor.data.temperature))
                #Convert the above variable to fahrenheit and assign the result to temperature
                temperature = float(temperatureCelcius*(9/5) + 32)
                pressure = float("{0:.2f}".format(sensor.data.pressure))
                humidity = float("{0:.2f}".format(sensor.data.humidity))
                gas = float("{0:.2f}".format(sensor.data.gas_resistance))
                
                cursor.execute('''INSERT INTO b827eb06efa4(dateTime, temperature, pressure, humidity, gas)
                  VALUES(?,?,?,?,?)''', (dateTime, temperature, pressure, humidity, gas))

                #Print the data however you wish given the above variables.
                print("Temperature: " + str(temperature))
                print("Pressure:" + str(pressure))
                print("Humidity:" + str(humidity))
                print("Gas:" + str(gas))

                #Increase incrimenter
                count += 1
                
                #Tell Board to wait 'wait_peroid' amount of secionds before moving on
                time.sleep(wait_period)

        #Update Changes And Close Databse
        db.commit()    
        db.close()

    #Pressing any button on they keyboard will stop the program.
    except KeyboardInterrupt:
        pass
    
#RUN MAIN FUNCTION
if __name__ == '__main__':
    main()
