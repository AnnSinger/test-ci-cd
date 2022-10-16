
class TestPswRecovery:

    def test_back_to_app_from_psw_recovery_page(self, loaded_psw_recovery_page):
        loaded_psw_recovery_page.click_back_to_app()
        url_match = loaded_psw_recovery_page.current_url == loaded_psw_recovery_page.config.base_url()
        assert url_match, 'Ссылка назад в прилажение возвращает на главную страницу'

    def test_back_to_login(self, loaded_psw_recovery_page):
        login_page = loaded_psw_recovery_page.click_back_to_login()
        assert login_page.loaded, 'Ссылка назад ко входу возвращает на страницу авторизации'

    def test_psw_recovery(self, loaded_psw_recovery_page):
        loaded_psw_recovery_page.enter_email('admin@flydrone.ru')
        login_page = loaded_psw_recovery_page.click_confirm_button()
        assert login_page.is_text_after_psw_recovery_confirmation_visible, \
            'После подтвержения о смене пароля происходит редирект на страницу авторизации с сообщением'

