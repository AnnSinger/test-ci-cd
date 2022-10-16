from ssl import SSLError
from warnings import warn

import requests
from _pytest.recwarn import warns
from requests import ReadTimeout, Response
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page import Base


def open_link_by_locator_and_switch_back(page: Base, locator: (str, str)) -> bool:
    original_window = page.driver.current_window_handle

    element: WebElement = page.find_element(*locator)
    ActionChains(page.selenium).move_to_element(element).click().perform()

    for window_handle in page.driver.window_handles:
        if window_handle != original_window:
            page.driver.switch_to.window(original_window)
            return True
    return False


def scroll_to_down(page: Base):
    page.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


def request_for_url(url: str) -> Response:
    try:
        return requests.get(url, verify=True, timeout=5)
    except ReadTimeout as e:
        with warns(UserWarning):
            warn(f'Timeout at url {e.request.url}', UserWarning)
    except SSLError as e:
        with warns(UserWarning):
            warn(f'SSLError {e.reason}', UserWarning)
    except:
        with warns(UserWarning):
            warn('Unknown error', UserWarning)
