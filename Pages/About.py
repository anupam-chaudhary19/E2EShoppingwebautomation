from Locators.locators import Locators

class About():
    Link_access_4items_xpath = Locators.Link_4items
    Link_About_xpath = Locators.Link_about
    Link_Try_it_free_xpath = Locators.Try_it_free
    Work_Email_name = Locators.w_name
    Work_un_name = Locators.w_name
    Work_pwd_name = Locators.w_name
    Signup_xpath = Locators.clicksignup

    def __init__(self, driver):
        self.driver = driver

    def Click_Access_4items(self):
        self.driver.find_element_by_xpath(self.Link_access_4items_xpath).click()

    def Click_About(self):
        self.driver.find_element_by_xpath(self.Link_About_xpath).click()

    def Click_try_it_free(self):
        self.driver.find_element_by_xpath(self.Link_Try_it_free_xpath).click()

    def enter_workemail(self, wemail):
        self.driver.find_element_by_name(self.Work_Email_name).send_keys(wemail)

    def enter_username(self, uname):
        self.driver.find_element_by_name(self.Work_un_name).send_keys(uname)

    def enter_password(self, pwd):
        self.driver.find_element_by_name(self.Work_pwd_name).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.Signup_xpath).click()



