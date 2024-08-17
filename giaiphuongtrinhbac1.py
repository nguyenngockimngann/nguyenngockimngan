# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:05:07 2024

@author: Nguyen Ngoc Kim Ngan

"""

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0 and b == 0:
    print("Phuong trinh co vo so nghiem.")
elif a == 0 and b != 0:

    print("Phuong trinh vo nghiem")
elif a != 0 and b!= 0:

    print("Phuong trinh co 1 nghiem duy nhat X=", -b/a)
else:

    print("Khong hop le!")
