import os
from math import floor
from adafruit_rplidar import RPLidar
import numpy as np
import matplotlib.pyplot as plt


# Setup the RPLidar
PORT_NAME = '/dev/ttyUSB0'
lidar = RPLidar(None, PORT_NAME, timeout=3)

# used to scale data to fit on the screen
max_distance = 0

def process_data(data):
    print(data)

scan_data = [0]*360
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
theta = np.arange(0, 2 * np.pi, np.pi/180)

try:
#    print(lidar.get_info())
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            scan_data[min([359, floor(angle)])] = distance
#         process_data(scan_data)
        
#         fig, ax = plt.subplots()

#         for i, img in enumerate(data):
        ax.cla()
#         ax.imshow()
#             ax.set_title(f"frame {i}")
#             # Note that using time.sleep does *not* work here!
        
        ax.plot(theta, scan_data, ".")
        ax.set_rmax(2000)
#         ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#         ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
        ax.grid(True)

#         ax.set_title("A line plot on a polar axis", va='bottom')
        plt.pause(0.001)
        fig.show()
               

except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()


