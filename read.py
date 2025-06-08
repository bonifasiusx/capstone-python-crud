from tabulate import tabulate
from Database import *
from Utilities import gradeNilai

# Flow yang diinginkan:
# Menu 1 -> Siswa + Status
# SubMenu1 -> Input NIS -> Siswa + Nilai Setiap Mapel = cariDataSiswa()
# showSiswaInDetails() ??? -> Rombak untuk jadi function di Menu [5] Insight -> Siswa/Mapel + Insight

def showSiswaInDetails(): # PROBLEM TO FIX
    siswa.clear() # .clear() agar output tabel data tidak tumpang-tindih
    
    print('\nDashboard Siswa in Details:\n')
    for nis, items in enumerate(siswaDict):        
        row = [items['nis'], items['nama'], items['kelas']]
        for mapel in listMapel:
            row.append(items['nilai'].get(mapel))
        siswa.append(row)       
           
    print(tabulate(siswa, siswaColumn, tablefmt="grid", numalign='center', rowalign='align'))
    return
    # return subMenu1

def cariDataSiswa(): # Sub-Menu [1] -> Detail Siswa Berdasarkan NIS
    cariSiswa = input('\nMasukkan NIS: ').upper()
    targetSiswa = {} # Cocokin type data dengan tempat data siswa disimpan -> siswa == Dictionary
    
    for siswa in siswaDict:
        if siswa['nis'] == cariSiswa:
            targetSiswa = siswa
            break
    # for loop dulu baru cek validasi, jangan ketuker!
    if targetSiswa == {}:
        print(f'Siswa dengan NIS: {cariSiswa} tidak ditemukan')
        return
    
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
    siswa.clear() # .clear() agar output tabel data tidak tumpang-tindih
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

