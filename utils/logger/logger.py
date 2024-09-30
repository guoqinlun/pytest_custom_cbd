import logging


class Logger:
    def __init__(self, log_file='app.log', log_level=logging.INFO, name='root'):
        self.log_file = log_file
        self.log_level = log_level

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 创建日志处理器，输出到文件
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setFormatter(formatter)

        # 创建日志处理器，输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # 获取根日志器并添加处理器
        #     获取日志记录器对象的函数
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.log_level)
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)
