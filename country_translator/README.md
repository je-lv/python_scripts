# Traductor simple de países de Inglés a Español

## Uso

```bash
pip3 install install fuzzywuzzy

#or

conda install -c conda-forge fuzzywuzzy

python translator.py germany,france,italy
```


![Traducciones](/imgs/translate_results.png)

### Datos

En el directorio 'data' se encuentra el archivo json con las traducciones de países de inglés - español.

Sin embargo este repositorio incluye el script usado para generar ese archivo json, ya que pudiera utilizarse para otro tipo de proyectos.


```bash
pip3 install requests

#or

conda install -c conda-forge requests

python get_countries_data.py
```

![Data script](/imgs/data_script.png)

