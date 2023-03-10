import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class testday17(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_HRM_8_MyInfo_1(self):
        #Add/update My Info(Positive)
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)

        #My_Info
        web.find_element(By.LINK_TEXT,"My Info").click()
        time.sleep(3)
        
        #First_name
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Mr.")

        #Middle_name
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys("World")
        
        #Last_name
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Wide")
        
        #Nickname
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL,"a")
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.DELETE)
        time.sleep(1)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input").send_keys("Dale")

        #Nationality
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[1]").click()
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[15]").click()
        time.sleep(3)
        
        #save
        web.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
        time.sleep(6)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")
    
    
    def test_HRM_8_MyInfo_2(self):
        #Input characters instead number(Negative)
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"My Info").click()
        time.sleep(3)
        
        #Contact_Details
        web.find_element(By.XPATH,"//a[normalize-space()='Contact Details']").click()
        time.sleep(2)
        
        #Home
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input").send_keys("negativetesting")
        #Mobile
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input").send_keys("negativetesting2")
        web.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(4)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/span")
        assert web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/span")
    
    def test_HRM_8_MyInfo_3(self):
        #Add Education
        
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"My Info").click()
        time.sleep(3)

        #Qualifications
        web.find_element(By.LINK_TEXT,"Qualifications").click()
        time.sleep(1)

        #Level
        web.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[3]/div[1]/div[1]/button[1]").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']").click()
        time.sleep(2)
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(1)
        #Institute
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[2]/div/div[2]/input").send_keys("Assurance University")
        #Major/Specialization
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[3]/div/div[2]/input").send_keys("Quality Assurance")
        #Year
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[4]/div/div[2]/input").send_keys("2015")
        #GPA/Score
        web.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']//form[@class='oxd-form']/div[1]/div/div[5]/div/div[2]/input").send_keys("3.50")
        #Start_Date
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("2018-05-24")
        #End_Date
        web.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys("2023-06-13")
        time.sleep(5)
        #Save
        web.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[2]")

    def test_HRM_8_MyInfo_4(self):
        #Delete Education
       
        #Pre-Condition
        web = self.browser
        web.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        web.maximize_window()
        time.sleep(3)
        web.find_element(By.NAME,"username").send_keys("Admin")
        web.find_element(By.NAME,"password").send_keys("admin123")
        web.find_element(By.XPATH,"//button[@type='submit']").send_keys(Keys.ENTER)
        time.sleep(3)
        web.find_element(By.XPATH,"//span[normalize-space()='My Info']").click()
        time.sleep(3)
        web.find_element(By.LINK_TEXT,"Qualifications").click()
        time.sleep(1)

        #Delete_Education
        web.find_element(By.XPATH,"//div[@class='orangehrm-edit-employee-content']//div//div[5]//div[1]//button[1]//i[1]").click()
        time.sleep(1)
        web.find_element(By.XPATH,"//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click()
        time.sleep(3)

        #Validation
        assert web.find_element(By.XPATH,"//*[@id='oxd-toaster_1']")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
