from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import Base
from pages.helper import open_link_by_locator_and_switch_back, scroll_to_down
from pages.related_to_start_page.start_page import StartPage


class StartPageLoggedIn(StartPage):
    """
        This class describes main page of Flydrone web application
        User's state is logged in
        It checks availability of important links and auth buttons
    """
    _hover_navigation_container_locator = (By.CSS_SELECTOR, 'nav[class*=StickyHeader_main-navigation] > ul')
    _user_avatar_locator = (By.CSS_SELECTOR, 'div > div[class*=HeaderUserContextMenu_menu__border]')

    @property
    def loaded(self):
        return self.is_user_avatar_displayed

    @property
    def is_user_avatar_displayed(self):
        return self.is_element_displayed(*self._user_avatar_locator)
