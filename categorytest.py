from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get("http://localhost:3000/")

waittime = 120

#click filter  button
driver.implicitly_wait(waittime)
link = driver.find_element_by_css_selector("#root > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-3 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-4 > a > span.MuiFab-label")
link.click()

#click Category button
driver.implicitly_wait(waittime)
element = driver.find_element_by_css_selector("#search_input")
action = ActionChains(driver)
action.drag_and_drop_by_offset(element,100,0)
action.perform()


#Selected one of Category
driver.implicitly_wait(waittime)
element2 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li:nth-child(1) > input")
action2 = ActionChains(driver)
action2.drag_and_drop_by_offset(element2,100,0)
action2.perform()


#Unselected one of Category
driver.implicitly_wait(waittime)
element3 = driver.find_element_by_css_selector("#multiselectContainerReact > div.optionListContainer.displayBlock > ul > li.option.selected.highlightOption.highlight > input")
action3 = ActionChains(driver)
action3.drag_and_drop_by_offset(element3,100,0)
action3.perform()



driver.implicitly_wait(waittime)
action.drag_and_drop_by_offset(element,200,0)
action.perform()