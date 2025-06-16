from read import cariDataSiswa, showSiswaInDetails
from Utilities import digitCheck, checkSystemOS, loopValidator
from Database import siswaDict, listMapel

def updateDataSiswa():
    showSiswaInDetails() # Tampilkan data sebagai acuan untuk user

    hasil = cariDataSiswa('\nMasukkan NIS untuk data yang ingin di-update: ')
    
    if hasil is None:
        return # Kembali ke Menu Utama (Kuota 3x Pencarian Gagal)
    
    cariSiswa = hasil[0]
    dataSiswaFound = False
    
    for idx, siswa in enumerate(siswaDict):
        if siswa['nis'] == cariSiswa:
            dataSiswaFound = True
            break
        
    if dataSiswaFound:
        siswa = siswaDict[idx]
        return idx, siswa
    
def validUpdate(): # Fungsi untuk Operasi Update Data Siswa
    isValid = False # Validasi untuk memastikan data siswa ditemukan
    try:
        idx, siswa = updateDataSiswa()
        isValid = True 
    except TypeError: # Jika updateDataSiswa mengembalikan None
        return 
    
    while isValid:
        update = digitCheck('''
    Update Data Siswa
    
    [1] NIS
    [2] Nama Siswa
    [3] Kelas Siswa
    [4] Nilai Siswa
    
    Pilih data yang ingin di-update: ''')
    
        if update == 1:
            print('\nDilarang melakukan perubahan pada NIS (Unique ID)')
            continue
        
        elif update == 2: 
            updateNama = input('''
    Masukkan Nama: ''').title()
            if updateNama == '': # Validasi input nama tidak boleh '' (kosong)
                print('\nNama siswa tidak boleh kosong, silahkan coba lagi.')
                continue
            siswa['nama'] = updateNama
        elif update == 3: 
            updateKelas = input('''
    Masukkan Kelas: ''').upper()
            if updateKelas == '': # Validasi input kelas tidak boleh kosong
                print('\nNama kelas tidak boleh kosong, silahkan coba lagi.')
                continue
            siswa['kelas'] = updateKelas
        elif update == 4:
            pilihMapel(siswa) # Update nilai berdasarkan mapel yg dipilih
        else:
            print('\nOpsi tidak tersedia, silahkan coba lagi.')
            continue
        
        isDoneUpdate = input('\nUpdate kolom lainnya? [Ya/Tidak]: ')
        if isDoneUpdate.lower() == 'tidak':
            checkSystemOS()
            print('\nProses update selesai.')
            showSiswaInDetails()
            return 
        elif isDoneUpdate.lower() == 'ya':
            continue

def pilihMapel(siswa): # Sub-Menu untuk memilih mapel yg mau di update
    while True:
        pilih = digitCheck('''    
    [1] Matematika
    [2] IPA
    [3] IPS
    [4] Bahasa Indonesia
    [5] Bahasa Inggris
    
    Pilih Mata Pelajaran: ''')
    
        # listMapel = ['MTK', 'IPA', 'IPS', 'B.IND', 'B.ING']
        
        if pilih in [1, 2, 3, 4, 5]:
            mapel = listMapel[pilih - 1] # Pilih mapel berdasarkan input
            nilaiUpdate = digitCheck(f'''
    Masukkan nilai untuk {mapel}: ''')
            siswa['nilai'][mapel] = nilaiUpdate # Update nilai berdasarkan mapel yg dipilih
            break
        else:
            ('\nMata Pelajaran tidak tersedia, silahkan coba lagi.')
            

def updateConsole():
    checkSystemOS()
    loopValidator(validUpdate, '\nLanjutkan update data siswa? [Ya/Tidak]: ')
