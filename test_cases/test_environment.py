import unittest
from appium import webdriver
from config.desired_caps import get_desired_caps

class TestEnvironment(unittest.TestCase):
    def test_environment_setup(self):
        """测试环境配置是否正确"""
        try:
            # 尝试启动driver
            desired_caps = get_desired_caps()
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            
            # 获取当前activity
            current_activity = driver.current_activity
            print(f"当前Activity: {current_activity}")
            
            # 获取页面源码
            page_source = driver.page_source
            print("页面源码获取成功")
            
            # 关闭driver
            driver.quit()
            
            self.assertTrue(True, "环境配置正确")
            
        except Exception as e:
            self.fail(f"环境配置错误: {str(e)}") 