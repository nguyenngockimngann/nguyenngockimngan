# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:06:21 2024

@author: Nguyen Ngoc Kim Ngan
"""

import math 
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
    




