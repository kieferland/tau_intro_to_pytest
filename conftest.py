import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture
def page() -> Page:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()