import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

def scrape_books():
    url = "http://books.toscrape.com/catalogue/page-1.html"
    titles, prices, ratings = [], [], []

    while url:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        for product in soup.select(".product_pod"):
            titles.append(product.h3.a["title"])
            prices.append(product.select_one(".price_color").text)
            ratings.append(product.p["class"][1])

        next_page = soup.select_one(".next > a")
        if next_page:
            url = "http://books.toscrape.com/catalogue/" + next_page["href"]
        else:
            url = None

    df = pd.DataFrame({"Title": titles, "Price": prices, "Rating": ratings})
    df.to_excel("products.xlsx", index=False)

    conn = sqlite3.connect("products.db")
    df.to_sql("products", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Data scraped and saved to products.xlsx and products.db")

if __name__ == "__main__":
    scrape_books()
