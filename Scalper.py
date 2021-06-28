from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
class PagePuller:
    def __init__(self, url) -> None:
        self.url=url
        self.driver = webdriver.Chrome("C:/Users/asadr/Documents/GitHub/GPUBot/chromedriver.exe",options=options)
        self.driver.get(url)
    def checkAvailability(self):
        addToCart = self.driver.find_element_by_class_name("addToCartButton")
        print(addToCart.get_attribute("class"))
        if ("disabled" in addToCart.get_attribute("class")):
            return False
        else:
            addToCart.click()
            return True
    def refresh(self):
        self.driver.refresh()
file = open("Links.txt", "r")
lines = file.readlines()
pages = []
for line in lines:
    page =PagePuller(line)
    pages.append(page)
while pages !=[]:
    found = []
    for page in pages:
        if page.checkAvailability():
            found.append(page)
        else:
            page.refresh()
    for page in found:
        pages.remove(page)
    time.sleep(0.3)
while True:
    time.sleep(5)