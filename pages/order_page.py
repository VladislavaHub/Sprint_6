import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.title('Выбор станции метро из выпадающего списка')
    def click_to_dropdown(self, locator):
        self.wait_and_click_element(OrderPageLocators. METRO_STATION)
        self.wait_and_click_element(locator)

    @allure.title('Переход на страницу заказа')
    def go_to_order(self, button):
        self.scroll_to_element(button)
        self.wait_and_find_element(button)
        self.wait_and_click_element(button)
        self.assert_url_change(Urls.SCOOTER_MAIN)

    @allure.title('Заполнение данных для оформления заказа')
    def fill_order(self, params, station):
        self.wait_and_send_keys(OrderPageLocators.FIELDS_NAME, params[0])
        self.wait_and_send_keys(OrderPageLocators.FIELDS_SURNAME, params[1])
        self.wait_and_send_keys(OrderPageLocators.FIELDS_ADDRESS, params[2])
        self.click_to_dropdown(station)
        self.wait_and_send_keys(OrderPageLocators.FIELD_PHONE, params[3])
        self.wait_and_click_element(OrderPageLocators.BUTTON_NEXT)
        self.wait_and_click_element(OrderPageLocators.RENTAL_TERM)
        self.wait_and_click_element(params[4])
        self.wait_and_click_element(OrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)
        self.wait_and_click_element(params[5])
        self.wait_and_click_element(params[6])
        self.wait_and_send_keys(OrderPageLocators.COMMENT, params[7])
        self.wait_and_click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.title('Ожидание смены адреса')
    def assert_url_change(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(url))