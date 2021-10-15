# https://economia.uol.com.br/cotacoes/

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Tabela
arquivo_excel = Workbook()
planilha1 = arquivo_excel.active
planilha1.title = "Cotação"

planilha1['A1'] = 'Moeda'
planilha1['B1'] = 'Preço'
planilha1['C1'] = 'Dif %'

# Configurações Gerais - Cotação
site_cotacao = requests.get('https://valor.globo.com/valor-data/')
content_nk = site_cotacao.content
site_cot = BeautifulSoup(content_nk, 'html.parser')

moeda = site_cot.find('div', attrs={'class': 'valor-data__component'})
nome_moeda = moeda.findAll('div', attrs={'class': 'data-cotacao__ticker_name'})
valor_moeda = moeda.findAll('div', attrs={'class': 'data-cotacao__ticker_quote'})
dif_moeda = moeda.findAll('div', attrs={'class': 'data-cotacao__ticker_percentage_green'})

nomes = []
valores = []
dif = []
resultado = []

for nome in nome_moeda:
    nomes.append(nome.text)
    
for valor in valor_moeda:
    valores.append(valor.text)
    
for diferenca in dif_moeda:
    dif.append(diferenca.text)
    
for conjunto in zip(nomes, valores, dif):
    resultado.append(conjunto)
    
    
for result in resultado:
    valores = [
        (result)
    ]
    
    for linha in valores:
        planilha1.append(linha)
        
try:
    arquivo_excel.save("relatorio-cotacao.xlsx")
    print('Relatorio gerado com sucesso')
except:
    print("Erro ao salvar o Relatório.")
