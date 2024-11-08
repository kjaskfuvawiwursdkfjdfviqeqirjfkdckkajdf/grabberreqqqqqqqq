import requests, os, threading
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

linux = "clear"
windows = "cls"
os.system([linux, windows][os.name == "nt"])

green = "\033[32;1m"
red = "\033[31;1m"
yellow = "\033[33;1m"

page = 0
lock = threading.Lock()

def Hypestatgrab():
	global page
	while True:
		with lock:
			page+=1
			numberget = page
		url = 'https://hypestat.com/recently-updated'
		ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
		r = requests.get(url,headers=ua).text
		bs = BeautifulSoup(r, 'html.parser')
		finder = bs.find('dl',class_='recently_updated')
		if finder:
			geta = finder.find_all('a')
			for site in geta:
				domain = site.text
				print(f'{green}[+] Get {numberget} {domain}')
				sv = open(savef, 'a').write(domain+'\n')
		else:
			print('{red}[!] Not found updated site')
			continue
			
if __name__ == '__main__':
	banner = '''
	Hypestat Grabber Last Viewed Site
	
           by : wannazid
           github : github.com/wannazid
	'''
	print(yellow+banner)
	run_ip = input('[#] Run grab or no? (y/n) > ')
	if run_ip == 'y' or run_ip == 'Y':
		savef = input('[#] Savefiles name > ')
		thrd = input('[#] Thread > ')
		print('\n')
		with ThreadPoolExecutor(max_workers=int(thrd)) as t:
			t.submit(Hypestatgrab)
	elif run_ip == 'n' or run_ip == 'N':
		print(f'{red}#~> Bybye.....')
		exit()
	else:
		print(f'{red}#~> Your choice is not in the menu, byebye...')
