# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:17:04 2024

@author: ASUS-PC
"""

try:
     a = float(input("Nhập hệ số a: "))
     b = float(input("Nhập hệ số b: "))
     c = float(input("Nhập hệ số c: "))
except: print("Dinh dang do dai ba canh a, b, c sai!")
if a>0 and b>0 and c>0: 
	if a+b>c and b+c>a and a+c>b:
		print('a =',a,'b =',b,'c =',c,"la do dai ba canh cua mot tam giac", sep=(' '))
	else:
		print('a =',a,'b =',b,'c =',c,"khong la do dai ba canh cua mot tam giac", sep=(' '))
else: print("Dinh dang do dai ba canh a, b, c sai!")
