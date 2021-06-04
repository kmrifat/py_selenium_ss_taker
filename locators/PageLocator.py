from selenium.webdriver.common.by import By


class PageLocator(object):
    EMAIL_ADDRESS = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[1]/input')
    PASSWORD = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[2]/input')
    LOGIN_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/form/div[5]/button')
    BUILD_WEBSITE_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[6]/div/div[1]/div[2]/a')

    TMP_LIVE_PAGE_BTN = (By.XPATH,
                         '/html/body/div[1]/div[2]/div[1]/div[6]/div/div[2]/div/form/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/a')
