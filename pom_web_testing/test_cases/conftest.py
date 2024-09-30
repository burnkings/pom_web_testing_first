import allure
import pytest

from pom_testing.utils.web_driver import init_driver


@pytest.fixture(scope="class")
def driver():
    with allure.step("webdriver初始化"):
        driver_instance = init_driver()
    try:
        yield driver_instance
    finally:
        with allure.step("退出浏览器"):
            driver_instance.quit()