from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
#If you don't want auto checkout leave these as is
#If you do want auto checkout put your login and password in between the quotes
# Example: BESTBUYLOGIN="MyLogin"
BESTBUYLOGIN=""
BESTBUYPASSWORD=""
class PagePuller:
    def __init__(self, url) -> None:
        self.url=url
        self.driver = webdriver.Chrome("chromedriver.exe",options=options)
        self.signIn()
        self.driver.get(url)
        self.addedToCart = self.checkedOut= False
    def signIn(self):
        if BESTBUYLOGIN != "":
            self.driver.get("https://www.bestbuy.ca/account/en-ca")
            time.sleep(0.3)
            for char in BESTBUYLOGIN:
                self.driver.find_element_by_id("username").send_keys(char)
            for char in BESTBUYPASSWORD:
                self.driver.find_element_by_id("password").send_keys(char)
            self.driver.find_element_by_class_name("signin-form-button").click()
            time.sleep(3)
    def checkAvailability(self):
        addToCart = self.driver.find_element_by_class_name("addToCartButton")
        if ("disabled" in addToCart.get_attribute("class")):
            return False
        else:
            addToCart.click()
            self.addedToCart= True
            if BESTBUYLOGIN !="":
                time.sleep(2)
                self.checkout()
            return True
    def checkout(self):
        if self.addedToCart:
            self.driver.find_element_by_class_name("viewCart").click()
            time.sleep(6)
            button = self.driver.find_element_by_class_name("continueToCheckout_3Dgpe")
            link = button.get_attribute("href")
            self.driver.get(link)
            self.driver.find_element_by_class_name("order-now").click()
            self.checkedOut= True
    def refresh(self):
        self.driver.refresh()
        self.url = self.driver.current_url
    def productPage(self):
        return page.driver.current_url.split("/")[4] == "product"
file = open("Links.txt", "r")
lines = file.readlines()

pages = []
for line in lines:
    page =PagePuller(line)
    pages.append(page)
while pages !=[]:
    found = []
    for page in pages:
        if page.productPage():
            if page.checkAvailability():
                found.append(page)
            else:
                page.refresh()
    for page in found:
        pages.remove(page)
    time.sleep(0.1)
while True:
    time.sleep(5)