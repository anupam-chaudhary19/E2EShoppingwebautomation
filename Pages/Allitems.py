from Locators.locators import Locators

class Allitems():
    Link_access_4items_xpath = Locators.Link_4items
    Link_All_items_xpath = Locators.Link_allitems

    def __init__(self, driver):
        self.driver = driver

    def Click_All_items(self):
        self.driver.find_element_by_xpath(self.Link_All_items_xpath).click()

    def Click_Access_4items(self):
        self.driver.find_element_by_xpath(self.Link_access_4items_xpath).click()