from andpylib.Mobile import Mobile
from andpylib.Setting import Setting
from andpylib.ShortcutMenu import ShortcutMenu
from andpylib.Browser import Browser
from andpylib.KeyEvents import KeyEvents
from andpylib.Swipes import Swipes
import time

class DataConnection(Mobile):
    def wifiOpen(self):
        s=KeyEvents()
        s.setNetwork_wifi()
        time.sleep(15)
        Mobile.phone.quit()
        s = Browser()
        s.android("6.0.1", 'com.android.chrome', 'org.chromium.chrome.browser.ChromeTabbedActivity')
        info = s.linkbaidu()
        return info


    def mobileNetwork(self):
        # sm=ShortcutMenu() #打开通知界面
        # sm.notice()
        time.sleep(2)
        s = Swipes()
        s.swipeUp()

        code = u'new UiSelector().text("移动数据")'
        Mobile.phone.find_element_by_android_uiautomator(code).click()
        # Mobile.phone.quit()
        s = Browser()
        # s.android("6.0.1", 'com.android.chrome', 'org.chromium.chrome.browser.ChromeTabbedActivity')
        info=s.linkbaidu()
        return info



if __name__ == '__main__':
    s = DataConnection()
    s.android("6.0.1", 'com.android.chrome', 'org.chromium.chrome.browser.ChromeTabbedActivity')
    s.mobileNetwork()
    # ss=Browser()
    # ss.linkbaidu()
    # s.wifi()
