import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from config.desired_caps import get_desired_caps
import time

class TestGame(unittest.TestCase):
    def setUp(self):
        """每个测试用例执行前的设置"""
        desired_caps = get_desired_caps()
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
            
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        time.sleep(2)  # 等待应用启动
        
    def tearDown(self):
        """每个测试用例执行后的清理"""
        if self.driver:
            self.driver.quit()
            
    def test_game_launch(self):
        """测试游戏启动"""
        # 验证当前页面是否正确
        current_activity = self.driver.current_activity
        self.assertEqual(current_activity, "com.cocos.game.AppActivity")
        
        # 等待游戏加载
        time.sleep(5)
        
        # 获取页面源码，验证是否包含特定元素
        page_source = self.driver.page_source
        self.assertIn("com.game.sanguo", page_source)
        
    def test_game_login(self):
        """测试游戏登录"""
        # 等待游戏加载
        time.sleep(5)
        
        try:
            # 这里需要根据实际的元素定位来修改
            # 例如：查找登录按钮
            login_button = self.driver.find_element(AppiumBy.ID, "login_button")
            login_button.click()
            
            # 添加更多登录相关的测试步骤
            
        except Exception as e:
            self.fail(f"登录测试失败: {str(e)}")

if __name__ == '__main__':
    unittest.main() 