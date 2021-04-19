import MPU6050
# import RPi.GPIO as GPIO

A = MPU6050.Accelerometer()

try:

    while True:

        A.read_all_data()

except KeyboardInterrupt:
    print('Cleaning pins...')
    # GPIO.cleanup()
