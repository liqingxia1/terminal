#coding=utf-8
import time
from appium import webdriver
from andpylib.Mobile import Mobile
from andpylib.Swipes import Swipes
from andpylib.KeyEvents import KeyEvents

class Setting(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'  # ROBOT_LIBRARY_SCOPE为ROBOT库范围，这个范围有三个等级，分别是TEST CASE、TEST SUITE、GLOBAL三个等级，默认是TEST CASE，每个test case中引用都会实例化一次

    ########################################################################################
    #                                   打开设置列表中的菜单                               #
    ########################################################################################

    # 点击 搜索 菜单
    def click_search(self):
        Mobile.phone.find_element_by_id('search').click()

    # 点击 McWill数据 菜单
    def click_mcWill(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("McWiLL数据")').click()

    def click_wifi(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("WLAN")').click()

    def click_bluetooth(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("蓝牙")').click()

    def click_simCard(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("SIM卡")').click()

    def click_dataUsage(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("流量使用情况")').click()

    def click_more(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("更多")').click()

    def click_display(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("显示")').click()

    def click_soundAndNotification(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("提示音和通知")').click()

    def click_apps(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("应用")').click()

    def click_phone(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("电话")').click()

    def click_storageAndUsb(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("存储设备和 USB")').click()

    def click_battery(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("电池")').click()

    def click_memory(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("内存")').click()

    def click_systemProfiles(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("情景模式")').click()

    def click_location(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("位置信息")').click()

    def click_security(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("安全")').click()

    def click_account(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("账户")').click()

    def click_google(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("Google")').click()

    def click_languageAndInput(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("语言和输入法")').click()

    def click_backupAndReset(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("备份和重置")').click()

    def click_dateAndTime(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("日期和时间")').click()

    def click_scheduledPowerOnAndOff(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("定时开关机")').click()

    def click_accessibility(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("无障碍")').click()

    def click_printing(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("打印")').click()

    def click_developerOptions(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("开发者选项")').click()

    def click_aboutPhone(self):
        Mobile.phone.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("关于手机")').click()


def oneTest():
    # 实例化对象
    C8_Device = Setting()
    # 启动测试机，并设置APP包.
    listV =["5.1.1","6.0.1"]
    listP =["com.android.settings","com.android.settings"]
    listA =["Settings","Settings"]
    listU =['36bb3446', 'c47ad30c']
    # C8_Device.android('6.0.1', 'com.android.settings', '.Settings')
    C8_Device.androidThread(listV,listP,listA,listU)
    # 实例化 滑动与输入 对象
    swp = Swipes()
    # keyevt = KeyEvents()

    # # 点击搜索，并输入wlan与123456进行搜索，再点击搜索界面左上角返回图标
    # C8_Device.click_search()
    # keyevt.sendKey_Id("search_src_text","wlan")
    # C8_Device.phone.find_element_by_id("search_src_text").set_text("123456")
    # keyevt.clickKey_classname("android.widget.ImageButton")
    #
    #
    # # 等待2秒，再点击mcWill，并返回
    # time.sleep(1)
    # C8_Device.click_mcWill()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_wifi()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_bluetooth()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_simCard()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_dataUsage()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_more()
    # keyevt.back()
    #
    # # 等待1秒，并向上滑动一屏
    # time.sleep(1)
    # swp.swipeUp()
    # swp.swipeUp()
    #
    # time.sleep(1)
    # C8_Device.click_display()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_soundAndNotification()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_apps()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_phone()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_storageAndUsb()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_battery()
    # keyevt.back()
    #
    # time.sleep(1)
    # C8_Device.click_memory()
    # keyevt.back()

    # 等待2秒，并向上滑动两屏，点击 关于手机
    time.sleep(2)
    swp.swipeUp()
    swp.swipeUp()

    swp.swipeUp()
    swp.swipeUp()
    # C8_Device.click_aboutPhone()
    # C8_Device.phone.close_app()

if __name__ == '__main__':
    # 进行代码调试
    oneTest()

