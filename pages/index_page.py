from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage(BasePage):
    """首页"""

    # 元素定位:
    index_add_course_up_locator = (By.XPATH, "//div[contains(@class, 'ktcon1l')]")
    index_add_course_down_locator = (By.XPATH, "//p[text()='加入课程']")
    add_course_code_locator = (By.XPATH, "//div[@class='chuangjiankccon']/input[@type='text']")
    add_course_ok_btn_locator = (By.XPATH, "//li[@class='cjli2']/a[@class='btn btn-positive']")
    add_course_cancel_locator = (By.XPATH, "//a[@class='btn btn-defalut']")
    toast_locator = (By.XPATH, "//div[@id='error-tip']")
    course_title_locator = (By.XPATH, "//a[@title='jmeter赠送性能9期']")

    def get_course_title(self):
        return self.driver.find_element(*self.course_title_locator)

    def get_index_add_course_up_btn(self):
        """加入课程"""
        return self.driver.find_element(*self.index_add_course_up_locator)

    def get_index_add_course_down_btn(self):
        return self.driver.find_element(*self.index_add_course_down_locator)

    def get_add_course_code(self):
        """课程名称"""
        return self.driver.find_element(*self.add_course_code_locator)

    def get_add_course_ok_btn(self):
        """确定"""
        # return self.driver.find_element(*self.add_course_ok_btn_locator)
        return self.wait_ele_visible(self.get_add_course_ok_btn())
        # return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.get_add_course_ok_btn()))

    def get_add_course_cancel_btn(self):
        """取消"""
        return self.driver.find_element(*self.add_course_cancel_locator)

    def get_toast(self):
        return self.wait_ele_visible(self.toast_locator)

    def add_course_up(self, course_code):
        self.get_index_add_course_up_btn().click()
        self.get_add_course_code().send_keys(course_code)
        self.driver.find_element(*self.add_course_ok_btn_locator).click()

    def add_course_down(self, course_code):
        self.get_index_add_course_down_btn().click()
        self.get_add_course_code().send_keys(course_code)
        self.driver.find_element(*self.add_course_ok_btn_locator).click()
