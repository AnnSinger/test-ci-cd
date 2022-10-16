import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expected

from pages.helper import scroll_to_down, request_for_url


class TestStartLoggedIn:
    def test_telegram_channel(self, loaded_start_page_logged_in):
        loaded_start_page_logged_in.go_to_our_telegram_channel()
        assert 't.me/FlydroneNews'.lower() in loaded_start_page_logged_in.current_url.lower()

    def test_alfa_bank(self, loaded_start_page_logged_in):
        loaded_start_page_logged_in.go_to_alfa_bank()
        assert loaded_start_page_logged_in.loaded, \
            'После перехода на страницу сайта Альфа-банка, должны оказаться на стартовой странице'

    def test_visa(self, loaded_start_page_logged_in):
        visa = loaded_start_page_logged_in.go_to_visa()
        visa.wait_for_page_to_load()
        assert visa.loaded, 'Должна загрузиться страница информация об уплате'

    def test_mir(self, loaded_start_page_logged_in):
        mir = loaded_start_page_logged_in.go_to_mir()
        mir.wait_for_page_to_load()
        assert mir.loaded, 'Должна загрузиться страница информация об уплате'

    def test_mastercard(self, loaded_start_page_logged_in):
        mastercard = loaded_start_page_logged_in.go_to_mastercard()
        mastercard.wait_for_page_to_load()
        assert mastercard.loaded, 'Должна загрузиться страница информация об уплате'

    def test_user_agreement(self, loaded_start_page_logged_in):
        politics_page = loaded_start_page_logged_in.go_to_politics()
        politics_page.wait_for_page_to_load()
        assert politics_page.loaded, 'Должны оказаться на странице с пользовательскими соглашениями'
        assert politics_page.open_privacy_and_go_back(), 'Сбегали на страичку с политикой конфиденциальности'
        assert politics_page.open_agreement_and_go_back(), 'Сбегали на страичку с пользовательскими соглашениями'
        assert politics_page.open_personal_data_and_go_back(), 'Сбегали на страичку с согласиями на обработку персональных данных'

    def test_useful_links(self, loaded_start_page_logged_in):
        scroll_to_down(loaded_start_page_logged_in)
        legislation_page = loaded_start_page_logged_in.go_to_legislation()
        legislation_page.wait_for_page_to_load()
        assert legislation_page.loaded, 'Страница с полезными ссылками законодательства должна загрузиться'

        federal_links = legislation_page.get_all_federal_links()
        assert len(federal_links) == 16, 'Предполагается 16 ссылок на ФЗ и НПА'

        for link in federal_links:
            url = link.get_attribute('href')

            response = request_for_url(url)
            if response is not None:
                assert 'text/html' in response.headers['content-type']

    def test_how_to_fly_footer(self, loaded_start_page_logged_in):
        scroll_to_down(loaded_start_page_logged_in)
        how_to_fly_page = loaded_start_page_logged_in.go_to_how_to_fly_footer()
        how_to_fly_page.wait_for_page_to_load()
        assert how_to_fly_page.loaded, 'Должна загрузиться страница как совершить полет'

    def test_technical_support(self, loaded_start_page_logged_in):
        loaded_start_page_logged_in.go_to_technical_support()
        assert loaded_start_page_logged_in.loaded, \
            'После перехода на страницу с телеграм каналом, должны оказаться на стартовой странице'

    def test_about_company(self, loaded_start_page_logged_in):
        scroll_to_down(loaded_start_page_logged_in)
        about_page = loaded_start_page_logged_in.go_to_about_company()
        about_page.wait_for_page_to_load()
        assert about_page.loaded, 'Должна загрузиться страница о нас'

    def test_requisites(self, loaded_start_page_logged_in):
        scroll_to_down(loaded_start_page_logged_in)
        requisites_page = loaded_start_page_logged_in.go_to_requisites()
        requisites_page.wait_for_page_to_load()
        assert requisites_page.loaded, 'Должна загрузиться страница с реквизитами'




