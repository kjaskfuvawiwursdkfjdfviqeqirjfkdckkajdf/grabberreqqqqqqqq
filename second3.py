import requests
from bs4 import BeautifulSoup
import time

# Fungsi untuk mengambil dan parsing data dari halaman web
def fetch_domains(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    domains = set()  # Menggunakan set untuk menyimpan domain unik
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('https://www.hupso.com/www/'):
            domain = href.split('/')[-1]
            domains.add(domain)
    return domains

def main():
    url = 'https://www.hupso.com/'  # URL yang ingin diambil datanya
    
    # Input file untuk menyimpan hasil
    save_path = input("[+] Save your domains result to (file path): ")
    if not save_path:
        save_path = 'domains.txt'  # Default file name if no input

    print(f"Saving results to {save_path}")

    seen_domains = set()  # Menggunakan set untuk menyimpan domain yang sudah diproses

    # Main loop untuk mengambil data dan menyimpannya
    while True:
        try:
            domains = fetch_domains(url)
            new_domains = domains - seen_domains  # Temukan domain baru
            seen_domains.update(new_domains)  # Tambahkan domain baru ke set
            
            with open(save_path, 'a') as file:
                for domain in new_domains:
                    print(domain)  # Print the domain in the terminal
                    file.write(domain + '\n')  # Save the domain to file
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(0.5)  # Delay for 0.5 seconds

if __name__ == "__main__":
    main()

