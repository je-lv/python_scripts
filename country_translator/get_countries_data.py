#!/usr/bin/env python3

import requests
import json

OK = '\033[92m'             #verde
ERR = '\033[91m'            #rojo
INFO = '\033[94m'           #azul
ENDC = '\033[0m'            #end color
BOLD = '\033[1m'            #bold!

print((f'''
{OK}========================================={ENDC}
{BOLD}{INFO}Obteniendo nombres de países ESP-ENG{ENDC}
{OK}========================================={ENDC}
'''))

response = requests.get("https://restcountries.eu/rest/v2/all")

json_file = "countries_translations_ESP-ENG.json"

if response.status_code == 200:
    countries = dict(zip([i['name'] for i in response.json()], [i['translations']['es'] for i in response.json()]))
    json.dump(countries, open(f'data/{json_file}', 'w'))
    print(f'{BOLD}{OK}[+] Archivo {INFO}"{json_file}"{ENDC}{BOLD}{OK} guardado exitosamente.{ENDC}\n')

else:
    print(f'{BOLD}{ERR}[!] Request falló con estatus: {response.status_code}{ENDC}\n')
    exit()