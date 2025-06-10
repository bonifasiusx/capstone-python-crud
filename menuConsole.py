from create import *
from read import *
from delete import *
from Utilities import *

'''
To-Do Next:
-> Update.py berdasarkan key dari siswaDict
-> Menu [5]
'''

def subMenu1(backToMainMenu):
    while True:
        inputSubM1 = digitCheck('''
    [1] Detail Siswa Berdasarkan NIS
    [2] Kembali ke Menu Utama

    Silahkan pilih Sub Menu: ''')

        if inputSubM1 > 2 or inputSubM1 < 1:
            print('\nOpsi tidak tersedia (Mohon pilih opsi 1 atau 2)')     
        elif inputSubM1 == 1:
            cariDataSiswa('\nMasukkan NIS: ')
        else:
            break
    backToMainMenu()
       
def mainMenu():
    welcomeMessage()
        
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
    elif menu == 1:
        showSiswa(), subMenu1(mainMenu) # Loop user di subMenu1()
    elif menu == 2:
        showSiswaBaru(), isContinue('\nLanjutkan menambah Data Siswa Baru? [Ya/Tidak]: ', mainMenu, showSiswaBaru)
    elif menu == 3:
        pass
        # ============ #
    elif menu == 4:
        askDelete(), isContinue('\nLanjutkan menghapus data? [Ya/Tidak]: ', mainMenu, askDelete)
    elif menu == 5: # ---> Refactor Utilities.py
        pass

