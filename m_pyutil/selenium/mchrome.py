import logging
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ChromeCli(WebDriver):

    def __init__(self,
                 proxy: str = None,
                 headless: bool = False,
                 images_disabled: bool = True,
                 extensions: list = None,
                 unpacked_extensions: list = None,
                 **kwargs):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        if proxy:
            options.add_argument(f'--proxy-server={proxy}')
        if headless:
            options.add_argument('--headless=new')
        if images_disabled:
            options.add_argument('--blink-settings=imagesEnabled=false')
        if extensions:
            for extension in extensions:
                options.add_extension(extension)
        if unpacked_extensions:
            options.add_argument(f'--load-extension={",".join(unpacked_extensions)}')
        if kwargs:
            for key, value in kwargs.items():
                options.add_argument(f'{key}={value}')

        super().__init__(options=options)
        self.maximize_window()

    def query_element_d(self,
                        by: str,
                        value: str,
                        timeout: int = 10,
                        count: int = 3,
                        raise_e: bool = True) -> WebElement:
        return self.query_element(src=self, by=by, value=value, timeout=timeout, count=count, raise_e=raise_e)

    def query_element(self,
                      src: WebDriver or WebElement,
                      by: str,
                      value: str,
                      timeout: int = 10,
                      count: int = 3,
                      raise_e: bool = True) -> WebElement or None:
        elements = self.query_elements(src=src, by=by, value=value, timeout=timeout, count=count, raise_e=raise_e)
        if elements:
            return elements[0]
        return None

    def query_elements_d(self,
                         by: str,
                         value: str,
                         timeout: int = 10,
                         count: int = 3,
                         raise_e: bool = True) -> list[WebElement]:
        return self.query_elements(src=self, by=by, value=value, timeout=timeout, count=count, raise_e=raise_e)

    def query_elements(self,
                       src: WebDriver or WebElement,
                       by: str,
                       value: str,
                       timeout: int = 10,
                       count: int = 3,
                       raise_e: bool = True) -> list[WebElement]:
        while count > 0:
            try:
                WebDriverWait(self, timeout).until(ec.presence_of_element_located((by, value)))
                return src.find_elements(by=by, value=value)
            except Exception as e:
                count -= 1
                logging.debug(str(e))
        if raise_e:
            raise RuntimeError(f'elements were not found: by={by}, value={value}')
        return []

    def click(self, ele):
        ActionChains(self).move_to_element(ele).click().perform()

    def click_and_move_by_x_offset(self, ele, x_offset):
        action_chains = ActionChains(self)
        action_chains.click_and_hold(ele).perform()
        moved_x_offset = 0
        while True:
            if moved_x_offset >= x_offset:
                break
            delta_x_offset = x_offset - moved_x_offset
            delta_x_offset = min(x_offset / random.randint(2, 5), delta_x_offset)
            action_chains.move_by_offset(delta_x_offset, 0).perform()
            moved_x_offset += delta_x_offset
            time.sleep(random.uniform(0.005, 0.7))
