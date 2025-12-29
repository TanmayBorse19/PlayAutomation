from playwright.sync_api import Page, expect

class Seleniumbase:
    def __init__(self, page: Page):
        self.page = page
        
        
        self.input_field = page.locator("//input[@id='myTextInput']")
        self.input_textarea = page.locator("//textarea[@id='myTextarea']")
        self.prefeild_text = page.locator("//textarea[@name='textareaName']")
        self.click_button = page.locator("//button[@id='myButton']")
        self.checkbox = page.locator("//input[@id='checkBox2']")
        self.dropdwon = page.locator("//select[@id='mySelect']")

    def open(self):
        self.page.goto("https://seleniumbase.io/demo_page")

    def enter_input(self,name):
        self.input_field.fill(name)

    def input_textarea_field(self,textname):
        self.input_textarea.fill(textname)

    def predfeild_input(self,pretext):
        self.prefeild_text.fill(pretext)

    def button(self):
        self.click_button.click()

    def click_checkbox(self):
        self.checkbox.check()

    def select_dropdown(self,value):
        self.dropdwon.select_option(value)





    



