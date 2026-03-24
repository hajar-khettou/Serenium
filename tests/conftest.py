import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--disable-notifications")

    browser = webdriver.Edge(options=edge_options)
    browser.implicitly_wait(0)

    yield browser

    browser.quit()