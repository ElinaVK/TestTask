from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocatorsImage:
    LOCATOR_YANDEX_SEARCH_ALL_LINKS = (By.CSS_SELECTOR, "a")
    LOCATOR_YANDEX_IMAGE_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item")
    LOCATOR_YANDEX_INPUT_TEXT = (By.CSS_SELECTOR, ".input__control.mini-suggest__input")
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CSS_SELECTOR, "a.serp-item__link")
    LOCATOR_YANDEX_PREVIEW_IMAGE = (By.CLASS_NAME, "MMImage-Preview")
    LOCATOR_YANDEX_PREVIEW_IMAGE_BTN_NEXT = (By.CLASS_NAME, "MediaViewer_theme_fiji-ButtonNext")
    LOCATOR_YANDEX_PREVIEW_IMAGE_BTN_PREV = (By.CLASS_NAME, "MediaViewer_theme_fiji-ButtonPrev")

class SearchHelperImage(BasePage):

    def find_link_on_image_with_text(self, word):
        img_href=''
        links_img_all = self.find_elements(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_SEARCH_ALL_LINKS,time=2)
        for item in links_img_all:
            if (item.text == word):
                img_href = item.get_attribute("href")
                item.click()
                break
        self.driver.switch_to.window(self.driver.window_handles[1])
        return img_href

    def open_first_category(self):
        first_category = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_IMAGE_CATEGORY,time=2)
        first_category.click()
        name_first_category = first_category.text
        return name_first_category

    def search_input_value(self):
        input_element = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_INPUT_TEXT,time=2)
        text_in_search_input = input_element.get_property("value")
        return text_in_search_input

    def get_image_link(self):
        search_container = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_PREVIEW_IMAGE,time=2)
        img_src = search_container.get_attribute("src")
        return img_src

    def preview_image(self):
        self.driver.get(self.driver.current_url)
        search_field = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_FIRST_IMAGE,time=2)
        search_field.click()
        preview_image = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_PREVIEW_IMAGE,time=2)
        return preview_image.is_displayed()

    def search_btn_next(self):
        search_btn = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_PREVIEW_IMAGE_BTN_NEXT,time=2)
        return search_btn.click()

    def search_btn_prev(self):
        search_btn = self.find_element(YandexSeacrhLocatorsImage.LOCATOR_YANDEX_PREVIEW_IMAGE_BTN_PREV,time=2)
        return search_btn.click()
