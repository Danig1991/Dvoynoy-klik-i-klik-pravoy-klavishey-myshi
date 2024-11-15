import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://demoqa.com/buttons"

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# расширение класса
action = ActionChains(driver_chrome)

# произвести двойной клик
double_click_button = driver_chrome.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click_button).perform()
print("Двойной клик.")

time.sleep(1)

# произвести клик правой клавишей
right_click_button = driver_chrome.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click_button).perform()
print("Клик правой клавишей.")