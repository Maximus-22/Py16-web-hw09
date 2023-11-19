from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Вказуємо шлях до драйвера
driver_path = r"D:\Geckodriver-Firefox\chromedriver.exe"

# Вказуємо шлях до файла браузера Chrome
chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Створюємо сервіс і опції для драйвера
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path
options.add_argument('--headless')

# Створюємо екземпляр драйвера, передаючи сервіс і опції
with webdriver.Chrome(service=service, options=options) as drv:
    drv.get("https://quotes.toscrape.com/login")
    WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.ID, "password")))
    username = drv.find_element(by=By.ID, value="username")
    password = drv.find_element(by=By.ID, value="password")

    username.send_keys("admin")
    password.send_keys("admin")

    button = drv.find_element(by=By.XPATH, value="/html//input[@class='btn btn-primary']")
    button.click()
    WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
    html = drv.page_source     # -> цi данi можна вже напряму передавати у Beautifulsoup4
    links = drv.find_elements(by=By.TAG_NAME, value='a')
    [print(link.get_attribute('href')) for link in links]

    sleep(3)

# driver.quit()
