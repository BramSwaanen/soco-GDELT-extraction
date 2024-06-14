from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

class NewsExtractor:
    '''
    This object holds the url to an overview page of articles on a given news website.
    Params:
        - self.url (string) holds the url to the overview page;
        - self.site (string) identifies the specific website the overview url is from,
        possible values are 'foxnews', 'cnn', [TODO: add];
        - self.arts_url (list[string]) contains the urls to all relevant article web pages;
        - self.data (dict{datetime:(title,content,writer)}) identifies each article as produced
        at a certain datetime with associated title, content and writer.
    Functions:
        - list_articles();
        - get_arts_data() extracts for all web pages indicated by urls in self.arts_url their 
        specific datetime of publication, their title, content and writer and saves the results
        in self.data as dict({date:(title,content,writer)})
    '''

    def __init__(self, url:str, site:str):
        self.url = url
        self.site = site
        self.arts_url = []#should be replaced after debug by list_articles()
        self.data = {}#should be replaced after debug by get_arts_data()
    
    def __str__(self):
        return f'NewsExtractor object with data {self.data}'

    def list_articles(self):
        '''
        Extracts and saves all relevant article urls from the page indicated 
        by self.url in self.arts_url.
        '''
        # Load page
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(5)

        if self.site == "foxnews":
            # Code to click the load-more button on Fox News search results page
            for i in range(9):
                element = driver.find_element(By.CSS_SELECTOR, ".button.load-more")
                element.click()
                time.sleep(1)
            
            time.sleep(30)