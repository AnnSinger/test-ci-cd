from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class PasswordRecoveryPage(Base):
    _header_psw_recovery_locator = (By.ID, 'kc-page-title')
    _back_to_app_locator_from_psw_recovery_page = (By.CSS_SELECTOR, 'header.login-pf-header > span.check-text > a')
    _back_to_login_locator = (By.CSS_SELECTOR, 'div > span.check-text > a[href*=auth]')
    _username_locator = (By.ID, 'username')
    _confirm_button_locator = (By.CSS_SELECTOR, 'div > input.btn ')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_psw_recovery_locator)).text == 'Забыли пароль?'

    def click_back_to_app(self):
        self.find_element(*self._back_to_app_locator_from_psw_recovery_page).click()

    def click_back_to_login(self):
        self.find_element(*self._back_to_login_locator).click()
        from pages.auth.login_page import LoginPage
        return LoginPage(self.selenium)

    def enter_email(self, username: str):
        element = self.find_element(*self._username_locator)
        element.clear()
        element.send_keys(username)

    def click_confirm_button(self):
        self.find_element(*self._confirm_button_locator).click()
        from pages.auth.login_page import LoginPage
        return LoginPage(self.selenium)
