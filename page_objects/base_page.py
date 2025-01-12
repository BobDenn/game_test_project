from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Logger
import os
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger().get_logger()
        
    def find_element(self, locator, timeout=10):
        """查找单个元素"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
            self.logger.error(f"未找到元素: {locator}, 错误: {str(e)}")
            self.take_screenshot()
            raise
            
    def click(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        element.click()
        
    def input_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        
    def take_screenshot(self):
        """截图"""
        screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                    'reports', 'screenshots')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
            
        screenshot_path = os.path.join(screenshot_dir, 
                                    f'screenshot_{int(time.time())}.png')
        self.driver.get_screenshot_as_file(screenshot_path)
        self.logger.info(f"截图保存在: {screenshot_path}")
