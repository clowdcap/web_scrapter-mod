import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Tabela
arquivo_excel = Workbook()
planilha1 = arquivo_excel.active
planilha1.title = "Nike"

planilha1['A1'] = 'Nome'
planilha1['B1'] = 'Categoria'
planilha1['C1'] = 'Preco Antigo'
planilha1['D1'] = 'Preco Atual'
planilha1['E1'] = 'Porcentagem'
planilha1['F1'] = 'Cores'

# Configurações Gerais - Nike
site_nike = requests.get('https://www.nike.com.br/masculino?p=1&Fabricante=&Filtros=Tipo+de+Produto%3ACal%E7ados&cor=&tamanho=&precode=&precoate=&ofertas=sim&ordenacao=0&limit=24&ordemFiltro=Tipo+de+Produto&site_id=')
content_nk = site_nike.content
site_nk = BeautifulSoup(content_nk, 'html.parser')
    # Achar div referencia o produto
produto_nike = site_nk.find('div', attrs={'class': 'produto'})
produtos_nike = site_nk.find('div', attrs={'class': 'box-resultados'})

for p in produtos_nike:
    # Produto Nome
    produto_nome = p.find('a', attrs={'class': 'produto__nome'})
    nome_do_produto = produto_nome.text
    
    # Produto Categoria
    produto_categoria = p.find('a', attrs={'class': 'produto__descricaocurta'})
    categoria_do_produto = produto_categoria.text
    
    # Produto PREÇO
    produto_preco = p.find('a', attrs={'class': 'produto__preco'})
        # Produto PREÇO Antigo
    produto_preco_antigo = produto_preco.find('span', attrs='produto__preco--desabilitado')
    preco_antigo = produto_preco_antigo.text
        # Produto PREÇO Novo
    produto_preco_novo = produto_preco.find('span', attrs='produto__preco_por')
    preco_novo = produto_preco_novo.text
        # Produto PREÇO Porcentagem
    produto_procentagem_dif = produto_preco.find('span', attrs='produto__percentdesconto')
    preco_porcentagem_dif = produto_procentagem_dif.text
    
    # Produto Cor
    produto_cor = p.find('a', attrs='produto__cores')
    cor_do_produto = produto_cor.text
    
    # Prints
    #print(nome_do_produto)
    #print(categoria_do_produto)
    #print(preco_antigo)
    #print(preco_novo)
    #print(preco_porcentagem_dif)
    #print(cor_do_produto)
    #print('\n\n')
    
    valores = [
        (nome_do_produto, categoria_do_produto, preco_antigo, preco_novo, preco_porcentagem_dif, cor_do_produto)
    ]
    
    for linha in valores:
        planilha1.append(linha)

try:
    arquivo_excel.save("relatorio-nike.xlsx")
    print('Relatorio gerado com sucesso')
except:
    print("Erro ao salvar o Relatório.")

