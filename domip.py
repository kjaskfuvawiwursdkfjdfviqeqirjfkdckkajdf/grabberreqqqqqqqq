import socket
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init, Style
import os

# Initialize colorama for colored output in terminal
init(autoreset=True)

# Ensure 'ips.txt' exists or create it
if not os.path.exists('ips.txt'):
    open('ips.txt', 'a').close()

def domaintoip(domain):
    """Convert a domain to an IP address and store it if unique."""
    try:
        ip_address = socket.gethostbyname(domain)
        with open('ips.txt', 'r') as file:
            if ip_address in file.read():
                return  # Skip if IP already exists in file
        print(f"Retrieve IP: {Fore.YELLOW}{Style.BRIGHT}{ip_address}")
        with open('ips.txt', 'a') as file:
            file.write(ip_address + '\n')
    except socket.gaierror:
        pass  # Ignore domain if unable to resolve

def main():
    # Display the title
    print(f"{Fore.YELLOW}{Style.BRIGHT}MASS DOMAIN TO IP")

    # Input for domains file
    domains_file = input(f"[+] Input site tanpa http/s: {Fore.RED}{Style.BRIGHT}")
    
    # Check if the file exists
    if not os.path.isfile(domains_file):
        print(f"{Fore.RED}File not found. Please check the file path and try again.")
        return
    
    # Read and clean up domain list
    with open(domains_file, 'r') as file:
        domains = [line.strip().replace('http://', '').replace('https://', '') for line in file]
    
    # Input for number of threads
    try:
        threads = int(input(f"[+] Threads: {Fore.WHITE}"))
    except ValueError:
        print(f"{Fore.RED}Invalid number of threads. Please enter a valid integer.")
        return
    
    # Use ThreadPool for concurrent IP retrieval
    pool = ThreadPool(threads)
    pool.map(domaintoip, domains)
    pool.close()
    pool.join()
    print(f"{Fore.GREEN}Finished retrieving IPs for provided domains.")

if __name__ == "__main__":
    main()
