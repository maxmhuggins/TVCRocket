#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:37:51 2020

@author: maxmhuggins

This script is meant to handle interfacing with the MPU6050. This is a 3-axis
accelerometer that is supposed to be used for TVC.

Most of this code was taken from: 
    https://www.electronicwings.com/raspberry-pi/mpu6050-
    accelerometergyroscope-interfacing-with-raspberry-pi
    
I've simply edited it for my purposes.
"""
#============================================================================#
import smbus
from time import sleep
#============================================================================#

class ACCELEROMETER():
    
    
    def __init__(self):

        self.DeviceAddress = 0x68
        self.PWR_MGMT_1   = 0x6B
        self.SMPLRT_DIV   = 0x19
        self.CONFIG       = 0x1A
        self.GYRO_CONFIG  = 0x1B
        self.INT_ENABLE   = 0x38
        self.ACCEL_XOUT_H = 0x3B
        self.ACCEL_YOUT_H = 0x3D
        self.ACCEL_ZOUT_H = 0x3F
        self.GYRO_XOUT_H  = 0x43
        self.GYRO_YOUT_H  = 0x45
        self.GYRO_ZOUT_H  = 0x47
        
        self.bus = smbus.SMBus(1)
        
        	#write to sample rate register
        self.bus.write_byte_data(self.DeviceAddress, self.SMPLRT_DIV, 7)
        	
        	#Write to power management register
        self.bus.write_byte_data(self.DeviceAddress, self.PWR_MGMT_1, 1)
        	
        	#Write to Configuration register
        self.bus.write_byte_data(self.DeviceAddress, self.CONFIG, 0)
        	
        	#Write to Gyro configuration register
        self.bus.write_byte_data(self.DeviceAddress, self.GYRO_CONFIG, 24)
        	
        	#Write to interrupt enable register
        self.bus.write_byte_data(self.DeviceAddress, self.INT_ENABLE, 1)

    def read_raw_data(self, addr):
    	#Accelero and Gyro value are 16-bit
            high = self.bus.read_byte_data(self.DeviceAddress, addr)
            low = self.bus.read_byte_data(self.DeviceAddress, addr+1)
        
            #concatenate higher and lower value
            value = ((high << 8) | low)
            
            #to get signed value from mpu6050
            if(value > 32768):
                    value = value - 65536
            return value
        

    def ReadAllData(self):
        
    	acc_x = self.read_raw_data(self.ACCEL_XOUT_H)
    	acc_y = self.read_raw_data(self.ACCEL_YOUT_H)
    	acc_z = self.read_raw_data(self.ACCEL_ZOUT_H)
    	
    	#Read Gyroscope raw value
    	gyro_x = self.read_raw_data(self.GYRO_XOUT_H)
    	gyro_y = self.read_raw_data(self.GYRO_YOUT_H)
    	gyro_z = self.read_raw_data(self.GYRO_ZOUT_H)
    	
    	#Full scale range +/- 250 degree/C as per sensitivity scale factor
    	Ax = acc_x/16384.0
    	Ay = acc_y/16384.0
    	Az = acc_z/16384.0
    	
    	Gx = gyro_x/131.0
    	Gy = gyro_y/131.0
    	Gz = gyro_z/131.0
	

    	print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	