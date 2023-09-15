from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np
import pandas as pd
import time

def scrape_jiomart(product_name):
    # Specify the path to your WebDriver executable (change this to your driver's path)
    driver_path = 'C:\webdrivers'
    # Create a WebDriver instance (for Chrome in this example)
    service = Service(executable_path="C:\webdrivers\chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to a webpage

    product_name=product_name.replace(" ","%20")
    URL = f"https://www.jiomart.com/search/{product_name}"
    driver.get(URL)


    # Find elements using various methods (e.g., by ID, by class name, by CSS selector, by XPath)
    product_details = driver.find_elements(By.CSS_SELECTOR, '.plp-card-details-name.line-clamp.jm-body-xs.jm-fc-primary-grey-80')
    prices = driver.find_elements(By.CSS_SELECTOR,'.plp-card-details-price')

    # Extract data from the elements

    d = {"Name of the Product":[],"SP":[], "MRP":[],}

    for element in product_details:
        d['Name of the Product'].append(element.text)


    for element in prices:
        l=element.text.split(" ")
        if(len(l)==1):
            sp_string=l[0]
            mrp_string=l[0]
        else:
            sp_string=l[0]
            mrp_string=l[1]
        if(mrp_string[0]=='('):
            d['SP'].append(sp_string)
            d['MRP'].append(sp_string)
        else:
            d['SP'].append(sp_string)
            d['MRP'].append(mrp_string)
        
    #Close the browser when done
    driver.quit()
    return d
