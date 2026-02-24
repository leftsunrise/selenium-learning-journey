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
browser.get("https://jqueryui.com/")
anchors = ['effect', 'addClass', 'animate', 'easing', 'hide', 'removeClass', 'show', 'switchClass', 'toggle', 'toggleClass']
for anchor in anchors:
    browser.get(f"https://jqueryui.com/{anchor}/")
    sleep(1)
    browser.refresh()
    browser.execute_script("window.scrollTo(0, 200)")
    iframe = browser.find_element(By.CLASS_NAME, 'demo-frame')
    browser.switch_to.frame(iframe)
    if anchor == anchors[0]:
        select = wait.until(EC.visibility_of_element_located((By.ID, 'effectTypes'))).send_keys("puff")
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button'))).click()
        sleep(3)

    elif anchor == anchors[1]:
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        run.click()
        sleep(3)
        run.click()
        sleep(3)
    elif anchor == anchors[2]:
        toggle = wait.until(EC.element_to_be_clickable((By.ID, 'button'))).click()
        sleep(3)
    elif anchor == anchors[3]:
        linear = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="graphs"]/div[6]'))).click()
        sleep(3)
        browser.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
        ease = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="graphs"]/div[30]'))).click()
        sleep(3)
    elif anchor == anchors[4]:
        select = wait.until(EC.visibility_of_element_located((By.ID, 'effectTypes'))).send_keys("size")
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button'))).click()
        sleep(3)
    elif anchor == anchors[5]:
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button'))).click()
        sleep(3)
    elif anchor == anchors[6]:
        select = wait.until(EC.visibility_of_element_located((By.ID, 'effectTypes'))).send_keys("drop")
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button'))).click()
        sleep(3)
    elif anchor == anchors[7]:
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        run.click()
        sleep(3)
        run.click
        sleep(3)
    elif anchor == anchors[8]:
        select = wait.until(EC.visibility_of_element_located((By.ID, 'effectTypes'))).send_keys("highlight")
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button'))).click()
        sleep(3)
    elif anchor == anchors[9]:
        run = wait.until(EC.element_to_be_clickable((By.ID, 'button')))
        run.click()
        sleep(3)
        run.click()
        sleep(3)