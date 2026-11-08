#Nama : Dzakwan Naharezka Pasha
#NIM : 2604430
#Contoh penggunaan numpy untuk array
import numpy as np
#data 30 nilai menggunakan list 30
nilai = np.array([80, 90, 70, 60, 85, 75, 95, 88, 92, 78,
               82, 76, 89, 91, 87, 84, 79, 81, 83, 86,
               77, 74, 73, 72, 71, 69, 68, 67, 66, 65])
urut = np.sort(nilai)[::-1]
print("nilai ujian dari terbesar ke terkecil:")
print(urut)
print("5 nilai terbesar:")
print(urut[:5])