from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, locator):
        self.driver.find_element(*locator).click()

    def answer_the_question(self, locator):
        answer_the_question = self.wait_and_find_element(locator)
        return answer_the_question.text

    def click_header_order_button(self):
        header_order_button = self.wait_and_find_element(MainPageLocators.ORDER_BUTTON_IN_HEADER)
        return header_order_button.click()

    def click_order_button(self, locator):
        self.scroll_to_element(locator)
        order_button = self.wait_and_find_element(locator)
        return order_button.click()

    def click_yandex_logo(self):
        click_yandex_logo = self.wait_and_find_element(MainPageLocators.LOGO_YANDEX)
        return click_yandex_logo.click()