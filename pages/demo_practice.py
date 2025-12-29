from playwright.sync_api import sync_playwright

def test_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.automationtesting.in/Register.html")
        #page.locator('input[placeholder="First Name"]').wait_for()
        page.locator('input[placeholder="First Name"]').fill("Tanmay")
        #page.locator('input[placeholder="Last Name"]').wait_for()
        page.locator('input[placeholder="Last Name"]').fill("Borse")
        #page.locator("//textarea[@ng-model='Adress']").wait_for()
        page.locator("//textarea[@ng-model='Adress']").fill("Madhapur Hyderabad")
        #page.locator("//input[@type='email']").wait_for()
        page.locator("//input[@type='email']").fill("tanmay@2344")
        #page.locator("//input[@type='tel']").wait_for()
        page.locator("//input[@type='tel']").fill("123456")
        page.locator("//select[@id='Skills']").select_option("Python")
        page.locator("//input[@value='Male']").check()
        
        
        
test_google()