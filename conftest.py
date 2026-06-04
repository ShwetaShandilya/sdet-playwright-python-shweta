import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


load_dotenv()


@pytest.fixture(scope="session")
def browser_type_name():
    return os.getenv("BROWSER", "chromium")


@pytest.fixture(scope="session")
def headless():
    return os.getenv("HEADLESS", "true").lower() == "true"


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://practice.expandtesting.com")


@pytest.fixture(scope="function")
def page(browser_type_name, headless):
    with sync_playwright() as p:
        browser_type = getattr(p, browser_type_name)
        browser = browser_type.launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, page):
    yield

    if request.node.rep_call.failed:
        screenshot_name = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_name)
        print(f"Screenshot saved: {screenshot_name}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)