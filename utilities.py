from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from locators import Elements

e = Elements()


def find_element(driver, el, action):
    """
    Helper function that allows for shorthand use of 'WebDriverWait.until...' whilst
    also handling errors

    :param driver: selenium webdriver
    :param el: tup (by, element)
    """
    i = 1
    while i > 0:
        try:
            wait = WebDriverWait(driver, 10)
            if action == "click":
                element = wait.until(EC.element_to_be_clickable(el))
                element.click()
                break
            else:
                element = wait.until(EC.presence_of_element_located(el))
                return element
        except (TimeoutException, StaleElementReferenceException, WebDriverException) as err:
            print(f"Finding element failed. Refreshing page and trying again. {i} tries left")
            print(str(err))
            i -= 1
            driver.refresh()


def get_xpath(var, index, xpath):
    """
    Gets the xpath based on the inputted variables

    :param var: int
    :param index: int
    :param xpath: str
    :return: str
    """
    xpath_list = list(xpath[1])
    xpath_list[index] = str(var)
    return "".join(xpath_list)

