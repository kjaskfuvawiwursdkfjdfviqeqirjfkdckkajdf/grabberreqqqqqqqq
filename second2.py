import requests
from bs4 import BeautifulSoup
import time
import re

# Function to fetch and parse data from the webpage
def fetch_domains(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    domains = set()  # Using a set to store unique domains
    for img_tag in soup.find_all('img', attrs={'data-src': True}):
        data_src = img_tag['data-src']
        match = re.search(r'domain_url=([^&]+)', data_src)
        if match:
            domain = match.group(1)
            domains.add(domain)
    return domains

def main():
    url = 'https://www.dubdomain.com/'  # URL to fetch data from
    
    # Input file for saving results
    save_path = input("[+] Save your domains result to (file path): ")
    if not save_path:
        save_path = 'domains.txt'  # Default file name if no input

    print(f"Saving results to {save_path}")

    seen_domains = set()  # Using a set to keep track of processed domains

    # Main loop to fetch data and save it
    while True:
        try:
            domains = fetch_domains(url)
            new_domains = domains - seen_domains  # Find new domains
            seen_domains.update(new_domains)  # Add new domains to the set
            
            with open(save_path, 'a') as file:
                for domain in new_domains:
                    print(domain)  # Print the domain to the terminal
                    file.write(domain + '\n')  # Save the domain to file
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(0.5)  # Delay for 0.5 seconds

if __name__ == "__main__":
    main()
