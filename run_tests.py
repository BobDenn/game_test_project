import unittest
import pytest
import time
import os

def run_tests():
    # 获取测试用例目录
    test_dir = os.path.join(os.path.dirname(__file__), 'test_cases')
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # 创建报告目录
    report_dir = os.path.join(os.path.dirname(__file__), 'reports', 'html_reports')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
        
    # 生成报告文件名
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_dir, f'test_report_{timestamp}.html')
    
    # 运行测试并生成报告
    pytest.main([
        test_dir,
        f'--html={report_file}',
        '--self-contained-html',
        '-v'
    ])
    
    print(f"\n测试报告已生成: {report_file}")

if __name__ == '__main__':
    run_tests()
