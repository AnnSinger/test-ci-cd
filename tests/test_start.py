import time

import pytest
from pages.helper import scroll_to_down, request_for_url


class TestStart:

    def test_flymarket_link(self, loaded_start_page):
        loaded_start_page.go_to_flymarket()
        assert loaded_start_page.loaded, \
            'После перехода на страницу flymarket, должны оказаться на стартовой странице flydrone'

    def test_dropdown_agreements_and_politics(self, loaded_start_page):
        loaded_start_page.hover_dropdown()
        assert loaded_start_page.is_hover_dropdown_displayed, 'Должен отобразиться dropdown Пользователям'
        politics_page = loaded_start_page.go_to_dropdown_politics()
        politics_page.wait_for_page_to_load()
        assert politics_page.loaded, 'Должна загрузиться страница Пользовательский соглашения'

    def test_dropdown_frequent_questions(self, loaded_start_page):
        loaded_start_page.hover_dropdown()
        assert loaded_start_page.is_hover_dropdown_displayed, 'Должен отобразиться dropdown Пользователям'
        faq_page = loaded_start_page.go_to_dropdown_faq()
        faq_page.wait_for_page_to_load()
        assert faq_page.loaded, 'Должна загрузиться страница Часто задаваемый вопросы'

    def test_dropdown_legislation(self, loaded_start_page):
        loaded_start_page.hover_dropdown()
        assert loaded_start_page.is_hover_dropdown_displayed, 'Должен отобразиться dropdown Пользователям'
        legislation_page = loaded_start_page.go_to_dropdown_legislation()
        legislation_page.wait_for_page_to_load()
        assert legislation_page.loaded, 'Должна загрузиться страница Законодательство'

    def test_dropdown_system_versions(self, loaded_start_page):
        loaded_start_page.hover_dropdown()
        assert loaded_start_page.is_hover_dropdown_displayed, 'Должен отобразиться dropdown Пользователям'
        system_versions_page = loaded_start_page.go_to_dropdown_system_versions()
        system_versions_page.wait_for_page_to_load()
        assert system_versions_page.loaded, 'Должна загрузиться страница Версии системы'

    def test_login_button(self, loaded_start_page):
        login_page = loaded_start_page.click_login_button()
        login_page.wait_for_page_to_load()
        assert login_page.loaded, 'Должна загрузиться страница регистрации'

    @pytest.mark.nondestructive
    def test_correct_email(self, loaded_start_page):
        loaded_start_page.enter_email('admin@flydrone.ru')
        registration_page = loaded_start_page.click_register_button_from_start_page()
        assert registration_page.loaded, 'Должен быть переход на страницу регистрации'

    def test_input_symbols_and_latin_email(self, loaded_start_page):
        loaded_start_page.enter_email('bsert#%*oalk')
        url_before = loaded_start_page.current_url
        loaded_start_page.click_register_button_from_start_page()
        assert url_before == loaded_start_page.current_url, 'Не должно быть перехода на страницу регистрации'

    def test_input_number_and_cyrillic_email(self, loaded_start_page):
        loaded_start_page.enter_email('156кныпа')
        url_before = loaded_start_page.current_url
        loaded_start_page.click_register_button_from_start_page()
        assert url_before == loaded_start_page.current_url, 'Не должно быть перехода на страницу регистрации'

    def test_empty_email(self, loaded_start_page):
        loaded_start_page.enter_email('')
        url_before = loaded_start_page.current_url
        loaded_start_page.click_register_button_from_start_page()
        assert url_before == loaded_start_page.current_url, 'Не должно быть перехода на страницу регистрации'

    def test_how_to_fly(self, loaded_start_page):
        how_to_fly_page = loaded_start_page.go_to_how_to_fly()
        how_to_fly_page.wait_for_page_to_load()
        assert how_to_fly_page.loaded, 'Должна загрузиться страница как совершить полет'

    def test_how_to_insure_a_flight(self, loaded_start_page):
        how_to_insure_page = loaded_start_page.go_to_how_to_insure()
        how_to_insure_page.wait_for_page_to_load()
        assert how_to_insure_page.loaded, 'Должна загрузиться страница как застраховать полет'

    def test_how_to_find_work(self, loaded_start_page):
        how_to_find_work_page = loaded_start_page.go_to_how_to_find_work()
        how_to_find_work_page.wait_for_page_to_load()
        assert how_to_find_work_page.loaded, 'Должна загрузиться страница как найти работу'

    def test_how_to_find_performer(self, loaded_start_page):
        how_to_find_performer_page = loaded_start_page.go_to_how_to_find_performer()
        how_to_find_performer_page.wait_for_page_to_load()
        assert how_to_find_performer_page.loaded, 'Должна загрузиться страница как найти исполнителя'

    def test_how_to_ads(self, loaded_start_page):
        how_to_ads_page = loaded_start_page.go_to_how_to_ads()
        how_to_ads_page.wait_for_page_to_load()
        assert how_to_ads_page.loaded, 'Должна загрузиться страница как опубликовать объявления'

    def test_telegram_channel(self, loaded_start_page):
        loaded_start_page.go_to_our_telegram_channel()
        assert 't.me/FlydroneNews'.lower() in loaded_start_page.current_url.lower()

    def test_about_company(self, loaded_start_page):
        scroll_to_down(loaded_start_page)
        about_page = loaded_start_page.go_to_about_company()
        about_page.wait_for_page_to_load()
        assert about_page.loaded, 'Должна загрузиться страница о нас'

    def test_requisites(self, loaded_start_page):
        scroll_to_down(loaded_start_page)
        requisites_page = loaded_start_page.go_to_requisites()
        requisites_page.wait_for_page_to_load()
        assert requisites_page.loaded, 'Должна загрузиться страница с реквизитами'

    def test_user_agreement(self, loaded_start_page):
        politics_page = loaded_start_page.go_to_politics()
        politics_page.wait_for_page_to_load()
        assert politics_page.loaded, 'Должны оказаться на странице с пользовательскими соглашениями'
        assert politics_page.open_privacy_and_go_back(), 'Сбегали на страичку с политикой конфиденциальности'
        assert politics_page.open_agreement_and_go_back(), 'Сбегали на страичку с пользовательскими соглашениями'
        assert politics_page.open_personal_data_and_go_back(), 'Сбегали на страичку с согласиями на обработку персональных данных'

    def test_useful_links(self, loaded_start_page):
        scroll_to_down(loaded_start_page)
        legislation_page = loaded_start_page.go_to_legislation()
        legislation_page.wait_for_page_to_load()
        assert legislation_page.loaded, 'Страница с полезными ссылками законодательства должна загрузиться'

        federal_links = legislation_page.get_all_federal_links()
        assert len(federal_links) == 16, 'Предполагается 16 ссылок на ФЗ и НПА'

        for link in federal_links:
            url = link.get_attribute('href')

            response = request_for_url(url)
            if response is not None:
                assert 'text/html' in response.headers['content-type']

    def test_company_registration(self, loaded_start_page):
        scroll_to_down(loaded_start_page)
        registration_page = loaded_start_page.go_to_registration_company()
        registration_page.wait_for_page_to_load()
        assert registration_page.loaded, 'Должна загрузиться страница с добавлением компании'

    def test_how_to_fly_footer(self, loaded_start_page):
        scroll_to_down(loaded_start_page)
        how_to_fly_page = loaded_start_page.go_to_how_to_fly_footer()
        how_to_fly_page.wait_for_page_to_load()
        assert how_to_fly_page.loaded, 'Должна загрузиться страница как совершить полет'

    def test_alfa_bank(self, loaded_start_page):
        loaded_start_page.go_to_alfa_bank()
        assert loaded_start_page.loaded, \
            'После перехода на страницу сайта Альфа-банка, должны оказаться на стартовой странице'

    def test_visa(self, loaded_start_page):
        visa = loaded_start_page.go_to_visa()
        visa.wait_for_page_to_load()
        assert visa.loaded, 'Должна загрузиться страница информация об уплате'

    def test_mir(self, loaded_start_page):
        mir = loaded_start_page.go_to_mir()
        mir.wait_for_page_to_load()
        assert mir.loaded, 'Должна загрузиться страница информация об уплате'

    def test_mastercard(self, loaded_start_page):
        mastercard = loaded_start_page.go_to_mastercard()
        mastercard.wait_for_page_to_load()
        assert mastercard.loaded, 'Должна загрузиться страница информация об уплате'

    def test_technical_support(self, loaded_start_page):
        loaded_start_page.go_to_technical_support()
        assert loaded_start_page.loaded, \
            'После перехода на страницу с телеграм каналом, должны оказаться на стартовой странице'

    # def test_accordion(self, loaded_start_page):
    #     loaded_start_page.click_accordion()
