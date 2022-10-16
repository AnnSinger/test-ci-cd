from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class RegistrationPage(Base):
    _header_register_locator = (By.ID, 'kc-page-title')
    _back_to_app_locator_from_registration_page = (By.CSS_SELECTOR, 'header.login-pf-header > span.check-text > a')
    _link_login_locator = (By.CSS_SELECTOR, 'div.a-form-links > span.check-text > a')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_register_locator)).text == 'Регистрация'

    def click_back(self):
        self.find_element(*self._back_to_app_locator_from_registration_page).click()

    def click_login(self):
        self.find_element(*self._link_login_locator).click()
        from pages.auth.login_page import LoginPage
        return LoginPage(self.selenium)
