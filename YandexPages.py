from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CLASS_NAME, "search3__input")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup")
    LOCATOR_YANDEX_FIRST_LI_LINK_ON_PAGE = (By.CLASS_NAME, "Link.Link_theme_normal.OrganicTitle-Link.organic__url")
    LOCATOR_YANDEX_TABLE_RESULT = (By.CLASS_NAME, "serp-list")

class SearchHelper(BasePage):

    def input_search(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        return search_field

    def enter_word_in_input_search(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def suggest_is_displayed(self):
        suggest = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST,time=2)
        return suggest.is_displayed()

    def table_results(self, key):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(key)
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_TABLE_RESULT,time=2).click()

    def check_first_link(self):
        link = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_LI_LINK_ON_PAGE,time=2)
        val = link.get_attribute("href")
        return val