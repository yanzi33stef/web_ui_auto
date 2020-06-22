
import unittest
from ddt import ddt, data
from selenium import webdriver
from pages.login_page import LoginPage
from data.login_data import login_success, login_error_msg


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """打开浏览器"""
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # 设置隐式等待
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        """关闭浏览器"""
        cls.driver.quit()

    # @pytest.mark.parametrize('test_data', login_error_msg)
    @data(*login_error_msg)
    def test_login_error_msg(self, test_data):
        """测试登录账号或密码错误：{0}"""
        """
        1.打开浏览器
        2.输入错误的账号或密码
        3.点击登录
        """

        LoginPage(self.driver).login(test_data['account'], test_data['pwd'])
        actual = LoginPage(self.driver).get_error_msg().text

        self.assertEqual(test_data['expected'], actual)

    # @pytest.mark.jing
    # @pytest.mark.parametrize("test_data", login_success)
    @data(*login_success)
    def test_login_success(self, test_data):
        """登录成功"""

        LoginPage(self.driver).login(test_data['account'], test_data['pwd'])
        actual = LoginPage(self.driver).get_user_name()
        self.assertTrue(actual)

        # actual = self.driver.title
        # expected = test_data['expected']
        # self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
