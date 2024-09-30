import os

# 用户数据路径
user_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'user.yaml')


# 测试用例路径
def case_path(path):
    return os.path.join(os.path.dirname(path), 'test_cases')


# 测试报告路径
def report_path(path):
    return os.path.join(os.path.dirname(path), 'reports')


# 执行 pytest 命令生成 Allure 报告配置
pytest_command = [
    "pytest",
    "test_login.py", # 登陆测试
    "test_home.py", # 首页测试
    "test_search.py", # 搜索测试
    "--alluredir=../reports/report",
    "--clean-alluredir"]
# 执行 Allure 命令生成并打开报告配置
allure_command = ["allure", "generate", "report", "--clean"]
# 打开allure报告
allure_open = ["allure", "open", "allure-report"]
