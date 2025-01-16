import os
import yaml
from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cv2
import numpy as np


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
        time.sleep(0.5)
        # 输入账号
        for char in str(account):
            if char.isdigit():
                self.driver.press_keycode(int(char) + 7)
                time.sleep(0.2)
            else:
                self.logger.warning(f"不支持的字符: {char}")
            

    def input_password(self, password):
        """输入密码"""
        self.logger.info(f"输入密码: {password}")
        # 点击密码输入框
        self.driver.tap([(self.elements['password_input']['x'], self.elements['password_input']['y'])])
        time.sleep(0.5)
        # 输入密码
        for char in str(password):
            if char.isdigit():
                self.driver.press_keycode(int(char) + 7)
                time.sleep(0.2)
            else:
                self.logger.warning(f"不支持的字符: {char}")


    def click_confirm(self):
        """点击确认按钮"""
        self.logger.info("点击确认按钮")
        self.driver.tap([(self.elements['confirm_button']['x'], 
                        self.elements['confirm_button']['y'])])
        
    def wait_for_screen(self, template_image_path, timeout=10, interval=0.5):
        """
        等待登录页面
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            screenshot_path = "test_data/screenshots/current_screen.png"
            # 截图
            self.driver.get_screenshot_as_file(screenshot_path)
            # 读图
            img = cv2.imread(screenshot_path, 0)
            # 读模板
            template = cv2.imread(template_image_path, 0)
            template = cv2.resize(template, (3200, 1440))

            # 模板匹配
            res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            if (res >= 0.7).any():  # 匹配成功
                self.logger.info("目标界面已加载完成！")
                return True

            time.sleep(interval)

        self.logger.error("等待超时，目标界面未加载！")
        return False

    def assert_login_success(self, template_image_path):
        """
        检查登录是否成功
        """
        # 获取当前屏幕截图
        screenshot_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test_data', 'screenshots', 'current_screen.png')
        self.driver.get_screenshot_as_file(screenshot_path)

        # 读取模板图像
        img = cv2.imread(screenshot_path, 0)
        template = cv2.imread(template_image_path, 0) 
        template = cv2.resize(template, (3200, 1440))

        # 模板匹配
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.6)

        # 检查是否找到匹配
        if len(loc[0]) > 0:
            self.logger.info("登录成功界面匹配成功！")
            return True
        else:
            self.logger.error("登录成功界面未匹配到！")
            return False


    def login(self, account, password):
        """执行完整的登录操作"""
        self.input_account(account)
        self.input_password(password)
        self.click_confirm()

    