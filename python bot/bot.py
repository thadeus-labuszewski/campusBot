from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def order():

    # Connect to website
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://campvs.com/profile/OPTIX')
    time.sleep(2)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
    
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")

    # Press heart button
    driver.find_element_by_xpath('//*[@id="col_352517432"]/div/div[3]/div[3]/button').click()

    time.sleep(2)

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
    
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")


        time.sleep(2)  

     # Enter email
    driver.find_element_by_xpath('//*[@id="email-input"]').send_keys("test@gmail.com")

    # Submit vote
    driver.find_element_by_xpath('//*[@id="vote-submit-button"]').click()
   
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')
    
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")

    # Close driver
    driver.close()

def accept():

if __name__ == '__main__':
    order()