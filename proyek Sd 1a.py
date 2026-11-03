# ==================================================
# PROYEK 1A - STRUKTUR DATA
# SISTEM MANAJEMEN INVENTARIS PRODUK
# Struktur Data: HASH TABLE (PYTHON DICTIONARY)
# ==================================================


# ==================================================
# CLASS INVENTARIS PRODUK (ADT)
# ==================================================

class InventarisProduk:

    def __init__(self):
        # Dictionary digunakan sebagai Hash Table.
        # ID produk menjadi key dan informasi produk menjadi value.
        self.data_produk = {}

    # ------------------------------------------------
    # METHOD 1: MENAMBAHKAN PRODUK (INSERTION)
    # ------------------------------------------------

    def tambah_produk(self, id_produk, nama_produk,
                      kategori, harga, stok):

        # Memeriksa apakah ID produk sudah digunakan.
        if id_produk in self.data_produk:
            print("\nGagal! ID produk sudah terdaftar.")
            return False

        # Membuat data produk.
        produk = {
            "id_produk": id_produk,
            "nama_produk": nama_produk,
            "kategori": kategori,
            "harga": harga,
            "stok": stok
        }

        # Menyimpan produk ke dalam Hash Table.
        self.data_produk[id_produk] = produk

        print("\nProduk berhasil ditambahkan.")
        return True

    # ------------------------------------------------
    # METHOD 2: MENCARI PRODUK (SEARCHING)
    # ------------------------------------------------

    def cari_produk(self, id_produk):

        # Mencari produk berdasarkan key ID.
        produk = self.data_produk.get(id_produk)

        if produk is not None:
            print("\n===== PRODUK DITEMUKAN =====")
            print("ID Produk  :", produk["id_produk"])
            print("Nama Produk:", produk["nama_produk"])
            print("Kategori   :", produk["kategori"])
            print("Harga      : Rp", produk["harga"])
            print("Stok       :", produk["stok"])

            return produk

        else:
            print("\nProduk dengan ID tersebut tidak ditemukan.")
            return None

    # ------------------------------------------------
    # METHOD 3: MENGHAPUS PRODUK (DELETION)
    # ------------------------------------------------

    def hapus_produk(self, id_produk):

        # Memeriksa apakah ID produk tersedia.
        if id_produk in self.data_produk:

            # Menghapus produk dari Hash Table.
            del self.data_produk[id_produk]

            print("\nProduk berhasil dihapus.")
            return True

        else:
            print("\nGagal! Produk tidak ditemukan.")
            return False

    # ------------------------------------------------
    # METHOD TAMBAHAN: MENAMPILKAN SEMUA PRODUK
    # ------------------------------------------------

    def tampilkan_produk(self):

        if len(self.data_produk) == 0:
            print("\nInventaris produk masih kosong.")
            return

        print("\n========== DAFTAR INVENTARIS PRODUK ==========")

        for produk in self.data_produk.values():

            print("----------------------------------------------")
            print("ID Produk  :", produk["id_produk"])
            print("Nama Produk:", produk["nama_produk"])
            print("Kategori   :", produk["kategori"])
            print("Harga      : Rp", produk["harga"])
            print("Stok       :", produk["stok"])

        print("----------------------------------------------")
        print("Jumlah produk:", len(self.data_produk))


# ==================================================
# FUNGSI MENU UTAMA (COMMAND LINE INTERFACE)
# ==================================================

def menu_utama():

    # Membuat objek dari class InventarisProduk.
    inventaris = InventarisProduk()

    while True:
        print("\n==========================================")
        print("       SISTEM MANAJEMEN INVENTARIS")
        print("==========================================")
        print("1. Tambah Produk")
        print("2. Cari Produk")
        print("3. Hapus Produk")
        print("4. Tampilkan Semua Produk")
        print("5. Keluar")
        print("==========================================")

        pilihan = input("Pilih menu (1-5): ")

        # ------------------------------------------
        # MENU 1: TAMBAH PRODUK
        # ------------------------------------------

        if pilihan == "1":

            print("\n========== TAMBAH PRODUK ==========")

            id_produk = input("Masukkan ID Produk  : ").strip()
            nama_produk = input("Masukkan Nama Produk: ").strip()
            kategori = input("Masukkan Kategori   : ").strip()

            if not id_produk or not nama_produk or not kategori:
                print("\nSemua data harus diisi.")
                continue

            try:
                harga = float(input("Masukkan Harga      : "))
                stok = int(input("Masukkan Stok       : "))

                if harga < 0 or stok < 0:
                    print("\nHarga dan stok tidak boleh negatif.")
                    continue

            except ValueError:
                print("\nHarga harus berupa angka dan stok harus berupa bilangan bulat.")
                continue

            inventaris.tambah_produk(
                id_produk,
                nama_produk,
                kategori,
                harga,
                stok
            )

        # ------------------------------------------
        # MENU 2: CARI PRODUK
        # ------------------------------------------

        elif pilihan == "2":

            print("\n========== CARI PRODUK ==========")

            id_produk = input("Masukkan ID Produk: ").strip()

            if not id_produk:
                print("\nID produk tidak boleh kosong.")
                continue

            inventaris.cari_produk(id_produk)

        # ------------------------------------------
        # MENU 3: HAPUS PRODUK
        # ------------------------------------------

        elif pilihan == "3":

            print("\n========== HAPUS PRODUK ==========")

            id_produk = input("Masukkan ID Produk: ").strip()

            if not id_produk:
                print("\nID produk tidak boleh kosong.")
                continue

            inventaris.hapus_produk(id_produk)

        # ------------------------------------------
        # MENU 4: TAMPILKAN SEMUA PRODUK
        # ------------------------------------------

        elif pilihan == "4":

            inventaris.tampilkan_produk()

        # ------------------------------------------
        # MENU 5: KELUAR
        # ------------------------------------------

        elif pilihan == "5":

            print("\nTerima kasih telah menggunakan program.")
            print("Program selesai.")
            break

        # ------------------------------------------
        # PILIHAN MENU TIDAK VALID
        # ------------------------------------------

        else:

            print("\nPilihan tidak valid. Silakan pilih menu 1-5.")


# ==================================================
# MENJALANKAN PROGRAM
# ==================================================

if __name__ == "__main__":
    menu_utama()