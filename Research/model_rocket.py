#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:37:06 2021

The idea with this document is to make a model of a rocket that can be used
to simulate thrust vector control on random wind data interpreted by an
accelerometer

@author: maxmhuggins
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random

g = 9.81  # m/s^2


class RocketCoordinates:

    def __init__(self, center_of_mass, center_of_pressure, mass):
        self.CenterOfMass = (0, 0, center_of_mass)
        self.CenterOfPressure = (0, 0, center_of_pressure)
        self.Mass = mass
        self.ForceOfGravity = np.array([0, 0, -mass * g])

    def plot_vector(self, vector):
        x, y, z, = 0, 0, 0
        x_dir, y_dir, z_dir = vector[0], vector[1], vector[2]

        return x, y, z, x_dir, y_dir, z_dir

    def rotation(self, theta, vector):
        c, s = np.cos(theta), np.sin(theta)
        R = np.array([(c, -s, 0), (s, c, 0), (0, 0, 1)])

        return R.dot(vector)

    def perturb(self, vector, amount):
        original_mag = np.linalg.norm(vector)
        print(np.linalg.norm(vector))
        random_x, random_y, random_z = (random.uniform(-.1, .1),
                                        random.uniform(-.1, .1),
                                        random.uniform(-.1, .1))
        vector[0] = vector[0] + random_x
        vector[1] = vector[1] + random_y
        vector[2] = vector[2] + random_z
        vector = self.rotation(random.uniform(-amount, amount), vector)
        new_mag = np.linalg.norm(vector)
        vector[0] = vector[0] * new_mag / original_mag
        vector[1] = vector[1] * new_mag / original_mag
        vector[2] = vector[2] * new_mag / original_mag
        print(np.linalg.norm(vector))
        # return vector

    def show_model(self):
        COM = self.CenterOfMass
        FOG = self.ForceOfGravity

        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(0, 0, COM, color='m', label='Center of Mass')
        ax.quiver(*self.plot_vector(FOG), color='m', label='Force of Gravity')
        plt.show()

test_rocket = RocketCoordinates(1, .9, .05)

test_rocket.show_model()
# u = np.array([0.,0.,1.])
# test_rocket.perturb(u, 1)