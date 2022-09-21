from YandexPages import SearchHelper
from selenium.webdriver.common.keys import Keys

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site("https://ya.ru/")
    yandex_main_page.input_search()
    yandex_main_page.enter_word_in_input_search("Тензор")
    yandex_main_page.suggest_is_displayed()
    yandex_main_page.table_results(Keys.ENTER)
    first_link = yandex_main_page.check_first_link()
    assert "https://tensor.ru/" == first_link, "The links are not the same"

