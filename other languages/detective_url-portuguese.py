import requests
from colorama import Fore

print(Fore.GREEN + '''
▒█▀▀▄ █▀▀ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ ░▀░ ▀█░█▀ █▀▀ 　 ▒█░▒█ ▒█▀▀█ ▒█░░░ 
▒█░▒█ █▀▀ ░░█░░ █▀▀ █░░ ░░█░░ ▀█▀ ░█▄█░ █▀▀ 　 ▒█░▒█ ▒█▄▄▀ ▒█░░░ 
▒█▄▄▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ░░▀░░ ▀▀▀ 　 ░▀▄▄▀ ▒█░▒█ ▒█▄▄█

              ●❯──────────────｢⊙｣─────────────❮●
              ● Ferramenta criado por Mr Empy ●
              ● Versão 1.0                    ●
              ●❯──────────────｢⊙｣─────────────❮●
                       ''')

site = input(Fore.GREEN + '[!] Cole a URL do Site: ')
pass_list = input(Fore.GREEN + '[!] Cole o diretório da usa Wordlist: ')

print(Fore.GREEN + '')
print('=================================================')
print('[+] URL:', site)
print('[+] Wordlist:', pass_list)
print('[+] Status: 200, 301, 302, 307, 403')
print('=================================================')
print('')

wrd_lst=open(pass_list, "r")
read_lines=wrd_lst.readlines()
for line in read_lines:
    lst=line.strip('\r\n')
    result=requests.get(site + lst)
    if (result.status_code == 200):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 200)')
    if (result.status_code == 204):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 204)')
    if (result.status_code == 301):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 301)')
    if (result.status_code == 302):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 302)')
    if (result.status_code == 307):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 307)')
    if (result.status_code == 403):
        print(Fore.GREEN + '[+]', Fore.WHITE + site + lst, Fore.GREEN + '(status: 403)')
print('')
print(Fore.GREEN + "[+] Finalizado!")