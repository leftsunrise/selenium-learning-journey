from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=chrome_options)
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.maximize_window()
wait = WebDriverWait(browser, 10)
browser.get(f"https://jqueryui.com/position/")
sleep(1)
anchors = ['default', 'cycler']
for anchor in anchors:
    browser.get(f"https://jqueryui.com/position/#{anchor}")
    browser.refresh()
    browser.execute_script("window.scrollTo(0, 200)")
    iframe = browser.find_element(By.CLASS_NAME, 'demo-frame')
    browser.switch_to.frame(iframe)
    if anchor == anchors[0]:
        my_1 = wait.until(EC.visibility_of_element_located((By.ID, 'my_horizontal'))).send_keys("center")
        sleep(3)
        my_2 = wait.until(EC.visibility_of_element_located((By.ID, 'my_vertical'))).send_keys("bottom")
        sleep(3)
        at_1 = wait.until(EC.visibility_of_element_located((By.ID, 'at_horizontal'))).send_keys("center")
        sleep(3)
        at_2 = wait.until(EC.visibility_of_element_located((By.ID, 'at_vertical'))).send_keys("top")
        sleep(3)
        collision_1 = wait.until(EC.visibility_of_element_located((By.ID, 'collision_horizontal'))).send_keys("flipfit")
        sleep(3)
        collision_2 = wait.until(EC.visibility_of_element_located((By.ID, 'collision_vertical'))).send_keys("fit")
        sleep(3)
    elif anchor == anchors[1]:
        for i in range(5):
            previous = wait.until(EC.visibility_of_element_located((By.ID, 'previous'))).click()
            sleep(3)
        for i in range(5):
            next_btn = wait.until(EC.visibility_of_element_located((By.ID, 'next'))).click()
            sleep(3)