def scan(site):
    ur = site.rstrip()
    ch = site.split('\n')[0].split('.')
    ip1 = ch[0]
    ip2 = ch[1]
    ip3 = ch[2]
    taz = str(ip1) + '.' + str(ip2) + '.'
    i = 0
    while i <= 255:
        i += 1
        c = 0
        while c <= 255:
            c += 1
            print("Ranging ==> " + str(taz) + str(c) + '.' + str(i))
            with open('Ranged.txt', 'a') as file:
                file.write(str(taz) + str(c) + '.' + str(i) + '\n')


nam = input('List IPs: ')
with open(nam) as f:
    for site in f:
        scan(site)
