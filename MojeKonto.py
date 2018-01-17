from selenium import webdriver
browser=webdriver.Firefox(executable_path="C:\\Users\\polakowc\\PycharmProjects\\Zegarownia\\geckodriver.exe")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest

class MojeKonto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def testFailLogin_(self):
        driver = self.driver
        self.driver.get("https://zegarownia.pl/customer/account/login/")

        emailFieldId = "email"
        passFieldId = "pass"
        loginButtonId = "send2"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldId))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginButtonId))

        emailFieldElement.clear()
        passFieldElement.clear()
        loginButtonElement.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "advice-required-entry-email")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "advice-required-entry-pass")))

    def testLogin_(self):
        """
        Test login function successfully
        """
        driver = self.driver
        self.driver.get("https://zegarownia.pl/customer/account/login/")
        userName = "snowdogtest@mailinator.com"
        passWord = "Snowdog1"
        emailFieldId = "email"
        passFieldId = "pass"
        loginButtonId = "send2"
        logoutButtonId = "Wyloguj się"

        emailFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passFieldId))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginButtonId))

        emailFieldElement.clear()
        emailFieldElement.send_keys(userName)
        passFieldElement.clear()
        passFieldElement.send_keys(passWord)
        loginButtonElement.click()

        logoutButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(logoutButtonId))
        logoutButtonElement.click()

if __name__ == '__main__':
  unittest.main()