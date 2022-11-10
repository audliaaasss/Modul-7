# -*- coding: utf-8 -*-
"""
Created on Fri Nov 4 20:24:04 2022

@author: Audi Aulia
"""
def ordinal():
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")
    while True:
        num = int(input("Masukan ankga : "))
        if num in [10, 11, 12, 13]:
            print("(", num, "'th'", ")")
        else:
            no = num % 10
            if no == 1:
                print("(", num, "'st'", ")")
            elif no == 2:
                print("(", num, "'nd'", ")")
            elif no == 3:
                print("(", num, "'rd'", ")")
            else:
                print("(", num, "'th'", ")")
        if num == 0:
            print("Terima kasih telah menggunakan program saya")
            break
x = ordinal()
print(x)
