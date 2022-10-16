from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class FaqPage(Base):
    _header_faq_locator = (By.CSS_SELECTOR, 'div > h1[class*=fd-heading]')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_faq_locator)).text == 'Часто задаваемые вопросы'
