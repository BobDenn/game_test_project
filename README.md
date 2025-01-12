# Game Test Project

An Appium automation test project for testing game application.

## Directory Structure
- config/: Configuration files
- test_cases/: Test case files
- page_objects/: Page object model files
- common/: Common utilities
- test_data/: Test data files
- reports/: Test reports and screenshots
- logs/: Log files

## Setup
1. Install requirements:
    ```
    pip install -r requirements.txt
    ```

2. Configure device capabilities in config/config.yaml

3. Run tests:
    ```
    python run_tests.py
    ```

## 项目结构特点
- 配置分离: 将所有配置信息放在config目录下，便于管理和修改
- POM模式: 使用Page Object Model模式，将页面元素和操作封装在page_objects目录下
- 测试分层:
    - test_cases: 存放具体测试用例
    - common: 存放公共方法
    - test_data: 存放测试数据
- 报告管理:
    - reports/screenshots: 存放测试过程的截图
    - reports/html_reports: 存放HTMLTestRunner生成的报告
- 日志管理: 单独的logs目录存放运行日志
---
如果有多个项目，会考虑使用虚拟环境管理项目依赖