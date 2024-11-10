import requests, os, threading
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Membersihkan layar sesuai OS
os.system("clear" if os.name != "nt" else "cls")

# Warna output
green = "\033[32;1m"
red = "\033[31;1m"
yellow = "\033[33;1m"

page = 0
lock = threading.Lock()

def Hypestatgrab():
	global page
	while True:
		with lock:
			page += 1
			numberget = page
		url = 'https://hypestat.com/recently-updated'
		ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
		r = requests.get(url, headers=ua).text
		bs = BeautifulSoup(r, 'html.parser')
		finder = bs.find('dl', class_='recently_updated')
		if finder:
			geta = finder.find_all('a')
			for site in geta:
				domain = site.text
				print(f'{green}[+] Get {numberget} {domain}')
				with open(savef, 'a') as sv:
					sv.write(domain + '\n')
		else:
			print(f'{red}[!] Not found updated site')
			continue

if __name__ == '__main__':
	run_ip = input('[#] Run grab or no? (y/n) > ')
	if run_ip.lower() == 'y':
		savef = input('[#] Save file name > ')
		thrd = input('[#] Thread > ')
		print('\n')
		with ThreadPoolExecutor(max_workers=int(thrd)) as t:
			t.submit(Hypestatgrab)
	elif run_ip.lower() == 'n':
		print(f'{red}#~> Bye...')
		exit()
	else:
		print(f'{red}#~> Your choice is not in the menu, bye...')
