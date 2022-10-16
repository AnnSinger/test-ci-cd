
class TestRegistration:

    def test_back_to_app_from_registration_page(self, loaded_registration_page):
        loaded_registration_page.click_back()
        url_match = loaded_registration_page.current_url == loaded_registration_page.config.base_url()
        assert url_match, 'Ссылка назад в прилажение возвращает на главную страницу'

    def test_login_link(self, loaded_registration_page):
        login_page = loaded_registration_page.click_login()
        assert login_page.loaded, 'Ссылка войдите возвращает на страницу авторизации'
