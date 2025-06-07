'''
INI ADALAH TUGAS LATIHAN PERTAMA (RAW VERSION)
Dokumentasi proses, capstone lihat (main.py)
assignment_script.py sebagai baseline awal
'''


from tabulate import tabulate

welcome = '\nSelamat Datang di Pasar Buah'

# Tabel Produk
myProduct = [
    ['apel', 40, 10000],
    ['jeruk', 30, 15000],
    ['anggur', 20, 20000]
]   

# Column List PRODUCT
headers = ['Index', 'Nama', 'Stok', 'Harga']

print(welcome) # Welcome di luar while loop supaya muncul hanya 1x (Pertama kali program dijalankan)

while True:
    print('''
[1] Menampilkan daftar buah
[2] Menambah buah
[3] Menghapus buah
[4] Membeli buah
[0] Exit Program
''')
    
    PRODUCT = [] # Kalau diluar while, nanti tabelnya tumpang-tindih
    
    user_menu_option = input('Silahkan pilih menu: ')
    
    if user_menu_option == '0':
        # [0] Exit Program
        closing_msg = [['PROGRAM SELESAI, TERIMAKASIH']]
        print()
        print(tabulate(closing_msg, tablefmt='grid', stralign='center'))
        break
    elif user_menu_option == '1': # [1] Menampilkan Daftar Buah
        for idx, item in enumerate(myProduct, start=1): # Enumerate untuk membuat index di List final
            PRODUCT.append([idx] + item)
            
        print('\nDaftar Buah:\n')
        print(tabulate(PRODUCT, headers, tablefmt="grid", rowalign='right'))
        continue
    
    elif user_menu_option == '2': # [2] Menambah Buah
        add_product = input('\nMasukkan Nama Buah\t: ').lower() # Biar hasilnya rapih pas pake .title()
        add_stock = input('Masukkan Stock Buah\t: ')
        add_price = input('Masukkan Harga Buah\t: ')
        
        # Looping sampai user kasih input yang valid
        if not add_price.isdigit() or not add_stock.isdigit():
            print('\nInput tidak dikenali, silahkan coba lagi.')
            continue
        else:
            # Membuat list baru
            new_product = [add_product, add_stock, add_price]
            myProduct.append(new_product) # Append ke list awal
            
            for idx, item in enumerate(myProduct, start=1):
                PRODUCT.append([idx] + item) # Append ke list final
                
            # Tampilkan Hasil Update Data Daftar Buah
            print('\nDaftar Buah:\n')
            print(tabulate(PRODUCT, headers, tablefmt="grid", rowalign='right'))
            # continue
        print() 
        
    elif user_menu_option == '3': # [3] Menghapus Buah
        del_product = input('\nMasukkan index buah yang ingin dihapus: ')
        
        # Loop user sampai kasih input yang valid
        if not del_product.isdigit():
            print('\nInvalid Input, silahkan coba lagi.')
            continue
        
        idx_del = int(del_product)    
        # Jika index yang di-input > jumlah data PRODUCT atau kurang dari 1
        if idx_del > len(myProduct) or idx_del < 1:
            print('\nIndex tidak dikenali, silahkan coba lagi.')
            # continue
        # Hapus anak list dari list final PRODUCT berdasarkan index (dikurangi 1 karena list 0-indexed)
        else:
            del myProduct[idx_del - 1]
            # Tampilkan Hasil Data Buah Setelah Delete
            for idx, item in enumerate(myProduct, start=1):
                PRODUCT.append([idx] + item)
                
            print('\nDaftar Buah:\n')
            print(tabulate(PRODUCT, headers, tablefmt="grid", rowalign='right'))
            # continue
        print()
        
    elif user_menu_option == '4': # Membeli Buah
    # Column List Cart untuk Tabulate Baru 
        cart = []        
        cart_header = ['Nama', 'Qty', 'Harga']
        
# !!! SAYA MOHON MAAF KARENA GATAU LAGI MAU MAKE CARA APA KECUALI MAKE WHILE LOOP DI DALAM WHILE LOOP !!! #
        while True: # Kondisi awal User melakukan transaksi        
            idx_user = input('\nMasukkan index buah yang ingin dibeli: ')
            qty = input('\nMasukkan jumlah: ')
            
            idx = int(idx_user) - 1 # Penyesuaian indexing
            qty = int(qty)
            
            # Ambil buah berdasarkan index dari list awal -> myProduct
            buah = myProduct[idx][0]
            stock = int(myProduct[idx][1])
            price = int(myProduct[idx][2])
            
            total = price * qty # Mencari harga total dari setiap buah
            
            if idx < 0 or idx >= len(myProduct): # Validasi buah diluar index
                print('\nIndex tidak tersedia.')
                continue
            
            if qty < stock: # Kondisi transaksi dengan Cart
                # print(f'Anda membeli {qty} {buah} seharga Rp {total}')
                myProduct[idx][1] = stock - qty  # update stok

                print('\nCart:')
                cart.append([buah, qty, price])
                print(tabulate(cart, cart_header, tablefmt="grid", rowalign='right'))
                buy_more = input('Mau beli yang lain (Ya/Tidak): ')
                if buy_more.lower() == 'tidak':
                    # hitung Total Harga
                    total_price = sum(item[1] * item[2] for item in cart)
                    # Tambah Column 'Total Harga'
                    cart_header_with_total = cart_header + ['Total Harga']
                    
                    cart_with_total = []
                    for item in cart:
                        total_per_item = item[1] * item[2]
                        cart_with_total.append(item + [total_per_item])

                    print('\nShopping Cart:')
                    print(tabulate(cart_with_total, cart_header_with_total, tablefmt="grid", rowalign='right'))
                    print(f'Total belanja: Rp {total_price}')         
                    # break
                    # Looping Statements saat transaksi berlangsung
                    transaksi = True
                    
# !!! SAYA MOHON MAAF KARENA GATAU LAGI MAU MAKE CARA APA KECUALI MAKE WHILE LOOP DI DALAM WHILE LOOP !!! #
                    while transaksi:    
                        # 10
                        # Minta uang dari user dan hitung uang dengan total harga belanja
                        uang = int(input('\nMasukkan jumlah uang: '))
                        
# !!! SAYA MOHON MAAF KARENA GATAU LAGI MAU MAKE CARA APA KECUALI MAKE WHILE LOOP DI DALAM WHILE LOOP !!! #                        
                        while uang < total_price:
                            # Skenario Transaksi GAGAL sampai kondisi uang > total_price tercapai
                            print('\nTransaksi GAGAL')
                            print(f'Pembayaran diterima: Rp {uang}')
                            print(f'Kekurangan pembayaran sebesar: Rp {total_price - uang}\n')
                            
                            uang_tambahan = int(input('Masukkan Dana Tambahan: '))
                            uang += uang_tambahan # Selalu update jumlah uang di dalam loop
                        
                            if uang > total_price: # Keluar dari while loop uang < total_price
                                break
                            else:
                                continue # Transaksi GAGAL sampai kondisi uang > total_price tercapai
                        
                        if uang > total_price: # Jika uang > total_price, kasih kembalian
                            kembalian = uang - total_price
                            print('\nTransaksi Selesai!')
                            print(f'Uang kembali (Rp {kembalian})')
                            print('Terima kasih\n')
                            transaksi = False # Keluar dari while loop transaksi
                            
                        elif uang == total_price:
                            print('\nTransaksi Selesai!')
                            print('Terima kasih\n')
                            transaksi = False
                        break
                    break

                else:
                    continue
              
            else:
                print(f'Maaf stok tidak cukup. Stok {buah} tinggal {stock}.')
                continue        
    else:
        print('\nPilihan tidak tersedia, silahkan coba lagi.')
        continue
    