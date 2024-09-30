import allure
import pytest
import yaml

from pom_testing.config.allure_conf import user_data_path
from pom_testing.page_object.login_page import LoginPage
from pom_testing.screenshot.screenshot import Screenshot


@allure.epic("xxx系统")
@allure.feature("首页登陆页面")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self._lp = LoginPage(driver)

    @allure.title("正确账号登录")
    @allure.description("验证正确账号可以登录首页")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize("login_account", yaml.safe_load(open(user_data_path))['login_data'])
    def test_login(self, driver, login_account):
        try:
            self._lp.correct_login(login_account['CorrectAccount'], login_account['CorrectPassword'])
        except Exception as e:
            screenshot_taker = Screenshot(driver)
            screenshot_taker.screenshot(f"登陆出错")
            raise e
