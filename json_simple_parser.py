#!/usr/bin/python3

"""

Parseador simple de jsons de un solo nivel de produnfidad.


"""

import json
import os
import pandas as pd
import optparse
parser = optparse.OptionParser()
parser.add_option('-f', '--file', action="store", dest="file", help="Aregar archivo TXT.")
parser.add_option('-o', '--out', action="store", dest="out", help="Aregar nombre de archivo CSV de salida.")
options, args = parser.parse_args()

success, err, info, end = '\033[92m', '\033[91m', '\033[94m', '\033[0m'

if not options.file:
    print(f'{err}[-] Es necesario ingresar archivo!{end}')
    exit()
elif not options.out:
    print(f'{err}Es necesario ingresar nombre de archivo!{end}')
    exit()
else:
    df = pd.DataFrame.from_records([json.loads(f+'}') for f in open(options.file).read().replace('\n','').split('}') if f], index='id')
    df.fillna(value='sin dato', inplace=True)
    zipped = dict(method='zip',archive_name=f'{options.out}.csv')  
    df.to_csv(f'{options.out}.zip', index=True,compression=zipped)  
    
print(f'{success}[+] Archivo {info}{options.out}.zip{end} {success}guardado en {info}{os.getcwd()}{end}')
