from selenium.webdriver.common.by import By
from pages.base_page import Base
from selenium.webdriver.support import expected_conditions as expected


class AcquiringPage(Base):
    _header_bank_card_locator = (By.CSS_SELECTOR, 'div > h1')

    @property
    def loaded(self) -> bool:
        return self.wait.until(expected.visibility_of_element_located(
            self._header_bank_card_locator)).text == 'Условия оплаты банковской картой в сети Интернет'