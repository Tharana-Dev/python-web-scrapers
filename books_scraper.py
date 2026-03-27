import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time

base_url = "http://books.toscrape.com"
next_url = "http://books.toscrape.com/index.html"

book_list = []
count =1

try:
    while next_url:
        url =next_url
        print(f"Scrapping {url}")

        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "lxml")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            try:
                title = book.find("h3").find("a")["title"]
            except:
                title = book.find("h3").find("a").text
                
            try:
                price = book.find("p", class_="price_color").text
                # Remove the pound sign and any other non‑numeric characters (keep dots)
                import re
                price = re.sub(r"[^\d.]", "", price)  
                price = float(price)
            except:
                price = None
                
            try:
                rating_tag =book.find("p", class_="star-rating")
                if rating_tag and len(rating_tag)>1:
                    rating = rating_tag["class"][1]
            except:
                 rating = None
                 
            try:
                link = book.find("h3").find("a")["href"]
                if link:
                    from urllib.parse import urljoin
                    full_link = urljoin(base_url, link)
            except:
                link = None

            try:
                avail_tag = book.find("p", class_="instock availability")
                availability = avail_tag.text.strip() 
            except:
                availability = None

            book_list.append({
                "ID": count,
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Link": full_link,
                "Availability": availability
                        })
            count += 1
        next_li = soup.find("li", class_="next")
        if next_li and next_li.find("a"):
            relative_link = next_li.find("a")["href"]
            next_url = urljoin(url, relative_link) 
        else:
            next_url = None

    time.sleep(1)

    csv_filename = "Books.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["ID", "Title", "Price", "Rating", "Link", "Availability"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(book_list)
    
except requests.exceptions.Timeout:
    print("Timeout occurred.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
























