# -*- coding: utf-8 -*-
import os
import subprocess

from config.allure_conf import pytest_command, allure_command, allure_open
from logs.log import Logs

# 初始化日志配置
logger = Logs.get_logger()

# 路径配置
BASE_DIR = os.path.dirname(__file__)
TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_cases')
REPORT_DIR = os.path.join(BASE_DIR, 'reports')


def main():
    try:
        # 执行 pytest 命令生成 Allure 报告
        logger.info("正在运行 pytest 以生成 Allure 报告...")
        subprocess.run(pytest_command, cwd=TEST_CASE_DIR, shell=True)

        # 执行 Allure 命令生成报告
        logger.info("正在生成 Allure 报告...")
        subprocess.run(allure_command, cwd=REPORT_DIR, shell=True)

        # 打开 Allure 报告
        logger.info("打开Allure报告...")
        subprocess.run(allure_open, cwd=REPORT_DIR, shell=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"发生错误: {e}")
        exit(1)


if __name__ == "__main__":
    main()
