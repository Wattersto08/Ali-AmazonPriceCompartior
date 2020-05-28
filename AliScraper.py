from Utils import ALI_Convertcost
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os        



URL = 'https://www.aliexpress.com/'
SCROLL_PAUSE_TIME = 0.5




def Scrape_Ali(product, pages):

    # Init Browser Window
    browser = webdriver.Chrome(os.getcwd()+'\\chromedriver')
    browser.get(URL)

    # Search for Product
    searchbar = browser.find_element_by_id('search-key')
    sleep(SCROLL_PAUSE_TIME)
    searchbar.send_keys(product)
    searchbar.send_keys(Keys.ENTER)

    #init lists
    prodname = []
    prodprice = []
    
    
    # Search Defined number of pages
    while True:
        if pages != 0:
            try:
                browser.get(browser.current_url + "&page=" + str(pages))
            except:
                break


        # allow browser to settle
        sleep(SCROLL_PAUSE_TIME)
        browser.execute_script("window.scrollTo(0, 15000)")
        sleep(1)
        # Search page for class names of product names and prices
        
        for i in browser.find_elements_by_class_name('item-title'):
            print(i.text)
            prodname.append(i.text)
        for k in browser.find_elements_by_class_name('price-current'):
            print(k.text)
            prodprice.append(k.text)

        # PROTO LINK RETURN 
        #for y in browser.find_elements_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li[1]/div/div[2]/div[1]/div[1]/a'):
        #    prodlink.append(y.get_attribute("href"))
        
        # Tick Page countdown
        pages = pages - 1

        # If Final page is reached return the lists and close the browser
        if pages == 0:
            return prodname, prodprice #, prodlink
            browser.quit()
            break
        # else print the page number being searched
        print('page %d Searched!'% pages)

        
        
   





#Scrape_Ali('micro SD', 5)
