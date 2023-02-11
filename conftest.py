import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='function')  # use scope for TearDown and TearUp driver after everyone test
def driver():
    options = webdriver.ChromeOptions()

    '''to ignore "USB: usb_device_handle_win.cc:1046 Failed to read descriptor
    from node connection" and "Bluetooth: bluetooth_adapter_winrt.cc:1074 Getting Default Adapter failed.'''

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    yield driver  # return generator
    driver.quit()
