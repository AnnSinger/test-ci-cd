import os
import pytest

from _pytest.fixtures import FixtureDef
from helper.webdriver_manager import WebDriverManager, BrowserEnum
from pages.related_to_start_page.start_page import StartPage

browser_list = [BrowserEnum.chrome,
                BrowserEnum.firefox,]

# For OS Windows specific
if os.name == 'nt':
    browser_list.append(BrowserEnum.edge)


@pytest.fixture(scope='function', params=browser_list)
def loaded_start_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return start_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_login_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    login_page = start_page.click_login_button()
    login_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return login_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_start_page_logged_in(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    login_page = start_page.click_login_button()
    login_page.wait_for_page_to_load()
    login_page.enter_username('chernyh@flydrone.ru')
    login_page.enter_password('151694Aa*')

    start_page_logged_in = login_page.click_login()
    start_page_logged_in.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return start_page_logged_in


@pytest.fixture(scope='function', params=browser_list)
def loaded_registration_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    start_page.enter_email('admin@flydrone.ru')
    registration_page = start_page.click_register_button_from_start_page()
    registration_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return registration_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_psw_recovery_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    login_page = start_page.click_login_button()
    login_page.wait_for_page_to_load()

    psw_recovery_page = login_page.click_forgot_password()
    psw_recovery_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return psw_recovery_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_how_to_fly_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    how_to_fly_page = start_page.go_to_how_to_fly()
    how_to_fly_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return how_to_fly_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_how_to_insure_flight_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    how_to_insure_flight_page = start_page.go_to_how_to_insure()
    how_to_insure_flight_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return how_to_insure_flight_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_how_to_find_work_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    how_to_find_work_page = start_page.go_to_how_to_find_work()
    how_to_find_work_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return how_to_find_work_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_how_to_find_performer_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    how_to_find_performer_page = start_page.go_to_how_to_find_performer()
    how_to_find_performer_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return how_to_find_performer_page


@pytest.fixture(scope='function', params=browser_list)
def loaded_how_to_ads_page(request: FixtureDef):
    driver = WebDriverManager().get_driver(request.param)

    start_page = StartPage(driver)
    start_page.go_to()
    start_page.wait_for_page_to_load()

    how_to_ads_page = start_page.go_to_how_to_ads()
    how_to_ads_page.wait_for_page_to_load()

    request.addfinalizer(driver.quit)
    return how_to_ads_page
