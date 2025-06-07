from read import *

def subMenu1():
    while True:
        subMenuInputUser = digitCheck('''
[1] Lihat Detail Data Siswa
[2] Detail Siswa Berdasarkan NIS
[3] Kembali ke Menu Utama

Silahkan pilih Sub Menu: ''')
        
        if subMenuInputUser == '1':
            showSiswaInDetails()
        elif subMenuInputUser == '2':
            cariDataSiswa()
        elif subMenuInputUser == '3':
            return welcomeMessage(), mainMenu()
        else:
            print('Pilihan tidak tersedia, silahkan coba lagi.')

def mainMenu():
    # welcomeMessage() # checkSystemOS() ada disokin
        
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
        showSiswa(), subMenu1() # Loop user di subMenu1()
    elif menu == '2':
        return mainMenu()
        # pass
        # return addSiswa()
    elif menu == '3':
        return mainMenu()
        # pass
        # editDataSiswa()
    elif menu == '4':
        return mainMenu()
        # pass
        # return delDataSiswa()
    else: # Loop mainMenu() sampai user kasih input yang valid
        print('''
    Pilihan tidak tersedia, silahkan coba lagi.''')
        return mainMenu()

# def main():
#     mainMenu()

# if __name__ == '__main__':
#     main()