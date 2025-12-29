from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage

def test_register_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        register = RegisterPage(page)

        register.open()
        register.enter_first_name("Tanmay")
        register.enter_last_name("Borse")
        register.enter_address("Hyderabad")
        register.enter_email("tanmay@test.com")
        register.enter_phone("9876543210")
        register.select_gender_male()
        register.select_skill("Python")

        register.verify_first_name("Tanmay")
        register.verify_gender_male_selected()

        browser.close()