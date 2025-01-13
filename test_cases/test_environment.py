import unittest
from appium import webdriver
from config.desired_caps import get_desired_caps
from appium.options.android import UiAutomator2Options

class TestEnvironment(unittest.TestCase):
    def test_environment_setup(self):
        """Test if the environment is configured correctly"""
        try:
            # Get configuration
            desired_caps = get_desired_caps()
            print("Desired Capabilities:", desired_caps)
            
            # Create UiAutomator2Options object
            options = UiAutomator2Options()
            for key, value in desired_caps.items():
                options.set_capability(key, value)
            print("Options set successfully")
            
            # Connect to Appium server
            server_url = 'http://127.0.0.1:4723/wd/hub'
            print(f"Connecting to Appium server at: {server_url}")
            driver = webdriver.Remote(server_url, options=options)
            
            print("Connected to Appium server successfully")
            
            # Get and verify current activity
            current_activity = driver.current_activity
            print(f"Current Activity: {current_activity}")
            self.assertIsNotNone(current_activity, "Activity should not be None")
            
            # Verify package name
            current_package = driver.current_package
            print(f"Current Package: {current_package}")
            self.assertEqual(current_package, desired_caps['appPackage'], 
                            "Package name should match")
            
            # Get page source
            page_source = driver.page_source
            self.assertIsNotNone(page_source, "Page source should not be None")
            print("Page source retrieved successfully")
            
            # Close driver
            driver.quit()
            print("Driver closed successfully")
            
        except Exception as e:
            print(f"Error details: {str(e)}")
            self.fail(f"Environment configuration error: {str(e)}") 
