# Book to scrape

Build a Crawler which will crawl all the books from all the available pages in `books.toscrape` website
the goal is to visit each book page and scrape the "book name", the "price" and the "availability" from all the available pages.
- http://books.toscrape.com/

## Code style

- This project is written in python 3.
- Use Scrapy.

## Clone/Run app
````
# Clone repo
$ git clone https://github.com/MotazBellah/book_crawler

# Install all dependencies
$ pip install -r requirements.txt

# Run
$ cd books
$  scrapy scrapy crawl all_books -o books.csv

````
