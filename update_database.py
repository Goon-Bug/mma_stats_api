from locators import Elements
import processes as p
import database as db
from selenium import webdriver
import chromedriver_autoinstaller

dict_divisions = {
    1: "heavyweight",
    2: "lightheavyweight",
    3: "middleweight",
    4: "welterweight",
    5: "lightweight",
    6: "featherweight",
    7: "bantamweight",
    8: "flyweight",
    9: "wfeatherweight",
    10: "wbantamweight",
    11: "wflyweight",
    12: "wstrawweight",
    13: "watomweight"
}


def driver_options():
    """
    This sets all the driver options including driver path and strategy
    """
    chromedriver_autoinstaller.install()
    op = webdriver.ChromeOptions()
    op.add_argument("start-maximised")
    op.add_argument("enable-automation")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-shm-usage")
    op.add_argument("--disable-browser-side-navigation")
    op.add_argument("--disable-gpu")
    op.add_argument("--dns-prefetch-disable")
    op.add_argument("user-data-dir=selenium")
    op.page_load_strategy = "eager"
    return webdriver.Chrome(options=op)


def update_database(driver, divisions):
    """
    Fetches new stats from website and updates the database

    :param driver: selenium webdriver
    :param divisions: 'all' or [1, 3, 6...]
    """
    divisions_to_update = []
    if divisions == "all":
        db.delete_all_records("stats")
        divisions_to_update = range(1, 14)
    else:
        for num in divisions:
            divisions_to_update.append(num)
            db.delete_records_where("stats", "division", dict_divisions[num])

    for weight_ind in divisions_to_update:
        p.select_division(driver, weight_ind)

        for fighter_ind in range(2, 12):
            p.select_fighter(driver, fighter_ind)
            d = p.save_fighter_stats(driver)
            d["division"] = dict_divisions[weight_ind].upper()
            db.insert_row('stats', **d)
            driver.execute_script("window.history.go(-1)")
        driver.get(list_of_div_url)
        print(f"{d['division']} Division update Complete")


driver = driver_options()
e = Elements()

# get page and accept cookies
driver.get(e.start_page)
# p.accept_cookies(driver, By) uncomment if cookies pop up pops up

list_of_div_url = p.click_on_latest_rankings(driver)

update_database(driver, ["all"])

print("Update Complete")

driver.quit()
