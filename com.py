from bs4 import BeautifulSoup
import requests
import os
from concurrent.futures import ThreadPoolExecutor

# Clear the terminal screen
os.system("cls" if os.name == "nt" else "clear")

# Colors
green = '\033[32m'
reset = '\033[1;37m'

def Main():
    global green
    domain_ip = input('[#] Pilih domain di atas salah satu (.net) > ')
    go_page = int(input('[#] Mulai Dari Page > '))
    page = go_page - 1
    end_page = int(input('[#] End Page > '))
    epage = end_page + 1
    save_ip = input('[#] Result Name > ')
    
    while True:
        page += 1
        url = f'https://www.topsitessearch.com/domains/{domain_ip}/{page}'
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-A530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.0.3922.70977'}
        r = requests.get(url, headers=headers).text
        bs = BeautifulSoup(r, 'html.parser')
        
        try:
            find = bs.find('tbody').find_all('tr')
        except AttributeError:
            break
        
        stop = f'https://www.topsitessearch.com/domains/{domain_ip}/{epage}'
        if stop in url:
            break
        else:
            for a in find:
                c = a.find('td').text
                rmv = ''.join([i for i in c if not i.isdigit() and i != ':'])
                spc_rmv = rmv.strip()
                print(f'{green}{page} > {spc_rmv}{reset}')
                with open(save_ip, 'a') as file:
                    file.write(spc_rmv + '\n')

Main()
