from selenium.webdriver.common.by import By


class Elements:
    def __init__(self):
        self.start_page = "https://www.sherdog.com/news/rankings/list"
        self.accept_all = (By.XPATH, "//button[text()='Accept all']")
        self.accept_cookies = (By.LINK_TEXT, "Accept Cookies")  # link text
        self.division = (By.LINK_TEXT, "Sherdog’s Official Mixed Martial Arts Rankings")
        self.start_weight = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/article/div[1]/div[1]/div[2]/strong/a[1]")
        self.starting_class = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/article/div[1]/div[1]/div[2]/strong/a[1]")
        self.no1_fighter = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/article/div[1]/div[1]/div[2]/h2[2]/a")

        self.fighter_name = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[1]/div[1]/h1/span")
        self.nationality = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[1]/div[1]/div/div/span/strong")
        self.age = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]/b")
        self.organization = (By.XPATH, "//*[@itemprop='award']")
        self.height = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[2]/b")
        self.weight = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[2]/b")
        self.wins = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[2]")
        self.losses = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]")
        self.kos = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]")
        self.submissions = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[5]/div[1]")
        self.decisions = (By.XPATH, "/html/body/div[4]/div[3]/div[1]/div/section[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[7]/div[1]")
