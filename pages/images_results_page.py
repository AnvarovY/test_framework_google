from selenium.webdriver.remote.webelement import WebElement
from .locators import GoogleImagesResultsPageLocators
from .base_page import BasePage


class GoogleImagesResultsPage(BasePage):
    def click_previous_button(self) -> None:
        self.element_is_clickable(GoogleImagesResultsPageLocators.PREV_BUTTON).click()

    def click_next_button(self) -> None:
        self.element_is_clickable(GoogleImagesResultsPageLocators.NEXT_BUTTON).click()

    def get_preview_image_source(self) -> str:
        return self.__get_image_preview_element().get_attribute('src')

    def get_preview_image_name(self) -> str:
        return self.__get_image_preview_element().get_attribute('alt')

    def get_selected_image_name(self) -> str:
        return self.__get_selected_image_element().get_attribute('alt')

    def select_image_by_index(self, index: int = 0) -> None:
        images = self.__get_images()
        images[index].click()

    def __get_images(self) -> list:
        return self.elements_are_present(GoogleImagesResultsPageLocators.IMAGES)

    def __get_image_preview_element(self) -> WebElement:
        return self.element_is_visible(GoogleImagesResultsPageLocators.BIG_IMAGE)

    def __get_selected_image_element(self) -> WebElement:
        return self.element_is_visible(GoogleImagesResultsPageLocators.SELECTED_IMAGE)
