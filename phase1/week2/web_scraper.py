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

# Step 4 — extract data from each book
for book in books:
    # Extract title
    title = book.find("h3").find("a")["title"]
    
    # Extract price
    price = book.find("p", class_="price_color").text
    
    # Extract rating
    rating = book.find("p", class_="star-rating")["class"][1]
    
    print(f"{title} | {price} | {rating}")

import csv

# Step 5 — save to CSV
with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Rating"])  # header row
    
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        writer.writerow([title, price, rating])

print("Scraping complete. Data saved to books.csv")