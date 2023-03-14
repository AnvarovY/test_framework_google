from .base_page import BasePage
from .locators import GoogleHomePageLocators
from .search_results_page import GoogleSearchResultsPage


class GoogleHomePage(BasePage):
    url = "http://google.com"

    def open(self) -> None:
        self.open_url(self.url)

    def get_hints(self) -> list:
        hints_list = self.get_elements(GoogleHomePageLocators.HINT_TEXT)
        return [x.text.lower() for x in hints_list]

    def go_to_search_result_page(self):
        self.get_element(GoogleHomePageLocators.SEARCH_BUTTON).click()
        return GoogleSearchResultsPage(driver=self.driver)

    def is_search_field_displayed(self) -> bool:
        return self.element_is_present(GoogleHomePageLocators.SEARCH_FIELD).is_displayed()

    def is_hints_table_present(self) -> bool:
        return self.element_is_present(GoogleHomePageLocators.HINTS_TABLE).is_displayed()

    def send_search_query(self, value) -> None:
        search_field = self.element_is_clickable(GoogleHomePageLocators.SEARCH_FIELD)
        self.send_keys_to_element(search_field, value)
