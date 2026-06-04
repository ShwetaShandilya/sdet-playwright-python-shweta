import pytest
from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.smoke
def test_homepage_title(page, base_url):

    logger.info(f"Opening {base_url}")

    page.goto(base_url)

    page.wait_for_timeout(5000)

    logger.info("Verifying page title")

    assert "Automation Testing Practice Website" in page.title()