from Locators.locators import Locators

class Logout():
    Link_access_4items_xpath = Locators.Link_4items
    Link_logout_xpath = Locators.Link_logout

    def __init__(self, driver):
        self.driver = driver

    def Click_logout(self):
        self.driver.find_element_by_xpath(self.Link_logout_xpath).click()

    def Click_Access_4items(self):
        self.driver.find_element_by_xpath(self.Link_access_4items_xpath).click()
