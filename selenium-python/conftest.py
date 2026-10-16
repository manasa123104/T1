import os

import pytest
from selenium import webdriver


@pytest.fixture
def base_url():
    return os.environ.get("APP_BASE_URL", "http://localhost:8080").rstrip("/")


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "true") != "false":
        options.add_argument("--headless=new")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()
