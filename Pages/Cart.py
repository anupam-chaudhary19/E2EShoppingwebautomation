from Locators.locators import Locators
from Locators.Globalvariables import Globalvar

class Cart():
    Checkout_Add_to_cart_id = Locators.Checkout
    Continueshopping_id = Locators.Continueshoppingid
    Removeprod_id = Locators.Removeproduct
    Checkout_Userdetails_fn_id = Locators.Userfn
    Checkout_Userdetails_ln_id = Locators.Userln
    Checkout_Userdetails_Zip_id = Locators.Zip
    Checkout_Continue_name = Locators.Checkoutname
    Checkout_Finish_id = Locators.Finishcall
    Checkout_Success_xpath = Locators.Checkoutsuccesstext

    def __init__(self, driver):
        self.driver = driver

    def Checkout(self):
        self.driver.find_element_by_id(self.Checkout_Add_to_cart_id).click()
        self.driver.find_element_by_id(self.Checkout_Userdetails_fn_id).send_keys(Globalvar.fn)
        self.driver.find_element_by_id(self.Checkout_Userdetails_ln_id).send_keys(Globalvar.ln)
        self.driver.find_element_by_id(self.Checkout_Userdetails_Zip_id).send_keys(Globalvar.zip)
        self.driver.find_element_by_name(self.Checkout_Continue_name).click()
        self.driver.find_element_by_name(self.Checkout_Finish_id).click()

    def Continueshopping_ID(self):
        self.driver.find_element_by_id(self.Continueshopping_id).click()

    def Remproduct(self):
        self.driver.find_element_by_id(self.Removeprod_id).click()

    def Checkout_Successtext_verify(self):
        self.driver.find_element_by_xpath(self.Checkout_Success_xpath)
