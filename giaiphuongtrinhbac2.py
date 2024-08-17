# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:24:07 2024

@author: Nguyen Ngoc Kim Ngan
"""

import math 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép x = {x}", x)
else:
    x1 = -b + math.sqrt(delta) / (2*a)
    x2 = -b - math.sqrt(delta) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt x1 = {x1}, x2 = {x2}")
    print("x1:", x1)
    print("x2:", x2)

    
    

    
    
    