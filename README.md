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

## LinkedIn Scrapper using Selenium

Crawl LinkedIn profile pages with the pipeline to fetch urls by Google search and then use the fetched urls for scraping,
 using Selenium
 

```bash
python3 ./scrapy_tutorial_dse203/spiders/linkedin_script.py
```

Note: I have to encrypt my password for privacy, you can go into the code and replace the credentials with yours.
The output is saved in output/linkedin_output.csv

