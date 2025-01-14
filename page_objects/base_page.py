from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Logger
import os
import time

class BasePage:
    """
    封装了常用页面操作方法，比如查找元素、点击、输入文本等
    """
    def __init__(self, driver):
        """
        初始化基础页面类
        """
        self.driver = driver
        self.logger = Logger().get_logger()
        # 获取实际设备分辨率
        window_size = self.driver.get_window_size()
        self.scale_width = window_size['width'] / 3200  # 基准宽度
        self.scale_height = window_size['height'] / 1440  # 基准高度
    
    def find_element(self, locator, timeout=10):
        """
        查找单个元素
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
            self.logger.error(f"未找到元素: {locator}, 错误: {str(e)}")
            self.take_screenshot()  # 出错时自动截图
            raise
    
    def click(self, locator):
        """
        点击元素
        """
        element = self.find_element(locator)
        element.click()
        self.logger.info(f"点击元素: {locator}")
    
    def input_text(self, locator, text):
        """
        输入文本
        """
        element = self.find_element(locator)
        element.clear()  # 清除现有文本
        element.send_keys(text)
        self.logger.info(f"输入文本: {text} 到元素: {locator}")
    
    def take_screenshot(self):
        """截图并保存"""
        screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                    'reports', 'screenshots')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        screenshot_path = os.path.join(screenshot_dir, f'screenshot_{int(time.time())}.png')
        self.driver.get_screenshot_as_file(screenshot_path)
        self.logger.info(f"截图保存在: {screenshot_path}")
    
    def get_scaled_coords(self, x, y):
        """按比例缩放坐标"""
        return (int(x * self.scale_width), int(y * self.scale_height))
    
    def tap_element(self, x, y, duration=100):
        """点击经过缩放的坐标"""
        scaled_x, scaled_y = self.get_scaled_coords(x, y)
        try:
            self.driver.tap([(scaled_x, scaled_y)], duration)
            self.logger.info(f"点击坐标: ({scaled_x}, {scaled_y})")
        except Exception as e:
            self.logger.error(f"点击失败: {str(e)}")
            self.take_screenshot()
            raise
