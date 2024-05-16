from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')
options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)


driver.execute_script("window.open('https://gptchatly.com/', '_blank')")
driver.switch_to.window(driver.window_handles[1])

time.sleep(5)

while True:
    driver.switch_to.frame(0)
    driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div/label/input').click()
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)
    actions.move_by_offset(x, y)  
    actions.perform()
    time.sleep(random.uniform(0, 1)) 

# driver.close()