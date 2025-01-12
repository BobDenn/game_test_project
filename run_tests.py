import unittest
import time
import os
from HTMLTestRunner import HTMLTestRunner

def run_tests():
    # 获取测试用例目录
    test_dir = os.path.join(os.path.dirname(__file__), 'test_cases')
    # 发现测试用例
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    
    # 创建报告目录
    report_dir = os.path.join(os.path.dirname(__file__), 'reports', 'html_reports')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        
    # 生成报告文件名
    report_file = os.path.join(report_dir, f'test_report_{time.strftime("%Y%m%d_%H%M%S")}.html')
    
    # 运行测试并生成报告
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title='城池大作战自动化测试报告',
            description='测试用例执行情况'
        )
        runner.run(suite)

if __name__ == '__main__':
    run_tests()
