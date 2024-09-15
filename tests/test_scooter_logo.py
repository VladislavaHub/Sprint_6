import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls


@allure.title('Проверка при клике по логотипу "Самокат"')
@allure.description('Находимся в разделе "Заказать", нажимаем по логотипу "Самокат", и проверяем переход на главную страницу')
class TestScooterLogo:

    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER_MAIN)
        main_page.click_order_button(OrderPage.LOGO_SCOOTER)

        order_page = OrderPage(driver)
        order_page.click_scooter_logo()

        assert main_page.wait_and_find_element(MainPage.LOGO_SCOOTER).is_displayed()