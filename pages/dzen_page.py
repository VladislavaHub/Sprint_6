from pages.base_page import BasePage


class DzenPage(BasePage):

    def switch_dzen_window(self, driver):
        return driver.switch_to.window(driver.window_handles[1])

    def get_current_url(self, driver):
        return driver.current_url