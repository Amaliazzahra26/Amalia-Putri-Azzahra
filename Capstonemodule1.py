listSayur = [
    {
        'Nama Sayur' : 'Bayam',
        'Stok' : 10,
        'Harga' : 10000,
        'Jenis Sayur' : 'Organik',
        'Satuan' : 'Ikat',
    },
    {
        'Nama Sayur' : 'Sawi',
        'Stok' : 15,
        'Harga' : 10000,
        'Jenis Sayur' : 'Organik',
        'Satuan' : 'Ikat',
    },
    {
        'Nama Sayur' : 'Wortel',
        'Stok' : 5,
        'Harga' : 15000,
        'Jenis Sayur' : 'Organik',
        'Satuan' : 'Kg',
    },
    {
        'Nama Sayur' : 'Kol',
        'Stok' : 20,
        'Harga' : 8000,
        'Jenis Sayur' : 'Organik',
        'Satuan' : 'Kg',
    }
]

cart = []


def sayur() :
    if len(listSayur) == 0 :
        print('===Tidak ada data===')
    else :
        print('+++Daftar Sayur di Toko\n+++')
        print('index\t| Nama Sayur \t| Stock\t| Harga\t| Jenis Sayur\t| Satuan')
        for i in range(len(listSayur)) :
            print('{}\t| {} \t| {}\t| {}\t| {}\t| {}'. format(i,listSayur[i]['Nama Sayur'],listSayur[i]['Stok'],listSayur[i]['Harga'],listSayur[i]['Jenis Sayur'],listSayur[i]['Satuan']))

def add_sayur():
    while True:
        NamaSayur = input('Masukkan Nama Sayur : ') 
        for k in listSayur:
            if k['Nama Sayur'] == NamaSayur :
                print('===Data barang sudah ada===')
                return
        StockSayur = int(input('Masukkan Stock Sayur : '))
        HargaSayur = int(input('Masukkan Harga Sayur : '))
        JenisSayur = str(input('Masukkan Jenis Sayur : '))
        SatuanSayur = str(input('Masukkan Satuan Sayur : '))
        while True :
            a = input('Apakah data yang anda masukkan telah benar (Y/T) :')
            if (a == 'Y') :
                listSayur.append({
                    'Nama Sayur' : NamaSayur,
                    'Stok' : StockSayur,
                    'Harga' : HargaSayur,
                    'Jenis Sayur' : JenisSayur,
                    'Satuan' : SatuanSayur,
                })
                print('===Data tersimpan===')
                return
            elif (a == 'T'):
                break

def update_sayur():
    while True:
        NamaSayur = input('Masukkan Nama Sayur : ')
        PunyaSayur = False
        for i in listSayur:
            if i['Nama Sayur'] == NamaSayur :
                StockSayur = int(input('Masukkan Stock Sayur : '))
                while True:
                    a = input('Apakah data yang anda masukkan telah benar (Y/T) :')
                    if(a =='Y'):
                        for k in listSayur:
                            if k['Nama Sayur'] == NamaSayur :
                                k.update({'Stok' : StockSayur})
                                print('===Data terupdate===')
                                PunyaSayur = True
                                return
                    elif (a == 'T') :
                        break
            if PunyaSayur == False :
                print ('===Barang tidak ditemukkan===')
def delete_sayur():
    indexSayur = int(input('Masukkan index sayur yang ingin dihapus'))
    del listSayur[indexSayur]
    print('===Data terhapus===')

def show_menu():
    print('Toko Sayur Amalia')
    print(' ')
    print('List Menu:')
    print('1.Menampilkan Daftar Sayur')
    print('2.Menambahkan Sayur')
    print('3.Memperbarui Stock Sayur')
    print('4,Menghapus Sayur')
    print('5.Keluar dari Program')

def menu_1():
    while True :
        print('Data Sayur di Toko')
        print(' ')
        print('1.Tampilkan Seluruh Daftar Sayur')
        print('2.Tampilkan Data Sagur Tertentu')
        print('3.Kembali Ke Menu Utama')
        MenuSatu = input('Silahkan pilihsub menu (1-3) : ')
        if(MenuSatu == '1') :
            sayur()
        elif(MenuSatu == '2') :
            sayur_tertentu()
        elif(MenuSatu == '3') :
            break
        else :
            print('===Pilihan yang anda masukkan salah===')

def sayur_tertentu() :
    NamaSayur = input('Masukkan Nama Sayur : ')
    PunyaSayur = False
    for i in range(len(listSayur)):
        if listSayur[i]['Nama Sayur'] == NamaSayur :
            print(' Nama Sayur \t| Stok\t| Harga\t| Jenis Sayur\t| Satuan')
            print('{}\t| {} \t| {}\t| {}\t| {}\t| {}'. format(i,listSayur[i]['Nama Sayur'],listSayur[i]['Stok'],listSayur[i]['Harga'],listSayur[i]['Jenis Sayur'],listSayur[i]['Satuan']))
            PunyaSayur == True
            break
    else:
        print ('===Barang tidak ditemukan===')

def menu_2():
    while True :
        print('Tambah Data Sayur di Toko')
        print(' ')
        print('1.Tambah Data Sayur di Toko')
        print('2.Kembali ke Menu Utama')
        MenuDua = input('Silahkan pilih sub menu (1-2) : ')
        if(MenuDua == '1') :
            add_sayur()
            sayur()
        elif(MenuDua == '2') :
            break
            sayur_tertentu()
        else :
            print('===Pilihan yang anda masukkan salah===')

def menu_3():
    while True :
        print('Memperbarui Stok Sayur di Toko')
        print(' ')
        print('1.Memperbarui Stok Sayur di Toko')
        print('2.Kembali ke Menu Utama')
        MenuTiga = input('Silahkan pilih sub menu (1-2) : ')
        if(MenuTiga == '1') :
            update_sayur()
            sayur()
        elif(MenuTiga == '2') :
            break
        else :
            print('===Pilihan yang anda masukkan salah===')

def menu_4():
    while True :
        print('Menghapus Sayur di Toko')
        print(' ')
        print('1.Hapus Sayur di Toko')
        print('2.Kembali ke Menu Utama')
        MenuEmpat = input('Silahkan pilih sub menu (1-2) : ')
        if(MenuEmpat == '1') :
            delete_sayur()
            sayur()
        elif(MenuEmpat == '2') :
            break
        else :
            print('===Pilihan yang anda masukkan salah===')
def MenuUtama():
    while True :
        print('''
    Selamat Datang di Toko Sayur Amalia


    List Menu :
    1. Menampilkan Daftar Sayur
    2. Menambah Sayur
    3. Update Sayur
    4. Menghapus Sayur
    5. Exit Program

     ''')

        PilihanMenu = input ('Masukkan Angka Menu yang Ingin Dijalankan : ')
        if(PilihanMenu == '1') :
            menu_1()
        elif(PilihanMenu == '2') :
            menu_2()
        elif(PilihanMenu == '3') :
            menu_3()
        elif(PilihanMenu == '4') :
            menu_4()
        elif(PilihanMenu == '5') :
            break
        else :
            print('---Pilihan yang Anda Masukkan Salah---')

MenuUtama() 





        