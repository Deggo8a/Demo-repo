## Import Statements 
from bs4 import BeautifulSoup
import os 
import csv
import requests 
import re
import pandas as pd
import json






## Function definition to get prices
def getProductPrices(soup):
    product_elements = soup.find_all('li', class_= re.compile(r'.ListingItemContainer.'))
    for pe in product_elements:
        getProductDetails(pe)
        
    return

def getProductDetails(product_details):
    product_name = product_details.find(attrs={"name": "aria-label" })
    product_price = product_details.find('div', re.compile(r'text__Text-sc.')).text
    print(product_name, product_price)
    
    return

 
## main stub

if __name__ == "__main__":
    
    headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
        }
    URL = "https://weedmaps.com/dispensaries/flavors-santa-cruz"
    page= requests.get(URL,headers=headers)
    
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    a_tags = soup.select('a[aria-label]')
    for tag in a_tags:
     print(tag.text.strip())
    a_tags = soup.findAll('a', attrs={"aria-label": True})


    a_tags = soup.findAll(lambda tag: tag.name == "a" and "aria-label" in tag.attrs)
    soup = BeautifulSoup(page.content, "html.parser")
    
    getProductPrices(soup)
    

    ## Creating the Data Frame


## Exporting the DataFrame as csv




