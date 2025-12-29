from playwright.sync_api import sync_playwright
from pages.alert_automation import AlertMessage
from pages.toolsQA import ToolsQA


def test_alert():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        at=AlertMessage(page)
        at.open()
        at.click_element_alert()
        at.click_Alert_values()
        at.click_alert_button()
        at.alert_text()
        at.click_me_Alert()
      
        
        
