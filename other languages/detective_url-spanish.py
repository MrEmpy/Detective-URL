import requests
from colorama import Fore

print(Fore.GREEN + '''
▒█▀▀▄ █▀▀ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ ░▀░ ▀█░█▀ █▀▀ 　 ▒█░▒█ ▒█▀▀█ ▒█░░░ 
▒█░▒█ █▀▀ ░░█░░ █▀▀ █░░ ░░█░░ ▀█▀ ░█▄█░ █▀▀ 　 ▒█░▒█ ▒█▄▄▀ ▒█░░░ 
▒█▄▄▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ░░▀░░ ▀▀▀ 　 ░▀▄▄▀ ▒█░▒█ ▒█▄▄█

           ●❯────────────────｢⊙｣───────────────❮●
           ● Herramienta creada por Mr Empy    ●
           ● Versión 1.0                       ●
           ●❯────────────────｢⊙｣───────────────❮●
                       ''')

site = input(Fore.GREEN + '[!] Pegue la URL del sitio: ')
pass_list = input(Fore.GREEN + '[!] Pegue su directorio de Wordlist: ')

print(Fore.GREEN + '')
print('=================================================')
print('[+] URL:', site)
print('[+] Wordlist:', pass_list)
print('[+] Estado: 200, 301, 302, 307, 403')
print('=================================================')
print('')

wrd_lst=open(pass_list, "r")
read_lines=wrd_lst.readlines()
for line in read_lines:
    lst=line.strip('\r\n')
    result=requests.get(site + lst)
    if (result.status_code == 200):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(Estado: 200)')
    if (result.status_code == 204):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(Estado: 204)')
    if (result.status_code == 301):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(Estado: 301)')
    if (result.status_code == 302):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(Estado: 302)')
    if (result.status_code == 307):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(Estado: 307)')
    if (result.status_code == 403):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(Estado: 403)')
print('')
print(Fore.GREEN + "[+] ¡Terminado!")