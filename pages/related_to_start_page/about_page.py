from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class AboutPage(Base):
    _header_about_locator = (By.CSS_SELECTOR, 'h2.fd-heading')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_about_locator)).text == 'Кто мы?'