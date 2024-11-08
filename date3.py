import requests
from bs4 import BeautifulSoup
import time

def fetch_domains(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    domains = set()
    for item in soup.find_all('div', class_='item'):
        a_tag = item.find('a', href=True)
        if a_tag:
            domain = a_tag['href']
            domains.add(domain)
    return domains

def main():
    tahun = input("[+] Tahun: ")
    bulan = input("[+] Bulan: ")
    tanggal = input("[+] Tanggal: ")
    part = 1  # Start part

    save_path = input("[+] Save your domains result to (file path): ")
    if not save_path:
        save_path = 'domains.txt'

    print(f"Saving results to {save_path}")

    seen_domains = set()

    while True:
        try:
            url = f'https://bitcoinmix.biz/domain/list.php?part={tahun}/{bulan}/{tanggal}/{part}'
            domains = fetch_domains(url)
            new_domains = domains - seen_domains
            seen_domains.update(new_domains)
            
            with open(save_path, 'a') as file:
                for domain in new_domains:
                    print(domain)
                    file.write(domain + '\n')

            # Increment part for the next iteration
            part += 1
            
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(0.5)

if __name__ == "__main__":
    main()

