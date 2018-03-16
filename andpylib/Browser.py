from andpylib.Mobile import Mobile


class Browser(Mobile):
    def linkbaidu(self):
        Mobile.phone.get("http://www.baidu.com")
        try:
            baidu = Mobile.phone.find_element_by_css_selector('#index-form #index-bn').text
            print(baidu)
            baidu.quit()
        except Exception:
            print("不可以连接到百度")

            return 0
        else:
            if baidu != "":
                print("可以正确连接到百度")
                return 1


# if __name__ == '__main__':
#     s = Browser()
#     s.android("6.0.1", 'com.android.chrome', 'org.chromium.chrome.browser.ChromeTabbedActivity')
#     s.linkbaidu()