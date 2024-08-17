# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:48:02 2024

@author: Nguyen Ngoc Kim Ngan
"""

GPA =float(input("Nhap diem trung binh GPA:"))
if GPA < 3.5:
    print("Hoc luc kem.")
elif 3.5<= GPA <= 5.0:
    print("Hoc luc yeu.")
elif 5.0<= GPA <= 7.0:
    print("Hoc luc yeu.")
elif 7.0<= GPA <= 8.0:
    print("Hoc luc kha.")
elif 8.0<= GPA <= 9.0:
    print("Hoc luc gioi.")
elif 9.0<= GPA <= 10:
    print("Hoc luc xuat sac.")
