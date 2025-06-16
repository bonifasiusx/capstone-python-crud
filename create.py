from Database import siswaDict
from Utilities import digitCheck, checkSystemOS, loopValidator
from read import showSiswaInDetails
import random

def isSiswaExist(msg): # Fungsi untuk validasi jika input data baru sudah ada
    while True:
        cekNama = input(msg).title()
        if cekNama == '': # Validasi nama kosong
            print('\nNama siswa tidak boleh kosong, silahkan coba lagi.')
            continue        
            
        # Validasi data siswa baru sudah ada duplikatnya
        for siswa in siswaDict:
            if cekNama == siswa['nama']:
                print(f'''
Data siswa bernama {cekNama} sudah tercatat di dashboard
Silahkan pilih Menu Edit Data jika ingin melakukan perubahan''')
                return False
        return cekNama # Else -> Nama yang baru dimasukkan = Valid
        
def addSiswaBaru(): # Fungsi untuk menambahkan data siswa baru
    namaSiswaBaru = isSiswaExist('\nTambah Nama Siswa Baru\t: ')
    if not namaSiswaBaru:
        return None # Jika input baru tervalidasi tidak ada duplikat

    while True: # Validasi kelas tidak boleh kosong
        kelasSiswaBaru = input('Kelas\t\t\t: ').upper()
        if kelasSiswaBaru == '':
            print('\nKelas siswa tidak boleh kosong, silahkan coba lagi.\n')
            continue
        else:
            break
                
    # Validasi input user untuk siswa baru
    nilaiBaruMTK = digitCheck('Nilai Matematika\t: ')
    nilaiBaruIPA = digitCheck('Nilai IPA\t\t: ')
    nilaiBaruIPS = digitCheck('Nilai IPS\t\t: ')
    nilaiBaruIND = digitCheck('Nilai Bahasa Indonesia\t: ')
    nilaiBaruENG = digitCheck('Nilai Bahasa Inggris\t: ')
    
    # Validasi simpan data
    isSave = input(f'\nSimpan data? [Ya/Tidak]: ')
    if isSave.lower() == 'ya':
        return namaSiswaBaru, kelasSiswaBaru, nilaiBaruMTK, \
        nilaiBaruIPA, nilaiBaruIPS, nilaiBaruIND, nilaiBaruENG
    else:
        print('\nPenambahan data baru telah dibatalkan.')
        return None
        
def nisSiswaBaru(nama): # Fungsi untuk generate Unique NIS untuk siswa baru
# NIS =  2 Angka Random + 2 Huruf Inisial
    randomNIS = str(random.randrange(10,100,3))
    inisial = nama[:5:2].upper()
    nisBaru = randomNIS + inisial[:2]    

    return nisBaru
    
def showSiswaBaru(): 
    # Tangkap user input dari fungsi addSiswaBaru()
    hasilSiswaBaru = addSiswaBaru()
    if hasilSiswaBaru == None or len(hasilSiswaBaru) < 7:
        return 
    
    namaBaru, kelasBaru, nMTk, nIPA, nIPS, nIND, nENG = hasilSiswaBaru
    
    nisBaru = nisSiswaBaru(namaBaru) # Append data siswa baru ke siswaDict
    siswaDict.append({
        'nis': nisBaru,
        'nama': namaBaru,
        'kelas': kelasBaru,
        'nilai': {
            'MTK': nMTk,
            'IPA': nIPA,
            'IPS': nIPS,
            'B.IND': nIND,
            'B.ING': nENG
            }
        })
    
    print('\nSiswa baru berhasil ditambahkan!')
    print(f'\nData Siswa Baru:\nNIS\t: {siswaDict[-1]['nis']}\nNama\t: {siswaDict[-1]['nama']}')
    showSiswaInDetails()
    
    
def createConsole():
    checkSystemOS()
    loopValidator(showSiswaBaru, '\nLanjutkan menambah Data Siswa Baru? [Ya/Tidak]: ')
