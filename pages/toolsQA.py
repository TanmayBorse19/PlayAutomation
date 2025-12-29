from playwright.sync_api import Page,expect

class ToolsQA:
    def __init__(self,page: Page):
        self.page = page

    #locators
        self.element_option=page.locator("//div[@class='card-body']/child::h5")
        self.textbox=page.locator("//span[text()='Text Box']")
        self.full_name_text=page.locator("//input[@placeholder='Full Name']")
        self.email=page.locator("//input[@placeholder='name@example.com']")
        self.current_address=page.locator("//textarea[@placeholder='Current Address']")
        self.permanent_address=page.locator("//textarea[@id='permanentAddress']")

    def open(self):
        self.page.goto("https://demoqa.com/text-box")

    def click_element_icon(self):
        self.element_option.click()

    def click_textbox_icon(self):
        self.textbox.click()

    def enter_full_name(self,full_name):
        self.full_name_text.fill(full_name)


    def enter_email(self,email):
        self.email.fill(email)

    def enter_current_address(self,current_address):
        self.current_address.fill(current_address)

    def enter_permanent_addres(self,permanent_address):
        self.permanent_address.fill(permanent_address)


class ToolsQA2:
    def __init__(self,page: Page):
        self.page=page

        #locator
        self.radiobutton_icon=page.locator("//span[text()='Radio Button']")
        self.select_radio_btn=page.locator("label[for='impressiveRadio']")
    
    def select_radio_icon(self):
        self.radiobutton_icon.click()


    def select_radiobutton(self):
        self.select_radio_btn.click()

class ToolsQA3:
    def __init__(self,page: Page):
        self.page=page

        #locator:
        self.Web_tables_button=page.locator("//span[text()='Web Tables']")
        self.add_button=page.locator("//button[@id='addNewRecordButton']")
        self.input_test_in_popup=page.locator("//input[@id='firstName']")
        self.input_last_name_inpopup=page.locator("//input[@id='lastName']")
        self.email_popup=page.locator("//input[@id='userEmail']")
        self.age_popup=page.locator("//input[@id='age']")
        self.salary_popup=page.locator("//input[@id='salary']")
        self.department_popup=page.locator("//input[@id='department']")
        self.submit_button=page.locator("//button[@id='submit']")


    def click_webtable(self):
        self.Web_tables_button.click()

    def click_button(self):
        self.add_button.click()

    def enter_input(self,fname):
        self.input_test_in_popup.fill(fname)

    def enter_last(self,lname):
        self.input_last_name_inpopup.fill(lname)

    def enter_email(self,Email):
        self.email_popup.fill(Email)

    def enter_age(self,Age):
        self.age_popup.fill(Age)

    def enter_salary(self,salary):
        self.salary_popup.fill(salary)

    def enter_department(self,department):
        self.department_popup.fill(department)

    def enter_submit(self):
        self.submit_button.click()



        
class TooolsQA1(ToolsQA,ToolsQA2,ToolsQA3):
    def __init__(self,page: Page):
        ToolsQA.__init__(self, page)
        ToolsQA2.__init__(self, page)
        ToolsQA3.__init__(self, page)
        self.page=page

        #locator
        self.checkbox_icon=page.locator("//span[text()='Check Box']")
        self.check_checkbox=page.locator("//span[@class=rct-checkbox']")
        self.expand_icon=page.locator("//button[@title='Toggle']")


    def select_checkbox_icon(self):
        self.checkbox_icon.click()

    def check_checkbox_square(self):
        self.check_checkbox.check()

    def select_expand(self):
        self.expand_icon.click()







