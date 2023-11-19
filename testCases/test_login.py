import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.configtest import setup
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_001_login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username="admin@yourstore.com"
    # password= "admin"

    baseURL = readConfig.getApplicationUrl()
    username= readConfig.getUsername()

    password= readConfig.getpassword()

    # stroing the value of logger in logger variable
    logger = LogGen.loggen()

    #Note:We use self keyword in order to use the variable that belongs to the same class.
    def test_homepageTitle(self):
        self.logger.info("****************** Test_001_Login*****************************")
        self.logger.info("********************** Verifying Home page title ********************* ")
        self.driver = webdriver.Chrome()
        # alternate way instead of defining everytime just use setup in the value
        # self.driver = setup
        self.driver.get(self.baseURL)
        act_title= self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************** Home page title is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("****************** Home page title is failed *****************")

            assert False

    def test_login(self):
        self.logger.info("********************** Verifying login test ********************* ")

        # self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title= self.driver.title
        if act_title== "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********************** Login test is passed ********************* ")


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********************** Login test is failed ********************* ")

            assert False




