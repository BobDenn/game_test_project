import unittest
from appium import webdriver
from config.desired_caps import get_desired_caps
from page_objects.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from common.utils import load_test_data
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """加载测试数据"""
        cls.test_data = load_test_data()
    
    def setUp(self):
        """测试前准备"""
        desired_caps = get_desired_caps()
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        self.login_page = LoginPage(self.driver)
    
    def tearDown(self):
        """测试后清理"""
        if self.driver:
            self.driver.quit()
    
    def test_login_success(self):
        """测试登录成功"""
        # 从测试数据文件中获取账号密码
        account = self.test_data['login']['account']
        password = self.test_data['login']['password']
        
        self.login_page.login(account, password)
        time.sleep(2)  # 等待登录响应
        

if __name__ == '__main__':
    # 单元测试
    suite = unittest.TestLoader()
    suite.loadTestsFromTestCase(TestLogin)
    runner = unittest.TextTestRunner()
    runner.run(suite)