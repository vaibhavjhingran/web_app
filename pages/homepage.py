class HomePage:

    homepage_icon = "a[href$='news']"
    header_links = {
        "new": ".pagetop > a:nth-child(2)",
        "past": ".pagetop > a:nth-child(3)",
        "comments": ".pagetop > a:nth-child(4)",
        "ask": ".pagetop > a:nth-child(5)",
        "show": ".pagetop > a:nth-child(6)",
        "jobs": ".pagetop > a:nth-child(7)",
        "submit": ".pagetop > a:nth-child(8)",
        }

    def __init__(self, driver):
        self.driver = driver

    def click_home_icon(self):
        banner_icon = self.driver.find_element_by_css_selector(self.homepage_icon)
        banner_icon.click()

    def assert_title(self):
        title = 'Hacker News'
        assert title in self.driver.title

