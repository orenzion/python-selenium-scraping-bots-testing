import time
from selenium import webdriver
# this will give us accesss to elements in the keyboard so that we can perform automations
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


'''
this tutorial is about page navigation and clicking elements

the most common way to access html elements is through id, name and class name
we would want to use:
id
name
class   
'''


driver.get("https://www.techwithtim.net/")


link = driver.find_element_by_link_text("Python Programming")
