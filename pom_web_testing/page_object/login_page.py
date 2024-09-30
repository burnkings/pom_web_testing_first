"""
登陆页面
"""
import allure

from pom_testing.base.base_page import BasePage


class LoginPage(BasePage):
    # 网址
    _url = 'http://baidu.com'
    # 账号
    _account = ('id', 'account')
    # 密码
    _password = ('id', 'PASSWORD')
    # 登录
    _login_button = ('id', 'login_button')

    def correct_login(self, username, password):
        with allure.step("打开登陆页面"):
            self.open_url(self._url)
        with allure.step(f"输入账号:{username}"):
            self.input(self._account, username)
        with allure.step(f"输入密码:{password}"):
            self.input(self._password, password)
        with allure.step("点击登陆"):
            self.click(self._login_button)
