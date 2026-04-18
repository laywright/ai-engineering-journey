import requests
from bs4 import BeautifulSoup

# Step 1 — fetch the page
response = requests.get("http://books.toscrape.com")
print(response.status_code)  # 200 means success
# Step 2 — parse the HTML
soup = BeautifulSoup(response.text, "html.parser")
# Step 3 — find elements
books = soup.find_all("article", class_="product_pod")
print(len(books))  # should print 20

import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(f"{title} - {price}")