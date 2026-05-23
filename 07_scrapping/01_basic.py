import requests
# pip3 install requests -> instalas la dependencia para hacer peticiones HTTP

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"
response = requests.get(url)

if response.status_code == 200:
    print('La peticion fue exitosa')

    html = response.text
    # print(html)

    # Regex para encontrar el precio