from playwright.sync_api import sync_playwright
from pages.NEW_test import NewTest

def test_New_test():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()

        n=NewTest(page)
        n.open()
        n.fill_name("tanmay")
        n.fill_email("tanmay@123")
        n.fill_phone("123334")
        n.fill_address("madhapur")
        n.select_radio()
        n.select_checkbox()
        n.select_dropdowns("india")

        browser.close()
