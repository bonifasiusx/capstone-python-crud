import os
import random
from Database import *
from tabulate import tabulate

def checkSystemOS():
# Fungsi untuk menghapus tampilan di terminal
# Setiap kali checkSystemOS dijalankan
# checkSystemOS() dipanggil di dalam fungsi welcomeMessage(), create.py --> showSiswaBaru()
    system = os.name
    if system == 'posix':
        os.system('clear')
    elif system == 'nt':
        os.system('cls')

def welcomeMessage():
    checkSystemOS() # Clear terminal setiap kali welcomeMessage() dipanggil
    welcome = 'RUNGKAD SCHOOL STUDENT DASHBOARD'
    welcomeSymbol = '=' * len(welcome)

    print(f'    {welcomeSymbol}')
    print(f'    {welcome}')
    print(f'    {welcomeSymbol}')

def closingMessage():
    closing_msg = [['PROGRAM SELESAI, TERIMAKASIH']]
    print('\n')
    print(tabulate(closing_msg, tablefmt='grid', stralign='center'))

def generateUniqueNIS(): # HELPER
# Dibuat hanya untuk generate Unique NIS untuk setiap siswa di siswaDict
    for siswa in siswaDict:
        # NIS =  2 Angka Random + 2 Huruf Inisial
        randomNIS = str(random.randrange(10,100,3))
        inisial = siswa['nama'][:5:2].upper()
        nisBaru = randomNIS + inisial[:2]
        
        # Append (key:'NIS', values:nis) ke siswaDict
        siswa['NIS'] = nisBaru
        print(siswa['NIS'])

def digitCheck(message):
# Fungsi ini akan meng-handle error jika
# User memberikan input yang bukan digit
# User memberikan input berupa angka negatif
# Lalu memberikan feedback di setiap error yang terdeksi oleh digitCheck(message)
# digitCheck dipanggil di --> menuConsole.py
    while True:
        try:
            userInput = int(input(message))
            if userInput < 0:
                print('''
    Input tidak boleh negatif, silahkan coba lagi.''')
                continue
            return userInput
        except ValueError:
            print('''
    Invalid input, silahkan coba lagi.''')

def gradeNilai(nilaiDict):
# Fungsi ini menghitung rata-rata nilai setiap siswa
# Lalu merubah nilai rata-rata tsb menjadi Grade -> [A, B, C, F]
# gradeNilai dipanggil di --> read.py -> showSiswa()
    listNilai = list(nilaiDict.values())
    listNilai = [int(nilai) for nilai in listNilai]
    averageNilai = sum(listNilai) / len(listNilai)
    
    if averageNilai >= 85:
        return 'A'
    elif averageNilai >= 75:
        return 'B'
    elif averageNilai >= 65:
        return 'C'
    else:
        return 'F'