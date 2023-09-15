import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np
import pandas as pd
import time

def scrape_bigbasket(product_name):
    # Specify the path to your WebDriver executable (change this to your driver's path)
    driver_path = 'C:\webdrivers'
    # Create a WebDriver instance (for Chrome in this example)
    service = Service(executable_path="C:\webdrivers\chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to a webpage

    product_name=product_name.replace(" ","+")
    URL = f"https://www.bigbasket.com/ps/?q={product_name}"
    driver.get(URL)
    time.sleep(5)

    # Find elements using various methods (e.g., by ID, by class name, by CSS selector, by XPath)
    product_details = driver.find_elements(By.XPATH, '//div[@qa="product_name" and contains(@class, "col-sm-12 col-xs-7 prod-name")]')
    prices = driver.find_elements(By.XPATH, '//div[@qa="price" and @class="po-markup"]')

    # Extract data from the elements

    d = {"Name of the Product":[],"Price":[], "Star Ratings":[], "No. of Ratings":[],"Seller Name":[]}

    for element in product_details:
        l=element.text.split("\n")
        if(len(l)==2):
            d['Seller Name'].append(l[0])
            d['Name of the Product'].append(l[1])
            d['Star Ratings'].append(np.nan)
            d['No. of Ratings'].append(np.nan)
        else:
            d['Seller Name'].append(l[0])
            d['Name of the Product'].append(l[1])
            d['Star Ratings'].append(l[2])
            d['No. of Ratings'].append(l[3])
        
    for element in prices:
        l=element.text.split("\n")
        if(len(l)==1):
            d['Price'].append(l[0].split(" ")[2])
        else:
            price_string=l[1]
            d['Price'].append(price_string.split(" ")[3])
            #price_string.split(" ")[1] contains MRP
        
    # Close the browser when done
    driver.quit()
    return d
