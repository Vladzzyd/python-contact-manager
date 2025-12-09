# WARNA
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

daftar_kontak = {"ikan":"081111111111","ayam":"082222222222","sapi":"083333333333","babi":"084444444444"}
daftar_fungsi = ("lihat","tambah","hapus","edit","quit")

def header(judul):
    print(CYAN + "="*35 + RESET)
    print(CYAN + judul.center(35) + RESET)
    print(CYAN + "="*35 + RESET)

def tampilkan():
    print("DAFTAR KONTAK")

    if not daftar_kontak:
        print(YELLOW+"daftar kontak masih kosong"+RESET)
        return
    
    for nama, nomor in daftar_kontak.items():
        print(GREEN+f"{nama} - {nomor}"+RESET)

def tambah():
    header("MENAMBAH KONTAK")

    while True:
        nama = input(CYAN+"masukkan nama kontak: "+RESET).lower().strip()
        if not nama:
            print(RED+"ERROR: nama tidak boleh kosong!!"+RESET)
        
        elif nama in daftar_kontak:
            print(YELLOW+"nama tersebut sudah ada!!"+RESET)

        else:
            break
    
    while True:
        nomor = input(CYAN+f"masukkan nomor telepon {nama}: "+RESET).strip()
        if not nomor:
            print(RED+"ERROR: nomor tidak boleh kosong"+RESET)

        elif len(nomor) < 10:
            print(RESET+"ERROR: nomor telepon tidak boleh kurang dari 10 digit"+RESET)

        elif nomor.isdigit():
            if nomor in daftar_kontak.values():
                pemilik_nomor = [k for k, v in daftar_kontak.items() if v == nomor]
                return YELLOW+f"nomor tersebut sudah ada di kontak dengan nama {pemilik_nomor}"+RESET
            
            else:
                break

        else:
            print(RED+"ERROR: nomor harus berupa angka!!"+RESET)

    while True:
        konfirmasi = input(CYAN+f"apakah anda ingin menambahkan kontak {nama} (y/n): "+RESET).lower().strip()
        if konfirmasi in ("y","n"):
            if konfirmasi == "y":
                break

            else:
                return YELLOW+f"nomor kontak {nama} tidak jadi ditambahkan!!"+RESET

        else:
            print(YELLOW+"masukkan ya (y) atau tidak (n)!!"+RESET)
    
    daftar_kontak[nama] = nomor
    return GREEN+f"nomor kontak {nama} berhasil ditambahkan!!"+RESET


def hapus():
    header("MENGHAPUS KONTAK")

    if not daftar_kontak:
        print(YELLOW+"daftar kontak masih kosong!!"+RESET)

    tampilkan()
    
    while True:
        nama = input(CYAN+"masukkan nama kontak yang mau dihapus (q to quit): "+RESET).lower().strip()
        if nama == "q":
            return
        if not nama:
            print(RED+"ERROR: nama tidak boleh kosong!!"+RESET)
            continue
        if nama in daftar_kontak:
            konfirmasi = input(CYAN+f"apakah anda yakin ingin menghapus {nama}? (y/n): "+RESET).lower().strip()
            if konfirmasi == "y":
                del daftar_kontak[nama]
                print(GREEN+f"berhasil menghapus {nama} dari kontak!!"+RESET)
            
            else:
                print(YELLOW+"penghapusan dibatalkan!!"+RESET)
                break
        
        else:
            print(RED+"ERROR: nama tidak ditemukan didalam kontak!!"+RESET)

def edit():
    header("MENGEDIT KONTAK")

    if not daftar_kontak:
        print(YELLOW+"daftar kontak masih kosong!!"+RESET)

    tampilkan()

    while True:
        nama = input(CYAN+"masukkan nama kontak yang mau diedit (q to quit): "+RESET).lower().strip()
        if nama == "q":
            print(YELLOW+"pengeditan dibatalkan!!"+RESET)
            return
        
        if not nama:
            print(RED+"ERROR: nama tidak boleh kosong!!"+RESET)
            continue

        if nama in daftar_kontak:
            while True:
                nomor = input(CYAN+f"masukkan nomor baru untuk {nama}: "+RESET).strip()
                if not nomor:
                    print(RED+"ERROR: nomor tidak boleh kosong"+RESET)
                    continue

                elif len(nomor) < 10 or not nomor.isdigit():
                    print(RED+"ERROR: nomor tidak boleh kurang dari 10 dan harus angka!!"+RESET)

                elif nomor in daftar_kontak.values():
                    pemilik = next((k for k, v in daftar_kontak.items() if v == nomor), None)
                    print(RED+f"ERROR: nomor sudah digunakan oleh {pemilik}!!"+RESET)
                    continue

                else:
                    daftar_kontak[nama] = nomor
                    print(GREEN+f"kontak {nama} berhasil diupdate!!"+RESET)
                    break

            break

        else:
            print(RED+"ERROR: nama tidak ditemukan di daftar kontak!!"+RESET)

while True:
    header("PROGRAM DAFTAR KONTAK")
    for i,item in enumerate(daftar_fungsi, start=1):
        print(f"{i}. {item}")
    
    while True:
        fungsi = input(CYAN+"masukkan fungsi yang ingin digunakan: "+RESET).lower().strip()
        if fungsi in daftar_fungsi:
            break
        else:
            print(RED+"ERROR: fungsi tidak valid!!"+RESET)

    if fungsi == "lihat":
        tampilkan()

    elif fungsi == "tambah":
        hasil = tambah()
        print(hasil)

    elif fungsi == "hapus":
        hapus()

    elif fungsi == "edit":
        edit()
    
    elif fungsi == "quit":
        print(GREEN+"terimakasih sudah menggunakan program ini!!"+RESET)
        break