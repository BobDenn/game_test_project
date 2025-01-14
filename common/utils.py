import yaml
import os

def load_test_data():
    """加载测试数据"""
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    yaml_file = os.path.join(current_dir, 'test_data', 'test_data.yaml')
    
    with open(yaml_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
