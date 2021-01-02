import MPU6050
import RPi.GPIO as GPIO

A = MPU6050.ACCELEROMETER()

try:
    
    while True:
        
        A.ReadAllData()

except KeyboardInterrupt:
    print('Cleaning pins...')
    GPIO.cleanup()

