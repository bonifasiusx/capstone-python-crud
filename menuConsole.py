from read import *
from create import *
from Utilities import *

def subMenu1():
    while True:
        inputSubM1 = digitCheck('''
    [1] Detail Siswa Berdasarkan NIS
    [2] Kembali ke Menu Utama

    Silahkan pilih Sub Menu: ''')

        if inputSubM1 == 1:
            cariDataSiswa()
        elif inputSubM1 == 2:
            return welcomeMessage(), mainMenu()
        else:
            print('''
    Opsi tidak tersedia (Mohon pilih opsi 1 atau 2)''')

def mainMenu():
    # welcomeMessage() # checkSystemOS() ada disokin
        
    menu = digitCheck('''
    [1] Tampilkan Data Siswa
    [2] Tambah Data Siswa
    [3] Edit Data Siswa
    [4] Hapus Data Siswa 
    [5] Insight
    [0] Exit

    Silahkan pilih menu: ''')

    if menu == 0:
        return closingMessage()
    elif menu == 1: # checksystemOS() jangan ditaro di dalam showSiswa() supaya pernyataan validasi dari Menu lain ga langsung terhapus
        showSiswa(), subMenu1() # Loop user di subMenu1()
    elif menu == 2:
        return mainMenu()
        # addSiswaBaru(), showSiswa()
    elif menu == 3:
        return mainMenu()
        # pass
        # editDataSiswa()
    elif menu == 4:
        return mainMenu()
        # pass
        # return delDataSiswa()
    else: # Loop mainMenu() sampai user kasih input yang valid
        print('''
    Opsi tidak tersedia (Mohon pilih opsi yang ada)''')
    #     print('''
    # Pilihan tidak tersedia, silahkan coba lagi.''')
        return mainMenu()

