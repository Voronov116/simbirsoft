
class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self, url):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
