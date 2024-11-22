# Soal 5: Pembelian Diskon 
# Harga Barang
harga_minyak = 25000
harga_indomie = 5000
harga_beras = 75000
harga_gula = 25000
harga_kopi = 20000
harga_teh = 10000

# Input jumlah pembelian untuk setiap produk
jumlah_pembelian_minyak = int(input("Masukkan jumlah pembelian minyak: "))
jumlah_pembelian_indomie = int(input("Masukkan jumlah pembelian indomie: "))
jumlah_pembelian_beras = int(input("Masukkan jumlah pembelian beras: "))
jumlah_pembelian_gula = int(input("Masukkan jumlah pembelian gula: "))
jumlah_pembelian_kopi = int(input("Masukkan jumlah pembelian kopi: "))
jumlah_pembelian_teh = int(input("Masukkan jumlah pembelian teh: "))

# Hitung total harga
total_harga = (
    (harga_minyak * jumlah_pembelian_minyak) +
    (harga_indomie * jumlah_pembelian_indomie) +
    (harga_beras * jumlah_pembelian_beras) +
    (harga_gula * jumlah_pembelian_gula) +
    (harga_kopi * jumlah_pembelian_kopi) +
    (harga_teh * jumlah_pembelian_teh)
)

diskon = 0.1

# Cek apakah total pembelian lebih dari 100 item
total_item = (jumlah_pembelian_minyak + jumlah_pembelian_indomie +
              jumlah_pembelian_beras + jumlah_pembelian_gula +
              jumlah_pembelian_kopi + jumlah_pembelian_teh)

if total_item > 100:
    total_diskon = total_harga * diskon
else:
    total_diskon = 0

total_harga -= total_diskon

# Cetak hasil
if total_diskon > 0:
    print("Anda mendapatkan diskon sebesar 10% : Rp", total_diskon)
else:
    print("Tidak ada diskon yang diberikan.")

print("Total harga setelah diskon (jika ada) : Rp", total_harga)