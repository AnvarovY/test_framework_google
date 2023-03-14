from pages.home_page import GoogleHomePage


def test_google_search(driver):
    home_page = GoogleHomePage(driver)
    home_page.open()
    assert home_page.is_search_field_displayed(), 'Search field not found on page'

    bank_name = 'Совкомбанк'
    home_page.send_search_query(bank_name)
    assert home_page.is_hints_table_present(), 'Hint table not found on page'
    hints_result = home_page.get_hints()
    filtered_hints = list(filter(lambda x: bank_name.lower() in x, hints_result))
    assert len(filtered_hints) == len(hints_result), f'Not all results contain "{bank_name}": {hints_result}'

    results_page = home_page.go_to_search_result_page()
    assert results_page.is_search_results_table_present(), 'Result table not found on page'

    bank_url = 'sovcombank.ru'
    expected_hints_num = 5
    result = results_page.get_link_search_result()[0:expected_hints_num]
    filtered_results = list(filter(lambda x: bank_url in x, result))
    assert len(filtered_results) == expected_hints_num, f'Found the links that do not have a link to {bank_url}'


def test_google_images(driver):
    home_page = GoogleHomePage(driver)
    home_page.open()
    assert home_page.is_search_field_displayed(), 'Search field not found on page'

    bank_name = 'Совкомбанк'
    home_page.send_search_query(bank_name)
    assert home_page.is_hints_table_present(), 'Hint table not found on page'
    hints_result = home_page.get_hints()
    filtered_hints = list(filter(lambda x: bank_name.lower() in x, hints_result))
    assert len(filtered_hints) == len(hints_result), f'Not all results contain "{bank_name}": {hints_result}'

    results_page = home_page.go_to_search_result_page()
    assert results_page.is_search_results_table_present(), 'Result table not found on page'

    bank_url = 'sovcombank.ru'
    expected_hints_num = 5
    result = results_page.get_link_search_result()[0:expected_hints_num]
    filtered_results = list(filter(lambda x: bank_url in x, result))
    assert len(filtered_results) == expected_hints_num, f'Found the links that do not have a link to {bank_url}'

    assert results_page.is_images_button_present(), 'Images button not found on page'
    images_page = results_page.go_to_images_results_page()
    images_page.select_image_by_index(1)
    selected_image_name = images_page.get_selected_image_name()
    preview_image_name = images_page.get_selected_image_name()
    assert selected_image_name == preview_image_name, 'Image description is not the same, it opened ' \
                                                      'a different image!'

    preview_image_src = images_page.get_preview_image_source()
    images_page.click_next_button()
    next_preview_image_src = images_page.get_preview_image_source()
    assert preview_image_src != next_preview_image_src, 'Image resource matched, the image did not change'

    images_page.click_previous_button()
    new_preview_image_src = images_page.get_preview_image_source()
    assert preview_image_src == new_preview_image_src, 'Image resource did not match, the first image did not return'
