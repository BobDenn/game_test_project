import yaml
import os

def get_desired_caps():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file = os.path.join(current_dir, 'config.yaml')
    
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        
    desired_caps = {}
    desired_caps.update(data['device'])
    desired_caps.update(data['app'])
    
    return desired_caps
