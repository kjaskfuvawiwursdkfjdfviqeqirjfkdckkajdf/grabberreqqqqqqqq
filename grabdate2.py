import requests
from bs4 import BeautifulSoup

def grab_domains_from_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}: HTTP {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', rel='nofollow', target='_blank', class_='text-decoration-none text-dark link text-center')

    return [link.get_text(strip=True) for link in links]

def append_to_file(domains, filename):
    with open(filename, 'a') as file:
        for domain in domains:
            file.write(domain + '\n')

def grab_domains(tahun, bulan, tanggal, filename):
    page_number = 1
    
    while True:
        url = f"https://www.xploredomains.com/{tahun}-{bulan}-{tanggal}?page={page_number}"
        print(f"Fetching page {page_number}...")
        
        domains = grab_domains_from_page(url)
        
        if not domains:
            print("No more pages found.")
            break

        append_to_file(domains, filename)
        print(f"Page {page_number} data saved to {filename}.")
        page_number += 1

if __name__ == "__main__":
    print_banner()
    
    tahun = input("Masukkan tahun: ")
    bulan = input("Masukkan bulan: ")
    tanggal = input("Masukkan tanggal: ")
    filename = input("Masukkan nama file untuk menyimpan hasil (misalnya: hasil.txt): ")

    grab_domains(tahun, bulan, tanggal, filename)
    print(f"Data successfully saved to {filename}.")
