from .base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class LoginPage(BasePage):
    # 定位器
    ACCOUNT_INPUT = (MobileBy.ID, "com.your.game.package:id/account_input")
    PASSWORD_INPUT = (MobileBy.ID, "com.your.game.package:id/password_input")
    LOGIN_BUTTON = (MobileBy.ID, "com.your.game.package:id/login_button")
    
    def login(self, username, password):
        """登录方法"""
        self.logger.info(f"正在使用账号 {username} 登录")
        self.input_text(self.ACCOUNT_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
