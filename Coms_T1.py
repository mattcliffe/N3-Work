# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:54:42 2018

@author: mattj
"""

import usbiss


Port = 'COM6'
spi=SPI(Port)
spi.mode = 1
spi.max_speed_hz = 300000
