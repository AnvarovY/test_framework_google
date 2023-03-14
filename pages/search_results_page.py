from .locators import GoogleSearchResultsPageLocators
from .base_page import BasePage
from .images_results_page import GoogleImagesResultsPage


class GoogleSearchResultsPage(BasePage):
    def go_to_images_results_page(self):
        button = self.get_element(GoogleSearchResultsPageLocators.IMAGES_BUTTON)
        button.click()
        return GoogleImagesResultsPage(driver=self.driver)

    def is_images_button_present(self) -> bool:
        return self.element_is_present(GoogleSearchResultsPageLocators.SEARCH_RESULTS_TABLE).is_displayed()

    def is_search_results_table_present(self) -> bool:
        return self.element_is_present(GoogleSearchResultsPageLocators.SEARCH_RESULTS_TABLE).is_displayed()

    def get_link_search_result(self) -> list:
        result = self.get_elements(GoogleSearchResultsPageLocators.SEARCH_RESULT_LINK)
        return [x.get_attribute("href") for x in result]
