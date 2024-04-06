from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests


class RentalPlaces:
    def __init__(self):
        # Keep browser open so you can manually log out
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        # Add option to start Chrome in fullscreen mode
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.webpage_link = (
            "https://www.nobroker.in/property/rent/pune/Pune/?searchParam=W3sibGF0IjoxOC41ODczNjU5NTA4ODc4LCJsb24iOjczLjg3Njc5MTY2MTYxMDEsInBsYWNlSWQiOiJDaElKQVJGR1p5Nl93anNSUS1PZW5iOURqWUkiLCJwbGFjZU5hbWUiOiJQdW5lIiwic2hvd01hcCI6ZmFsc2V9XQ==&sharedAccomodation=1&accomodationType=SHARED_ROOM&tenantType=FEMALE&rent=0,10000&furnishing=SEMI_FURNISHED&bathroom=1")
        self.link_prefix = "https://www.nobroker.in"
        self.all_links = []
        self.all_addresses = []
        self.all_prices = []
        self.all_mobile_numbers = []
        self.form_link = "https://docs.google.com/forms/d/e/1FAIpQLScm0iqK-53xX6TZxFw8SHJYF0kn14STQm6YVSQBP9LF4n5qTg/viewform?usp=sf_link"
        self.submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        self.address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea'
        self.price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea'
        self.link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea'

    def scrap_webpage(self):
        response = requests.get(self.webpage_link)
        soup = BeautifulSoup(response.text, "html.parser")
        places_list = soup.select(".infinite-scroll-component div")
        for place in places_list:
            try:
                link = self.link_prefix + place.select_one("a")["href"]
                address = (place.find("meta", {"content": True, "itemprop": False}))["content"]
                price = (((place.find("meta", {"itemprop": "price"}))["content"]).split(" "))[1]
                self.all_links.append(link)
                self.all_addresses.append(address)
                self.all_prices.append(price)
            except:
                pass
        self.fill_out_form()

    def fill_out_form(self):
        for index in range(len(self.all_addresses)):
            self.driver.get(self.form_link)
            time.sleep(2)
            address = self.driver.find_element(By.XPATH, value=self.address_xpath)
            price = self.driver.find_element(By.XPATH, value=self.price_xpath)
            link = self.driver.find_element(By.XPATH, value=self.link_xpath)
            submit_button = self.driver.find_element(By.XPATH, value=self.submit_button_xpath)

            address.send_keys(self.all_addresses[index])
            price.send_keys(self.all_prices[index])
            link.send_keys(self.all_links[index])
            submit_button.click()


rent = RentalPlaces()
rent.scrap_webpage()
