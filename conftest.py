from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()

    yield firefox
    firefox.quit()