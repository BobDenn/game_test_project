import logging
import time
import os

class Logger:
    def __init__(self):
        # 创建logger实例
        self.logger = logging.getLogger('game_test')
        self.logger.setLevel(logging.INFO)
        
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # 创建日志目录
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # 创建日志文件handler
        log_file = os.path.join(log_dir, f'test_{time.strftime("%Y%m%d")}.log')
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setFormatter(formatter)
        
        # 创建控制台handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # 添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
    def get_logger(self):
        return self.logger
