import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.desired_caps import get_desired_caps
import time

class TestLogin:  # 移除 unittest.TestCase
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """每个测试用例执行前的设置和之后的清理"""
        # 设置
        desired_caps = get_desired_caps()
        options = UiAutomator2Options()
        for key, value in desired_caps.items():
            options.set_capability(key, value)
            
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        time.sleep(5)  # 等待应用启动
        
        yield  # 这里是测试用例执行的地方
        
        # 清理
        if hasattr(self, 'driver'):
            self.driver.quit()
            
    def test_app_launch(self):
        """测试应用启动"""
        current_activity = self.driver.current_activity
        assert current_activity is not None, "应用未成功启动"
        print(f"当前Activity: {current_activity}")
        
    def test_app_title(self):
        """测试应用标题"""
        time.sleep(3)
        page_source = self.driver.page_source
        assert "城池大作战" in page_source, "未找到应用标题"

