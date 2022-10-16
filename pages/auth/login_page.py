from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected

from pages.helper import open_link_by_locator_and_switch_back


class LoginPage(Base):
    _header_login_locator = (By.ID, 'kc-page-title')
    _username_locator = (By.ID, 'username')
    _password_locator = (By.ID, 'password')
    _login_button_locator = (By.ID, 'kc-login')
    _back_to_app_locator_from_login_page = (By.CSS_SELECTOR, 'header.login-pf-header > span.check-text > a')
    _forgot_password_locator = (By.CSS_SELECTOR, 'div.login-pf-settings > div > span.check-text > a[href*="auth"]')
    _text_after_psw_recovery_confirmation_locator = (By.CSS_SELECTOR, 'div > span.kc-feedback-text')
    _privacy_locator = (By.CSS_SELECTOR, 'div > span > a[href*="privacyPolicy"]')

    @property
    def loaded(self):
        return self.is_header_login_visible

    @property
    def is_header_login_visible(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_login_locator)).text == 'Войти'

    @property
    def is_text_after_psw_recovery_confirmation_visible(self):
        return self.wait.until(expected.visibility_of_element_located(
            self._text_after_psw_recovery_confirmation_locator)).text == \
               'В ближайшее время Вы должны получить письмо с дальнейшими инструкциями.'

    def enter_username(self, username: str):
        element = self.find_element(*self._username_locator)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password: str):
        element = self.find_element(*self._password_locator)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.find_element(*self._login_button_locator).click()
        from pages.related_to_start_page.start_page_logged_in import StartPageLoggedIn
        return StartPageLoggedIn(self.selenium)

    def click_back(self):
        self.find_element(*self._back_to_app_locator_from_login_page).click()

    def click_forgot_password(self):
        self.find_element(*self._forgot_password_locator).click()
        from pages.auth.password_recovery_page import PasswordRecoveryPage
        return PasswordRecoveryPage(self.selenium)

    def click_privacy_policy(self) -> bool:
        return open_link_by_locator_and_switch_back(self, self._privacy_locator)
