from andpylib.Mobile import Mobile
from appium.webdriver.connectiontype import ConnectionType
import time

class KeyEvents(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    # 返回键
    def back(self,deviceName):
        Mobile.phone[deviceName].keyevent(4)

    # home键
    def home(self,deviceName):
        Mobile.phone[deviceName].keyevent(3)

    # 菜单键
    def menu(self,deviceName):
        Mobile.phone[deviceName].keyevent(82)

    # 电源键
    def power(self,deviceName):
        Mobile.phone[deviceName].keyevent(26)

    # 音量加
    def volumeUp(self,deviceName):
        Mobile.phone.keyevent(24)

    # 音量减
    def volumeDown(self,deviceName):
        Mobile.phone[deviceName].keyevent(25)

    # 拍照键
    def camera(self,deviceName):
        Mobile.phone[deviceName].keyevent(27)

    # 清除
    def clear(self,deviceName):
        Mobile.phone[deviceName].clear()

    def sleep(self,value):
        time.sleep(value)

    # 输入
    def sendKey_Id(self,button,value,deviceName):
        Mobile.phone[deviceName].find_element_by_id(button).send_keys(value)

    def sendKey_classname(self,button,value,deviceName):
        Mobile.phone[deviceName].find_element_by_class_name(button).send_keys(value)

    def sendKey_android(self,value,deviceName):
        Mobile.phone[deviceName].find_element_by_android_uiautomator(value)

    # 点击
    def clickKey_id(self, button,deviceName):
        Mobile.phone[deviceName].find_element_by_id(button).click()

    def clickKey_classname(self, button,deviceName):
        Mobile.phone[deviceName].find_element_by_class_name(button).click()

    # 网络切换 开启 wifi
    def setNetwork_wifi(self,deviceName):
        Mobile.phone[deviceName].set_network_connection(ConnectionType.WIFI_ONLY)

    # 网络切换 飞行模式
    def setNetwork_airplane(self,deviceName):
        Mobile.phone[deviceName].set_network_connection(ConnectionType.AIRPLANE_MODE)

    # 网络切换 关闭网络连接
    def setNetwork_none(self,deviceName):
        Mobile.phone[deviceName].set_network_connection(ConnectionType.NO_CONNECTION)





