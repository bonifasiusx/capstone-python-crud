from Database import *
from Utilities import digitCheck, checkSystemOS
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
                bin.append(siswa) # Data pindah ke bin (soft delete)
                dataSiswaFound = True
                break
            
        if dataSiswaFound:          
            # Validasi hapus data
            isDel = input(f'\nYakin hapus data siswa {bin[-1]['nama']} [Ya/Tidak]: ')
            if isDel.lower() == 'ya':
                print(f'\nData siswa {bin[-1]['nama']} (NIS: {cariSiswa}) berhasil dihapus.')
                del siswaDict[idx] # Hapus data dari siswaDict
                showSiswaInDetails() # Tampilkan setelah soft delete selesai
                return        
            elif isDel.lower() == 'tidak':
                print(f'\nPenghapusan data siswa {bin[-1]['nama']} telah dibatalkan.')
                return ''
            else:
                print('\nInput tidak dikenali, silahkan coba lagi.')
        
        else:
            print(f'\nSiswa dengan NIS {hasilCariSiswa} tidak ditemukan, silahkan coba lagi.')

def displayBin(): # Function untuk menampilkan Recycle Bin
    if not bin:
        print('\nRecycle Bin kosong.')
        return False  # Tidak menampilkan apa-apa
    print('\nRecycle Bin (Recently Deleted):\n')
    for i, siswa in enumerate(bin): # Tampilkan data yang ada di Recycle Bin
        print(f"{i + 1}. NIS: {siswa['nis']}, Nama: {siswa['nama']}, Kelas: {siswa['kelas']}")
    return True 

def restoreStudent(): # Function untuk mengembalikan siswa dari bin ke siswaDict
    siswaIndex = digitCheck('\nMasukkan nomor data yang ingin di-restore: ') - 1
    if siswaIndex >= 0 and siswaIndex < len(bin): # Validasi Index yang dipilih
        restoreDelSiswa = bin.pop(siswaIndex)  # Hapus data dari Recycle Bin
        siswaDict.append(restoreDelSiswa)  # Masukkan kembali data ke siswaDict
        print(f"\nData siswa {restoreDelSiswa['nama']} berhasil di-restore.")
        showSiswaInDetails()
        return True
    else:
        print('\nInput nomor tidak valid. Silahkan coba lagi.')
        return False

def permanentlyDeleteStudent(): # Function untuk menghapus siswa secara permanen dari bin
    siswaIndex = digitCheck('\nMasukkan nomor data yang ingin dihapus permanen: ') - 1
    if siswaIndex >= 0 and siswaIndex < len(bin):
        deletePermanent = bin.pop(siswaIndex)  # Hapus data secara permanen
        print(f"\nData siswa {deletePermanent['nama']} berhasil dihapus secara permanen.")
        showSiswaInDetails() # Tampilkan setelah permanent delete selesai
        return True
    else:
        print('\nInput nomor tidak valid. Silahkan coba lagi.')
        return False
    
def deleteConsole():
    while True:
        askDelete()
        isDone = input('\nLanjutkan menghapus Data Siswa? [Ya/Tidak]: ')
        if isDone.lower() == 'tidak':
            return
        elif isDone.lower() == 'ya':
            checkSystemOS()
            continue
        else:
            print('\nInput tidak dikenali, kembali ke Menu Utama.')
            return


if __name__ == '__main__':
    deleteConsole()