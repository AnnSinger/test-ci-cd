import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import Base
from pages.helper import open_link_by_locator_and_switch_back, scroll_to_down


class StartPage(Base):
    """
        This class describes main page of Flydrone web application
        User's state is unauthorized
        It checks availability of important links and auth buttons
    """

    """Common locators"""
    _flymarket_locator = (By.CSS_SELECTOR, 'li[class*=MainNavigation_item] > div >a[href*=fm]')
    _login_button_locator = (By.CSS_SELECTOR, 'div.fd-container > button')
    _header_sky_available_everyone_locator = (By.CSS_SELECTOR, 'h1.fd-heading')
    _enter_email_locator = (By.CSS_SELECTOR,
                            'div[class*=Hero_content] > form.d-none > div[class*=Registration_email_hrow] > input')
    _register_button_locator = (By.CSS_SELECTOR,
                                'div[class*="Hero_content"]:not([class*="d-md-none"]) > form > button.fd-button')
    _accordion_list_locator = (By.CSS_SELECTOR,
                               'div[class*=LandingSection] >div[class*=PartialFaq_list] > div.fd-accordion')
    """Hover dropdown locators"""
    _users_hover_dropdown_locator = (
        By.CSS_SELECTOR, 'ul[class*="MainNavigation_container"] > li > span[class*="MainNavigation_group-title"]')
    _users_hover_politics_locator = (
        By.CSS_SELECTOR, 'div[class*="MainNavigation_inner"] > div.fd-list > a[href*="politics"]')
    _users_hover_faq_locator = (By.CSS_SELECTOR, 'div[class*="MainNavigation_inner"] > div.fd-list > a[href*="faq"]')
    _users_hover_legislation_locator = (
        By.CSS_SELECTOR, 'div[class*="MainNavigation_inner"] > div.fd-list > a[href*="legislation"]')
    _users_hover_system_versions_locator = (
        By.CSS_SELECTOR, 'div[class*="MainNavigation_inner"] > div.fd-list > a[href*="system-versions"]')
    """Services locators"""
    _how_to_fly_locator = (By.CSS_SELECTOR, f'div[class*="Services_grid"] > a[href*="how-to-fly"] ')
    _how_to_insure_locator = (By.CSS_SELECTOR, f'a[href*="how-to-insure"]')
    _how_to_find_work_locator = (By.CSS_SELECTOR, f'a[href*="how-to-find-work"]')
    _how_to_find_performer_locator = (By.CSS_SELECTOR, f'a[href*="how-to-find-perfomer"]')
    _how_to_ads_locator = (By.CSS_SELECTOR, f'a[href*="how-to-ads"]')
    _our_telegram_channel_locator = (
        By.CSS_SELECTOR,
        'div[class*="LandingSection_content"] > div[class*=Services_grid] > a[href*="t.me/FlydroneNews"]')
    """Footer locators"""
    _about_company_locator = (By.CSS_SELECTOR, 'div.footer-col > div > a[href*=about]')
    _requisites_locator = (By.CSS_SELECTOR, 'div.footer-col > div > a[href*=requisites]')
    _legislation_locator = (By.CSS_SELECTOR, f'div.footer-link > a[href*="legislation"]')
    _politics_locator = (By.CSS_SELECTOR, 'div.footer-link > a[href*="politics"]')
    _registration_company_locator = (By.CSS_SELECTOR, 'div.footer-col > div > a[href*=register-company]')
    _how_to_fly_footer_locator = (By.CSS_SELECTOR, 'div[class*="footer-link"] > a[href*="how-to-fly"] ')
    _technical_support_locator = (
        By.CSS_SELECTOR, 'div.d-none > div.contact-information >  div.contact-information__contacts > a[href*="t.me"]')
    """Payment locators"""
    _visa_locator = (By.CSS_SELECTOR, 'div > a[class*=payment-info__visa]')
    _mir_locator = (By.CSS_SELECTOR, 'div > a[class*=payment-info__mir]')
    _mastercard_locator = (By.CSS_SELECTOR, 'div > a[class*=payment-info__mastercard]')
    _alfa_bank_locator = (By.CSS_SELECTOR, 'div > div[class*=payment-info__alfa] > a[href*="alfabank"]')

    _nav_accordion: list[WebElement] = []

    def go_to(self):
        self.selenium.get(self.config.base_url())

    @property
    def loaded(self):
        return self.is_header_sky_available_everyone_visible

    @property
    def is_header_sky_available_everyone_visible(self):
        return self.is_element_displayed(*self._header_sky_available_everyone_locator)

    @property
    def is_hover_dropdown_displayed(self):
        return self.is_element_displayed(*self._users_hover_dropdown_locator)

    def go_to_flymarket(self):
        self.find_element(*self._flymarket_locator)
        return open_link_by_locator_and_switch_back(self, self._flymarket_locator)

    def hover_dropdown(self):
        dropdown_to_hover = self.find_element(*self._users_hover_dropdown_locator)
        hover = ActionChains(self.driver).move_to_element(dropdown_to_hover)
        hover.perform()

    def go_to_dropdown_politics(self) -> Base:
        self.find_element(*self._users_hover_politics_locator).click()
        from pages.related_to_start_page.politics_page import PoliticsPage
        return PoliticsPage(self.selenium)

    def go_to_dropdown_faq(self) -> Base:
        self.find_element(*self._users_hover_faq_locator).click()
        from pages.commons.faq_page import FaqPage
        return FaqPage(self.selenium)

    def go_to_dropdown_legislation(self) -> Base:
        self.find_element(*self._users_hover_legislation_locator).click()
        from pages.related_to_start_page.legislation_page import LegislationPage
        return LegislationPage(self.selenium)

    def go_to_dropdown_system_versions(self) -> Base:
        self.find_element(*self._users_hover_system_versions_locator).click()
        from pages.related_to_start_page.system_versions_page import SystemVersionsPage
        return SystemVersionsPage(self.selenium)

    def click_login_button(self):
        self.find_element(*self._login_button_locator).click()
        from pages.auth.login_page import LoginPage
        return LoginPage(self.selenium)

    def enter_email(self, email: str):
        element = self.find_element(*self._enter_email_locator)
        element.clear()
        element.send_keys(email)

    def click_register_button_from_start_page(self):
        self.find_element(*self._register_button_locator).click()
        from pages.auth.registration_page import RegistrationPage
        return RegistrationPage(self.selenium)

    def go_to_how_to_fly(self):
        self.find_element(*self._how_to_fly_locator).click()
        from pages.commons.services_page import ServiceHowToFlyPage
        return ServiceHowToFlyPage(self.selenium)

    def go_to_how_to_insure(self):
        self.find_element(*self._how_to_insure_locator).click()
        from pages.commons.services_page import ServiceHowToInsurePage
        return ServiceHowToInsurePage(self.selenium)

    def go_to_how_to_find_work(self):
        self.find_element(*self._how_to_find_work_locator).click()
        from pages.commons.services_page import ServiceHowToFindWorkPage
        return ServiceHowToFindWorkPage(self.selenium)

    def go_to_how_to_find_performer(self):
        self.find_element(*self._how_to_find_performer_locator).click()
        from pages.commons.services_page import ServiceHowToFindPerformerPage
        return ServiceHowToFindPerformerPage(self.selenium)

    def go_to_how_to_ads(self):
        self.find_element(*self._how_to_ads_locator).click()
        from pages.commons.services_page import ServiceHowToAdsPage
        return ServiceHowToAdsPage(self.selenium)

    def go_to_our_telegram_channel(self):
        scroll_to_down(self)
        self.find_element(*self._our_telegram_channel_locator).click()

    def go_to_about_company(self):
        self.find_element(*self._about_company_locator).click()
        from pages.related_to_start_page.about_page import AboutPage
        return AboutPage(self.selenium)

    def go_to_requisites(self):
        self.find_element(*self._requisites_locator).click()
        from pages.related_to_start_page.requisites_page import RequisitesPage
        return RequisitesPage(self.selenium)

    def go_to_politics(self):
        scroll_to_down(self)
        self.find_element(*self._politics_locator).click()
        from pages.related_to_start_page.politics_page import PoliticsPage
        return PoliticsPage(self.selenium)

    def go_to_legislation(self):
        self.find_element(*self._legislation_locator).click()
        from pages.related_to_start_page.legislation_page import LegislationPage
        return LegislationPage(self.selenium)

    def go_to_registration_company(self):
        self.find_element(*self._registration_company_locator).click()
        from pages.related_to_start_page.registration_company_page import RegistrationCompanyPage
        return RegistrationCompanyPage(self.selenium)

    def go_to_how_to_fly_footer(self):
        self.find_element(*self._how_to_fly_footer_locator).click()
        from pages.commons.services_page import ServiceHowToFlyPage
        return ServiceHowToFlyPage(self.selenium)

    def go_to_alfa_bank(self):
        scroll_to_down(self)
        return open_link_by_locator_and_switch_back(self, self._alfa_bank_locator)

    def go_to_visa(self):
        scroll_to_down(self)
        self.find_element(*self._visa_locator).click()
        from pages.related_to_start_page.acquiring_page import AcquiringPage
        return AcquiringPage(self.selenium)

    def go_to_mir(self):
        scroll_to_down(self)
        self.find_element(*self._mir_locator).click()
        from pages.related_to_start_page.acquiring_page import AcquiringPage
        return AcquiringPage(self.selenium)

    def go_to_mastercard(self):
        scroll_to_down(self)
        self.find_element(*self._mastercard_locator).click()
        from pages.related_to_start_page.acquiring_page import AcquiringPage
        return AcquiringPage(self.selenium)

    def go_to_technical_support(self):
        scroll_to_down(self)
        return open_link_by_locator_and_switch_back(self, self._technical_support_locator)

    def click_accordion(self):
        if len(self._nav_accordion) == 0:
            self._nav_accordion = self.find_elements(*self._accordion_list_locator)
            # self._nav_accordion.reverse()
        self._nav_accordion.pop().click()
        time.sleep(1)
