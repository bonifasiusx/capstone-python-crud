from Database import *
from Utilities import backToMenu
from tabulate import tabulate

def mapelSulit():
    # Mendapatkan semua mapel yang ada
    listMapel = list(siswaDict[0]['nilai'].keys())
    avgMapel = {}
    
    # Hitung rata-rata nilai per mapel
    for mapel in listMapel:
        totalNilai = 0
        for siswa in siswaDict:
            totalNilai += int(siswa['nilai'][mapel]) # pastikan konversi ke int 
        rata2Mapel = totalNilai / len(siswaDict)  # hitung rata-rata mapel
        avgMapel[mapel] = rata2Mapel

    # Tentukan mapel terberat dan termudah 
    mapelTertinggi = max(avgMapel, key=avgMapel.get)  
    mapelTerendah = min(avgMapel, key=avgMapel.get)  

    return mapelTertinggi, avgMapel[mapelTertinggi], mapelTerendah, avgMapel[mapelTerendah]

def rataKelulusan():
    lulus = 0
    totalSiswa = len(siswaDict)

    for siswa in siswaDict:
        if all(int(nilai) >= 60 for nilai in siswa['nilai'].values()):  # Cek semua nilai >= 60
            lulus += 1
    
    persentaseKelulusan = (lulus / totalSiswa) * 100
    return persentaseKelulusan

def showMapelSulit():
    # Mengambil hasil mapel sulit dan mudah
    mapelTertinggi, nilaiTertinggi, mapelTerendah, nilaiTerendah = mapelSulit()
    nilaiTerendah = round(nilaiTerendah, 2)
    nilaiTertinggi = round(nilaiTertinggi, 2)
    persentaseLulus = rataKelulusan()
    persentaseLulus = round(persentaseLulus, 2)

    # Data untuk tabel mapel sulit dan mudah
    dataMapel = [
        ['Mata Pelajaran Tersulit', mapelTerendah, nilaiTerendah],
        ['Mata Pelajaran Termudah', mapelTertinggi, nilaiTertinggi],
    ]
    
    # Header tabel mapel
    headersMapel = ['Keterangan', 'Mata Pelajaran', 'Rata-Rata']

    # Menampilkan tabel mapel dengan tabulate
    print(tabulate(dataMapel, headers=headersMapel, tablefmt="grid", numalign="center"))
    
    # Data untuk tabel persentase kelulusan
    dataKelulusan = [[f'Persentase Kelulusan Seluruh Siswa = {persentaseLulus}%']]
    
    # Menampilkan tabel persentase kelulusan terpisah
    print("\n" + tabulate(dataKelulusan, tablefmt="grid", numalign="center"))

def insightConsole():
    while True:
        showMapelSulit()
        backToMenu('\nTekan ENTER untuk kembali ke Menu Utama\n')
        return
