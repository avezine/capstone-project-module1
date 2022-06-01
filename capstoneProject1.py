# ALDILA AVEZINE JCDSVL
# CAPSTONE PROJECT MODULE 1
# DATA PASIEN RUMAH SAKIT

import string

dataPasien = [
    {
        'nomor pasien':1,
        'nama depan':'Alex',
        'nama belakang':'Graham',
        'umur':32,
        'jenis kelamin':'Pria'
    },
    {
        'nomor pasien':2,
        'nama depan':'Nur',
        'nama belakang':'Aliyanto',
        'umur':43,
        'jenis kelamin':'Pria'
    },
    {
        'nomor pasien':3,
        'nama depan':'Novi',
        'nama belakang':'Sulistya',
        'umur':25,
        'jenis kelamin':'Wanita'
    },
    {
        'nomor pasien':4,
        'nama depan':'Fitri',
        'nama belakang':'Sukmaning',
        'umur':36,
        'jenis kelamin':'Wanita'
    }
]

def pilihanMenuBaca():
    while True:
        menuBaca = input('''
        DATA PASIEN RUMAH SAKIT

        1.  Menampilkan Seluruh Data Pasien
        2.  Mencari Data Menggunakan Nomor Pasien
        3.  Mencari Data Menggunakan Nama Depan
        4.  Kembali ke Menu Utama

        Masukkan angka Menu yang ingin dijalankan : ''')
    
        if(menuBaca == '1'):
            menuBaca1()
        
        elif(menuBaca == '2'):
            menuBaca2()

        elif(menuBaca == '3'):
            menuBaca3()

        elif(menuBaca == '4'):
            menuUtama()
            break
    return
        


def menuBaca1():    
    print('\nData Pasien Rumah Sakit\n')
    print('No Pasien\t| Nama Depan\t| Nama Belakang\t| Umur\t| Jenis Kelamin')
    for i in range(len(dataPasien)):
            print('{}\t\t| {}\t\t| {}\t| {}\t| {}\n'.format(dataPasien[i]['nomor pasien'],dataPasien[i]['nama depan'],dataPasien[i]['nama belakang'],dataPasien[i]['umur'],dataPasien[i]['jenis kelamin']))

def menuBaca2():
    cariPasien = int(input('Masukkan Nomor Pasien: '))
    for i in range(len(dataPasien)):
        if cariPasien == dataPasien[i]['nomor pasien']:
            print('\nData Pasien Rumah Sakit\n')
            print('No Pasien\t| Nama Depan\t| Nama Belakang\t| Umur\t| Jenis Kelamin')
            print('{}\t\t|{}\t\t| {}\t| {}\t| {}\n'.format(dataPasien[i]['nomor pasien'],dataPasien[i]['nama depan'],dataPasien[i]['nama belakang'],dataPasien[i]['umur'],dataPasien[i]['jenis kelamin']))
            break
    else:
        print('\nData Pasien Tidak Ditemukan')

def menuBaca3():
    cariPasien = str.capitalize(input('Masukkan Nama Depan Pasien: '))
    for i in range(len(dataPasien)):
        if cariPasien == dataPasien[i]['nama depan']:
            print('\nData Pasien Rumah Sakit\n')
            print('No Pasien\t| Nama Depan\t| Nama Belakang\t| Umur\t| Jenis Kelamin')
            print('{}\t\t| {}\t\t| {}\t| {}\t| {}\n'.format(dataPasien[i]['nomor pasien'],dataPasien[i]['nama depan'],dataPasien[i]['nama belakang'],dataPasien[i]['umur'],dataPasien[i]['jenis kelamin']))
            break
    else:
        print('\nData Pasien Tidak Ditemukan')


def pilihanMenuTambah():
    while True:
        nomorPasien = int(input('Masukkan Nomor Pasien: '))
        for i in range(len(dataPasien)):
            if nomorPasien == dataPasien[i]['nomor pasien']:
                print('Nomor Pasien Sudah Digunakan')
                break
        
        else:
            namaDepan = str.capitalize(input('Masukkan Nama Depan: '))
            namaBelakang = str.capitalize(input('Masukkan Nama Belakang: '))
            umur = int(input('Masukkan Umur: '))
            jenisKelamin = str.capitalize(input('Masukkan Jenis Kelamin (Pria/Wanita): '))
            checker = str(input('Apakah Anda ingin menyimpan data ini? (ya/tidak)'))
            if checker == 'ya':
                dataPasien.append({
                'nomor pasien': nomorPasien,
                'nama depan': namaDepan,
                'nama belakang': namaBelakang,
                'umur' : umur,
                'jenis kelamin': jenisKelamin
                })
                print('\nData Berhasil Ditambahkan')
                menuBaca1()
                break
            else:
                print('\nData Tidak Ditambahkan')
                menuBaca1()
                break
    return


def pilihanMenuUbah():
    menuBaca1()
    while True:
        nomorPasien = int(input('Masukkan Nomor Pasien yang Ingin Diubah: '))
        if nomorPasien not in range(len(dataPasien)+1):
                print('Data Pasien Tidak Ditemukan')
                continue
        else:
            for i in range(len(dataPasien)):
                if nomorPasien == dataPasien[i]['nomor pasien']:
                    subMenuUbah = input('''
                    MENGUBAH DATA PASIEN

                    Ubah Data Pasien :
                    1.  Nama Depan
                    2.  Nama Belakang
                    3.  Umur  
                    4.  Jenis Kelamin
                    5.  Kembali ke Menu Utama

                    Masukkan angka kolom data yang ingin diubah : ''')
    
                    if(subMenuUbah == '1'):
                        namaDepan = str.capitalize(input('Masukkan Nama Depan: '))
                        checker = str(input('Apakah Anda ingin menyimpan data ini? (ya/tidak)'))
                        if checker == 'ya':
                            dataPasien[i]['nama depan'] = namaDepan
                            print('\nData Berhasil Diubah')
                            menuBaca1()
                            continue
                        else:
                            print('\nData tidak diubah')
                            menuBaca1()
                            break
                
                    elif(subMenuUbah == '2'):
                        namaBelakang = str.capitalize(input('Masukkan Nama Belakang: '))
                        checker = str(input('Apakah Anda ingin menyimpan data ini? (ya/tidak)'))
                        if checker == 'ya':
                            dataPasien[i]['nama belakang'] = namaBelakang
                            print('\nData Berhasil Diubah')
                            menuBaca1()
                            continue
                        else:
                            print('\nData tidak diubah')
                            menuBaca1()
                            break

                    elif(subMenuUbah == '3'):
                        umur = int(input('Masukkan Umur: '))
                        checker = str(input('Apakah Anda ingin menyimpan data ini? (ya/tidak)'))
                        if checker == 'ya':
                            dataPasien[i]['umur'] = umur
                            print('\nData Berhasil Diubah')
                            menuBaca1()
                            continue
                        else:
                            print('\nData tidak diubah')
                            menuBaca1()
                            break

                    elif(subMenuUbah == '4'):
                        jenisKelamin = str.capitalize(input('Masukkan Jenis Kelamin: '))
                        checker = str(input('Apakah Anda ingin menyimpan data ini? (ya/tidak)'))
                        if checker == 'ya':
                            dataPasien[i]['jenis kelamin'] = jenisKelamin
                            print('\nData Berhasil Diubah')
                            menuBaca1()
                            continue
                        else:
                            print('\nData tidak diubah')
                            menuBaca1()
                            break

                    elif(subMenuUbah == '5'):
                        menuUtama()

        checker = str(input('Apakah Anda ingin mengubah data lainnya? (ya/tidak)'))
        if checker == 'ya':
            continue
        else:
            break
    return

def pilihanMenuHapus():
    menuBaca1()
    while True:
        nomorPasien = int(input('Masukkan Nomor Pasien yang Ingin Dihapus: '))
        for i in range(len(dataPasien)):
            if int(nomorPasien) == dataPasien[i]['nomor pasien']:
                print('\nData Pasien Rumah Sakit\n')
                print('No Pasien\t| Nama Depan\t| Nama Belakang\t| Umur\t| Jenis Kelamin')
                print('{}\t\t|{}\t\t| {}\t| {}\t| {}\n'.format(dataPasien[i]['nomor pasien'],dataPasien[i]['nama depan'],dataPasien[i]['nama belakang'],dataPasien[i]['umur'],dataPasien[i]['jenis kelamin']))
                checker = str(input('Apakah Anda ingin menghapus data ini? (ya/tidak)'))
                if checker == 'ya':
                    del dataPasien[i]
                    print('\nData Berhasil Dihapus')
                    menuBaca1()
                    return
                else:
                    return
        else:
            print('\nData Pasien Tidak Ditemukan')
        return



def menuUtama():
    while True:
        pilihanMenu = input('''
        RUMAH SAKIT SUMBER WARAS

        List Menu :
        1.  Daftar Data Pasien
        2.  Menambah Data Pasien
        3.  Mengubah Data Pasien  
        4.  Menghapus Data Pasien
        5.  Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')
    
        if(pilihanMenu == '1'):
            pilihanMenuBaca()

        elif(pilihanMenu == '2'):
            pilihanMenuTambah()

        elif(pilihanMenu == '3'):
            pilihanMenuUbah()

        elif(pilihanMenu == '4'):
            pilihanMenuHapus()

        elif(pilihanMenu == '5'):
            print('\nTerima Kasih, Sampai Jumpa!\n')
            quit()
    
menuUtama()


