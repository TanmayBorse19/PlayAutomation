from playwright.sync_api import Page, expect


class autopractice:
    def __init__(self,page:Page):
        self.page=page

    #locator
        self.test_case=page.locator("(//button[text()='Test Cases'])[1]")
        self.testcase1=page.locator("//u[text()='Test Case 2: Login User with correct email and password']")

    def open(self):
        self.page.goto("https://automationexercise.com/")

    def click_test(self):
        self.test_case.click()

    def click_test1(self):
        self.testcase1.click()
