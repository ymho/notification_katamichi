from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_binary

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = 'https://cp.toyota.jp/rentacar/'
driver.get(url)

carslist = driver.find_element(By.ID, "service-items-shop-type-start")
cars = carslist.find_elements(By.TAG_NAME, "li")

for car in cars:
    try:
        car.find_element_by_css_selector('.service-item__body.show-entry-end')
    except:
        print('==============================')
        print(car.text)

driver.quit()
