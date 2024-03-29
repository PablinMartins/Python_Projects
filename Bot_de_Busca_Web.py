#/////////// IMPORTS ///////////
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

#////////////////////////

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://www.etf.com/etfanalytics/etf-finder')

time.sleep(10)

botao_100 = driver.find_element("xpath", '/html/body/div[5]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/section[2]/div[1]/div/div[4]/button/label/span')

botao_100.click()

#driver.execute_script("arguments[0].click();", botao_100)

numero_paginas = driver.find_element("xpath", '//*[@id="totalPages"]')
numero_paginas = numero_paginas.text.replace("of ", "")
numero_paginas = int(numero_paginas)

lista_tabela_por_pagina = []

elemento = driver.find_element("xpath", '//*[@id="finderTable"]')

for pagina in range(1, numero_paginas + 1):
    
    html_tabela = elemento.get_attribute('outerHTML')
    tabela = pd.read_html(str(html_tabela))[0]
    
    lista_tabela_por_pagina.append(tabela)
    
    botao_avancar_pagina = driver.find_element("xpath", '//*[@id="nextPage"]')
    driver.execute_script("arguments[0].click();", botao_avancar_pagina)
    
#///////// TABELAS E FORMULARIOS ////////////////

tabela_cadastro_etfs = pd.concat(lista_tabela_por_pagina)    

tabela_cadastro_etfs

formulario_de_voltar_pagina = driver.find_element("xpath", '//*[@id="goToPage"]')

formulario_de_voltar_pagina.clear()
formulario_de_voltar_pagina.send_keys("1")
formulario_de_voltar_pagina.send_keys(u'\ue007')

botao_mudar_para_performance = driver.find_element("xpath", '/html/body/div[5]/section/div/div[3]/section/div/div/div/div/div[2]/section[2]/div[2]/ul/li[2]/span')
driver.execute_script("arguments[0].click();", botao_mudar_para_performance)

#////////// A PARTIR DAQUI É TUDO IGUAL ///////////////

lista_tabela_por_pagina = []

elemento = driver.find_element("xpath", '//*[@id="finderTable"]')

for pagina in range(1, numero_paginas + 1):
    
    html_tabela = elemento.get_attribute('outerHTML')
    tabela = pd.read_html(str(html_tabela))[0]
    
    lista_tabela_por_pagina.append(tabela)
    
    botao_avancar_pagina = driver.find_element("xpath", '//*[@id="nextPage"]')
    driver.execute_script("arguments[0].click();", botao_avancar_pagina)
    
#///////////// TABELAS DE RENTABILIDADE /////////////////////

tabela_rentabilidade_etfs = pd.concat(lista_tabela_por_pagina) 

tabela_rentabilidade_etfs = tabela_rentabilidade_etfs.set_index("Ticker")
tabela_rentabilidade_etfs = tabela_rentabilidade_etfs[['1 Year', '3 Years', '5 Years']]
tabela_cadastro_etfs = tabela_cadastro_etfs.set_index("Ticker")

#//////////// BASE DE DADOS FINAL /////////////////

base_de_dados_final = tabela_cadastro_etfs.join(tabela_rentabilidade_etfs, how = 'inner')

