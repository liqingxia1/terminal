from andpylib.Mobile import Mobile
from andpylib.Setting import Setting

class ShortcutMenu(Mobile):
    def notice(self):
        Mobile.phone.open_notifications()  # 打开通知界面
        ele = Mobile.phone.find_element_by_id('com.android.systemui:id/header')
        location = ele.location
        size1 = ele.size
        x1 = location['x'] + int(size1['width'] * 0.5)
        x2 = location['x'] + int(size1['width'] * 0.8)
        y = location['x'] + int(size1['height'] * 0.5)
        Mobile.phone.swipe(start_x=x1, start_y=y, end_x=x2, end_y=y, duration=500)

# if __name__ == '__main__':
#     s = ShortcutMenu()
#     s.android("5.1.1", 'com.android.settings', '.Settings')
#     st = Setting()
#     s.notice()