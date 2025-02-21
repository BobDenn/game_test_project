import unittest
from appium import webdriver
from config.desired_caps import get_desired_caps
from page_objects.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from common.utils import load_test_data
import time
import os

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
        """测试登录功能"""
        try:
            time.sleep(10)
            template_image_path = "test_data/screenshots/login.png"
            self.assertTrue(self.login_page.wait_for_screen(template_image_path, timeout=15), "登录页面未成功加载！")

            account = self.test_data['login']['account']
            password = self.test_data['login']['password']
            self.login_page.login(account, password)

            time.sleep(25)  # 等待登录成功

            template_image_path = "test_data/screenshots/login_success.png"
            self.assertTrue(self.login_page.assert_login_success(template_image_path), "登录成功界面未匹配到，登录失败！")

            screenshot_path = "test_data/screenshots/current_screen.png"
            os.remove(screenshot_path)
        except Exception as e:
            self.login_page.capture_screenshot("login_failure")  # 如果出错，保存截图
            raise e    
    

if __name__ == '__main__':
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    runner = unittest.TextTestRunner()
    runner.run(suite)