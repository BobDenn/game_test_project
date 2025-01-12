import unittest
from appium import webdriver
from config.desired_caps import get_desired_caps
from page_objects.login_page import LoginPage
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化driver
        desired_caps = get_desired_caps()
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
    def setUp(self):
        self.login_page = LoginPage(self.driver)
        
    def test_login_success(self):
        """测试登录成功"""
        self.login_page.login("test_user", "test_password")
        time.sleep(2)  # 等待登录完成
        # 这里添加登录成功的断言
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
