from Database import *
from Utilities import digitCheck
from read import cariDataSiswa, showSiswaInDetails

def askDelete():
    showSiswaInDetails()
    while True:
        global bin # Lokasi penampungan soft-delete
        hasilCariSiswa = cariDataSiswa('\nMasukkan NIS untuk menghapus data: ') # Return values -> Tuple

        if hasilCariSiswa == '':
            continue
        
        cariSiswa = hasilCariSiswa[0] 
        
        for idx, siswa in enumerate(siswaDict):
            if siswa['nis'] == cariSiswa:
                bin = siswa
                break
                
        # Validasi hapus data
        isDel = input(f'\nYakin hapus data siswa {bin['nama']} [Ya/Tidak]: ')
        if isDel.lower() == 'ya':
            print(f'\nData siswa {bin['nama']} (NIS: {cariSiswa}) berhasil dihapus.')
            del siswaDict[idx]
            return showSiswaInDetails()        
        elif isDel.lower() == 'tidak':
            print(f'\nPenghapusan data siswa {bin['nama']} telah dibatalkan.')
            return ''
        else:
            print('\nInput tidak dikenali, silahkan coba lagi.')

            

