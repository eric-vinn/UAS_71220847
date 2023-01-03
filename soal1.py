print("****** Kredit Keaktifan Mahasiswa ******")
print("(Student Activities Credit")
print("1. Menambahka Kegiatan")
print("2. Menampilkan Jumlah Poin")
print("3. Keluar")
print("---------------------")
pilihan = input("Silahkan masukan pilihan Anda: ")
nama = input("Nama Kegiatan: ")
tanggal = input("Tanggal Kegiatan: ")
print("Pilihan Kategori Kegiatan: ")
print("- Prestasi")
print("- Organisasi")
print("- Kepanitiaan")
print("- Rekognisi")
kegiatan = input("Masukkan Kategori kegiatan: ")

if kegiatan == ("Prestasi"):
    print("Kegiatan berhasi ditambahkan.")
elif kegiatan == ("PRESTASI"):
    print("Kegiatan berhasi ditambahkan.")
elif kegiatan == ("Organisasi"):
    print("Kegiatan berhasi ditambahkan.")
elif kegiatan == ("oRgAnIsAsI"):
    print("Kegiatan berhasi ditambahkan.")
elif kegiatan == ("Kepanitiaan"):
    print("Kegiatan berhasi ditambahkan.")
elif kegiatan == ("kepanitiaan"):
    print("Kegiatan berhasi ditambahkan.")
elif kegiatan == ("Rekognisi"):
    print("Kegiatan berhasi ditambahkan.")
else: 
    print("Kegiatan tidak tersedia")

print("1. ",pilihan, nama, tanggal, kegiatan)
