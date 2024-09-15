import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.title('Ожидание загрузки и поиск элемента на странице')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.title('Ожидание загрузки и клик по элементу')
    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.title('Открытие страницы по заданному адресу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.title('Прокрутка до указанного элемента')
    def scroll_to_element(self, element):
        element = self.wait_and_find_element(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.title('Ожидание загрузки и внесение данных')
    def wait_and_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)


    @allure.step('Переход на вторую вкладку браузера')
    def switch_second_browser_window(self, locator):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_and_find_element(locator)