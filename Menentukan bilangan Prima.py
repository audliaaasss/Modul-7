# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:23:45 2022

@author: Audi Aulia
"""
print ("Menentukan bilangan prima.")

def prima():
    num = int(input("Masukan angka : "))
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
x = prima()
print(x)