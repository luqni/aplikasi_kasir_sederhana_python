#program luas dan keliling segitiga
print("Selamat Datang DI Aplikasi Kasir")
namabrng=(input("Masukkan Nama Barang (imbuhkan tanda ('nama') saat input nama) ="))
harga=int(input("Masukan Harga Barang = "))
jmlbeli=int(input("Masukan Jumlah Beli = "))
print("---------------------------------------------------------------------------")
total=harga*jmlbeli
print('Total Harga', namabrng, 'Adalah Rp.',total)
print("---------------------------------------------------------------------------")
cast=int(input("masukan pembayaran = "))
print("---------------------------------------------------------------------------")
hu=total-cast
kmbl=cast-total
if(cast>total):
	print("Jumlah Kembalian anda adalah Rp.", kmbl)

else:
	print("Anda memiliki Hutang sebesar Rp.", hu)









