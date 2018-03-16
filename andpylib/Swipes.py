from andpylib.Mobile import Mobile

class Swipes(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 获得机器屏幕大小x,y


    # 屏幕向上滑动
    def swipeUp(self):
        x = Mobile.phone.get_window_size()['width']
        y = Mobile.phone.get_window_size()['height']
        x1 = int(x * 0.5)  # x坐标
        y1 = int(y * 0.71)  # 起始y坐标
        y2 = int(y * 0.3)  # 终点y坐标
        Mobile.phone.swipe(x1, y1, x1, y2, 2000)


    # 屏幕向下滑动
    def swipeDown(self):
        x = Mobile.phone.get_window_size()['width']
        y = Mobile.phone.get_window_size()['height']
        x1 = int(x * 0.5)  # x坐标
        y1 = int(y * 0.3)  # 起始y坐标
        y2 = int(y * 0.7)  # 终点y坐标
        Mobile.phone.swipe(x1, y1, x1, y2, 2000)


    # 屏幕向左滑动
    def swipLeft(self):
        x = Mobile.phone.get_window_size()['width']
        y = Mobile.phone.get_window_size()['height']
        x1 = int(x * 0.75)
        y1 = int(y * 0.5)
        x2 = int(y * 0.05)
        Mobile.phone.swipe(x1, y1, x2, y1, 2000)


    # 屏幕向右滑动
    def swipRight(self):
        x = Mobile.phone.get_window_size()['width']
        y = Mobile.phone.get_window_size()['height']
        x1 = int(x * 0.05)
        y1 = int(y * 0.5)
        x2 = int(y * 0.75)
        Mobile.phone.swipe(x1, y1, x2, y1, 2000)


    def swipeDown2(self):
        x = Mobile.phone.get_window_size()['width']
        y = Mobile.phone.get_window_size()['height']
        x1 = int(x * 0.5)  # x坐标
        y1 = int(y * 0.1)  # 起始y坐标
        y2 = int(y * 0.7)  # 终点y坐标
        Mobile.phone.swipe(x1, y1, x1, y2, 2000)
