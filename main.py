from selenium import webdriver
import pandas as pd
# Importamos esta librería para darle un tiempo de espera
import time
# from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(r'services/chrome/chromedriver.exe')

writer=pd.ExcelWriter('data.xlsx')
def obtener_data(year):

# Partidos de futbol ---> como encontrarlos
# td[@align="right"]/..
    web = f'https://es.wikipedia.org/wiki/Copa_Mundial_de_F%C3%BAtbol_de_{year}'
    driver.get(web)
    matches = driver.find_elements(by='xpath', value='//td[@align="right"]/.. | //td[@text-align="right"]/.. ')

    local = []
    score = []
    visitante = []

    for match in matches:
        # Si no agregamos el .text lo que nos devuelve es la etiqueta HTML y no el texto de dentro de ella.
        local.append(match.find_element(by='xpath', value='./td[2]').text)
        score.append(match.find_element(by='xpath', value='./td[3]').text)
        visitante.append(match.find_element(by='xpath', value='./td[4]').text)

    dict_futbol = {'home': local, 'score': score, 'visitante': visitante}
    df_futbol = pd.DataFrame(dict_futbol)

    df_futbol['year'] = year

    # Duerme la ejecución durante 2 segundos
    time.sleep(2)
    blank = df_futbol["home"][1]
    df_futbol.replace({blank: None},inplace=True)
    # print(df_futbol)
    data=df_futbol[df_futbol['home'].notna()]

    data.to_excel(writer, sheet_name=f'{year}',engine='openpyxl', index=False)
    writer.save()
    print(data)

    return data

years=[1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014,2018,2022]

fifa= [obtener_data(year) for year in years]
writer.close()
driver.quit()
