from Database import *
from Utilities import digitCheck, checkSystemOS, backToMenu, loopValidator
from read import cariDataSiswa, showSiswaInDetails

bin = [] # Lokasi penampungan soft-delete

def askDelete():
    showSiswaInDetails()
    while True:
        hasilCariSiswa = cariDataSiswa('\nMasukkan NIS untuk menghapus data: ') # Return values -> Tuple

        if hasilCariSiswa is None:
            return # Kembali ke Menu Utama (Kuota 3x Pencarian Gagal)
        
        cariSiswa = hasilCariSiswa[0] 
        dataSiswaFound = False
        
        for idx, siswa in enumerate(siswaDict): # Cari data berdasarkan input NIS
            if siswa['nis'] == cariSiswa:
                dataSiswaFound = True
                break
            
        if dataSiswaFound:          
            # Validasi hapus data
            isDel = input(f'\nYakin hapus data siswa {hasilCariSiswa[1]['nama']} [Ya/Tidak]: ')

            if isDel.lower() == 'ya':
                checkSystemOS()
                print(f'\nData siswa {hasilCariSiswa[1]['nama']} (NIS: {cariSiswa}) berhasil dihapus.')
                bin.append(siswa) # Data pindah ke bin (soft delete)
                del siswaDict[idx] # Hapus data dari siswaDict
                showSiswaInDetails() # Tampilkan setelah soft delete selesai
                return        
            elif isDel.lower() == 'tidak':
                print(f'\nPenghapusan data siswa {hasilCariSiswa[1]['nama']} telah dibatalkan.')
                return ''
            else:
                print('\nInput tidak dikenali, silahkan coba lagi.')
        
        else:
            print(f'\nSiswa dengan NIS {hasilCariSiswa} tidak ditemukan, silahkan coba lagi.')

def displayBin(): # Fungsi untuk menampilkan Recycle Bin
    if not bin:
        checkSystemOS()
        print('\nRecycle Bin kosong.')
        return False  # Tidak menampilkan apa-apa
    checkSystemOS()
    print('\nRecycle Bin (Recently Deleted):\n')
    for i, siswa in enumerate(bin): # Tampilkan data yang ada di Recycle Bin
        print(f"{i + 1}. NIS: {siswa['nis']}, Nama: {siswa['nama']}, Kelas: {siswa['kelas']}")
    return True 

def restoreStudent(): # Fungsi untuk mengembalikan siswa dari bin ke siswaDict
    siswaIndex = digitCheck('\nMasukkan nomor data yang ingin di-restore: ') - 1
    if siswaIndex >= 0 and siswaIndex < len(bin): # Validasi Index yang dipilih
        restoreDelSiswa = bin.pop(siswaIndex)  # Hapus data dari Recycle Bin
        siswaDict.append(restoreDelSiswa) # Masukkan kembali data ke siswaDict
        checkSystemOS()
        print(f"\nData siswa {restoreDelSiswa['nama']} berhasil di-restore.")
        showSiswaInDetails()
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
        return True
    else:
        print('\nInput nomor tidak valid. Silahkan coba lagi.')
        return False

def permanentlyDeleteStudent(): # Fungsi untuk menghapus siswa secara permanen dari bin
    siswaIndex = digitCheck('\nMasukkan nomor data yang ingin dihapus permanen: ') - 1
    if siswaIndex >= 0 and siswaIndex < len(bin):
        deletePermanent = bin.pop(siswaIndex)  # Hapus data secara permanen
        print(f"\nData siswa {deletePermanent['nama']} berhasil dihapus secara permanen.")
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
        return True
    else:
        print('\nInput nomor tidak valid. Silahkan coba lagi.')
        return False
    
def binConsole():    
    if not displayBin(): # Jika Recycle Bin kosong, keluar dari function
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
        return
                    
    while True:
        try:
            pilihan = digitCheck('''    
    [1] Restore Data Siswa
    [2] Hapus Permanen Data Siswa
    [3] Kembali ke Menu Utama
    
    Pilih Sub-Menu Recyle Bin: ''')
            
            if pilihan == 1:
                restoreStudent()
                break
            elif pilihan == 2:
                permanentlyDeleteStudent()
                break
            elif pilihan == 3:
                break
        except ValueError:
            print('\nInput tidak valid, mohon pilih Sub-Menu yang tersedia.')
            
def deleteConsole():
    checkSystemOS()
    loopValidator(askDelete, '\nLanjutkan menghapus Data Siswa? [Ya/Tidak]: ')
