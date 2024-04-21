from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


mail_url = r"https://poczta.wp.pl/rejestracja"
tv_url = r"https://sweet.tv"
chromedriver_path = r"C:\Users\default.DESKTOP-E4TLVMN\Downloads\chromedriver.exe"

service = Service(chromedriver_path)
options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get(mail_url)

name = driver.find_element(By.ID, "name").send_keys("asd")
last_name = driver.find_element(By.ID, "lastName").send_keys("asd")
login = driver.find_element(By.ID, "login").send_keys("iytuiyuij1231da2afasjfna")
sex = Select(driver.find_element(By.ID, "sex")).select_by_value('K')
date = driver.find_element(By.ID, "date").send_keys(1)
month = Select(driver.find_element(By.ID, "month")).select_by_value('1')
year = driver.find_element(By.ID, "year").send_keys(2000)

time.sleep(3)

driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

time.sleep(3)

password = driver.find_element(By.ID, "password").send_keys("ASsda2e1SA215a1a1002@@")
password_repeat = driver.find_element(By.ID, "passwordRepeat").send_keys("ASsda2e1SA215a1a1002@@")
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

recovery_email = driver.find_element(By.ID, "recoveryEmail").send_keys("fanbayernu806@gmail.com")
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

time.sleep(3)
driver.find_element(By.ID, 'check-all').click()
driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

time.sleep(3)
driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

## login in
time.sleep(2)
driver.find_element(By.ID, "login").send_keys("iytuiyuij1231da2afasjfna@wp.pl")
driver.find_element(By.ID, "password").send_keys("ASsda2e1SA215a1a1002@@")
time.sleep(2)
submit = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[1]/form/button').click()

                                        


# sc-bcXHqe Buttons__Button-sc-g2fyk2-0 iGblCX gwugjh

# mail_address = driver.find_element(By.ID, "geny").text
# print(mail_address)
# driver.switch_to.new_window('tab')

# driver.get(tv_url)
# time.sleep(1)
# cookies = driver.find_element(By.CLASS_NAME, "cookie__popup-buttons-button").click()
# driver.find_element(By.CLASS_NAME, "main-page-eu__favorite-button").click()

# time.sleep (3)
# driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[3]/form/div[2]/div/input').send_keys(mail_address)

# driver.find_element(By.CLASS_NAME, "v-button__text").click()
