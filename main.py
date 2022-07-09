from bs4 import BeautifulSoup

import requests


# Definindo URLs a serem buscadas

url_mundomax = ("https://www.mundomax.com.br/violao-eletrico-classico-nylon-natural-cx40-yamaha?gclid=Cj0KCQjwzqSWBhDPARIsAK38LY9lGAfSQVU2KEsKoXmU_jOuF8g2OLVSWjebQDx30go_r06eTmTKeyIaAu3WEALw_wcB#")

url_tronic = ("https://www.brasiltronic.com.br/violao-eletrico-classico-nylon-natural-cx40-ii-yamaha-p1330258")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

# Pegando conteúdo dos respectivos htmls através de requests

html_mundomax = requests.get(url_mundomax, headers=headers).content

html_tronic = requests.get(url_tronic, headers=headers).content

#Criando um objeto BeautifulSoup para ambas

soup_mundomax = BeautifulSoup(html_mundomax, 'html.parser')

soup_tronic = BeautifulSoup(html_tronic, 'html.parser')
# print(soup_mundomax.prettify())

# Extraindo o nome do produto em ambos sites
nomeProduto_mundomax = soup_mundomax.find("h1", {"id": "info-title"}).getText().strip()
nomeProduto_tronic = soup_tronic.find("h1", class_ = "col-12 name no-medium").getText().strip()

# print(nomeProduto_mundomax)
# print(nomeProduto_tronic)

# Extraindo preço do produto

# Preço original
precoOriginal_tronic = soup_tronic.find("del", class_ = 'list-price').getText().strip()
precoOriginal_mundomax = soup_mundomax.find("p", {"id": "info-price"}).getText().strip()

# print(precoOriginal_tronic)
# print(precoOriginal_mundomax)

#Preço à vista
precoAvista_tronic = soup_tronic.find("strong", class_='sale-price').find("span").get_text()
precoAvista_mundomax = soup_mundomax.find("span", class_="billet-discount-price").getText().strip()

# print(precoAvista_mundomax)
# print(precoAvista_tronic)

#Convertendo valores de string para number
 
preco_avista_tronic_number = float(precoAvista_tronic.split()[-1].replace('.','').replace(',','.'))
preco_avista_mundomax_number = float(precoAvista_mundomax.split()[-1].replace('.','').replace(',','.'))

# print(preco_avista_tronic_number)
# print(preco_avista_mundomax_number)
# print(type(preco_avista_tronic_number))
# print(type(preco_avista_mundomax_number))

preco_original_tronic_number = float(precoOriginal_tronic.split()[-1].replace('.','').replace(',','.'))
preco_original_mundomax_number = float(precoOriginal_mundomax.split()[-1].replace('.','').replace(',','.'))

# print(preco_original_mundomax_number)
# print(preco_original_tronic_number)
# print(type(preco_original_mundomax_number))
# print(type(preco_original_tronic_number))

# Calculando descontos de cada site

desconto_mundomax = ((preco_original_mundomax_number - preco_avista_mundomax_number)/preco_original_mundomax_number) * 100
desconto_tronic = ((preco_original_tronic_number - preco_avista_tronic_number)/preco_original_tronic_number) * 100
print('{0:.2f}%'.format(desconto_mundomax))
print('{0:.2f}%'.format(desconto_tronic))
