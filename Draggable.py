Draggable:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=chrome_options)
browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
browser.maximize_window()
browser.get("https://jqueryui.com/draggable/")
browser.execute_script("window.scrollTo(0, 200)")
iframe = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.demo-frame')))
browser.switch_to.frame(iframe)
draggable = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'draggable')))
action = ActionChains(browser)
action.click_and_hold(draggable).move_by_offset(100, 50).release().perform()
sleep(3)
browser.quit()