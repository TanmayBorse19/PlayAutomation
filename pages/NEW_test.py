from playwright.sync_api import Page,expect

class NewTest:
    
    def __init__(self,page:Page):
        self.page=page


        #locator

        self.enter_name=page.locator("//input[@placeholder='Enter Name']")
        self.enter_email=page.locator("//input[@placeholder='Enter EMail']")
        self.enter_phone=page.locator("//input[@placeholder='Enter Phone']")
        self.enter_address=page.locator("#textarea")
        self.radio_button=page.locator("//input[@value='male']")
        self.checkbox_day=page.get_by_role("checkbox",name="Sunday")
        self.country_dropdown=page.locator("//select[@id='country']")

    def open(self):
        self.page.goto("https://testautomationpractice.blogspot.com/")

    def fill_name(self,value):
        self.enter_name.fill(value)

    def fill_email(self,email):
        self.enter_email.fill(email)

    def fill_phone(self,phone):
        self.enter_phone.fill(phone)

    def fill_address(self,address):
        self.enter_address.fill(address)

    def select_radio(self):
        self.radio_button.click()

    def select_checkbox(self):
        self.checkbox_day.check()

    def select_dropdowns(self,value):
        self.country_dropdown.select_option(value)