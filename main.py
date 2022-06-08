from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://edalnice.cz/en/bulk-purchase/index.html#/multi_eshop/batch')

driver.implicitly_wait(5)
# country=driver.find_element(By.ID,'react-select-2-input')
# country.send_keys('India')
# country.send_keys(Keys.RETURN)
with open('sample.csv') as file_obj:
    # Create reader object by passing the file
    # object to reader method
    reader_obj = csv.reader(file_obj)

    # Iterate over each row in the csv
    # file using reader object
    count = 0
    option_count=0
    for row in reader_obj:
        if (count > 0):
            country=driver.find_elements(By.CLASS_NAME,'react-select__input')
            country[count-1].send_keys(row[0])

            date = driver.find_elements(By.ID, 'valid-since-input')
            date[count-1].send_keys(row[1])

            license = driver.find_elements(By.CLASS_NAME, 'order-0')
            license[count - 1].send_keys(row[2])

            if row[3]:
                option = driver.find_element(By.ID, f'alternative_fuel_type_checkbox_{count-1}')
                driver.execute_script("arguments[0].click();", option)
                if row[3] == 'Biomethane':
                    gas = driver.find_element(By.ID, f'bio_methane_radio_array_option_{count-1}')
                    driver.execute_script("arguments[0].click();", gas)
                    option_count+=1
                elif row[3] == 'Natural Gas':
                    gas = driver.find_element(By.ID, f'natural_gas_radio_array_option_{count-1}')
                    driver.execute_script("arguments[0].click();", gas)
                    option_count+=1
            if row[4] == 'Annual':
                vignette = driver.find_element(By.ID, f'1Y2021_{count-1}')
                driver.execute_script("arguments[0].click();", vignette)
            elif row[4] == '30-day':
                vignette = driver.find_element(By.ID, f'30D2021_{count-1}')
                driver.execute_script(f"arguments[0].click();", vignette)
            elif row[4] == '10-day':
                vignette = driver.find_element(By.ID, f'10D2021_{count-1}')
                driver.execute_script(f"arguments[0].click();", vignette)
            if (count < 6):
                batch = driver.find_element(By.CLASS_NAME,'kit__button.btn.btn-danger')

                driver.execute_script(f"arguments[0].click();", batch)
        count += 1


# Code to be run after all batch information is filled

# next=driver.find_element(By.CLASS_NAME,'kit__button.w-100.btn.btn-primary')
# driver.execute_script("arguments[0].click();", next)
# main = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "kit__button.w-100.btn.btn-primary"))
# )
# driver.execute_script("arguments[0].click();", main)
# email = driver.find_element(By.ID, 'email-input')
# email.send_keys('sample@gmail.com')
# confirm = driver.find_element(By.ID, 'email-confirmation-input')
# confirm.send_keys('sample@gmail.com')
# confirm.send_keys(Keys.ENTER)
# payment = driver.find_element(By.ID, 'card_payment_radio_array_option')
# driver.execute_script("arguments[0].click();", payment)
# consent = driver.find_element(By.ID, '_termsAgreement-true')
# driver.execute_script("arguments[0].click();", consent)
# main = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "kit__button.w-100.btn.btn-primary"))
# )
# driver.execute_script("arguments[0].click();", main)
#
# card = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.ID, "cardnumber"))
# )
# card.send_keys('5422000180911025')
#
# validity=driver.find_element(By.ID,'expiry')
# validity.send_keys('05/25')
# cvv=driver.find_element(By.ID,'cvc')
# cvv.send_keys('913')
#
# submit=driver.find_element(By.ID,'pay-submit')
# driver.execute_script("arguments[0].click();", submit)
