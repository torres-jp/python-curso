from bs4 import BeautifulSoup
import requests
import os

os.system("cls" if os.name == "nt" else "clear")

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"
response = requests.get(url)

if response.status_code == 200:
    print("La peticion fue un exito!")

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())
    # title_tag = soup.title
    # if title_tag:
    #     print(f"El titulo de la pagina es: {title_tag.text}")

    # metas = soup.title.parent.find_all("meta")
    # # print(metas)

    # price_span = soup.find("span", class_="as-pricepoint-fullprice")
    # if price_span:
    #     print(f"El precio es: {price_span.text}")
    # else:
    #     print("No se encontro el precio")

    # find each product and get the name and price
    products = soup.find_all(class_="rc-productselection-item")
    for product in products:
        name = product.find(class_="list-title")
        price = product.find(class_="as-pricepoint-fullprice")
        print(f"Producto: {name.text} - Precio: {price.text}")
