from Database import *
from Utilities import digitCheck, checkSystemOS
from read import showSiswaInDetails
import random

'''
To-Do Next:
-> Optimasi flow untuk showSiswaBaru() (Hindari nested-while & return recursive function)
-> Sambungkan create.py ke menuConsole
'''

def checkDuplicateSiswa(msg):
    while True: # Validasi nama kosong
        cekNama = input(msg).title()
        if cekNama == '':
            print('''
    Nama siswa tidak boleh kosong, silahkan coba lagi.''')
            continue        
    
        # Validasi data siswa baru sudah ada duplikatnya
        for siswa in siswaDict:
            if cekNama == siswa['nama']:
                print(f'''
    Data siswa bernama {cekNama} sudah tercatat di dashboard
    Silahkan pilih Menu Edit Data jika ingin melakukan perubahan''')
                return ''
        return cekNama

def addSiswaBaru():
    # while True:
        # checkDuplicateSiswa(namaSiswaBaru) # Cek duplikat data siswa baru
    namaSiswaBaru = checkDuplicateSiswa('\nTambah Nama Siswa Baru\t: ') 
        # if namaSiswaBaru != '':
            # break
    while True:    
        kelasSiswaBaru = input('Kelas\t\t\t: ').upper()
        if kelasSiswaBaru == '':
            print('''
    Kelas siswa tidak boleh kosong, silahkan coba lagi.''')
            continue
        else:
            break        
    # Validasi userInput untuk siswa baru
    nilaiBaruMTK = digitCheck('Nilai Matematika\t: ')
    nilaiBaruIPA = digitCheck('Nilai IPA\t\t: ')
    nilaiBaruIPS = digitCheck('Nilai IPS\t\t: ')
    nilaiBaruIND = digitCheck('Nilai Bahasa Indonesia\t: ')
    nilaiBaruENG = digitCheck('Nilai Bahasa Inggris\t: ')
     
    return namaSiswaBaru, kelasSiswaBaru, nilaiBaruMTK, \
    nilaiBaruIPA, nilaiBaruIPS, nilaiBaruIND, nilaiBaruENG
# addSiswaBaru()

def nisSiswaBaru(nama):
    # Generate Unique NIS untuk siswa baru
    # NIS =  2 Angka Random + 2 Huruf Inisial
    randomNIS = str(random.randrange(10,100,3))
    inisial = nama[:5:2].upper()
    nisBaru = randomNIS + inisial[:2]    

    return nisBaru
# nisSiswaBaru()

def showSiswaBaru(): # [2]
    while True:
        # Tangkap user input dari fungsi addSiswaBaru()
        namaBaru, kelasBaru, nMTk, nIPA, nIPS, nIND, nENG = addSiswaBaru()
        
        isSave = input('\nSimpan Data? [Ya/Tidak]: ')
        if isSave.lower() == 'tidak':
            print(f'''
    Penambahan Data Siswa ({namaBaru}) dibatalkan.''')
        elif isSave.lower() == 'ya':
            nisBaru = nisSiswaBaru(namaBaru) # Append data siswa baru ke siswaDict
            siswaDict.append({
                'nis': nisBaru,
                'nama': namaBaru,
                'kelas': kelasBaru,
                'nilai': {
                    'Matematika': nMTk,
                    'IPA': nIPA,
                    'IPS': nIPS,
                    'Bahasa IND': nIND,
                    'English': nENG
                    }
                })
            # Validasi Penyimpanan Data
            print(f'\nData Siswa Baru:\nNIS\t: {siswaDict[-1]['nis']}\nNama\t: {siswaDict[-1]['nama']}')

            print('Siswa baru berhasil ditambahkan!')
            # checkSystemOS()
            showSiswaInDetails()
        else:
            print('Input tidak dikenali, melanjutkan program.')
            continue
        
        isContinue = input('\nLanjutkan menambah Data Siswa Baru? [Ya/Tidak]: ')
        if isContinue.lower() == 'tidak':
            break
        else:
            print('Input tidak dikenali, melanjutkan program.')
            continue
showSiswaBaru()
