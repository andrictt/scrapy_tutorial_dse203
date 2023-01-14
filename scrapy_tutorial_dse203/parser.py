import re
import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Text Mining with Python tutorial
from bs4 import BeautifulSoup

# Step1: open the target response file and use BS to parse it
HTMLFile = open(
    "quotes-as-a-new-study-spotlights-a-growing-role-for-lrrk2-in-parkinsons-denali-clears-an-early-trial-hurdle.html",
    "r")
index = HTMLFile.read()

S = BeautifulSoup(index, 'lxml')

# Step2: Use beautiful soup to parse the response
# Example 1: Finding the first paragraph


# Exercise 1: Getting the published date
para = S.find_all(class_='epn_time')[0].get_text()
# print(para)

# Example 2: Getting the sentences with keyword "apple"
txt = "I like to eat apple. Me too. Let's go buy some apples."
print(re.findall(r"([^.]*?buy[^.]*\.)", txt))

# Exercise 2: Returning the sentences with the keyword "LRRK2"
sentences = S.find_all('p')
for sentence in sentences:
    sentenceToString = sentence.get_text()
    res = re.findall(r"([^.]*?LRRK[^.]*\.)", sentenceToString)
    if len(res) > 0:
        # data cleaning here
        print(res)

# Example 3: Tokenizing the sentence into words
print(para)
print(para.split())

# Exercise 3: Given a list of keywords, return the sentences from the news with those keywords
wordsToSearch = ["LRRK2", "Parkin"]

driver = webdriver.Chrome('driver/chromedriver')

driver.get('https://www.google.com/')
search_query = driver.find_element("name", 'q')
search_query.send_keys('site:https://endpts.com/ AND "LRRK2"')
search_query.send_keys(Keys.RETURN)
sleep(0.5)

elem = driver.find_elements("xpath", "//*[@href]")
urls = [url.get_attribute('href') for url in elem]
urls = [url for url in urls if str(url).startswith("https://endpts.com/")]
print(urls)

driver.quit()


# Example 4: Search google with keywords and site name
# type in Google search bar: site:https://endpts.com/ AND "LRRK2"

# Exercise 4: How to use selenium to do the above search and get the urls

# Assignment 1: Find Company Names from the news articles -- Shera

# Assignment 2: Find all articles with the given drug target names (selenium) -- David

# Assignment 3: Return all the sentences from the news article with given development stages (data cleaning) -- Gavin

# Assignment 4: Return all the sentences from the news article with the given disease indications --Andric

# Assignment 5: Return all the sentences from the news article with the given deals info (?) -- Holy & Amanda

