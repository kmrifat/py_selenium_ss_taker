from locators.PageLocator import PageLocator
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def login(self):
        email = self.driver.find_element(*PageLocator.EMAIL_ADDRESS)
        email.send_keys('saidulalam6012@gmail.com')
        password = self.driver.find_element(*PageLocator.PASSWORD)
        password.send_keys('12345678')
        login_btn = self.driver.find_element(*PageLocator.LOGIN_BUTTON)
        login_btn.click()
        build_a_website_btn = self.driver.find_element(*PageLocator.BUILD_WEBSITE_BUTTON)
        build_a_website_btn.click()
        ddd = self.driver.find_element(*PageLocator.TMP_LIVE_PAGE_BTN)
        ddd.click()
