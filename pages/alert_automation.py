from playwright.sync_api import Page, expect

class AlertMessage:
    def __init__(self,page: Page):
        self.page=page

        #locator
        self.Alert_dropdown=page.locator("//div[@class='header-text' and normalize-space()='Alerts, Frame & Windows']")
        self.Alert_button=page.locator("//div[@class='element-list collapse show' ]/ul/li[2]/span[text()='Alerts']")
        self.click_me=page.locator("//div[@class='element-list collapse show' ]/ul/li[2]/span[text()='Alerts']")
        self.click_element=page.locator("(//div[@class='card-body']/child::h5)[1]")

    def open(self):
       self.page.goto("https://demoqa.com/")
        
    def click_Alert_values(self):
        self.Alert_dropdown.click()

    def click_alert_button(self):
        self.Alert_button.click()

    def click_me_Alert(self):
        self.click_me.click()

    def alert_text(self):
        self.page.on("dialog",lambda dialog:(print(dialog.message),dialog.accept()))

    def click_element_alert(self):
        self.click_element.click()

    