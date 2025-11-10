# Aplikasi kontak sederhana

contacts = []

def add_contact():
    nama = input("Nama: ")
    noTelp = input("Nomor telp: ")
    email = input("Email (opsional): ")
    contact = {'Nama': nama, 'Telp': noTelp, 'Email': email}
    contacts.append(contact)
    print("Kontak baru telah ditambahkan!\n")

def list_contacts():
    if not contacts:
        print("Kontak tidak tersedia!\n")
        return
    print("List kontak:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Nama: {contact['nama']}, Telp: {contact['noTelp']}, Email: {contact['email']}")
    print()

def search_contact():
    query = input("Search nama: ").lower()
    found = [c for c in contacts if query in c['nama'].lower()]
    if not found:
        print("Kontak tidak ditemukan.\n")
        return
    print("Hasil search: ")
    for contact in found:
        print(f"Nama: {contact['nama']}, Telp: {contact['noTelp']}, Email: {contact['email']}")
    print()

def delete_contact():
    if not contacts:
        print("Tidak ada kontak (untuk dihapus).\n")
        return
    list_contacts()
    try:
        index = int(input("Nomor yang ingin dihapus: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            print(f"Kontak '{deleted['nama']}' berhasil dihapus!\n")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus berupa angka.\n")

def main():
    while True:
        print("Menu Aplikasi Kontak:")
        print("1. Tambah Kontak")
        print("2. List Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    main()