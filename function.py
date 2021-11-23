# program manajemen kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("====================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

def tambah_kontak():
    nama = input("Nama :")
    email = input("email :")
    telepon = input("telepon :")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon_dicari = input("No telepon yang akan dihapus : ")

    index = -1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon_dicari == daftar_kontak["telepon"]:
            index = i
            break

    if index == -1:
        print("Data Kontak tidak ditemukan")
    else:
        del daftar_kontak[index]
        print("Data ditemukan")

def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("Nama yang dicari : ")

    for kontak in daftar_kontak:
        nama = kontak ["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("====================")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")
