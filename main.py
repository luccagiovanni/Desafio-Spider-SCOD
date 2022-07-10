from attr import attrs
from bs4 import BeautifulSoup

import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# Definindo URLs a serem buscadas
url_mercadolivre = ("https://lista.mercadolivre.com.br/")

url_americanas = ("https://www.americanas.com.br/busca/")

#Definindo o item a ser buscado
produto = input('Qual produto você deseja?')

# Pegando conteúdo dos respectivos htmls através de requests
response_mercadolivre = requests.get(url_mercadolivre + produto, headers=headers).content

response_americanas = requests.get(url_americanas + produto, headers=headers).content

#Criando um objeto BeautifulSoup para ambas páginas
soup_mercadolivre = BeautifulSoup(response_mercadolivre, 'html.parser')
soup_americanas = BeautifulSoup(response_americanas, 'html.parser')
# print(soup_americanas.prettify())

def buscar_produto(item):
    # Extraindo os produtos em ambos sites
    produtos_mercadolivre = soup_mercadolivre.findAll('div', class_ = "ui-search-result__wrapper")
    produtos_americanas = soup_americanas.findAll("div", class_ = "col__StyledCol-sc-1snw5v3-0 jGlQWu src__ColGridItem-sc-122lblh-1 cJnBan")

    # print(len(produtos_americanas))

    # Criando listas para armazenar os dados extraídos
    resultados_lista_mercadolivre= []
    resultados_lista_americanas = []

    #Limitando a quantidade de elementos da list
    produtos_mercadolivre = produtos_mercadolivre[:7]
    produtos_americanas = produtos_americanas[:7]

    #Adquirindo os nomes e preços de cada elemento contido na lista
    for produto in produtos_mercadolivre:
        #Extraindo o nome dos produtos
        nome_produto_mercadolivre = produto.find('h2', class_ = "ui-search-item__title ui-search-item__group__element")
        # Extraindo preço do produto
        preco_real_mercadolivre = produto.find("span", class_ = 'price-tag-fraction')
        preco_cents_mercadolivre = produto.find('span', class_= 'price-tag-amount').find("span", class_ = 'price-tag-cents')
        if (preco_cents_mercadolivre):
            preco_mercadolivre = preco_real_mercadolivre.text + ',' + preco_cents_mercadolivre.text
        else:
            preco_mercadolivre = preco_real_mercadolivre.getText()
        site = "Mercado Livre"

        # Criação de uma dict
        resultado_mercadolivre_dict= {}

        resultado_mercadolivre_dict['site'] = site
        resultado_mercadolivre_dict['nome'] = nome_produto_mercadolivre.getText()
        resultado_mercadolivre_dict['preço'] = "R$ "+ preco_mercadolivre

        # Atribuindo os dados num dataframe
        resultados_lista_mercadolivre.append(resultado_mercadolivre_dict)

    print(resultados_lista_mercadolivre)
    print("Foram buscados: "+ str(len(resultados_lista_mercadolivre)) + " produtos em Mercado Livre.")

    #Adquirindo os nomes e preços de cada elemento contido na lista
    for teste in produtos_americanas:
        #Extraindo o nome dos produtos
        nome_produto_americanas = teste.find('h3', class_ = "product-name__Name-sc-1shovj0-0 gUjFDF")
        # Extraindo preço do produto
        preco_americanas = teste.find("span", class_ = 'src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM').getText().strip()
        site = "Americanas"

        # Criação de uma dict
        resultado_americanas_dict= {}

        resultado_americanas_dict['site'] = site
        resultado_americanas_dict['nome'] = nome_produto_americanas.getText()
        resultado_americanas_dict['preço'] = preco_americanas

        # Atribuindo os dados num dataframe
        resultados_lista_americanas.append(resultado_americanas_dict)

    print(resultados_lista_americanas)
    print("Foram buscados: " + str(len(resultados_lista_americanas)) + " produtos em Americanas.")

    # Merge nas duas listas de dict
    resultado_todos_produtos = []
    resultados_lista_mercadolivre.extend(resultados_lista_americanas)
    for myDict in resultados_lista_mercadolivre:
        if myDict not in resultado_todos_produtos:
            resultado_todos_produtos.append(myDict)
    print(resultado_todos_produtos)

buscar_produto(produto)