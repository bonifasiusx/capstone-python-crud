import os
from tabulate import tabulate

def checkSystemOS():
# Fungsi untuk menghapus tampilan di terminal
# Setiap kali checkSystemOS dijalankan
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
    closing_msg = [['PROGRAM SELESAI TERIMAKASIH']]
    print('\n')
    print(tabulate(closing_msg, tablefmt='grid', stralign='center'))

def digitCheck(message):
# Fungsi ini akan meng-handle error jika
    # -> User memberikan input yang bukan digit
    # -> User memberikan input berupa angka negatif
# Lalu memberikan feedback di setiap error yang terdeksi oleh digitCheck(message)
    while True:
        try:
            userInput = int(input(message))
            if userInput < 0:
                print('\nInput tidak boleh negatif, silahkan coba lagi.')
                continue
            elif userInput > 100:
                print('\nInput melebihi batasan, silahkan coba lagi.')
                continue
            return userInput
        except ValueError:
            print('\nInvalid input, silahkan coba lagi.')

def gradeNilai(nilaiDict):
# Fungsi ini menghitung rata-rata nilai setiap siswa
# Lalu merubah nilai rata-rata tsb menjadi Grade -> [A, B, C, F]
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

def backToMenu(prompt):
# Fungsi untuk handle error dari user input
# saat validasi lanjut/tidak di setiap fitur CRUD
    pressEnter = input(prompt)
    if pressEnter == '':
        return

def loopValidator(toDo, prompt):
    while True:
        checkSystemOS()
        toDo()
        isDone = input(prompt)
        if isDone.lower() == 'tidak':
            return
        elif isDone.lower() == 'ya':
            continue
        else:
            backToMenu('\nInput tidak dikenali\nTekan ENTER untuk kembali ke Menu Utama\n')
            return


# import random
# def generateUniqueNIS(): # HELPER saat membuat SiswaDict
# # Dibuat hanya untuk generate Unique NIS untuk setiap siswa di siswaDict
#     for siswa in siswaDict:
#         # NIS =  2 Angka Random + 2 Huruf Inisial
#         randomNIS = str(random.randrange(10,100,3))
#         inisial = siswa['nama'][:5:2].upper()
#         nisBaru = randomNIS + inisial[:2]
        
#         # Append (key:'NIS', values:nis) ke siswaDict
#         siswa['NIS'] = nisBaru
#         print(siswa['NIS'])