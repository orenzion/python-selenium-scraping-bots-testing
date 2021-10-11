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
the most common way to access html elements is through id, name and class name
we would want to use:
id
name
class   
'''


driver.get("https://www.techwithtim.net/")

# print the page title
print(driver.title)

# find the element which contains "s"
search = driver.find_element_by_name("s")
# type "test" in the search element
search.send_keys("test")
# press enter to perform the search
search.send_keys(Keys.RETURN)


# navigating to the search bar
# entering 'test'
# extracting the article summaries from the search results and printing them
try:
    main = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        summary = article.find_element_by_class_name("entry-summary")
        print(summary.text)
finally:
    driver.quit()
