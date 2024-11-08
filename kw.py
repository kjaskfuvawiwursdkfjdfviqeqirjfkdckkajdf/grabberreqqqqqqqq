import requests
from bs4 import BeautifulSoup

def fetch_domains(keyword):
    # URL dengan keyword yang dimasukkan
    url = f'https://iqwhois.com/search/{keyword}'
    
    # Mengirim permintaan HTTP GET ke URL
    response = requests.get(url)
    
    # Jika permintaan berhasil (status code 200)
    if response.status_code == 200:
        # Parse konten HTML menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mencari semua elemen yang mengandung domain yang diinginkan
        domains = soup.find_all('span', class_='conn-domain-name-class')
        
        # Mengambil dan menampilkan setiap domain
        domain_list = []
        for domain in domains:
            domain_list.append(domain.get_text().strip())
        
        return domain_list
    else:
        print(f"Error: Tidak bisa mengakses halaman untuk keyword '{keyword}'")
        return []

def read_keywords_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            keywords = [line.strip() for line in file.readlines() if line.strip()]
        return keywords
    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
        return []

def save_results_to_file(output_file, domains):
    with open(output_file, 'a', encoding='utf-8') as file:
        if domains:
            for domain in domains:
                file.write(f"{domain}\n")  # Menulis hanya domain tanpa tanda [+]
        else:
            file.write("Tidak ada domain ditemukan.\n")  # Jika tidak ada domain, simpan pesan ini
        file.write("\n")  # Tambahkan baris kosong antara keyword

def main():
    # Meminta input nama file yang berisi daftar keyword
    file_path = input("[+] input list keywordmu : ").strip()

    # Membaca daftar keyword dari file
    keywords = read_keywords_from_file(file_path)

    if not keywords:
        print("[+] Tidak ada keyword yang ditemukan atau file kosong.")
        return

    # Meminta nama file output untuk menyimpan hasil
    output_file = input("[+] save result : ").strip()

    # Iterasi untuk setiap keyword dan ambil data domain
    for keyword in keywords:
        print(f"\n-- parsing keyword '{keyword}'")
        
        # Mengambil daftar domain untuk keyword tersebut
        domains = fetch_domains(keyword)
        
        # Tampilkan hasilnya di layar
        if domains:
            for domain in domains:
                print(domain)  # Menampilkan domain tanpa tanda [+]
        else:
            print("Tidak ada domain ditemukan.")
        
        # Simpan hasil ke file output tanpa header atau informasi tambahan
        save_results_to_file(output_file, domains)

if __name__ == "__main__":
    main()
