from playwright.sync_api import sync_playwright
from pages.toolsQA import ToolsQA
from pages.toolsQA import TooolsQA1
from pages.toolsQA import ToolsQA2
from pages.toolsQA import ToolsQA3

def test_ToolsQA_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        test=ToolsQA(page)
        test.open()
        #test.element_option()
        test.click_textbox_icon()
        test.enter_full_name("Tanmay Pramod Borse")
        test.enter_email("tanmay2@67")
        test.enter_current_address("madhapure 500081 hyderabad telagana")
        test.enter_permanent_addres("kannad")

        browser.close()

def test_ToolsQA_form1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        test1=TooolsQA1(page)
        test1.open()
        #test1.click_element_icon()
        test1.select_checkbox_icon()
        test1.check_checkbox_square
        test1.select_expand()
        test1.open()
        #test1.click_element_icon()
        test1.select_radio_icon()
        test1.select_radiobutton()
        test1.open()
        test1.click_webtable()
        test1.click_button()
        test1.enter_input("tanmay")
        test1.enter_last("Borse")
        test1.enter_email("tanmay@123")
        test1.enter_age("30")
        test1.enter_salary("2000000")
        test1.enter_department("test Engineer")
        test1.enter_submit()
