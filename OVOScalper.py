from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, datetime

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument("--incognito")

OVOLOGIN=""
OVOPASSWORD=""
CARDNUM=""
CARDNAME=""
EXPDATE=""
SECURITYCODE=""
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"
driver = webdriver.Chrome(desired_capabilities=caps,executable_path="chromedriver.exe",options=options)
mainpage = "https://ca.octobersveryown.com/collections/new-arrivals"
loginpage= "https://ca.octobersveryown.com/account/login"
driver.get(loginpage)
dropdate = datetime.datetime(2021, 8,20,12,0,0)
#dropdate= datetime.datetime(2021, 8,19,21,55,59)
driver.implicitly_wait(10)
while datetime.datetime.now() <= dropdate:
    #print(dropdate- datetime.datetime.now())
    time.sleep(0.1)
productUrl = "https://ca.octobersveryown.com/collections/ovo-uoft/products/f21-ovo-x-uoft-varsity-jacket"
#productUrl = "https://ca.octobersveryown.com/collections/new-arrivals/products/s21-ovo-x-avanti-twill-short-slate"
driver.get(productUrl)
sizeDropdown = driver.find_element_by_class_name("variant-dropdown")
sizes = sizeDropdown.find_elements_by_tag_name("li")
driver.execute_script("arguments[0].click()", sizes[1])
print(sizeDropdown)
time.sleep(0.5) #Test how low to make this
addtocart=  driver.find_element_by_id("AddToCart")
addtocart.click()
time.sleep(1.25)
driver.get("https://ca.octobersveryown.com/cart")
# while driver.current_url !="https://ca.octobersveryown.com/cart":
#     time.sleep(1)
termsAC=  driver.find_element_by_id("agree_box")
driver.execute_script("arguments[0].click()", termsAC)
checkoutBox = driver.find_element_by_class_name("bag-bottom-section")
checkoutBox =checkoutBox.find_elements_by_tag_name("div")[3]
checkoutBox = checkoutBox.find_elements_by_tag_name("input")[0]
checkoutBox.click()
# cardbox = driver.find_element_by_name("content-box")
# for char in CARDNUM:
#     driver.find_element_by_id("number").send_keys(char)
# for char in CARDNAME:
#     driver.find_element_by_id("name").send_keys(char)
# for char in EXPDATE:
#     driver.find_element_by_id("expiry").send_keys(char)
# for char in SECURITYCODE:
#     driver.find_element_by_id("verification_value").send_keys(char)
# paybtn = driver.find_element_by_id("continue_button")
#paybtn.click()
time.sleep(10000)
def signin():
    driver.get("https://ca.octobersveryown.com/account/login")