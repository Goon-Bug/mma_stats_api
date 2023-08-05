import utilities as ut
from locators import Elements

e = Elements()

dict_elements = {
    "name": e.fighter_name,
    "age": e.age,
    "nationality": e.nationality,
    "organization": e.organization,
    "height": e.height,
    "weight": e.weight,
    "wins": e.wins,
    "losses": e.losses,
    "kos": e.kos,
    "submissions": e.submissions,
    "decisions": e.decisions,
}


def accept_cookies(driver):
    """
    Accepts cookie pop ups

    :param driver: selenium webdriver
    :param by: selenium locator
    """
    ut.find_element(driver, e.accept_all, "click")
    ut.find_element(driver, e.accept_cookies, "click")


def click_on_latest_rankings(driver):
    """
    Directs to latest rankings page and returns the url

    :param driver: selenium web driver
    :return: str
    """
    ut.find_element(driver, e.division, "click")
    return driver.current_url


def select_division(driver, weight):
    """
    Selects a fighter on the current division page based on the inputted weight index

    :param driver: selenium web driver
    :param by: selenium locator
    :param weight: int
    :return division_url: url (str)
    """
    new_xpath = ut.get_xpath(weight, -2, e.start_weight)
    ut.find_element(driver, (e.start_weight[0], new_xpath), "click")
    division_url = driver.current_url
    return division_url


def select_fighter(driver, fighter):
    """
    Selects a fighter on the current division page based on the inputted fighter index

    :param driver: selenium web driver
    :param by: selenium locator
    :param fighter: int
    """
    new_xpath = ut.get_xpath(fighter, -4, e.no1_fighter)
    ut.find_element(driver, (e.no1_fighter[0], new_xpath), "click")


def save_fighter_stats(driver):
    """
    Saves fighter stats into dictionary and then inputs that dictionary into database

    :param driver: webdriver
    """
    d = {}

    for stat in dict_elements:
        s = ut.find_element(driver, dict_elements[stat], "save")

        if s is None:
            s = ut.find_element(driver, dict_elements[stat], "save")

        if stat == "organization":
            s = s.text.split(' ')[0].upper()
            if s == "PROFESSIONAL":
                s = "PFL"
        else:
            s = s.text

        d[stat] = s

    return d
