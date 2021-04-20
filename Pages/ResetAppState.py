from Locators.locators import Locators

class Reset():
    Link_access_4items_xpath = Locators.Link_4items
    Link_reset_app_state_xpath = Locators.Link_reset_app_state

    def __init__(self, driver):
        self.driver = driver

    def Click_Reset(self):
        self.driver.find_element_by_xpath(self.Link_reset_app_state_xpath).click()

    def Click_Access_4items(self):
        self.driver.find_element_by_xpath(self.Link_access_4items_xpath).click()