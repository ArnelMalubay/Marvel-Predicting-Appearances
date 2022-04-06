
# Predicting Marvel Appearances using CatBoost

This project consists of four main parts.

1. Scraping the [Marvel Wiki](https://marvel.fandom.com/wiki/Marvel_Database) page for data about Marvel characters using scrapy. For the main file used for scraping, navigate to marvelscraping/marvelscraping/spiders/marvel_spider.py. The scraped data is stored in marvelscraping/characters.csv. To run this scraping job, you can clone this repository and run

`pip install -r requirements.txt`

preferably on a virtual environment. Then, navigate to the marvelscraping folder and run 

`scrapy crawl characters -o characters.csv`

on the terminal.

2. Visualizing results and identifying patterns and trends
3. Predicting number of appearances using Catboost 
4. Explaining created model using SHAP 

