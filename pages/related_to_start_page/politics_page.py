from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected
from pages.helper import open_link_by_locator_and_switch_back


class PoliticsPage(Base):
    _header_locator = (By.CSS_SELECTOR, 'h1.fd-heading')
    _privacy_locator = (By.CSS_SELECTOR, 'ol > li > a.fd-button[href*="privacyPolicy"]')
    _agreement_locator = (By.CSS_SELECTOR, 'ol > li > a.fd-button[href*="userAgreement"]')
    _personal_data_locator = (By.CSS_SELECTOR, 'ol > li > a.fd-button[href*="processingPersonalData"]')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.presence_of_element_located(
            self._header_locator)).text == 'Соглашения и политики платформы'

    def open_privacy_and_go_back(self) -> bool:
        return open_link_by_locator_and_switch_back(self, self._privacy_locator)

    def open_agreement_and_go_back(self) -> bool:
        return open_link_by_locator_and_switch_back(self, self._agreement_locator)

    def open_personal_data_and_go_back(self) -> bool:
        return open_link_by_locator_and_switch_back(self, self._personal_data_locator)
