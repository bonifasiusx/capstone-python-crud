from tabulate import tabulate
from Database import *
from Utilities import *
# import random
# from hello import *

# def generateUniqueNIS():
#     for siswa in siswaDict:
#         # Generate Unique ID untuk setiap siswa
#         randomNum = str(random.randrange(1,50,3))
#         inisial = siswa['nama'][:5:2].upper()
#         nis = randomNum + inisial
        
#         # Append key 'NIS' ke siswaDict
#         siswa['NIS'] = nis
#         print(siswa['NIS'])
# generateUniqueNIS()

# def digitCheck(message): # Jika userInput bukan digit, loop user sampai kasih input yang valid
#     while True:
#         userInput = input(message)
#         if userInput.isdigit():
#             return userInput
#         else:
#             print('Invalid input, silahkan coba lagi.')

# def gradeNilai(nilaiDict): # Rata-rata Nilai setiap Siswa -> Grade [A, B, C, F]
#     listNilai = list(nilaiDict.values())
#     listNilai = [int(nilai) for nilai in listNilai]
#     averageNilai = sum(listNilai) / len(listNilai)
    
#     if averageNilai >= 85:
#         return 'A'
#     elif averageNilai >= 75:
#         return 'B'
#     elif averageNilai >= 65:
#         return 'C'
#     else:
#         return 'F'

# def subMenu1():
#     subMenuInputUser = digitCheck('''
# [1] Lihat Detail Data Siswa
# [2] Detail Siswa Berdasarkan NIS
# [3] Kembali ke Menu Utama

# Silahkan pilih Sub Menu: ''')
        
#     if subMenuInputUser == '1':
#         return showSiswaInDetails(), subMenu1()
#     elif subMenuInputUser == '2':
#         return cariDataSiswa()
#     elif subMenuInputUser == '3':
#         return mainMenu()
#     else:
#         print('Pilihan tidak tersedia, silahkan coba lagi.')
#         return subMenu1()
    
def showSiswaInDetails(): # [1] -> [1]
    siswa.clear() # Hapus isi list siswa agar data di tabel tidak tumpang-tindih
    
    print('\nDashboard Siswa in Details:\n')
    for nis, items in enumerate(siswaDict):        
        row = [items['nis'], items['nama'], items['kelas']]
        for mapel in listMapel:
            row.append(items['nilai'].get(mapel))
        siswa.append(row)       
           
    print(tabulate(siswa, siswaColumn, tablefmt="grid", numalign='center', rowalign='align'))
    return
    # return subMenu1

def cariDataSiswa(): # Additional Menu + Support Function Menu [3]
    cariSiswa = input('\nMasukkan NIS: ').upper()
    targetSiswa = {} # Cocokin type data dengan tempat data siswa disimpan -> siswa == Dictionary
    
    for siswa in siswaDict:
        if siswa['nis'] == cariSiswa:
            targetSiswa = siswa
            break
    # for loop dulu baru cek validasi, jangan ketuker!
    if targetSiswa == {}:
        print(f'Siswa dengan NIS: {cariSiswa} tidak ditemukan')
        return cariDataSiswa()
    
    # Akses nested-dict supaya setiap mapel jadi kolom
    listMapelTarget = list(targetSiswa['nilai'].keys())
    listNilaiTarget = list(targetSiswa['nilai'].values())
    targetColumn = ['NIS', 'Nama', 'Kelas'] + listMapelTarget
    targetRow = [targetSiswa['nis'], targetSiswa['nama'], targetSiswa['kelas']] + listNilaiTarget
    
    # checkSystemOS()
    print(f'NIS: {cariSiswa} ditemukan!\n')
    print(tabulate([targetRow], headers=targetColumn, tablefmt="grid", numalign='center', rowalign='center'))
    # Jadiin function support untuk editDataSiswa()
    return cariSiswa, targetSiswa, listMapelTarget, listNilaiTarget, targetColumn, targetRow
    
def showSiswa(): # [1]
    print('\nDashboard Siswa:\n')
    siswa.clear() # Hapus isi list siswa agar data di tabel tidak tumpang-tindih
    for items in siswaDict:
        nis = items['nis']
        nama = items['nama']
        kelas = items['kelas']
        # Grading Nilai & Status Kelulusan
        grade = gradeNilai(items['nilai'])
        status = 'LULUS' if grade in ['A','B','C'] else 'TIDAK LULUS'
        
        siswa.append([nis, nama, kelas, grade, status]) # Rows
        showSiswaColumn = ['NIS', 'Nama', 'Kelas', 'Grade', 'Status']             
        
    print(tabulate(siswa, showSiswaColumn, tablefmt="grid", numalign='center', rowalign='align'))
    # subMenu1()
    # subMenu1()
# showSiswa()
# def subMenu1():
#     while True:
#         subMenuInputUser = digitCheck('''
# [1] Lihat Detail Data Siswa
# [2] Detail Siswa Berdasarkan NIS
# [3] Kembali ke Menu Utama

# Silahkan pilih Sub Menu: ''')
        
#         if subMenuInputUser == '1':
#             showSiswaInDetails()
#             continue
#         elif subMenuInputUser == '2':
#             cariDataSiswa()
#             continue
#         elif subMenuInputUser == '3':
#             break
#         else:
#             print('Pilihan tidak tersedia, silahkan coba lagi.')
            
        
# subMenu1()