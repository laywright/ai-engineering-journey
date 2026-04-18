import requests
import csv
from bs4 import BeautifulSoup

with open("books.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Rating"])  # header — written once

    for page in range(1, 51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)  # ← use the url variable
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_="price_color").text
            rating = book.find("p", class_="star-rating")["class"][1]
            writer.writerow([title, price, rating])

        print(f"Page {page} scraped — {len(books)} books found")

print("Scraping complete. Data saved to books.csv")