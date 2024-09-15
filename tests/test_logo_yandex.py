import allure
from data import Urls
from pages.main_page import MainPage
from pages.dzen_page import DzenPage
from locators.dzen_locators import DzenLocators


@allure.title('Проверка при клике по логотипу "Яндекс"')
@allure.description('Находимся на главной странице, нажимаем по логотипу "Яндекс" и проверяем переход на другую страницу')
class TestYandexLogo:

    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER_MAIN)
        main_page.click_yandex_logo()
        dzen_page = DzenPage(driver)
        dzen_page.switch_dzen_window(driver)
        dzen_page.wait_and_find_element(DzenLocators.SEARCH_BUTTON)

        assert Urls.DZEN_MAIN in dzen_page.get_current_url(driver)