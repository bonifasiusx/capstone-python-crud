import os
from tabulate import tabulate
# from read import *


def checkSystemOS(): # Function untuk auto-clear tampilan di terminal
    system = os.name
    if system == 'posix':
        os.system('clear')
    elif system == 'nt':
        os.system('cls')

siswaDict = [ # List of Dictionary
    {
        'nis': '49LO',
        'nama': 'Leon Kennedy', 
        'kelas': 'IX-1', 
        'nilai': {
            'Matematika': 80,
            'IPA': 78,
            'IPS': 82,
            'Bahasa IND': 88,
            'English': 85
        }
    },
    {
        'nis': '34SEI',
        'nama': 'Sheril Qonita', 
        'kelas': 'IX-1', 
        'nilai': {
            'Matematika': 94,
            'IPA': 88,
            'IPS': 78,
            'Bahasa IND': 86,
            'English': 90
        }
    },
    {
        'nis': '22EIA',
        'nama': 'Elisabeth Rose', 
        'kelas': 'IX-3', 
        'nilai': {
            'Matematika': 72,
            'IPA': 60,
            'IPS': 68,
            'Bahasa IND': 75,
            'English': 62
        }
    },
    {
        'nis': '25JEH',
        'nama': 'Joe Hendrix', 
        'kelas': 'IX-2', 
        'nilai': {
            'Matematika': 80,
            'IPA': 78,
            'IPS': 82,
            'Bahasa IND': 88,
            'English': 85
        }
    },
    {
        'nis': '7RYO',
        'nama': 'Raymond Murphy', 
        'kelas': 'IX-2', 
        'nilai': {
            'Matematika': 88,
            'IPA': 78,
            'IPS': 65,
            'Bahasa IND': 70,
            'English': 82
        }
    },
    {
        'nis': '16DDN',
        'nama': 'Dudung Nalepa', 
        'kelas': 'IX-3', 
        'nilai': {
            'Matematika': 62,
            'IPA': 65,
            'IPS': 65,
            'Bahasa IND': 70,
            'English': 45
        }
    },
]
siswa = [] # To-be --> Nested-list
listMapel = list(siswaDict[0]['nilai'].keys()) 
# Akses key dari: SiswaDict -> [] -> {nilai} {keys,value}
siswaColumn = ['NIS', 'Nama', 'Kelas'] + listMapel # Concate listMapel ke column

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

def showSiswa(): # [1]
    print('\nDaftar Siswa:\n')
    siswa.clear() # Hapus isi list siswa agar data di tabel tidak tumpang-tindih
    for idx, items in enumerate(siswaDict, start=1): # Enumerate untuk indexing tabel
        row = [idx, items['nama'], items['kelas']]
        for mapel in listMapel:
            row.append(items['nilai'].get(mapel))
        siswa.append(row)
           
    print(tabulate(siswa, siswaColumn, tablefmt="grid", numalign='center', rowalign='align'))
    # mainMenu()   

def addNilaiSiswa(): # Support Function Menu [2]
    nilaiBaruMTK = input('\nMasukkan nilai Matematika: ')
    nilaiBaruIPA = input('\nMasukkan nilai IPA: ')
    nilaiBaruIPS = input('\nMasukkan nilai IPS: ')
    nilaiBaruIND = input('\nMasukkan nilai Bahasa Indonesia: ')
    nilaiBaruENG = input('\nMasukkan nilai Bahasa Inggris: ')
    
    if not nilaiBaruMTK.isdigit() or not nilaiBaruIPA.isdigit() or not nilaiBaruIPS.isdigit() or not nilaiBaruIND.isdigit() or not nilaiBaruENG.isdigit():
        print('Invalid nilai! Mohon masukkan nilai yang valid.')
        return addNilaiSiswa()
    else:
        return nilaiBaruMTK, nilaiBaruIPA, nilaiBaruIPS, nilaiBaruIND, nilaiBaruENG

def addSiswa(): # [2]
    siswaBaru = input('\nNama Siswa Baru\t: ').title() 
    kelasSiswaBaru = input('Kelas\t\t: ').upper()
    # Validasi input nilai siswa baru
    nilaiBaruMTK = input('\nMasukkan nilai Matematika: ')
    nilaiBaruIPA = input('Masukkan nilai IPA: ')
    nilaiBaruIPS = input('Masukkan nilai IPS: ')
    nilaiBaruIND = input('Masukkan nilai Bahasa Indonesia: ')
    nilaiBaruENG = input('Masukkan nilai Bahasa Inggris: ')
    
    if not nilaiBaruMTK.isdigit() or not nilaiBaruIPA.isdigit() or not nilaiBaruIPS.isdigit() or not nilaiBaruIND.isdigit() or not nilaiBaruENG.isdigit():
        print('Invalid nilai! Mohon masukkan nilai yang valid.')
        return addSiswa()

    siswaDict.append({ # Append data baru ke siswaDict
        'nama': siswaBaru,
        'kelas': kelasSiswaBaru,
        'nilai': {
            'Matematika': nilaiBaruMTK,
            'IPA': nilaiBaruIPA,
            'IPS': nilaiBaruIPS,
            'Bahasa IND': nilaiBaruIND,
            'English': nilaiBaruENG
        }
    }) 
    checkSystemOS()
    print(f"\nConfirmed. Data siswa baru ({siswaDict[-1]['nama']}) berhasil ditambahkan!")
    showSiswa()

# UPDATE [3] PROBLEM ---> editDataSiswa()
def cariDataSiswa(): # Additional Menu + Support Function Menu [3]
    cariSiswa = input('\nMasukkan NIS: ').upper()
    targetSiswa = {} # Cocokin type data dengan tempat data siswa disimpan -> siswa == Dictionary
    
    for siswa in siswaDict:
        if siswa['nis'] == cariSiswa:
            targetSiswa = siswa
            break
    # for loop dulu baru cek validasi, jangan ketuker!
    if targetSiswa == {}:
        print(f'Siswa dengan NIS {cariSiswa} tidak ditemukan')
        return cariDataSiswa()
    
    # Akses nested-dict supaya setiap mapel jadi kolom
    listMapelTarget = list(targetSiswa['nilai'].keys())
    listNilaiTarget = list(targetSiswa['nilai'].values())
    targetColumn = ['Nama', 'Kelas'] + listMapelTarget
    targetRow = [targetSiswa['nama'], targetSiswa['kelas']] + listNilaiTarget
    
    checkSystemOS()
    print(f'NIS {cariSiswa} ditemukan!\n')
    print(tabulate([targetRow], headers=targetColumn, tablefmt="grid", numalign='center', rowalign='center'))
    # Jadiin function support untuk editDataSiswa()
    return cariSiswa, targetSiswa, listMapelTarget, listNilaiTarget, targetColumn, targetRow 

def editDataSiswa(): # [3] PROBLEM AT LINE 186-222
    # --> Simpan return value di cariDataSiswa() ke local var editDataSiswa()
    cariSiswa, targetSiswa, listMapelTarget, listNilaiTarget, targetColumn, targetRow = cariDataSiswa() 
    targetColumnUpper = targetColumn.copy()
    targetColumnUpper = [target.upper() for target in targetColumnUpper] # .copy() agar huruf besar-kecil kolom di tabel hasil tetap sama
    # Kolom -> UPPER supaya bisa dicocokkan dengan input editData
    editData = input('Pilih nama kolom yang ingin dirubah: ').upper()
    
    if editData != 'IPA' and editData != 'IPS':
        editData = editData.title()
    elif editData not in targetColumnUpper:
        print('Kolom tidak ditemukan, silahkan coba lagi.')
        return editData

    listMapelTarget = list(targetSiswa['nilai'].keys())
    listNilaiTarget = list(targetSiswa['nilai'].values())
    targetColumn = ['Nama', 'Kelas'] + listMapelTarget
    targetRow = [targetSiswa['nama'], targetSiswa['kelas']] + listNilaiTarget

    if editData == 'Nama':
        targetSiswa['nama'] = input('Masukkan nama baru: ').title()
    elif editData == 'Kelas':
        targetSiswa['kelas'] = input('Masukkan kelas baru: ').upper()
    else:
        updateNilaiSiswa = input(f'Masukkan nilai baru untuk {editData}: ') 
        if not updateNilaiSiswa.isdigit():
            print('Mohon masukkan nilai yang valid, silahkan coba lagi.')
            return updateNilaiSiswa
        
        targetSiswa['nilai'][editData] = updateNilaiSiswa
        listMapelTarget = list(targetSiswa['nilai'].keys())
        listNilaiTarget = list(targetSiswa['nilai'].values())
        targetColumn = ['Nama', 'Kelas'] + listMapelTarget
        targetRow = [targetSiswa['nama'], targetSiswa['kelas']] + listNilaiTarget 
                
    print(f'\nCompleted! Nilai {editData} {cariSiswa} berhasil diperbaharui.\n')
    print(tabulate([targetRow], headers=targetColumn, tablefmt="grid", numalign='center', rowalign='center'))

    isContinueEdit = input('\nLanjutkan edit data siswa? [Y/N]: ')
    if isContinueEdit == 'y' or isContinueEdit == 'Y':
        return cariDataSiswa()
    else:
        return
# editDataSiswa()
# user_pause = input()
'''
Problem to fix:
- Tampilan tabel 'target' tumpang-tindih setiap kali user pilih 'Y'
- isContinueEdit masih salah logic Return
- Opsi solusi:
    -> While True VS Re-Assign
    -> Bikin function support 1 lagi untuk menu [3]
- To Do Next:
    -> Pecah function-function setiap Menu ke script yang beda (Karena ini syntax udah 200+)
    -> [1] + Median, Status Kelulusan
    -> [2] + Looping addSiswa()
    -> [4] + Konfirmasi delDataSiswa()    
'''

def delDataSiswa(): # [4]
    delSiswa = input('\nMasukkan index siswa yang ingin dihapus: ')
        
    if not delSiswa.isdigit():
        print('\nInvalid Input, silahkan coba lagi.')
        delDataSiswa()
    
    idx_del = int(delSiswa)    
    # Jika index yang di-input > jumlah data PRODUCT atau kurang dari 1
    if idx_del > len(siswa) or idx_del < 1:
        print('Index tidak dikenali, silahkan coba lagi.')
        delDataSiswa()
    # Hapus isi list siswa berdasarkan index (dikurangi 1 agar sesuai dengan indexing)
    else:
        checkSystemOS()
        print(f'\nConfirmed. Data siswa ({siswa[idx_del - 1][1]}) berhasil dihapus!')
        del siswaDict[idx_del - 1] # Confirmed msg dulu, lalu hapus
        showSiswa()

def mainMenu():
    checkSystemOS()
    welcomeMessage()
    
    menu = input('''
    [1] Tampilkan Data Siswa
    [2] Tambah Data Siswa
    [3] Edit Data Siswa
    [4] Hapus Data Siswa 
    [5] Insight
    [0] Exit

    Silahkan pilih menu: ''')

    if menu == '0':
        return closingMessage()
    elif menu == '1': # checksystemOS() jangan ditaro di dalam showSiswa() supaya pernyataan validasi dari Menu lain ga langsung terhapus
        return showSiswa()
    elif menu == '2':
        return addSiswa()
    elif menu == '3':
        editDataSiswa()
    elif menu == '4':
        return delDataSiswa()
    else: # Loop mainMenu() sampai user kasih input yang valid
        print('''
    Pilihan tidak tersedia, silahkan coba lagi.''')
        return mainMenu()

def main():
    mainMenu()

if __name__ == '__main__':
    main()