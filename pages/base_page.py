from selenium.webdriver.remote.webdriver import WebDriver

from helper.configuration_manager import ConfigurationManager
from pypom import Page


class Base(Page):
    def __init__(self, selenium: WebDriver, locale='en-US', **url_kwargs):
        super(Base, self).__init__(selenium, ConfigurationManager().base_url(), locale=locale, **url_kwargs)
        self.config = ConfigurationManager()

    @property
    def page_title(self):
        return self.wait.until(lambda s: self.selenium.title)

    @property
    def current_url(self):
        return self.driver.current_url
