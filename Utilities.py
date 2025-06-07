import os
import random
from Database import *
from tabulate import tabulate

def checkSystemOS(): # Function untuk auto-clear tampilan di terminal
    system = os.name
    if system == 'posix':
        os.system('clear')
    elif system == 'nt':
        os.system('cls')

def welcomeMessage():
    checkSystemOS()
    welcome = 'RUNGKAD JHS STUDENT DASHBOARD'
    welcomeSymbol = '=' * len(welcome)

    print(f'    {welcomeSymbol}')
    print(f'    {welcome}')
    print(f'    {welcomeSymbol}')

def closingMessage():
    closing_msg = [['PROGRAM SELESAI, TERIMAKASIH']]
    print('\n')
    print(tabulate(closing_msg, tablefmt='grid', stralign='center'))  

def generateUniqueNIS():
    for siswa in siswaDict:
        # Generate Unique ID untuk setiap siswa
        randomNum = str(random.randrange(1,50,3))
        inisial = siswa['nama'][:5:2].upper()
        nis = randomNum + inisial
        
        # Append key 'NIS' ke siswaDict
        siswa['NIS'] = nis
        print(siswa['NIS'])
# generateUniqueNIS()

def digitCheck(message): # Jika userInput bukan digit, loop user sampai kasih input yang valid
    while True:
        userInput = input(message)
        if userInput.isdigit():
            return userInput
        else:
            print('Invalid input, silahkan coba lagi.')

def gradeNilai(nilaiDict): # Rata-rata Nilai setiap Siswa -> Grade [A, B, C, F]
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