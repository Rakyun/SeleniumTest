from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://localhost:3000/")

#If too fast, increase a value
waittime = 120

#click filter button
driver.implicitly_wait(waittime)
link = driver.find_element_by_css_selector("#root > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-3 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-12.MuiGrid-grid-md-4 > a > span.MuiFab-label")
link.click()

#slide the bar
driver.implicitly_wait(waittime)
element = driver.find_element_by_css_selector("#root > div:nth-child(2) > div.makeStyles-root-8 > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2 > div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-true > span > span.MuiSlider-thumb.MuiSlider-thumbColorPrimary")
action = ActionChains(driver)
action.drag_and_drop_by_offset(element,100,0)
action.perform()

driver.implicitly_wait(waittime)
action.drag_and_drop_by_offset(element,200,0)
action.perform()