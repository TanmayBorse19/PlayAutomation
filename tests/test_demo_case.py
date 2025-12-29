from playwright.sync_api import sync_playwright
from pages.new_demo import autopractice

def test_auto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        a=autopractice(page)
        a.open()
        a.click_test()
        a.click_test1()