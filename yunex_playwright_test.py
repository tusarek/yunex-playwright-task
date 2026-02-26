import re
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.example.com"

@pytest.fixture(autouse=True)
def setup_page(page: Page):
    """Setup function to navigate to the base URL before each test."""
    page.goto(BASE_URL)
    yield
    # Any teardown steps can be added here if necessary

def test_website_title(page: Page):
    """Tests whether the title of the example.com website is correct."""
    expect(page).to_have_title("Example Domain")
    # expect(page).to_have_title(re.compile(r"Example Domain"))

def test_text_of_first_paragraph_contains_info(page: Page):
    """Tests whether the first paragraph contains info about used specifications 'RFC 2606' after clicking 'Learn more' link on the example.com website."""
    page.get_by_role("link", name="Learn more").click()
    first_paragraph = page.locator("p").first
    expect(first_paragraph).to_contain_text("RFC 2606")