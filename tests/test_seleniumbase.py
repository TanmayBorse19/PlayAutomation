from playwright.sync_api import sync_playwright
from pages.seleniumbase_page import Seleniumbase

def test_seleniumbase_from():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        selenium=Seleniumbase(page)


        selenium.open()
        selenium.enter_input("tanmay")
        selenium.input_textarea_field("Borse")
        selenium.predfeild_input("love")
        selenium.button
        selenium.click_checkbox()
        selenium.select_dropdown("Set to 25%")

        browser.close()

