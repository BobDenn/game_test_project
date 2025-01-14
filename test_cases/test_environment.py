import unittest
from appium import webdriver
from config.desired_caps import get_desired_caps
from appium.options.android import UiAutomator2Options

class TestEnvironment(unittest.TestCase):
    def test_environment_setup(self):
        """测试环境是否正确配置"""
        try:
            # 获取配置
            desired_caps = get_desired_caps()
            print("期望的配置参数:", desired_caps)
            
            # 创建 UiAutomator2Options 对象
            options = UiAutomator2Options()
            for key, value in desired_caps.items():
                options.set_capability(key, value)
            print("配置参数设置成功")
            
            # 连接 Appium 服务器
            server_url = 'http://127.0.0.1:4723/wd/hub'
            print(f"正在连接 Appium 服务器: {server_url}")
            driver = webdriver.Remote(server_url, options=options)
            
            print("成功连接到 Appium 服务器")
            
            # 获取并验证当前活动页面
            current_activity = driver.current_activity
            print(f"当前活动页面: {current_activity}")
            self.assertIsNotNone(current_activity, "活动页面不应为空")
            
            # 验证包名
            current_package = driver.current_package
            print(f"当前包名: {current_package}")
            self.assertEqual(current_package, desired_caps['appPackage'], "包名应该匹配")
            
            # 获取页面源代码
            page_source = driver.page_source
            self.assertIsNotNone(page_source, "页面源代码不应为空")
            print("成功获取页面源代码")
            
            # 关闭驱动
            driver.quit()
            print("驱动已成功关闭")
            
        except Exception as e:
            print(f"错误详情: {str(e)}")
            self.fail(f"环境配置错误: {str(e)}") 
