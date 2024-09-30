import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pom_testing.logs.log import Logs
from pom_testing.screenshot.screenshot import Screenshot


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logs.get_logger()
        self.scr = Screenshot(driver)

    """打开url"""

    def open_url(self, url: str):
        self.driver.maximize_window()
        self.logger.info('最大化窗口')
        self.driver.get(url)
        self.logger.info(f'打开网址：{url}')
        # self.driver.implicitly_wait(80)

    """元素定位，元组形态，返回web_element对象"""

    def locator(self, loc: tuple) -> WebElement:
        try:
            # 显示等待直到元素可见并可交互
            return self.display_wait(loc)

        except NoSuchElementException:
            self.logger.error(f'元素{loc}未找到')
            self.scr.screenshot(loc)
            raise

        except TimeoutException:
            self.logger.error(f'元素{loc}未在规定时间内变为可见')
            self.scr.screenshot(loc)
            raise

    """输入"""

    def input(self, loc: tuple, txt: str):
        self.locator(loc).clear()
        self.locator(loc).send_keys(txt)
        self.logger.info(f'输入元素： {loc}，值为：{txt}')

    """点击"""

    def click(self, loc: tuple):
        self.locator(loc).click()
        self.logger.info(f'点击元素： {loc}')

    """强制等待"""

    def Forced_wait(self, number: int):
        time.sleep(number)
        self.logger.info(f'强制等待：{number}秒')

    """下拉框文字选择"""

    def select(self, loc: tuple, mode: str):
        select = Select(self.locator(loc))
        select.select_by_visible_text(mode)
        self.logger.info(f'选择内容为： {mode}')

    """检查元素是否存在"""

    def check(self, loc: tuple) -> bool:
        return True if self.locator(loc) else False

    """获取元素文本"""

    def txt(self, loc: tuple) -> str:
        return self.locator(loc).text

    """退出浏览器"""

    def quit(self):
        self.driver.quit()
        self.logger.info('退出浏览器')

    """断言元素文本"""

    def assert_element_text(self, loc: tuple, expected_text: str):
        try:
            actual_text = self.locator(loc).text
            assert actual_text == expected_text
            self.logger.info(f'断言元素{loc}文本成功：预期={expected_text}, 实际={actual_text}')
        except AssertionError:
            self.logger.error(f'断言元素{loc}文本失败：预期={expected_text}, 实际={actual_text}')
            raise

    """切换到frame"""

    def switch_frame(self, loc: tuple):
        self.driver.switch_to.frame(self.locator(loc))
        self.logger.info(f'进入的iframe元素为： {loc}')

    """退出frame"""

    def quit_iframe(self):
        self.driver.switch_to.default_content()
        self.logger.info('退出iframe')

    """显示等待"""

    def display_wait(self, loc):
        return WebDriverWait(self.driver, timeout=3).until(EC.element_to_be_clickable(loc))

    def wait_for_element_disappear(self, loc):
        """等待某个元素消失"""
        return WebDriverWait(self.driver, timeout=60).until(EC.invisibility_of_element_located(loc))

    def wait_for_element_to_appear(self, loc):
        """等待某个元素消失"""
        return WebDriverWait(self.driver, timeout=60).until(EC.visibility_of_element_located(loc))

    """切换浏览器页"""

    def switch_window(self, num: int):
        self.driver.switch_to.window(self.driver.window_handles[num])
        self.logger.info(f'切换到浏览器第{num}个浏览页')


if __name__ == '__main__':
    with webdriver.Edge() as driver:
        aa = Screenshot(driver)

        driver.get('https://www.baidu.com')
        time.sleep(2)
        aa.screenshot("截图")
        time.sleep(1)
