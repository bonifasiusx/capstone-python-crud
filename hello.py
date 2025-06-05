from tabulate import tabulate

siswaDict = [
    {
        'nama': 'Leon Kennedy', 
        'kelas': 'XII IPS 3', 
        'nilai': 65,
    },
    {
        'nama': 'Sheril Qonita', 
        'kelas': 'XII IPS 2', 
        'nilai': 75,
    },
    {
        'nama': 'Joe Hendrix', 
        'kelas': 'XII IPS 1', 
        'nilai': 90,
    }
]
siswa = []
siswaHeader = ['Idx', 'Nama', 'Kelas', 'Nilai']

def welcomeMessage():
    welcome = 'SOCIAL SCIENCES STUDENT DATABASE'
    welcomeSymbol = '=' * len(welcome)

    print(f'\t{welcomeSymbol}')
    print(f'\t{welcome}')
    print(f'\t{welcomeSymbol}')
welcomeMessage()

def closingMessage():
    closing_msg = [['PROGRAM SELESAI, TERIMAKASIH']]
    print('\n\n')
    print(tabulate(closing_msg, tablefmt='grid', stralign='center'))
closingMessage()    

def showSiswa():
    print('\nDaftar Siswa:\n')
    siswa.clear() # Hapus isi list siswa agar data di tabel tidak tumpang-tindih
    for idx, items in enumerate(siswaDict, start=1): # Enumerate untuk indexing tabel
        siswa.append([idx, items['nama'], items['kelas'], items['nilai']])
            
    print(tabulate(siswa, siswaHeader, tablefmt="grid", rowalign='left')) 
showSiswa()   

def addSiswa():
    siswaBaru = input('\nNama Siswa Baru\t: ').title() 
    kelasSiswaBaru = input('Kelas\t\t: ').upper()
    nilaiSiswaBaru = input('Masukkan Nilai\t: ')
    
    if not nilaiSiswaBaru.isdigit(): # Validasi input
        print('\nNilai tidak valid, silahkan coba lagi.')
        addSiswa() # Loop sampai user kasih input yang valid
    siswaDict.append({ # Append data baru ke siswaDict
        'nama': siswaBaru,
        'kelas': kelasSiswaBaru,
        'nilai': nilaiSiswaBaru
    }) 
    showSiswa()
    print('\nConfirmed. Siswa baru berhasil ditambahkan!\n')
addSiswa()

def mainMenu():
    menu = input('''
    [1] Tampilkan Data Siswa
    [2] Tambah Data Siswa
    [3] Edit Data Siswa
    [4] Hapus Data Siswa 
    [5] Insight
    [0] Exit

    Silahkan pilih menu: ''')

    if not menu.isdigit(): # Validasi input
        print('''
    Pilihan tidak tersedia, silahkan coba lagi.''')
        return mainMenu() # Loop mainMenu() sampai user kasih input yang valid
    else:
        return closingMessage()
mainMenu()

if mainMenu == '1': # [1] Tampilkan Data Siswa
    pass
elif mainMenu == '2': # [2] Tambah Data Siswa
    pass
elif mainMenu == '3': # [3] Edit Data Siswa 
    pass
elif mainMenu == '4': # [4] Hapus Data Siswa
    pass
elif mainMenu == '5': # [5] Insight
    pass
else: # [0] Exit
    pass