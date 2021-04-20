from selenium import webdriver
from Locators.locators import Locators


class login():
    textbox_username_id = Locators.username_id
    textbox_password_id = Locators.password_id
    button_login_id = Locators.login_id

    def __init__(self, driver):
        self.driver = driver

    def enterusername(self, un):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(un)

    def enterpassword(self, pwd):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(pwd)

    def Login(self):
        self.driver.find_element_by_id(self.button_login_id).click()