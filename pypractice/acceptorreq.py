import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)


url = "https://www.linkedin.com/mynetwork/"
driver.get(url)


while "1" != input("press 1 when signed in: "):
    pass

acceptBtn = driver.find_element_by_class_name("invitation-card_action-btn")
ariaLabel = acceptBtn.getAttribute("aria-label")
print(acceptBtn)
print(ariaLabel)
if(ariaLabel.startwith("Accept")):
    print(acceptBtn)
    acceptBtn.click()