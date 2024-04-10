class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def open2window(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])
