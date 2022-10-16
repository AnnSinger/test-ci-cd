from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from helper.configuration_manager import ConfigurationManager
from enum import IntEnum


class BrowserEnum(IntEnum):
    firefox = 1
    chrome = 2
    edge = 3


class WebDriverManager:
    @staticmethod
    def set_chrome_options() -> webdriver.ChromeOptions:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_insecure_certs = True
        chrome_options.headless = ConfigurationManager().headless()

        return chrome_options

    @staticmethod
    def set_ff_options() -> webdriver.FirefoxOptions:
        ff_options = webdriver.FirefoxOptions()
        ff_options.accept_insecure_certs = True
        ff_options.headless = ConfigurationManager().headless()

        return ff_options

    @staticmethod
    def set_edge_options() -> webdriver.EdgeOptions:
        edge_options = webdriver.EdgeOptions()
        edge_options.accept_insecure_certs = True
        edge_options.headless = ConfigurationManager().headless()

        return edge_options

    def get_driver(self, browser) -> webdriver:
        if browser not in BrowserEnum:
            raise TypeError('Must be in Browser Enum')

        if browser == BrowserEnum.firefox:
            driver = webdriver.Firefox(options=self.set_ff_options(),
                                       executable_path=GeckoDriverManager().install())
        elif browser == BrowserEnum.edge:
            driver = webdriver.Edge(options=self.set_edge_options(),
                                    executable_path=EdgeChromiumDriverManager().install())
        elif browser == BrowserEnum.chrome:
            driver = webdriver.Chrome(options=self.set_chrome_options(),
                                      service=ChromeService(ChromeDriverManager().install()))

        if driver is None:
            raise TypeError("Object not constructed. It's not possible to use it further.")

        driver.set_page_load_timeout(80)
        driver.implicitly_wait(ConfigurationManager().timeout())
        driver.maximize_window()

        return driver
