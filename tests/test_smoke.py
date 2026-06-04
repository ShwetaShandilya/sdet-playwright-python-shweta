import pytest
from pages.automation_page import AutomationPage
from utils.helpers import read_json_file


test_data = read_json_file("test_data/home_page_data.json")


@pytest.mark.smoke
def test_homepage_title(page, base_url):
    automation_page = AutomationPage(page)

    automation_page.navigate_to_homepage(base_url)

    expected_title = test_data["home_page"]["expected_title_text"]

    assert expected_title in automation_page.get_homepage_title()