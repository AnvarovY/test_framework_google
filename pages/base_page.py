from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def element_is_visible(self, locator: list, timeout=5) -> WebElement:
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: list, timeout=5) -> list:
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: list, timeout=5) -> WebElement:
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator: list, timeout=5) -> list:
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator: list, timeout=5) -> WebElement:
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator: list, timeout=5) -> WebElement:
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_element(self, locator: list) -> WebElement:
        return self.driver.find_element(*locator)

    def get_elements(self, locator: list) -> list:
        return self.driver.find_elements(*locator)

    def go_to_element(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # noinspection PyMethodMayBeStatic
    def send_keys_to_element(self, element: WebElement, value: str) -> None:
        element.clear()
        element.send_keys(value)

    def wait_to_load_source(self, locator: list, attr: str, value: str) -> None:
        wait(self.driver, 10).until(
            lambda wd: value not in wd.find_element(*locator).get_attribute(attr))
