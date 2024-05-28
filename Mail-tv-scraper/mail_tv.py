# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time


# mail_url = r"https://poczta.wp.pl/rejestracja"
# tv_url = r"https://sweet.tv"
# chromedriver_path = r"C:\Users\default.DESKTOP-E4TLVMN\Downloads\chromedriver.exe"

# input_login = "monitonisnvidia912"
# input_password = "ASsda2e1SA215a1a1002@@"
# recovery_email = "fanbayernu806@gmail.com"

# service = Service(chromedriver_path)
# options = webdriver.ChromeOptions()
# # options.add_argument("headless")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

# # open mail website
# driver.get(mail_url)

# # fill mail information
# name = driver.find_element(By.ID, "name").send_keys("asd")
# last_name = driver.find_element(By.ID, "lastName").send_keys("asd")
# login = driver.find_element(By.ID, "login").send_keys(input_login)
# sex = Select(driver.find_element(By.ID, "sex")).select_by_value('K')
# date = driver.find_element(By.ID, "date").send_keys(1)
# month = Select(driver.find_element(By.ID, "month")).select_by_value('1')
# year = driver.find_element(By.ID, "year").send_keys(2000)

# time.sleep(3)
# # submit
# driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

# time.sleep(3)

# # type login and password
# password = driver.find_element(By.ID, "password").send_keys(input_password)
# password_repeat = driver.find_element(By.ID, "passwordRepeat").send_keys(input_password)
# time.sleep(3)
# # submit
# driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

# # alternative mail
# recovery_email = driver.find_element(By.ID, "recoveryEmail").send_keys(recovery_email)
# time.sleep(3)
# # submit
# driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

# time.sleep(3)
# # approve requirements
# driver.find_element(By.ID, 'check-all').click()
# # submit
# driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

# time.sleep(3)
# # submit
# driver.find_element(By.CLASS_NAME, 'Buttons__Button-sc-g2fyk2-0').click()

# # login in to mailbox
# time.sleep(2)
# driver.find_element(By.ID, "login").send_keys(f"{input_login}@wp.pl")
# driver.find_element(By.ID, "password").send_keys(input_password)
# time.sleep(2)
# submit = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[1]/form/button').click()

# time.sleep(2)

# # switch to new tab
# driver.switch_to.new_window('tab')

# # open tv url
# driver.get(tv_url)
# time.sleep(2)
# # accept cookies
# cookies = driver.find_element(By.CLASS_NAME, "cookie__popup-buttons-button").click()
# # go to login window
# driver.find_element(By.CLASS_NAME, "main-page-eu__favorite-button").click()

# time.sleep(3)
# # signig up
# tv_login = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[3]/form/div[1]/div/input').send_keys(input_login)
# tv_password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[3]/form/div[2]/div/input').send_keys(input_password)

# driver.find_element(By.CLASS_NAME, "v-button__content").click()
# time.sleep(3)

# # switch to mail tab
# driver.switch_to.window(driver.window_handles[0])

# time.sleep(5)

# # get list of mails in mailbox
# list_of_mails = driver.find_elements(By.CLASS_NAME, "css-bvy6jp")
# for mail in list_of_mails:
#     if "SWEET.TV" in mail.find_element(By.CLASS_NAME, "css-1iyod7o").text:
#         mail.find_element(By.CLASS_NAME, "css-1iyod7o").click()
#         break

# time.sleep(2)
# # verify mail
# driver.find_element(By.XPATH, '//*[@id="gwpc94be52eh"]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table[1]').click()



# print(f"login: {input_login}\npassword: {input_password}")



# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

#chrome_options = ChromeOptions()
#chrome_options.add_argument("--disable-infobars")  # Optional: Disable info bars

service = ChromeService(r"C:\Users\default.DESKTOP-E4TLVMN\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service) #, options=chrome_options)


# your data
your_first_name = "Gamal"
your_last_name = "DoeLy"
your_username = "monitonisnvidia912" # gama1445pro@gmail.com // make sure to be unique
your_birthday = "02 3 1995" #dd m yyyy exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

try:
    driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

    first_name = driver.find_element(By.NAME, "firstName")
    last_name = driver.find_element(By.NAME, "lastName")

    first_name.clear()
    first_name.send_keys(your_first_name)

    last_name.clear()
    last_name.send_keys(your_last_name)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    wait = WebDriverWait(driver, 20)
    day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

    birthday_elements = your_birthday.split()

    month_dropdown = Select(driver.find_element(By.ID, "month"))
    month_dropdown.select_by_value(birthday_elements[1])

    day_field = driver.find_element(By.ID, "day")
    day_field.clear()
    day_field.send_keys(birthday_elements[0])

    year_field = driver.find_element(By.ID, "year")
    year_field.clear()
    year_field.send_keys(birthday_elements[2])

    gender_dropdown = Select(driver.find_element(By.ID, "gender"))
    gender_dropdown.select_by_value(your_gender)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    create_own_option = wait.until(EC.element_to_be_clickable((By.ID, "selectionc2")))
    create_own_option.click()

    create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
    username_field = driver.find_element(By.NAME, "Username")
    username_field.clear()
    username_field.send_keys(your_username)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    password_field.clear()
    password_field.send_keys(your_password)

    password_confirmation_field = driver.find_element(By.NAME, "PasswdAgain")
    password_confirmation_field.clear()
    password_confirmation_field.send_keys(your_password)

    next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
    next_button.click()

    # Skip add phone number
    skip_button_is_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    skip_button = driver.find_element(By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")
    skip_button.click()

    # Skip add recovery email
    skip_button_is_visible = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    skip_button = driver.find_element(By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")
    skip_button.click()

    next_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "VfPpkd-LgbsSe")))
    next_button.click()

    # Agree on Google's privacies
    agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
    agree_button.click()

    # Close the browser window at the end of your automation
    driver.quit()

    print("Your Gmail successfully created:\n{\ngmail: " + your_username + "@gmail.com\npassword: " + your_password + "\n}")


except Exception as e:
    # Close the browser window in case of failure
    driver.quit()
    print("Failed to create your Gmail, Sorry")
    print(e)


####

# Different mail registration website approach

####

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time


# chromedriver_path = r"C:\Users\default.DESKTOP-E4TLVMN\Downloads\chromedriver.exe"
# service = Service(chromedriver_path)
# options = webdriver.ChromeOptions()
# # options.add_argument("headless")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

# # recovery_email = "fanbayernu806@gmail.com"

# # your data
# your_first_name = "Odyn2012"
# your_last_name = "podmiotowsky"
# your_username = "monitonisnvidia912" # gama1445pro@gmail.com // make sure to be unique
# your_birthday = "02 3 1995" #dd m yyyy exp : 24 11 2003
# your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
# your_password = "ASsda2e1SA215a1a1002@@"
# recovery_email = "fanbayernu806@gmail.com"

# driver.get("https://mail.onmail.com/signup")
# time.sleep(4)
# driver.find_element(By.NAME, "email").send_keys(your_username)
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()


# driver.find_element(By.NAME, "password").send_keys(your_password)
# driver.find_element(By.NAME, "confirmPassword").send_keys(your_password)
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()


# driver.find_element(By.NAME, "firstName").send_keys(your_first_name)
# driver.find_element(By.NAME, "lastName").send_keys(your_last_name)

# dates = driver.find_elements(By.CLASS_NAME, "MuiListItemText-root")
# for i in range(len(dates)):
#     dates[i].click()
#     time.sleep(1)
#     driver.find_elements(By.XPATH, "//div[@tabindex='0']")[1].click()

# driver.find_element(By.ID, "acceptTerms").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/form/div/div[2]/div[2]/button').click()


# driver.find_element(By.NAME, "email").send_keys(recovery_email)
# driver.find_element(By.NAME, "confirmEmail").send_keys(recovery_email)
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()