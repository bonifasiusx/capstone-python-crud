from create import *
from read import *
from update import *
from delete import *
from Utilities import *

'''
To-Do Next:
-> Menu [5] -> Mapel dengan tingkat kesulitan tertinggi/terendah
-> Rata-rata kelulusan siswa
'''

def subMenu1():
    while True:
        inputSubM1 = digitCheck('''
    [1] Detail Siswa Berdasarkan NIS
    [2] Kembali ke Menu Utama

    Silahkan pilih Sub Menu: ''')

        if inputSubM1 > 2 or inputSubM1 < 1:
            print('\nOpsi tidak tersedia, silahkan coba lagi.')     
        elif inputSubM1 == 1:
            cariDataSiswa('\nMasukkan NIS: ')
        else:
        #     # Jika memilih untuk kembali ke menu utama, panggil isContinue dengan returnToMainMenu=True
        #     isContinue('Apakah Anda ingin melanjutkan update data siswa? [Ya/Tidak]: ', None, returnToMainMenu=True)
            break # Kembali ke Main Menu jika isContinue = 'ya'

def manageBin():
    if not displayBin():
        return  # Jika Recycle Bin kosong, keluar dari function
    
    while True:
        try:
            pilihan = digitCheck('''    
    [1] Restore Data Siswa
    [2] Hapus Permanen Data Siswa
    
    Pilih Sub-Menu Recyle Bin: ''')
            
            if pilihan == 1:
                if restoreStudent():
                    break  # Exit setelah selesai restore
            elif pilihan == 2:
                if permanentlyDeleteStudent():
                    break  # Exit setelah permanent delete selesai
        except ValueError:
            print('\nInput tidak valid, mohon pilih Sub-Menu yang tersedia.')

def binConsole():
    while True:
        manageBin()
        isDone = input('\nKembali ke menu utama? [Ya/Tidak]: ')
        if isDone.lower() == 'ya':
            return
        elif isDone.lower() == 'tidak':
            checkSystemOS()
            continue
        else:
            print('\nInput tidak dikenali, kembali ke Menu Utama.')
            return
    
def mainMenu():
    while True:
        welcomeMessage() # -----------
            
        menu = digitCheck('''
    [1] Tampilkan Data Siswa
    [2] Tambah Data Siswa
    [3] Edit Data Siswa
    [4] Hapus Data Siswa 
    [5] Insight
    [6] Recycle Bin
    [0] Exit

    Silahkan pilih menu: ''')

        if menu == 0:
            return closingMessage()
        elif menu == 1:
            checkSystemOS()
            showSiswa(), subMenu1() # Loop user di subMenu1()
        elif menu == 2:
            checkSystemOS()
            createConsole()
            # showSiswaBaru(), isContinue('\nLanjutkan menambah Data Siswa Baru? [Ya/Tidak]: ', showSiswaBaru, returnToMainMenu=True)
        elif menu == 3:
            checkSystemOS()
            updateConsole()
        elif menu == 4:
            checkSystemOS()
            deleteConsole()
        elif menu == 5: # ---> Refactor Utilities.py
            pass
        elif menu == 6:
            checkSystemOS()
            binConsole()
     
            
if __name__ == '__main__':
    mainMenu()