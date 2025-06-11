from create import *
from read import *
from update import *
from delete import *
from Utilities import *

'''
To-Do Next:
-> TO FIX: update.py -> validUpdate() -> siswaDict[idx] (Issue: Looping saat idx = None -> Crash)
-> TO FIX: Implementasi isContinue()
-> Ide Solusi: Terapin while loop hanya di Main Menu dan function di Utilities.py saja
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
    
    # Panggil isContinue untuk kembali ke menu utama
    # if isContinue('\nKembali ke menu utama? [Ya/Tidak]: ', manageBin, returnToMainMenu=True):
    #     return  # Keluar dari manageBin dan kembali ke main menu
    
def mainMenu():
    while True:
        welcomeMessage()
            
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
            showSiswa(), subMenu1() # Loop user di subMenu1()
        elif menu == 2:
            showSiswaBaru(), isContinue('\nLanjutkan menambah Data Siswa Baru? [Ya/Tidak]: ', showSiswaBaru, returnToMainMenu=True)
        elif menu == 3:
            validUpdate(), isContinue('\nApakah Anda ingin melanjutkan update data siswa? [Ya/Tidak]: ', validUpdate, returnToMainMenu=True)
        elif menu == 4:
            askDelete(), isContinue('\nLanjutkan menghapus data? [Ya/Tidak]: ', askDelete, returnToMainMenu=True)
        elif menu == 5: # ---> Refactor Utilities.py
            pass
        elif menu == 6:
            manageBin(), isContinue('\nKembali ke menu utama? [Ya/Tidak]: ', manageBin, returnToMainMenu=True)
            pass