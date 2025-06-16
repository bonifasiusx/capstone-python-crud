from Utilities import welcomeMessage, closingMessage, checkSystemOS, digitCheck, backToMenu
from create import createConsole
from read import readConsole
from update import updateConsole
from delete import deleteConsole, binConsole
from insight import insightConsole
from time import sleep

def login(username, password): # Fungsi untuk limitasi akses antara ADMIN & GUEST
    user = 'admin'
    passwd = 'rungkad7x7x'
    roles = ['ADMIN', 'GUEST']

    loginAttempt = 0
    while loginAttempt < 3:
        checkUsername = input(username)
        checkPassword = input(password)
        
        if checkUsername == user and checkPassword == passwd:
            role = roles[0]
            print('\nLOGIN SUCCESS')
            sleep(0.5)
            print('Initializing system...')
            sleep(0.5)
            print('Granting full access...')
            sleep(0.5)
            break
        else:
            loginAttempt += 1
            if loginAttempt < 3:
                print(f'\nIncorrect Password ({3 - loginAttempt} attempts left)')
                sleep(0.5)
                checkSystemOS()
            else:
                role = roles[1]
                print(f'\nLimiting access...')
                sleep(0.5)
                print(f'SETTING ROLE AS {role}')
                sleep(0.5)
                break

    return checkUsername, checkPassword, role        

def mainMenu():
    isAdmin = login('\nUSER\t\t: ', 'PASSWORD\t: ')
    isAdmin = isAdmin[-1]

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
        
        if isAdmin == 'ADMIN':
            pass
        else: # Limitasi akses GUEST dari fitur Edit, Delete, dan Recycle Bin
            if menu == 3 or menu == 4 or menu == 6:
                checkSystemOS()
                print('\nAkses ditolak, hanya ADMIN yang dapat mengakses fitur ini.')
                backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
                continue
        
        if menu == 0:
            return closingMessage()
        elif menu == 1:
            readConsole()
        elif menu == 2:
            createConsole()
        elif menu == 3:
            updateConsole()
        elif menu == 4:
            deleteConsole()
        elif menu == 5:
            checkSystemOS()
            insightConsole()
        elif menu == 6:
            binConsole()
     

if __name__ == '__main__':
    mainMenu()