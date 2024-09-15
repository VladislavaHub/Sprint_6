from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGO_SCOOTER = By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]' # Логотип Самокат

    LOGO_YANDEX = By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]' # Логотип Яндекс

    # Кнопки на главной странице
    ORDER_BUTTON_IN_MAIN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    ORDER_BUTTON_IN_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    MAIN_HEADER = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')
    TITLE_OF_PAGE = (By.TAG_NAME, 'title')


# Вопросы в разделе "Вопросы о важном"
class QuestionLocators:
    HOW_MUCH_QUESTION = (By.XPATH, ".//*[contains(text(), 'Сколько это стоит')]")
    WANT_MORE_SCOOTERS_QUESTION = (By.XPATH, ".//*[contains(text(), 'Хочу сразу несколько')]")
    TIME_CALCULATION_QUESTION = (By.XPATH, ".//*[contains(text(), 'время аренды')]")
    ORDER_TODAY_QUESTION = (By.XPATH, ".//*[contains(text(), 'прямо на сегодня')]")
    ORDER_EXTEND_QUESTION = (By.XPATH, ".//*[contains(text(), 'продлить заказ или вернуть')]")
    CHARGE_QUESTION = (By.XPATH, ".//*[contains(text(), 'зарядку вместе с самокатом')]")
    ORDER_CANCELLATION_QUESTION = (By.XPATH, ".//*[contains(text(), 'отменить заказ')]")
    NOT_IN_MOSCOW_QUESTION = (By.XPATH, ".//*[contains(text(), 'жизу за МКАДом')]")

# Ответы в разделе "Вопросы о важном"
class AnswersLocators:
    HOW_MUCH_ANSWER = (By.XPATH, ".//p[contains(text(), 'Сутки — 400 рублей')]")
    WANT_MORE_SCOOTERS_ANSWER = (By.XPATH, ".//p[contains(text(), 'один заказ — один самокат')]")
    TIME_CALCULATION_ANSWER = (By.XPATH, ".//p[contains(text(), 'Отсчёт времени аренды начинается с момента')]")
    ORDER_TODAY_ANSWER = (By.XPATH, ".//p[contains(text(), 'начиная с завтрашнего дня')]")
    ORDER_EXTEND_ANSWER = (By.XPATH, ".//p[contains(text(), 'всегда можно позвонить в поддержку')]")
    CHARGE_ANSWER = (By.XPATH, ".//p[contains(text(), 'к вам с полной зарядкой')]")
    ORDER_CANCELLATION_ANSWER = (By.XPATH, ".//p[contains(text(), 'пока самокат не привезли')]")
    NOT_IN_MOSCOW_ANSWER = (By.XPATH, ".//p[contains(text(), 'И Москве, и Московской области')]")