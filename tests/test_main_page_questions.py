import allure
import pytest
from data import AnswerTexts
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestQuestion:

    @allure.title('Раздел "Вопросы о важном"')
    @pytest.mark.parametrize(AnswerTexts)
    def test_question(self, driver, number, expected_answer):

        main_page = MainPage(driver)
        main_page.scroll_to_element()
        main_page.click_question(number)
        answer = main_page.wait_and_find_element(MainPageLocators.AnswersLocators(number))
        assert answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым'