# scrapy_tutorial_dse203

## First Example

Simply crawl the whole wikipedia structure by running:

```bash
scrapy crawl example
```

The output is saved in "output/quotes-wiki.html"

## Wiki Infobox Scrapper

Crawl Wikipedia infobox section with the pipeline to fetch data from csv/database, data cleaning, crawling, data post-processing 
and save the output.

```bash
scrapy crawl infobox_spider -o output/info-result.json
```

The output is saved in "output/info-result.json"

