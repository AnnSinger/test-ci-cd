from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class LegislationPage(Base):
    _header_locator = (By.CSS_SELECTOR, 'h1.fd-heading')
    _federal_links_locator = (By.CSS_SELECTOR, 'div.fd-card ol > li > a')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.presence_of_element_located(
            self._header_locator)).text == 'Законодательство'

    def get_all_federal_links(self) -> list[WebElement]:
        return self.find_elements(*self._federal_links_locator)
