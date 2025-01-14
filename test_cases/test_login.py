import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.desired_caps import get_desired_caps
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        """每个测试用例执行前的设置"""
        desired_caps = get_desired_caps()
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        time.sleep(5)  # 等待游戏启动
        
    def tearDown(self):
        """每个测试用例执行后的清理"""
        if self.driver:
            self.driver.quit()
            
    def test_login_page(self):
        """测试登录页面是否正确加载"""
        try:
            # 获取当前页面源码
            page_source = self.driver.page_source
            print("页面源码:", page_source)
            
            # 这里可以添加登录页面的验证
            # 比如检查是否存在登录按钮等元素
            
            self.assertTrue(True, "登录页面加载成功")
        except Exception as e:
            self.fail(f"登录页面测试失败: {str(e)}")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    test_cases = [
        TestLogin('test_login_page')
        #TestLogin('other_test_method')
    ]
    suite.addTests(test_cases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

