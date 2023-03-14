from selenium.webdriver.common.by import By


class GoogleHomePageLocators:
    SEARCH_FIELD = (By.NAME, 'q')
    HINTS_TABLE = (By.CSS_SELECTOR, 'div.erkvQe > div > ul')
    HINT_TEXT = (By.CSS_SELECTOR, 'ul>li .wM6W7d')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.aajZCb center > [name = btnK]')


class GoogleSearchResultsPageLocators:
    SEARCH_RESULTS_TABLE = (By.CSS_SELECTOR, '#search')
    SEARCH_RESULT_LINK = (By.CSS_SELECTOR, 'div.BYM4Nd a')
    IMAGES_BUTTON = (By.CSS_SELECTOR, '.hdtb-mitem:nth-child(3)>a')


class GoogleImagesResultsPageLocators:
    BIG_IMAGE = (By.CSS_SELECTOR, '.BIB1wf a>img')
    IMAGES_CONTAINER = (By.CSS_SELECTOR, "div.islrc")
    IMAGES = (By.CSS_SELECTOR, "div.islrc>div>a:nth-child(2) img")
    NEXT_BUTTON = (By.CSS_SELECTOR, '.BIB1wf [jsaction="trigger.j5PO8b"]')
    PREV_BUTTON = (By.CSS_SELECTOR, '.BIB1wf [jsaction="trigger.BXCnre"]')
    SELECTED_IMAGE = (By.CSS_SELECTOR, 'div.fT6ABc>a:nth-child(2) img')
