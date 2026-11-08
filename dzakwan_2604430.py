#Nama : Dzakwan Naharezka Pasha
#NIM : 2604430
#Contoh penggunaan numpy untuk array
import numpy as np
#data 30 nilai menggunakan random integer
nilai = np.random.randint(0, 101, size=30)
urut = np.sort(nilai)[::-1]
print("nilai ujian dari terbesar ke terkecil:")
print(urut)
print("5 nilai terbesar:")
print(urut[:5])