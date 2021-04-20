from Locators.locators import Locators

class Products():
    Tshirt_Link_Add_to_cart_id = Locators.Tshirtlink
    backpack_Link_Add_to_cart_id = Locators.Backpacklink
    bikelight_Link_Add_to_cart_id = Locators.Bikelightlink
    fleecejacket_Add_to_cart_id = Locators.Fleecejacketlink
    Onsie_Add_to_cart_id = Locators.Oncielink
    Tshirtred_Add_to_cart_id = Locators.Tshirtredlink
    Add_to_cart_xpath = Locators.Cart

    def __init__(self, driver):
        self.driver = driver


    def Tshirts_Addtocart(self):
        self.driver.find_element_by_id(self.Tshirt_Link_Add_to_cart_id).click()
        self.driver.find_element_by_id(self.Tshirtred_Add_to_cart_id).click()

    def Jacket_Addtocart(self):
        self.driver.find_element_by_id(self.fleecejacket_Add_to_cart_id).click()

    def Onsie_Addtocart(self):
        self.driver.find_element_by_id(self.Onsie_Add_to_cart_id).click()

    def Backpack_Addtocart(self):
        self.driver.find_element_by_id(self.backpack_Link_Add_to_cart_id).click()
        self.driver.find_element_by_id(self.bikelight_Link_Add_to_cart_id).click()

    def Click_Add_to_cart(self):
        self.driver.find_element_by_xpath(self.Add_to_cart_xpath).click()



