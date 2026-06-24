from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mailosaur
from mailosaur.models import SearchCriteria
import time
import random
import re

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 40)
driver.get("https://authorized-partner.vercel.app/register?step=setup")
print("Successfully enter url")

#From mailosaur
server_id = "yourservrid"
api_key = "yourapikey"
email = f"test{int(time.time())}@{server_id}.mailosaur.net"
phone = "98" + str(random.randint(10000000, 99999999))
print(phone)
#1 Fill signup form

wait.until(
    EC.visibility_of_element_located((By.NAME, "firstName"))
).send_keys("Test")
driver.find_element(By.NAME, "lastName").send_keys("User")#lName
driver.find_element(By.NAME, "email").send_keys(email)#email
driver.find_element(By.NAME, "phoneNumber").send_keys(phone)#Phonenum
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Password123!")#pw
driver.find_element(By.XPATH, "//input[@name='confirmPassword']").send_keys("Password123!")#confirmPw
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Next')]"))).click()
print("filled all form")


#Connecting python with mailosaur
client = mailosaur.MailosaurClient("yourapikey")

#Finding email
criteria = SearchCriteria()
criteria.sent_to = email

message = client.messages.get(
    server_id,
    criteria,
    timeout=60000
)

print("Email received")

# To get message sent to the email
body = message.text.body
print(body)

# Extracting 6-digit OTP using regular exp
otp = re.search(r"\b\d{6}\b", body).group()
print("OTP:", otp)

otp_input = driver.find_element(By.CSS_SELECTOR, "input[data-input-otp='true']")
otp_input.click()
otp_input.send_keys(otp)
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Verify Code']").click()

#2 Agency details
wait.until(EC.visibility_of_element_located((By.NAME, "agency_name"))).send_keys("random")#name of agency
driver.find_element(By.NAME, "role_in_agency").send_keys("role")#role
driver.find_element(By.NAME, "agency_email").send_keys(email)#email
driver.find_element(By.NAME, "agency_website").send_keys("9website.com")#website
driver.find_element(By.NAME, "agency_address").send_keys("London")#add
driver.find_element(By.XPATH, "//button[@role='combobox']").click()#dropdown clicked
driver.find_element(By.XPATH, "//span[normalize-space()='Nepal']").click()#selected nepal
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()
print("successfully filled agency details")

#3 Professional exp
wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='Experience and Performance Metrics']")))
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@role='combobox' and .//span[text()='Select Your Experience Level']]"))
).click()#dropdown
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[./span[text()='1 year']]"))).click() #selected
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter an approximate number.']"))).send_keys("5")#no of stu
driver.find_element(By.NAME,"focus_area").send_keys("undergrad")#focus area
driver.find_element(By.NAME, "success_metrics").send_keys("10")#Success area
driver.find_element(By.XPATH, "//label[text()='Career Counseling']").click()#Check box
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))).click()
print("successfully filled prof exp details")

#4 Verification and Preference
wait.until(EC.presence_of_element_located((By.NAME, "business_registration_number"))).send_keys("1234")#reg num
wait.until(EC.element_to_be_clickable(
(By.XPATH, "//span[text()='Select Your Preferred Countries']"))
).click()#dropdown
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[./span[text()='Australia']]"))).click()# selected
driver.find_element(By.TAG_NAME, "body").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Vocational School']"))).click()#checkbox
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"C:\Users\A S P I R E 7\PyCharmMiscProject\image\images.jpg")#upload image
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()
print("successfully filled verification details")


# Assertion
exp_result = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='My Profile']")
    )
).text
actual_result = "My Profile"
assert actual_result == exp_result, "Failed"
print("Completed")
driver.quit()
