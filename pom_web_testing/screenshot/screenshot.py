import os
from datetime import datetime

import allure

from pom_testing.logs.log import Logs


class Screenshot:
    def __init__(self, driver):
        self._driver = driver
        self._screenshot_path = os.path.join(os.path.dirname(__file__), 'err_screenshot')
        self._ensure_screenshot_directory()
        self._logger = Logs.get_logger()
    def _ensure_screenshot_directory(self):
        try:
            if not os.path.exists(self._screenshot_path):
                os.makedirs(self._screenshot_path)
        except Exception as e:
            self._logger.error(f"创建屏幕截图目录时出错: {e}")
    def screenshot(self, error_name):
        date_time = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
        screenshot_name = f'{error_name}_{date_time}.png'
        screenshot_path = os.path.join(self._screenshot_path, screenshot_name)
        try:
            self._driver.get_screenshot_as_file(screenshot_path)
            with open(screenshot_path, 'rb') as image_file:
                image_data = image_file.read()
                allure.attach(image_data, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
                self._logger.info(f"截图成功: {screenshot_path}")
        except FileNotFoundError as e:
            self._logger.error(f"保存截图时文件路径不存在: {e}")
        except Exception as e:
            self._logger.error(f"截取屏幕快照并保存时出错: {type(e).__name__}: {e}")