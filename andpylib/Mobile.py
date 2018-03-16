from appium import webdriver
from multiprocessing import Process
import Collocations
import threading

from http import HTMLTestRunner


class Mobile():
    phoneParameter = []        # 存储设备参数
    phoneStart = []             # 存储需要启动的进程
    phone = {}                  # 存储启动的设备session

    def android(self, deviceName, port, platformVersion, appPackage, appActivity, udid):
        mobileNumber = range(len(deviceName))         # 获取设备数量
        for i in mobileNumber:
            desired_caps = {
                'platformName': 'Android',
                'deviceName': deviceName[i],
                'platformVersion': platformVersion[i],
                'appPackage': appPackage[i],  # APK包名
                'appActivity': appActivity[i],  # APK的Activity
                'unicodeKeyboard': True,  # 输入中文字符的时候appium server去被测试设备安装一个输入法可输入中文
                'newCommandTimeout': 6000,  # 设置会话结束时间 appiumsever失效时间
                'udid': udid[i]
            }
            Mobile.phoneParameter.append(desired_caps)

        for i in mobileNumber:
            parameter = webdriver.Remote('http://127.0.0.1:'+ port[i] +'/wd/hub', Mobile.phoneParameter [i]) # 对应appium对象，固定值
            Mobile.phone[deviceName[i]] = parameter
            print("deviceName=")
            print(Mobile.phone[deviceName[i]])
            Mobile.phoneStart.append(Process(target=Mobile.phone[deviceName[i]]))

        for i in mobileNumber:
            Mobile.phoneStart[i].start()
            Mobile.phone[deviceName[i]].implicitly_wait(5)


    def closeApp(self,deviceName):
        Mobile.phone[deviceName].quit()