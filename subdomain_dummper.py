import requests, json, signal
from pwn import *
from tabulate import tabulate
from bs4 import BeautifulSoup

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

subdomains = list()
name = list()
col_names = [f'{RED}Subdominios{RESET}']

def ctrl_c(sig, frame):
    print(f"\n{RED}[!] Saliendo...{RESET}")
    exit()

signal.signal(signal.SIGINT, ctrl_c)

banner = f"""{CYAN}
███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
███████╗██║   ██║██████╔╝██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
                        {RED}BY: Alcatraz2033{CYAN}
██████╗ ██╗   ██╗███╗   ███╗███╗   ███╗██████╗ ███████╗██████╗            
██╔══██╗██║   ██║████╗ ████║████╗ ████║██╔══██╗██╔════╝██╔══██╗           
██║  ██║██║   ██║██╔████╔██║██╔████╔██║██████╔╝█████╗  ██████╔╝           
██║  ██║██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗           
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║     ███████╗██║  ██║           
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝           
{RESET}"""

def request(r):
    p = BeautifulSoup(r.text, 'html5lib')    
    for i in json.loads(r.text):
        name.append(i['common_name'])
    name2 = list(set(name))

    for i in name2:
        subdomains.append([CYAN + i + RESET])    
    print(f'\n{tabulate(subdomains, headers=col_names, tablefmt="fancy_grid", showindex=True)}')
    
if __name__ == '__main__':

    print(banner)
    inicio = input(f'{CYAN}[+]{RESET} Ingrese la pagina web a escanear: ')
    p1 = log.progress("Buscando Subdominios...")

    if inicio[0:8] == 'https://':
        inicio = inicio[8:]
    elif inicio[0:7] == 'http://':
        print(f'{RED}[!] Esta pagina web no tiene certificaso SSL')
        exit()
    else:
        inicio = inicio

    url = f"https://crt.sh/?q=%25.{inicio}".replace('\n', '')
    r = requests.get(url + '&output=json')
    request(r)
