from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def init_driver():
    options = Options()
    # 可选配置项
    options.page_load_strategy = 'eager'  # 页面加载策略，默认为'normal'，可选'eager'和'none'。
    # options.add_argument('--headless')  #无头模式
    options.add_argument('--disable-gpu')  # 禁用gpu
    options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"')  # 用户代理
    # options.add_argument('--incognito')  # 隐身模式
    options.add_argument('--disable-infobars')  # 禁用信息栏（浏览器正在被自动化工具控制）
    options.add_argument('--start-maximized')  # 窗口最大化
    options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
    options.add_argument('--no-sandbox')  # 禁用沙箱模式

    # 设置浏览器首选项
    prefs = {
        'download.prompt_for_download': False,  # 下载文件时是否提示保存对话框
        'safebrowsing.enabled': True,  # 是否启用安全浏览功能
        'credentials_enable_service': False,  # 是否启用保存密码提示
        'profile.password_manager_enabled': False  # 是否启用密码管理功能
    }
    options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(options=options)

    return driver