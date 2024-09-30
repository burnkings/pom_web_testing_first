import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler  # 确保正确导入


class Logs:
    LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), 'log_file')
    LOG_FORMAT = '[%(asctime)s] %(levelname)s %(name)s(%(lineno)d): %(message)s'
    LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    LOG_LEVEL = logging.INFO
    BACKUP_COUNT = 0
    _logger = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.ensure_log_directory()

    @classmethod
    def ensure_log_directory(cls):
        if not os.path.exists(cls.LOG_DIRECTORY):
            os.makedirs(cls.LOG_DIRECTORY)

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            try:
                cls.ensure_log_directory()
                log_path = os.path.join(cls.LOG_DIRECTORY, f'{time.strftime("%Y%m%d")}.log')

                file_handler = TimedRotatingFileHandler(log_path, when="midnight", interval=1,
                                                        encoding='utf8', backupCount=cls.BACKUP_COUNT)

                formatter = logging.Formatter(cls.LOG_FORMAT, datefmt=cls.LOG_DATE_FORMAT)
                file_handler.setFormatter(formatter)

                cls._logger = logging.getLogger(cls.__name__)
                cls._logger.setLevel(cls.LOG_LEVEL)
                cls._logger.addHandler(file_handler)
            except Exception as e:
                raise RuntimeError(f"无法初始化类的记录器 '{cls.__name__}': {e}")

        return cls._logger


if __name__ == '__main__':
    # 示例如何获取和使用日志器
    logger = Logs.get_logger()
    logger.info("This is an info message.")
    logger.error("This is an error message.")
