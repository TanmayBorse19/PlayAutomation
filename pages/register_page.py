from playwright.sync_api import Page, expect

class RegisterPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.first_name = page.locator('input[placeholder="First Name"]')
        self.last_name = page.locator('input[placeholder="Last Name"]')
        self.address = page.locator("textarea[ng-model='Adress']")
        self.email = page.locator("input[type='email']")
        self.phone = page.locator("input[type='tel']")
        self.male_radio = page.locator("input[value='Male']")
        self.skills_dropdown = page.locator("#Skills")

    # Actions
    def open(self):
        self.page.goto("https://demo.automationtesting.in/Register.html")

    def enter_first_name(self, name):
        self.first_name.fill(name)

    def enter_last_name(self, name):
        self.last_name.fill(name)

    def enter_address(self, address):
        self.address.fill(address)

    def enter_email(self, email):
        self.email.fill(email)

    def enter_phone(self, phone):
        self.phone.fill(phone)

    def select_gender_male(self):
        self.male_radio.check()

    def select_skill(self, skill):
        self.skills_dropdown.select_option(skill)

    # Validations
    def verify_first_name(self, expected):
        expect(self.first_name).to_have_value(expected)

    def verify_gender_male_selected(self):
        expect(self.male_radio).to_be_checked()