from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


# Вказуємо шлях до драйвера
driver_path = r"D:\Geckodriver-Firefox\geckodriver.exe"

# # Вказуємо шлях до файла браузера Chrome
# chrome_binary_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Створюємо сервіс і опції для драйвера
service = Service(driver_path)
options = webdriver.FirefoxOptions()
# options.binary_location = chrome_binary_path
options.add_argument('--headless')

# Створюємо екземпляр драйвера, передаючи сервіс і опції
# with webdriver.Firefox(service=service) as drv:
with webdriver.Firefox(service=service, options=options) as drv:
    drv.get("https://quotes.toscrape.com/login")
    # Увага, методи expected_conditions as EC приймають кортежi (attrubute, value)
    # attribute -> ID, NAME, XPATH, CSS_SELECTOR, TAG_NAME, CLASS_NAME, LINK_TEXT
    # це страховка, щоб сторiнка завантажилася до кiнця -> з'являється вiкно введеня <password>
    WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.ID, "password")))
    username = drv.find_element(by=By.ID, value="username")
    password = drv.find_element(by=By.ID, value="password")

    username.send_keys("admin")
    password.send_keys("admin")

    button = drv.find_element(by=By.XPATH, value="/html//input[@class='btn btn-primary']")
    button.click()
    # це страховка, щоб сторiнка завантажилася до кiнця -> останнiм з'являється <footer>
    WebDriverWait(drv, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
    # в атрибутi <page_source> зберiгається уся html сторiнка
    # змiнна [html] -> цi данi можна вже напряму передавати у Beautifulsoup4
    html = drv.page_source
    links = drv.find_elements(by=By.TAG_NAME, value='a')
    [print(link.get_attribute('href')) for link in links]

    sleep(3)

# driver.quit()
