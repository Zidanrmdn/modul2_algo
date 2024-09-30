# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:58:38 2024

@author: ASUS
"""

import math
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
hasiljumlah = bil1 + bil2
print("Hasil jumlah bil1 dan bil2: {}".format(hasiljumlah))
hasilkurang = bil2 - bil1  
print("Hasil kurang bil2 dan bil1: {}".format(hasilkurang))
hasilkali = bil1 * bil2
print("Hasil kali bil1 dan bil2: {}".format(hasilkali))
if bil2 != 0:
    hasilmodulo = bil1 % bil2
    print("Sisa pembagian bil1 dengan bil2: {}".format(hasilmodulo))
    hasilfloatdev = bil1 / bil2
    print("Pembagian bil1 dengan bil2: {}".format(hasilfloatdev))
else:
    print("Pembagian dan modulo tidak dapat dilakukan karena bil2 adalah nol.")
if bil1 > 0:
    log_bil1 = math.log10(bil1)
    print("Logaritma dari bil1 (log10(bil1)): {}".format(log_bil1))
else:
    print("Logaritma hanya bisa dihitung untuk bilangan positif.")
hasilpangkat = bil1 ** bil2
print("Hasil pangkat bil1 pangkat bil2: {}".format(hasilpangkat)) 

