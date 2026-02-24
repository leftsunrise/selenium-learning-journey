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
browser.get(f"https://jqueryui.com/easing/")
sleep(1)
browser.refresh()
browser.execute_script("window.scrollTo(0, 200)")
iframe = browser.find_element(By.CLASS_NAME, 'demo-frame')
browser.switch_to.frame(iframe)
for i in range(1,33):
    easing = wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="graphs"]/div[{i}]')))
    sleep(3)
    browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", easing)
    sleep(1)
    easing.click()
    sleep(3)