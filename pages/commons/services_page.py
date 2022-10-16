import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class Services(Base):
    _header_locator = (By.CSS_SELECTOR, 'h1.fd-heading')
    _register_button_locator = (By.CSS_SELECTOR, 'button.fd-button.fd-button--primary')
    _navigation_tabs_locator = (By.CSS_SELECTOR, 'ul.numbered-tabs-navigation > li.numbered-tabs-navigation-item')
    _youtube_vidosix_locator = (By.CSS_SELECTOR, 'div.fd-tab:not([style*="display: none;"]) > section > div > div')

    _nav_buttons: list[WebElement] = []

    def click_register_button_from_service_page(self):
        self.find_element(*self._register_button_locator).click()
        from pages.auth.login_page import LoginPage
        return LoginPage(self.selenium)

    def click_next_nav_button(self):
        if len(self._nav_buttons) == 0:
            self._nav_buttons = self.find_elements(*self._navigation_tabs_locator)
            self._nav_buttons.reverse()
        self._nav_buttons.pop().click()
        time.sleep(1)

    def click_all_vidodixXx(self):
        videos_on_tab = self.find_elements(*self._youtube_vidosix_locator)
        for video in videos_on_tab:
            if video.is_displayed():
                video.click()


class ServiceHowToFlyPage(Services):
    _here_link_locator = (By.CSS_SELECTOR, 'section > span > a[href*="legislation"]')
    _rosaviation_link_locator = (By.CSS_SELECTOR, 'section > span > a[href*="favt.gov.ru"]')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_locator)).text == 'Как запланировать полет и получить разрешение'

    def go_to_here_link(self):
        self.find_element(*self._here_link_locator).click()
        new_window = self.selenium.window_handles[1]
        self.selenium.switch_to.window(new_window)
        from pages.related_to_start_page.legislation_page import LegislationPage
        return LegislationPage(self.selenium)

    def get_rosaviation_link(self):
        return self.find_element(*self._rosaviation_link_locator)


class ServiceHowToInsurePage(Services):

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_locator)).text == 'Как застраховать свой полет'


class ServiceHowToFindWorkPage(Services):

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_locator)).text == 'Как найти заказ на выполнение работы'


class ServiceHowToFindPerformerPage(Services):

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_locator)).text == 'Как найти исполнителя под Вашу задачу'


class ServiceHowToAdsPage(Services):

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_locator)).text == 'Как опубликовать объявление'
