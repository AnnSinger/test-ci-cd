import time


class TestLogin:

    def test_back_to_app_from_login_page(self, loaded_login_page):
        loaded_login_page.click_back()
        url_match = loaded_login_page.current_url == loaded_login_page.config.base_url()
        assert url_match, 'Ссылка назад в приложение возвращает на главную страницу'

    def test_forgot_password_link(self, loaded_login_page):
        psw_recovery_page = loaded_login_page.click_forgot_password()
        assert psw_recovery_page.loaded, 'Должна загрузиться страница восстановления пароля'

    def test_privacy_policy_link(self, loaded_login_page):
        loaded_login_page.click_privacy_policy()
        assert loaded_login_page.loaded, 'После открытия pdf должны оказаться на странице авторизации'

    def test_correct_username_and_correct_password(self, loaded_login_page):
        loaded_login_page.enter_username('chernyh@flydrone.ru')
        loaded_login_page.enter_password('151694Aa*')
        start_page_logged_in = loaded_login_page.click_login()
        assert start_page_logged_in.loaded, 'Должна загрзуиться стартовая страница с аватаркой пользователя'

    def test_incorrect_username_and_incorrect_password(self, loaded_login_page):
        loaded_login_page.enter_username(' YY@mail.ru')
        loaded_login_page.enter_password('3214')
        loaded_login_page.click_login()
        assert '/auth/realms/flydrone' in loaded_login_page.current_url,\
            'Стартовая страница с аватаркой пользователя не должна загрузиться'

    def test_empty_username_and_empty_password(self, loaded_login_page):
        loaded_login_page.enter_username('')
        loaded_login_page.enter_password('')
        loaded_login_page.click_login()
        assert '/auth/realms/flydrone' in loaded_login_page.current_url,\
            'Стартовая страница с аватаркой пользователя не должна загрузиться'



