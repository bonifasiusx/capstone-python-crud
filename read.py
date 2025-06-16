from tabulate import tabulate
from Database import siswaDict, siswa, listMapel, siswaColumn
from Utilities import gradeNilai, checkSystemOS, digitCheck

def showSiswa(): # Fungsi -> Tabulate Siswa + grade nilai
    print('\nDashboard Siswa:\n')
    siswa.clear()
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

def cariDataSiswa(prompt): # Fungsi untuk mencari siswa berdasarkan input NIS
# Fungsi untuk operasi di Sub-Menu [1]
# Sebagai function helper di [3] Update
    kuota = 0
    while kuota < 3:
        cariSiswa = input(prompt).upper()
        targetSiswa = {} # Cocokin type data dengan tempat data siswa disimpan -> siswa == Dictionary
    
        for siswa in siswaDict:
            if siswa['nis'] == cariSiswa:
                targetSiswa = siswa
                break
        # for loop dulu baru cek validasi, jangan ketuker!
        if not targetSiswa:
            kuota += 1
            if kuota == 3:
                print('\nInvalid input mencapai batas.')
                return None
            else:
                print(f'\nData siswa tidak ditemukan, mohon masukkan NIS yang valid.\n({3 - kuota} percobaan tersisa)')
        
        else:
            # Tampilkan data siswa yang dicari
            listMapelTarget = list(targetSiswa['nilai'].keys())
            listNilaiTarget = list(targetSiswa['nilai'].values())
            targetColumn = ['NIS', 'Nama', 'Kelas'] + listMapelTarget
            targetRow = [targetSiswa['nis'], targetSiswa['nama'], targetSiswa['kelas']] + listNilaiTarget
            
            print(f'\nNIS: {cariSiswa} ditemukan!\n')
            print(tabulate([targetRow], headers=targetColumn, tablefmt="grid", numalign='center', rowalign='center'))
            return cariSiswa, targetSiswa

def showSiswaInDetails(): # Fungsi -> Tabulate Siswa + rincian nilai setiap mapel
    siswa.clear() # .clear() agar output tabel data tidak tumpang-tindih
    
    print('\nDashboard Siswa in Details:\n')
    for nis, items in enumerate(siswaDict):        
        row = [items['nis'], items['nama'], items['kelas']]
        for mapel in listMapel:
            row.append(items['nilai'].get(mapel))
        siswa.append(row)       
           
    print(tabulate(siswa, siswaColumn, tablefmt="grid", numalign='center', rowalign='align'))

def subMenu1(): 
    while True:
        inputSubM1 = digitCheck('''
    [1] Detail Siswa Berdasarkan NIS
    [2] Kembali ke Menu Utama

    Silahkan pilih Sub-Menu: ''')

        if inputSubM1 > 2 or inputSubM1 < 1:
            print('\nOpsi tidak tersedia, silahkan coba lagi.')     
        elif inputSubM1 == 1:
            checkSystemOS()
            showSiswa()
            cariDataSiswa('\nMasukkan NIS: ')
        else:
            return


def readConsole():
    checkSystemOS()
    showSiswa()
    subMenu1()