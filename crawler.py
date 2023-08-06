import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com")

soup = BeautifulSoup(page.content, "html.parser")

tags = [tag.text.strip() for tag in soup.find_all("span", { "class": "tag-item" })]

response = requests.post("http://localhost:3001/crawler", json=tags)

if response.status_code == 200:
    print("POST bem-sucedido!")
    print("Resposta do servidor:", response.text)
else:
    print("Erro no POST. Código de status:", response.status_code)
    print("Resposta do servidor:", response.text)
