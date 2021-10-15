# https://economia.uol.com.br/cotacoes/

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Tabela
arquivo_excel = Workbook()
planilha1 = arquivo_excel.active
planilha1.title = "Shopee"

planilha1['A1'] = 'Produto'
planilha1['B1'] = 'Preço'
planilha1['C1'] = 'Total de Vendas'
planilha1['D1'] = 'Local'

# Configurações Gerais - Cotação
site_cotacao = requests.get('https://shopee.com.br/Informática-cat.22178')
content_nk = site_cotacao.content
site_cot = BeautifulSoup(content_nk, 'html.parser')

geral = site_cot.find('div', attrs={'class': 'row shopee-search-item-result__items'})
items = geral.findAll('div', attrs={'class': '_3QUP7l'})

for item in items:
    titulo_produto = item.find('div', attrs={'class': '_10Wbs- _5SSWfi UjjMrh'})
    valor_produto = item.find('div', attrs={'class': 'data-cotacao__ticker_percentage_green'}) # 
    total_vendas = item.find('div', attrs={'class': '_2VIlt8'})
    local_venda = item.find('div', attrs={'class': '_1w5FgK'})
    titulo_do_produto = titulo_produto.text
    valor_do_produto = valor_produto.text
    total_de_vendas = total_vendas.text
    local_de_venda = local_venda.text
    
    valores = [
        (titulo_do_produto, valor_do_produto, total_de_vendas, local_de_venda)
    ]
    
    for linha in valores:
        planilha1.append(linha)
        
try:
    arquivo_excel.save("relatorio-shoopee.xlsx")
    print('Relatorio gerado com sucesso')
except:
    print("Erro ao salvar o Relatório.")
