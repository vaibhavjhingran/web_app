from element_locators.homepage_elements import HomePageElements


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_home_icon(self):
        banner_icon = self.driver.find_element_by_css_selector(HomePageElements.homepage_icon_css)
        banner_icon.click()

    def click_api_link_in_footer(self):
        api = self.driver.find_element_by_css_selector(HomePageElements.footer_api_css)
        api.click()

    def click_all_header_links(self):
        for each in HomePageElements.header_links_css:
            item = self.driver.find_element_by_css_selector(HomePageElements.header_links_css[each])
            item.click()

    def assert_title(self):
        title = 'Hacker News'
        assert title in self.driver.title
