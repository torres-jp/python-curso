from bs4 import BeautifulSoup
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"
response = requests.get(url)

if response.status_code == 200:
    print('La peticion fue un exito!')

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    title_tag = soup.title
    if title_tag:
        print(f'El titulo de la pagina es: {title_tag.text}')
    
    metas = soup.title.parent.find_all('meta')
    # print(metas)

    price_span = soup.find('span', class_='rc-prices-fullprice')
    if price_span:
        print(f'El precio es: {price_span.text}')
    else:
        print('No se encontro el precio')