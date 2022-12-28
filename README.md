# python-web-scraping
Web Scraping con Python mediante Selenium

Uso del software Selenium para extraer los datos de todos los partidos de todos los mundiales hasta el 2022.

## Librerías Utilizadas
* Pandas
* Time
* Selenium 3.141.0

## NOTA IMPORTANTE

Si esta utilizando la versión 4.7.2 de Seleniumm tendrá que reemplazar un fragmento de código en el proyecto.

Específicamente tendrá que importar Service del webdriver y establecer la ruta del chromedriver.

### Fragmento a reemplazar:

driver = webdriver.Chrome(r'services/chrome/chromedriver.exe')

### Código en la versión 4.7.2:

from selenium.webdriver.chrome.service import Service

path="services/chrome/chromedriver.exe"

service=Service(executable_path=path)

driver=webdriver.Chrome(service=service)
