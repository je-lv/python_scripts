#!/usr/bin/env python3

from fuzzywuzzy import process
import json
import sys

OK = '\033[92m'             #verde
ERR = '\033[91m'            #rojo
INFO = '\033[94m'           #azul
ENDC = '\033[0m'            #end color
BOLD = '\033[1m'            #bold!

err_display = f'{ERR}{BOLD}\n[!] Ingresar país o países.{ENDC}\n'

usage_help = f'''\n[*] Ejemplo de uso: 
\n\n{INFO}{BOLD}python3 {sys.argv[0]} germany \n
python3 {sys.argv[0]} germany,france,italy {ENDC}\n
python3 {sys.argv[0]} 'germany, france, italy' {ENDC}\n
'''

if len(sys.argv[1:]) != 1:
    print(err_display)
    print(usage_help)
    exit()


print((f'''
{OK}========================================={ENDC}
{BOLD}{INFO}Traduciendo países de inglés a español{ENDC}
{OK}========================================={ENDC}
'''))

countries_eng = sys.argv[1]

countries_eng = countries_eng.replace(' ','').split(',')

countries_data = json.load(open('data/countries_translations_ESP-ENG.json'))

countries_esp = [countries_data[process.extractOne(c, countries_data.keys())[0]] for c  in countries_eng]

print(f'{BOLD}{", ".join(countries_esp)}{ENDC}\n')