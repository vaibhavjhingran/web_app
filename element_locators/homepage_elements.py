class HomePageElements:

    homepage_icon_css = "a[href$='news']"
    header_links_css = {
        "new": ".pagetop > a:nth-child(2)",
        "past": ".pagetop > a:nth-child(3)",
        "comments": ".pagetop > a:nth-child(4)",
        "ask": ".pagetop > a:nth-child(5)",
        "show": ".pagetop > a:nth-child(6)",
        "jobs": ".pagetop > a:nth-child(7)",
        "submit": ".pagetop > a:nth-child(8)",
    }
    footer_api_css = ".yclinks > a:nth-child(4)"