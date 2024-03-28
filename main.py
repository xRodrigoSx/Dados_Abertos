import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

time.sleep(15)

class Governo(scrapy.Spider):
    name = "Dados do Governo"
    start_urls = ["https://dados.gov.br/dados/conjuntos-dados"]

    def parse(self, response):
        SELETOR = "div .wrapper"
#        SELETOR = ".search-result.container.my-2"
        dados = []
        for categoria in response.css(SELETOR):
            dado = {}

            NOME_SELETOR = "h3 .capitalize.search-result-title.text-base.text-gray-900::text"

            dado['nome'] = categoria.css(NOME_SELETOR).extract_first()
            print(dado)

            dados.append(dado)

            print("Total de dados: ", len(dados))
            
#            driver = webdriver.Chrome()
#            driver.get("https://dados.gov.br/dados/conjuntos-dados")
#            pagina_pulada = pular_pagina(driver)

#            if pagina_pulada:
#                print("Página pulada com sucesso!")
#            else:
#                print("Erro ao pular página.")

#        def pular_pagina(driver):
#            try:
#                proxima_pagina = driver.find_element(By.CSS_SELECTOR, "a.next-page")
#                proxima_pagina.click()
#                return True
#            except:
#                return False
        