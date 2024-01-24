import tkinter as tk
from tkinter import messagebox

class JasaOrderMakananApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jasa Order Makanan")

        # Variabel StringVar untuk menyimpan pilihan menu
        self.menu_var = tk.StringVar()

        # Membuat label untuk judul
        judul_label = tk.Label(root, text="Selamat Datang di Jasa Order Makanan")
        judul_label.pack(pady=10)

        # Membuat label dan pilihan menu untuk makanan
        menu_label = tk.Label(root, text="Pilih Menu:")
        menu_label.pack(pady=5)

        # Opsi menu
        menu_options = ["Nasi Goreng", "Mie Goreng", "Ayam Goreng", "Soto Ayam"]

        # Membuat menu dropdown
        menu_dropdown = tk.OptionMenu(root, self.menu_var, *menu_options)
        menu_dropdown.pack(pady=10)

        # Membuat tombol untuk memesan
        pesan_button = tk.Button(root, text="Pesan", command=self.pesan_makanan)
        pesan_button.pack(pady=20)

    def pesan_makanan(self):
        # Mendapatkan nilai dari pilihan menu
        menu_pilihan = self.menu_var.get()

        # Memeriksa apakah pengguna telah memilih menu
        if not menu_pilihan:
            messagebox.showwarning("Peringatan", "Silakan pilih menu terlebih dahulu.")
        else:
            # Menampilkan pesan pemesanan
            pesan = f"Terima kasih! Anda telah memesan {menu_pilihan}. Pesanan akan segera diproses."
            messagebox.showinfo("Pesan Terima Kasih", pesan)

            # Mereset nilai pilihan menu setelah pesanan selesai
            self.menu_var.set("")

def main():
    root = tk.Tk()
    app = JasaOrderMakananApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
