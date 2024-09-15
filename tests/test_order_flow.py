import allure
from data import Urls, OrderData
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import pytest



@allure.title('Проверка заказа самоката')
@allure.description('Поочередно делаем заказ самоката через обе кнопки "Заказать" с двумя разными данными заказчика и заказа')
class TestOrderFlow:

    vlada_order = [MainPageLocators.ORDER_BUTTON_IN_HEADER,
         OrderData.NAME_1,
         OrderData.SURNAME_1,
         OrderData.ADDRESS_1,
         OrderPageLocators.FIELDS_ADDRESS,
         OrderData.PHONE_NUMBER_1,
         OrderPageLocators.FIELDS_DATE,
         OrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD,
         OrderPageLocators.COLOR_SAMOKATO,
         OrderData.COMMENT_1
         ]

    ira_order = [MainPageLocators.ORDER_BUTTON_IN_MAIN,
         OrderData.NAME_2,
         OrderData.SURNAME_2,
         OrderData.ADDRESS_2,
         OrderPageLocators.FIELDS_ADDRESS,
         OrderData.PHONE_NUMBER_2,
         OrderPageLocators.FIELDS_DATE,
         OrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD,
         OrderPageLocators.COLOR_SAMOKATO,
         OrderData.COMMENT_2
         ]

    @pytest.mark.parametrize('button, name, surname, address, subway, phone_number, date, period, colour, comment',[vlada_order, ira_order])
    def test_order_flow(self, driver, button, name, surname, address, subway, phone_number, date, period, colour, comment):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER_MAIN)
        main_page.click_order_button(button)

        order_page = OrderPageLocators(driver)
        order_page.YES_PLACE_ORDER(name, surname, address, subway, phone_number)
        order_page.BUTTON_VIEW_STATUS()
