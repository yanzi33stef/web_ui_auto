from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """登录页"""

    # 元素定位：
    account_locator = (By.XPATH, "//input[@name='account']")
    pwd_locator = (By.XPATH, "//input[@name='pass']")
    button_locator = (By.XPATH, "//div[contains(@class, 'pt-login')]/a[text()='登录']")
    error_msg_locator = (By.XPATH, "//p[@class='error-tips']")
    user_locator = (By.XPATH, "//a[@id='user']")
    user_name_locator = (By.XPATH, "//img[contains(@title, '北京-臭臭-24期')]")

    def login(self, account, pwd):
        """登录"""
        url = 'https://www.ketangpai.com/Home/User/login.html'
        # 打开网址
        self.driver.get(url)

        # 输入账号
        self.driver.find_element(*self.account_locator).send_keys(account)
        # 输入密码
        self.driver.find_element(*self.pwd_locator).send_keys(pwd)
        # 点击登录
        self.driver.find_element(*self.button_locator).click()

    def get_account_ele(self):
        return self.driver.find_element(*self.account_locator)

    def get_pwd_ele(self):
        return self.driver.find_element(*self.pwd_locator)

    def get_login_button(self):
        return self.driver.find_element(*self.button_locator)

    def get_error_msg(self):
        return self.wait_ele_visible(self.error_msg_locator)

    def get_user_name(self):
        user_img = self.wait_ele_visible(self.user_locator)
        self.move_to_ele(user_img)

        user_name = self.wait_ele_visible(self.user_name_locator)

        return user_name
