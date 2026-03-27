import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "http://quotes.toscrape.com"
next_url = "/"  # start at first page

quote_list = []
count = 1

try:
    while next_url:
        # Build full URL
        url = base_url + next_url
        print(f"Scraping {url}...")

        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "lxml")

        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            break  

        for quote in quotes:
            text = quote.find(class_="text").text
            author = quote.find(class_="author").text

            link = None
            details = quote.find("a")
            if details:
                href = details.get("href")
                if href and href.startswith("/author/"):
                    link = href

            quote_list.append({
                "ID": count,
                "Text": text,
                "Author": author,
                "Author_Details": link
            })
            count += 1

        # next page
        next_li = soup.find("li", class_="next")
        if next_li and next_li.find("a"):
            next_url = next_li.find("a")["href"]
            time.sleep(1)  
        else:
            next_url = None  # no more pages

   
    csv_filename = "quotes_all.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["ID", "Text", "Author", "Author_Details"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(quote_list)

    print(f"Done! Scraped {len(quote_list)} quotes from {count-1} pages.")
    print(f"Saved to {csv_filename}")

except requests.exceptions.Timeout:
    print("Timeout occurred.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
