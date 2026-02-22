element:1（text box)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
browser = webdriver.Chrome()
browser.get("https://demoqa.com/text-box")
browser.maximize_window()
browser.execute_script("window.scrollTo(0, 500)")
sleep(3)
element = browser.find_element(By.XPATH, ' //*[@id="userName"]').send_keys("SereneCoder")
element = browser.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys("13370699025@163.com")
element = browser.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys("NewYork")
element = browser.find_element(By.XPATH, '//*[@id="permanentAddress"]').send_keys("play_games")
sleep(3)
browser.find_element(By.ID, 'submit').click()


element:2(check box)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/checkbox")
browser.execute_script("window.scrollTo(0,500)")
sleep(3)
element_Toggle = browser.find_element(By.CSS_SELECTOR, 'button[title="Toggle"]')
element_Toggle.click()
sleep(2)
element_checkbox = browser.find_element(By.CLASS_NAME, 'rct-checkbox')
element_checkbox.click()
sleep(2)
element_all = browser.find_element(By.CSS_SELECTOR, 'button[title="Expand all"]')
element_all.click()
sleep(2)
element_collapse = browser.find_element(By.CSS_SELECTOR, 'button[title="Collapse all"]')
element_collapse.click()
sleep(2)

element:3(radio button)
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/radio-button")
browser.execute_script("window.scrollTo(0, 500)")
element = browser.find_element(By.CSS_SELECTOR, 'label[for="yesRadio"]')
element.click()
sleep(5)

element:4(web tables)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/webtables")
browser.execute_script("window.scrollTo(0, 500)")
element = browser.find_element(By.ID, "addNewRecordButton")
element.click()
sleep(2)
element_first = browser.find_element(By.ID, "firstName").send_keys("first")
sleep(2)
element_last = browser.find_element(By.ID, "lastName").send_keys("last")
sleep(2)
element_email = browser.find_element(By.ID, "userEmail").send_keys("email")
sleep(2)
element_age = browser.find_element(By.ID, "age").send_keys("age")
sleep(2)
element_salary = browser.find_element(By.ID, "salary").send_keys("salary")
sleep(2)
element_department = browser.find_element(By.ID, "department").send_keys("department")
sleep(2)
element_submit = browser.find_element(By.ID, "submit")
element_submit.click()
sleep(5)

element:4.1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/webtables")
browser.execute_script("window.scrollTo(0,400)")
searchBox = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "searchBox")))
searchBox.send_keys("searchBox")
sleep(3)

element：5(buttons)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/buttons")
browser.execute_script("window.scrollTo(0,400)")
doubleClickBtn = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'doubleClickBtn'))).click()
sleep(3)
rightClickBtn = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'rightClickBtn'))).context.click()
sleep(3)
BkUl = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Click Me"]'))).click()
sleep(3)

element:6(links)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/links")
browser.execute_script("window.scrollTo(0,500)")
Home = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR , 'a[href="https://demoqa.com"]'))).click()
sleep(3)
browser.back()
browser.execute_script("window.scrollTo(0,500)")
Home_GZ = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://demoqa.com"]'))).click()
sleep(3)
browser.back()
browser.close()

element:7（images)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import urllib.parse
import os
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/broken")
browser.execute_script("window.scrollTo(0, 500)")
img = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="/images/Toolsqa.jpg"]')))
broken_img = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img[src="/images/Toolsqa_1.jpg"]')))
valid_link = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Click Here for Valid Link'))).click()
sleep(3)
browser.back()
browser.execute_script("window.scrollTo(0, 500)")
valid_link = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Click Here for Broken Link'))).click()
sleep(3)

element:8(upload and download)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
chrome_options = Options()
user_data_dir = r'H:/素材文件夹/chrome_profile'  # 任意位置，会自动创建
chrome_options.add_argument(f'--user-data-dir={user_data_dir}')
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': r'H:\素材文件夹\download_file',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True,
})

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get("https://demoqa.com/upload-download")
browser.execute_script("window.scrollTo(0, 500)")
download_button = browser.find_element(By.ID, 'downloadButton').click()
sleep(10)
upload_button = browser.find_element(By.ID, 'uploadFile').send_keys("H:\A素材文件夹\音频\紧张")
sleep(5)

element:9（Dynamic Properties）
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/dynamic-properties")
browser.execute_script("window.scrollTo(0, 500)")
seconds = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'enableAfter'))).click()
sleep(3)
color_change = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'colorChange'))).click()
sleep(3)
visible = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'visibleAfter'))).click()
sleep(3)

forms:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/automation-practice-form")
browser.execute_script("window.scrollTo(0, 400)")
name = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'firstName'))).send_keys("SereneCoder")
lastname = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'lastName'))).send_keys("zuo")
userEmail = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'userEmail'))).send_keys("115932473@qq.com")
btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="gender-radio-1"]'))).click()
mobile = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'userNumber'))).send_keys("12718282983")
browser.execute_script("window.scrollTo(0, 400)")
WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'dateOfBirthInput'))).clear()
browser.find_element(By.ID, 'dateOfBirthInput').send_keys("12 Feb 2026")
browser.find_element(By.ID, 'dateOfBirthInput').send_keys(Keys.ESCAPE)
subjects = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'subjectsInput'))).send_keys("Panxm")
hobbies = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-3"]'))).click()
select_picture = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'uploadPicture'))).send_keys(r"H:\素材文件夹\download_file\sampleFile.jpeg")
current_address = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'currentAddress'))).send_keys("NewYork")
state_dropdown = browser.find_element(By.ID, 'state').click()
option = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH , "//*[contains(text(), 'NCR')]"))).click()
button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, 'submit'))).click()
sleep(5)

browser windows:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/browser-windows")
browser.execute_script("window.scrollTo(0,400)")
New_Tab = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'tabButton'))).click()
sleep(5)
window = browser.window_handles
browser.switch_to.window(window[0])
browser.execute_script("window.scrollTo(0,400)")
New_Window = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'windowButton'))).click()
sleep(5)
window = browser.window_handles
browser.switch_to.window(window[0])
browser.execute_script("window.scrollTo(0,400)")
massage = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'messageWindowButton'))).click()
sleep(5)

Alert:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/alerts")
browser.execute_script("window.scrollTo(0, 400)")
browser.find_element(By.ID, 'alertButton').click()
WebDriverWait(browser, 5).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.accept()
sleep(2)
appear = browser.find_element(By.ID, 'timerAlertButton').click()
WebDriverWait(browser, 10).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.accept()
sleep(3)
confirm = browser.find_element(By.ID, 'confirmButton').click()
WebDriverWait(browser, 5).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.accept()
sleep(3)
prompt_box = browser.find_element(By.ID, 'promtButton').click()
WebDriverWait(browser, 5).until(EC.alert_is_present())
alert = browser.switch_to.alert
alert.send_keys("SereneCoder")
alert.accept()
sleep(3)

frames:
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/frames")
browser.execute_script("window.scrollTo(0, 300)")
browser.switch_to.frame(0)
sleep(3)
browser.switch_to.default_content()
browser.switch_to.frame(1)
sleep(3)
browser.switch_to.parent_frame()
sleep(3)

nexted frames:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/nestedframes")
browser.execute_script("window.scrollTo(0, 400)")
browser.switch_to.frame(browser.find_element(By.XPATH, '//*[@id="frame1"]'))
sleep(3)
browser.switch_to.frame(browser.find_element(By.XPATH, '/html/body/iframe'))
sleep(3)
browser.switch_to.parent_frame()
sleep(3)

model dialogs:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/modal-dialogs")
browser.execute_script("window.scrollTo(0, 300)")
small_model = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'showSmallModal'))).click()
sleep(5)
browser.find_element(By.ID, 'closeSmallModal').click()
sleep(5)
large_model = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'showLargeModal'))).click()
sleep(5)
browser.find_element(By.ID, 'closeLargeModal').click()
sleep(5)

accordian:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/accordian")
browser.execute_script("window.scrollTo(0, 300)")

ipsum = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'section1Heading')))
ipsum.click()
sleep(3)
ipsum.click()
come_from = browser.find_element(By.ID, 'section2Heading')
come_from.click()
sleep(3)
come_from.click()
browser.execute_script("window.scrollTo(0, 300)")
use = WebDriverWait(browser, 5).until (EC.visibility_of_element_located((By.ID, 'section3Heading')))
use.click()
sleep(3)
use.click()

auto complete:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/auto-complete")
browser.execute_script("window.scrollTo(0, 300)")
browser.find_element(By.ID, 'autoCompleteMultipleInput').send_keys("red,yellow,green")
sleep(5)
browser.find_element(By.ID, 'autoCompleteSingleInput').send_keys("white")
sleep(5)

date picker:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/date-picker")
select_date = browser.find_element(By.ID, 'datePickerMonthYearInput')
select_date.clear()
select_date.send_keys("01/11/2025")
sleep(3)
date_and_time = browser.find_element(By.ID, 'dateAndTimePickerInput')
date_and_time.clear()
date_and_time.send_keys("April 2, 2025 19:00 PM")
sleep(3)

slider:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/slider")
browser.execute_script("window.scrollTo(0, 300)")
slider = browser.find_element(By.CSS_SELECTOR, 'input[type="range"]')
x_offset = 50
y_offset = 0
ActionChains(browser).drag_and_drop_by_offset(slider, x_offset, y_offset).perform()
sleep(10)

progress bar:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/progress-bar")
browser.execute_script("window.scrollTo(0, 200)")
start = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="startStopButton"]'))).click()
WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'progress'), "100%"))
sleep(10)
reset_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'resetButton'))).click()
sleep(5)

tabs:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://demoqa.com/tabs")
browser.execute_script("window.scrollTo(0, 200)")
what = browser.find_element(By.CSS_SELECTOR, '#demo-tab-what').click()
sleep(3)
origin = browser.find_element(By.CSS_SELECTOR, '#demo-tab-origin').click()
sleep(3)
origin = browser.find_element(By.CSS_SELECTOR, '#demo-tab-use').click()
sleep(3)

Dialog:
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
browser.get("https://jqueryui.com/dialog/")
browser.execute_script("window.scrollTo(0,200)")
iframe = browser.find_element(By.CSS_SELECTOR, '.demo-frame')
browser.switch_to.frame(iframe)
sleep(3)
dialog = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div/div[1]')))
x_offset = 50
y_offset = 50
ActionChains(browser).drag_and_drop_by_offset(dialog, x_offset, y_offset).perform()
sleep(3)
browser.execute_script("arguments[0].style.width = '200px'; arguments[0].style.height = '200px';", dialog)
sleep(3)
close = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="button"]'))).click()
sleep(3)