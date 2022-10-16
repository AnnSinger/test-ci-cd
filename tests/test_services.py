import time

from pages.helper import scroll_to_down, request_for_url


class TestServices:
    def test_register_button_in_how_to_fly(self, loaded_how_to_fly_page):
        login_page = loaded_how_to_fly_page.click_register_button_from_service_page()
        login_page.wait_for_page_to_load()
        assert login_page.loaded, 'Должна загрузиться страница логина'

    def test_here_link_in_how_to_fly(self, loaded_how_to_fly_page):
        scroll_to_down(loaded_how_to_fly_page)
        legislation_page = loaded_how_to_fly_page.go_to_here_link()
        legislation_page.wait_for_page_to_load()
        assert legislation_page.loaded, 'Страница с полезными ссылками законодательства должна загрузиться'

    def test_rosaviation_link_in_how_to_fly(self, loaded_how_to_fly_page):
        scroll_to_down(loaded_how_to_fly_page)
        link = loaded_how_to_fly_page.get_rosaviation_link()
        url = link.get_attribute('href')
        response = request_for_url(url)
        if response is not None:
            assert 'text/html' in response.headers['content-type']

    def test_register_button_in_how_to_insure_flight(self, loaded_how_to_insure_flight_page):
        login_page = loaded_how_to_insure_flight_page.click_register_button_from_service_page()
        login_page.wait_for_page_to_load()
        assert login_page.loaded, 'Должна загрузиться страница логина'

    def test_register_button_in_how_to_find_work(self, loaded_how_to_find_work_page):
        login_page = loaded_how_to_find_work_page.click_register_button_from_service_page()
        login_page.wait_for_page_to_load()
        assert login_page.loaded, 'Должна загрузиться страница логина'

    def test_register_button_in_how_to_find_performer(self, loaded_how_to_find_performer_page):
        login_page = loaded_how_to_find_performer_page.click_register_button_from_service_page()
        login_page.wait_for_page_to_load()
        assert login_page.loaded, 'Должна загрузиться страница логина'

    def test_register_button_in_how_to_ads(self, loaded_how_to_ads_page):
        login_page = loaded_how_to_ads_page.click_register_button_from_service_page()
        login_page.wait_for_page_to_load()
        assert login_page.loaded, 'Должна загрузиться страница логина'

    def test_how_to_fly_tabs(self, loaded_how_to_fly_page):
        loaded_how_to_fly_page.click_next_nav_button()
        loaded_how_to_fly_page.click_all_vidodixXx()
        loaded_how_to_fly_page.click_next_nav_button()
        loaded_how_to_fly_page.click_all_vidodixXx()
        loaded_how_to_fly_page.click_next_nav_button()
        loaded_how_to_fly_page.click_next_nav_button()


