'''
1. если зайти на https://ya.ru/, то там отсутствуют компонента "Картинки" с ссылкой,
поэтому в качестве входа была использована "https://yandex.ru/search"
2. Использована ссылка у "Картинки" - https://yandex.ru/images/?from=tabbar'''
from YandexPagesImages import SearchHelperImage

images_link = "https://yandex.ru/images/?from=tabbar"
def test_yandex_search_images(browser):
    yandex_main_page = SearchHelperImage(browser)
    yandex_main_page.go_to_site("https://yandex.ru/search")

    current_link = yandex_main_page.find_link_on_image_with_text("Картинки")
    assert images_link == current_link, "Invalid link"

    category_first = yandex_main_page.open_first_category()
    value_in_search_input = yandex_main_page.search_input_value()
    assert category_first == value_in_search_input, "Category names don't match"

    yandex_main_page.preview_image()
    first_image_src = yandex_main_page.get_image_link()

    yandex_main_page.search_btn_next()

    second_image_src = yandex_main_page.get_image_link()
    assert first_image_src != second_image_src, "The image didn't change"

    yandex_main_page.search_btn_prev()

    third_image_src = yandex_main_page.get_image_link()
    assert first_image_src == third_image_src, "The image should be the same"

