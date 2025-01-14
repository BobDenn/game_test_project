import os
import yaml
from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_data', 'elements', 'login_page.yaml')

        with open(config_path, 'r', encoding='utf-8') as f:
            self.elements = yaml.safe_load(f)['default']  # 使用默认分辨率的配置

    def input_account(self, account):
        """输入账号"""
        self.logger.info(f"输入账号: {account}")
        # 点击账号输入框
        self.driver.tap([(self.elements['account_input']['x'], self.elements['account_input']['y'])])
        
        # 输入账号
        for char in str(account):
            if char.isdigit():
                self.driver.press_keycode(int(char) + 7)
            

    def input_password(self, password):
        """输入密码"""
        self.logger.info(f"输入密码: {password}")
        # 点击密码输入框
        self.driver.tap([(self.elements['password_input']['x'], self.elements['password_input']['y'])])
        # 清除可能存在的文本
        self.driver.press_keycode(67)  # KEYCODE_DEL
        # 输入密码
        for char in str(password):
            if char.isdigit():
                self.driver.press_keycode(int(char) + 7)

    def click_confirm(self):
        """点击确认按钮"""
        self.logger.info("点击确认按钮")
        self.driver.tap([(self.elements['confirm_button']['x'], 
                        self.elements['confirm_button']['y'])])

    def login(self, account, password):
        """执行完整的登录操作"""
        self.input_account(account)
        self.input_password(password)
        self.click_confirm()

    