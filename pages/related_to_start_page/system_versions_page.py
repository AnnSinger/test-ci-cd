from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class SystemVersionsPage(Base):
    _system_versions_locator = (By.CSS_SELECTOR, 'div > h1[class*=fd-heading]')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._system_versions_locator)).text == 'Версии системы'
