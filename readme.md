# Web Scrapers – Books & Quotes

Two Python scripts that scrape data from `books.toscrape.com` and `quotes.toscrape.com` and save the results as CSV files.

## ✨ Features

- **Books scraper (`books_scraper.py`)** – collects book titles, prices (cleaned), ratings, links, and availability from all pages of the site.
- **Quotes scraper (`quotes_scrapper.py`)** – collects quotes, authors, and links to author detail pages.
- **Progress output** – prints the URL being scraped.
- **Error handling** – timeouts and request exceptions are caught.
- **CSV export** – results are saved to `Books.csv` and `quotes_all.csv`.

## 🚀 How to Run

1. **Install required packages**:
   ```bash
   pip install requests beautifulsoup4 lxml
   ```
2. **Run the scraper**:
   - For books:
     ```bash
     python books_scraper.py
     ```
   - For quotes:
     ```bash
     python quotes_scrapper.py
     ```
3. The scraped data will be saved in the same folder as the script.

## 📁 File Structure

```
web-scrapers/
├── books_scraper.py      # Books to scrape
├── quotes_scrapper.py    # Quotes to scrape
├── Books.csv             # Output from books scraper
├── quotes_all.csv        # Output from quotes scraper
└── README.md             # This file
```

## 🛠️ Technologies

- Python 3
- `requests` – HTTP requests
- `BeautifulSoup4` – HTML parsing
- `lxml` – parser (faster than html.parser)
- `csv` – standard library for CSV writing
- `re` – regular expressions for price cleaning

## 📊 Sample Output

**Books.csv** columns: ID, Title, Price (float), Rating, Link, Availability

**quotes_all.csv** columns: ID, Text, Author, Author_Details (URL)

## 🔧 Customisation

- Change the `base_url` or `next_url` to scrape different sections of the site.
- Modify the field extraction logic in the loops to capture additional data.

## 📧 Contact

For questions or suggestions:  
[dev.tharana@gmail.com](mailto:dev.tharana@gmail.com)

## 🙏 Acknowledgements

Built as a portfolio project to demonstrate web scraping with Python, using real test sites.
