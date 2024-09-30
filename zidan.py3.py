# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:29:03 2024

@author: ASUS
"""

import math 
lintang1 = math.radians(float(input("lintang Kota 1:")))
bujur1 = math.radians(float(input("bujur Kota 1:")))
lintang2 = math.radians(float(input("lintang kota 2:")))
bujur2 = math.radians(float(input("bujur kota 2:")))
r = 6371
lat = lintang2 - lintang1
long = bujur2 - bujur1
a = math.sin(lat/2)*2 + math.cos(lintang1) * math.cos(lintang2) * math.sin(long/2)*2
c3 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = r * c3
print(f"jarak antara dua titik tersebut adalah ", (d) , "kilometer")