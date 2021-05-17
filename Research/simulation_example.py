#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 05:18:03 2021

@author: maxmhuggins
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time
import subprocess
import random


span = 1
N = 50


def plot_vector(u, color='m', label=None):
    x, y, z, = 0, 0, 0
    x_dir, y_dir, z_dir = u[0], u[1], u[2]
    ax.quiver(x, y, z, x_dir, y_dir, z_dir, color=color, label=label)


def rotation(theta, vector):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([(c, -s, 0), (s, c, 0), (0, 0, 1)])
    return R.dot(vector)


def plane(u, span, shift=None):
    span = span/2
    a = u[0]
    b = u[1]
    c = u[2]

    if shift is None:
        d = 0
    else:
        d = shift

    if u[2] == 0:
        x, z = np.meshgrid(np.linspace(-span, span, 2),
                           np.linspace(-span, span, 2))

        y = d - a*x - c*z

    else:
        x, y = np.meshgrid(np.linspace(-span, span, 2),
                           np.linspace(-span, span, 2))

        z = (d - a*x - b*y) / c

    return x, y, z


# ========================================================================== #
# fig = plt.figure(figsize=(12, 12))
# ax = fig.add_subplot(111, projection='3d')
# ========================================================================== #
u = np.array([0., 0., 1.])

for i in range(0, 100):
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    random_x, random_y, random_z = (random.uniform(-.1, .1),
                                    random.uniform(-.1, .1),
                                    random.uniform(-.1, .1))
    u[0] = u[0] + random_x
    u[1] = u[1] + random_y
    u[2] = u[2] + random_z
    u = rotation(random.uniform(-np.pi/50, np.pi/50), u)
    plot_vector(u, color='m', label='u')
# ========================================================================== #
    ax.set_title('Some Title')
    ax.set_xlim([-3*span, 3*span])
    ax.set_ylim([-3*span, 3*span])
    ax.set_zlim([-3*span, 3*span])
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    ax.legend(loc='best')
    plt.show()
# ========================================================================== #

# counter = 0

# for i in np.linspace(0,2*np.pi, N):
#     fig = plt.figure(figsize=(12, 7))
#     ax = fig.add_subplot(111, projection='3d')

#     u = np.array([0, 1, 1])

#     counter += 1
#     u = rotation(i, u)
#     x, y, z = plane(u, span)
    
#     ax.plot_surface(x, y, z, alpha=0.5, color='black')
#     plot_vector(u)
#     ax.set_title('Some Title')
#     ax.set_xlim([-span, span])
#     ax.set_ylim([-span, span])
#     ax.set_zlim([-span, span])
#     ax.set_xlabel('x-axis')
#     ax.set_ylabel('y-axis')
#     ax.set_zlabel('z-axis')
#     plt.savefig('./figures/{}'.format(counter))

# subprocess.Popen(['convert','-delay', '1', 
#               '%d.png[0-{}]'.format(N), 'Spinny_GIF.gif'],  
#              cwd="./figures")


# Wind acts on rocket, setting it off course
# Accelerometer senses this change
# Data sent to computer regarding attitude change
# Attitude control sends a response to TVC system for correction
# 