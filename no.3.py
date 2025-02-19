## CODE UNTUK NO.3

from collections import deque

antrian = deque()
nim_set = set() 

def tambah_antrian():
    nomor_antrian = len(antrian) + 1
    NIM = input("Masukkan NIM Mahasiswa UNTARA : ")
    Nama_Mahasiswa = input("Masukkan Nama Mahasiswa UNTARA : ")
    
    if not NIM.isdigit():
        print("NIM harus berupa angka. Masukkan NIM yang valid.")
        return
    
    NIM = int(NIM)

    if NIM in nim_set:
        print("NIM sudah ada dalam antrian. Tambahkan NIM yang berbeda.")
        return

    Mahasiswa = {
        "Nomor Antrian": nomor_antrian,
        "NIM": NIM,
        "Nama Mahasiswa": Nama_Mahasiswa,
    }
    antrian.append(Mahasiswa)
    nim_set.add(NIM)
    print(f"Nomor antrian {nomor_antrian} telah ditambahkan.")

def panggil_antrian():
    if len(antrian) > 0:
        Mahasiswa = antrian.popleft()
        nim_set.remove(Mahasiswa['NIM'])
        print("Antrian dipanggil:")
        print(f"Nomor Antrian: {Mahasiswa['Nomor Antrian']}")
        print(f"NIM Mahasiswa: {Mahasiswa['NIM']}")
        print(f"Nama Mahasiswa: {Mahasiswa['Nama Mahasiswa']}")
    else:
        print("Tidak ada antrian saat ini.")

def tampil_antrian():
    if len(antrian) > 0:
        print("Daftar antrian:")
        for Mahasiswa in antrian:
            print(f"Nomor Antrian: {Mahasiswa['Nomor Antrian']}")
            print(f"NIM Mahasiswa: {Mahasiswa['NIM']}")
            print(f"Nama Mahasiswa: {Mahasiswa['Nama Mahasiswa']}")
            print("---")
    else:
        print("Tidak ada antrian saat ini.")

while True:
    print("========Antrian Mahasiswa Untara ========")
    print("1. Tambah Antrian")
    print("2. Panggil Antrian")
    print("3. Tampil Antrian")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-3): ")

    if pilihan == '1':
        tambah_antrian()
    elif pilihan == '2':
        panggil_antrian()
    elif pilihan == '3':
        tampil_antrian()
    elif pilihan == '0':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu (0-3).")
