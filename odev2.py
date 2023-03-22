from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_sauce:
    def test_invalid_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        usernameInput=driver.find_element(By.NAME,"user-name")
        passwordInput=driver.find_element(By.NAME,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button").click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"Error is : {errorMessage.text}")
        sleep(10)

    def test_none_password(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        usernameInput=driver.find_element(By.NAME,"user-name")
        passwordInput=driver.find_element(By.NAME,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button").click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"Error is : {errorMessage.text}")
        sleep(10)

    def test_lockedUser_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        usernameInput=driver.find_element(By.NAME,"user-name")
        passwordInput=driver.find_element(By.NAME,"password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button").click()
        sleep(2)
        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"Error is : {errorMessage.text}")
        sleep(10)

    def test_errorBtn_click(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        usernameInput=driver.find_element(By.NAME,"user-name")
        passwordInput=driver.find_element(By.NAME,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button").click()
        sleep(2)
        ErrorBtn=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()
        sleep(20)

    def test_inventory_login(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        usernameInput=driver.find_element(By.NAME,"user-name")
        passwordInput=driver.find_element(By.NAME,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button").click()
        sleep(10)

    def test_itemCount(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        sleep(2)
        usernameInput=driver.find_element(By.NAME,"user-name")
        passwordInput=driver.find_element(By.NAME,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button").click()
        sleep(2)
        itemCount=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Item count is : {(itemCount)}")
        sleep(10)


testClass=Test_sauce()
testClass.test_itemCount()
while True:
    continue

