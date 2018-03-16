import time


from andpylib.Mobile import Mobile
from andpylib.KeyEvents import KeyEvents
from appium.webdriver.connectiontype import ConnectionType
import Collocations

class CooTalk(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    # 切换国家
    def changeCountry(self,country, deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id('activity_login_country_name').click()
        Mobile.phone[deviceName].find_element_by_id('country_et_search').send_keys(country)
        time.sleep(1)
        co = 'new UiSelector().className("android.widget.TextView").text(\"'+country+' ")'
        Mobile.phone[deviceName].find_element_by_android_uiautomator(co).click()

    # 输入登录的手机号码或账户
    def changePhoneNum(self,phone,deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id('activity_login_home_phone_num').clear()
        Mobile.phone[deviceName].find_element_by_id('activity_login_home_phone_num').send_keys(phone)

    # 输入密码
    def sendPassWord(self,password, deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id('activity_login_by_pw_pw').clear()
        Mobile.phone[deviceName].find_element_by_id('activity_login_by_pw_pw').send_keys(password)

    # 登录账户
    def clickLogin(self, deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id('activity_login_home_next_step').click()
        Mobile.phone[deviceName].wait_activity("com.uip.start.activity.MainActivity", 120, 2)
w
    # 登录后弹出是否同步的提示框，且点击同步
    def clickPopUp(self, deviceName = Collocations.deviceNames[0]):
        time.sleep(2)
        popup = Mobile.phone[deviceName].find_elements_by_android_uiautomator( 'new UiSelector().className("android.widget.Button").text("同步")')
        if len(popup) > 0:
            Mobile.phone[deviceName].find_element_by_android_uiautomator( 'new UiSelector().className("android.widget.Button").text("同步")').click()


    def loginCooTalk(self, country, phone, password, deviceName = Collocations.deviceNames[0]):
        print("=============mobile.phone==============")
        valeu_country = Mobile.phone[deviceName].find_elements_by_id('activity_login_country_name')
        valeu_phone = Mobile.phone[deviceName].find_elements_by_id('activity_login_home_phone_num')
        if len(valeu_country) > 0 or len(valeu_phone) > 0 :
            keyevt = KeyEvents()
            keyevt.setNetwork_wifi(deviceName)
            co = CooTalk()
            co.changeCountry(country,deviceName)
            co.changePhoneNum(phone,deviceName)
            co.sendPassWord(password,deviceName)
            co.clickLogin(deviceName)
            co.clickPopUp(deviceName)
            time.sleep(1)
        else :
            print("已登录")



    # 获取NicTalk登录后 下方的 消息、电话、通讯录、我的 坐标
    def getMsgPhoneContactsCoordinate(self, value, deviceName):
        ele = Mobile.phone[deviceName].find_element_by_id('activity_main_bottom_tab')
        location = ele.location
        size1 = ele.size
        interval = size1['width'] / 4
        coordinates = {}
        coordinates['message'] = interval / 2
        coordinates['phone'] = coordinates['message'] + interval
        coordinates['contacts'] = coordinates['phone'] + interval
        coordinates['mine'] = coordinates['contacts'] + interval
        y = (size1['height'] / 2) + location['y']
        x = coordinates[value]
        return x, y

    # NicTalk界面，点击消息
    def clickMessage(self,deviceName = Collocations.deviceNames[0]):
        a = CooTalk()
        x, y = a.getMsgPhoneContactsCoordinate('message',deviceName)
        Mobile.phone[deviceName].tap([(x, y)], 2)

    # NicTalk界面，点击 电话
    def clickPhone(self,deviceName = Collocations.deviceNames[0]):
        a = CooTalk()
        x, y = a.getMsgPhoneContactsCoordinate('phone',deviceName)
        Mobile.phone[deviceName].tap([(x,y)], 2)

    # NicTalk界面，点击 通讯录
    def clicContacts(self,deviceName = Collocations.deviceNames[0]):
        a = CooTalk()
        x, y = a.getMsgPhoneContactsCoordinate('contacts',deviceName)
        Mobile.phone[deviceName].tap([(x,y)], 2)

    # NicTalk界面，点击 我的
    def clickMine(self,deviceName = Collocations.deviceNames[0]):
        a = CooTalk()
        x, y = a.getMsgPhoneContactsCoordinate('mine',deviceName)
        Mobile.phone[deviceName].tap([(x,y)], 2)

    # 删除联系人
    def deleteContact(self,deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id('right_drawable').click()
        value = Mobile.phone[deviceName].find_elements_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("确认")')
        value2 = Mobile.phone[deviceName].find_elements_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("删除联系人")')

        if len(value) > 0:
            Mobile.phone[deviceName].find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("确认")').click()

        elif len(value2) > 0:
            Mobile.phone[deviceName].find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("删除联系人")').click()
            Mobile.phone[deviceName].find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("确认")').click()

    # 面对面加好友
    def addFriendsNearby(self,deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("面对面加好友")').click()

    # 扫一扫
    def ScanQRCode(self,deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("扫一扫")').click()

    # 邀请好友
    def inviteFriends(self,deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_android_uiautomator(
            'new UiSelector().className("android.widget.TextView").text("邀请好友")').click()

    ################################
    #   以下为 通讯录 界面的详细操作
    ################################

    # 点击增加图标
    def clickAddAFriends(self,deviceName = Collocations.deviceNames[0]):
        print(Mobile.phone[deviceName])
        Mobile.phone[deviceName].find_element_by_id('right_drawable').click()

    # 点击增加手机联系人，并新增联系人信息并保存
    def clickAddPhoneContacts(self, name, phoneNumber, deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("添加手机联系人")').click()
        Mobile.phone[deviceName].find_element_by_id('activity_add_contact_first_name').send_keys(name)
        Mobile.phone[deviceName].find_element_by_id('et_info_input').send_keys(phoneNumber)
        Mobile.phone[deviceName].find_element_by_id('right_text').click()


    # 搜索联系人， 可验证新增联系人是否成功 , 搜索后若需要进入详情界面需传入click值
    def searchContacts_name(self, name, click=None ,deviceName = Collocations.deviceNames[0] ):
        Mobile.phone[deviceName].find_element_by_id('contacts_et_search').clear()
        Mobile.phone[deviceName].find_element_by_id('contacts_et_search').send_keys(name)
        valeu = 'new UiSelector().className("android.widget.TextView").text("'+name+'")'
        search_result = Mobile.phone[deviceName].find_elements_by_android_uiautomator(valeu)
        if len(search_result) > 0:
            if click != None:
                Mobile.phone[deviceName].find_element_by_android_uiautomator(valeu).click()
            return 1
        else: return 0

    ############################################  获取当前页面的用户列表  未实现
    def getContactsList(self, click=None, deviceName = Collocations.deviceNames[0] ):
        valeu = Mobile.phone[deviceName].find_elements_by_class_name("android.widget.LinearLayout")
        print(valeu)
        for i in valeu:
            print(i)
        # Mobile.phone[deviceName].find_elements_by_android_uiautomator(valeu)

    # 编辑联系人
    def editContacts(self,name,phoneNumber, deviceName = Collocations.deviceNames[0]):
        valeu = Mobile.phone[deviceName].find_elements_by_id('right_drawable_2')

        if len(valeu) > 0:
            Mobile.phone[deviceName].find_element_by_id('right_drawable_2').click()
        else:
            Mobile.phone[deviceName].find_element_by_id('com.nictalk.start:id/right_drawable').click()
            Mobile.phone[deviceName].find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("修改用户信息")')
        Mobile.phone[deviceName].find_element_by_id('activity_modify_contact_first_name').send_keys(name)
        Mobile.phone[deviceName].find_element_by_id('et_info_input').send_keys(phoneNumber)
        Mobile.phone[deviceName].find_element_by_id('right_text').click()

    # 拨打电话, valeu 接受拨号方式：M/V/G
    def call_ContactsList(self,valeu, deviceName = Collocations.deviceNames[0] ):
        Mobile.phone[deviceName].find_element_by_id("fragment_contact_call_phone").click()
        print(valeu)
        if valeu == "M":
            Mobile.phone[deviceName].find_element_by_id("dialog_dial_msg_item_image_1").click()
        elif valeu == "V":
            Mobile.phone[deviceName].find_element_by_id("dialog_dial_msg_item_image_2").click()
        elif valeu == "G":
            Mobile.phone[deviceName].find_element_by_id("dialog_dial_msg_item_image_3").click()
        else:
            print("拨号方式只支持 M/V/G")
        time.sleep(1)
        co = CooTalk()
        v1 =  Mobile.phone[deviceName].find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("无法连接到移动网络。")')
        if len(v1) > 0 :
            return co.call_PopUp()
        else:
            return co.clickHangUp()


    ################################
    #   以下为 电话 界面的详细操作
    ################################

    # 电话界面，点击拨号盘号码
    def call_sendPhoneNumber(self, key, deviceName = Collocations.deviceNames[0]):
        sendkey = 'ibtn_key_'+str(key)
        Mobile.phone[deviceName].find_element_by_id(sendkey).click()

    # 电话界面，清空 电话界面 输入栏
    def send_PhoneNumber(self, phoneNumber, deviceName):
        Mobile.phone[deviceName].find_element_by_id("com.nictalk.start:id/number").send_keys(phoneNumber)

    # 电话界面，清空 电话界面 输入栏
    def clear_PhoneNumber(self, deviceName):
        Mobile.phone[deviceName].find_element_by_id("com.nictalk.start:id/number").clear()


    # 点击 拨号 图标
    def clickDial(self, valeu=None, deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id("ibtn_key_g").click()
        choose =  Mobile.phone[deviceName].find_elements_by_id("com.nictalk.start:id/tv_mcwill_name")
        try:
            if len(choose) > 0:
                if valeu == "M":
                    Mobile.phone[deviceName].find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("CooTel呼叫")').click()
                elif valeu == "V":
                    Mobile.phone[deviceName].find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("VoIP呼叫")').click()
                elif valeu == "G":
                    Mobile.phone[deviceName].find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("G网呼叫")').click()
        except Exception:
            keyevt = KeyEvents()
            keyevt.back()
            return  0
        else:
            time.sleep(1)
            co = CooTalk()
            v1 = Mobile.phone[deviceName].find_elements_by_android_uiautomator(
                'new UiSelector().className("android.widget.TextView").text("无法连接到移动网络。")')
            if len(v1) > 0:
                return co.call_PopUp()
            else:
                return co.clickHangUp()


    # 点击 挂断按钮
    def clickHangUp(self, deviceName = Collocations.deviceNames[0]):
        time.sleep(3)
        valeu_button = Mobile.phone[deviceName].find_elements_by_id("com.android.dialer:id/floating_end_call_action_button")
        if len(valeu_button) > 0:
            Mobile.phone[deviceName].find_element_by_id("com.android.dialer:id/floating_end_call_action_button").click()
            return 1
        else:
            return 0


        ##########################
        # 弹框处理
        ##########################
    def call_PopUp(self, deviceName = Collocations.deviceNames[0]):
        Mobile.phone[deviceName].find_element_by_id("android:id/button1").click()
        return 0





def oneTest():
    C8_Device = CooTalk()
    # keyevt = KeyEvents()
    # keyevt.back()

    # C8_Device.android('4723', '6.0.1', 'com.nictalk.start', 'com.xinwei.cootalk.view.activity.SplashActivity','36bb3446')
    # 启动测试机，并设置APP包.
    #
    # C8_Device.androidThread(port,listV,listP,listA,listU)

    C8_Device.android(Collocations.deviceNames,Collocations.ports, Collocations.platformVersions, Collocations.appPackages, Collocations.appActivitys, Collocations.udids)
    print(Collocations.deviceNames)
    # C8_Device.clickAddAFriends('C8')

    # C8_Device.changeCountry(u"柬埔寨")
    # C8_Device.changePhoneNum("0383030081")
    # C8_Device.sendPassWord("123456")
    # C8_Device.clickLogin()
    for i in Collocations.deviceNames:
        C8_Device.loginCooTalk("柬埔寨", "0383030082", "123456", i)

        time.sleep(2)
        C8_Device.clickPopUp(i)
        C8_Device.clicContacts(i)
        C8_Device.clickAddAFriends(i)

        C8_Device.clickAddPhoneContacts("李青霞", "13570818004",i)
        Mobile.phone[i].keyevent(4)
        Mobile.phone[i].find_element_by_id('contacts_et_search').clear()
        # C8_Device.getContactsList(i)

        C8_Device.clicContacts(i)
        print(C8_Device.searchContacts_name("李青霞",1))


        C8_Device.editContacts("杨红艳","15988998899")

        #通讯录拨打电话
        C8_Device.clicContacts(i)
        print(C8_Device.searchContacts_name("杨红艳"))
        C8_Device.call_ContactsList("V")
        print(C8_Device.clickDial())
        C8_Device.call_ContactsList("G")

        print(C8_Device.searchContacts_name("杨红艳", 1))
        C8_Device.deleteContact(i)

        # 拨号盘拨打电话

        C8_Device.clickPhone()
        C8_Device.call_sendPhoneNumber("1")
        C8_Device.call_sendPhoneNumber("1")
        C8_Device.call_sendPhoneNumber("2")
        print(C8_Device.clickDial())
        time.sleep(2)
        C8_Device.clear_PhoneNumber()
        C8_Device.call_sendPhoneNumber("1")
        C8_Device.call_sendPhoneNumber("3")
        C8_Device.call_sendPhoneNumber("5")
        C8_Device.call_sendPhoneNumber("7")
        C8_Device.call_sendPhoneNumber("0")
        C8_Device.call_sendPhoneNumber("8")
        C8_Device.call_sendPhoneNumber("1")
        C8_Device.call_sendPhoneNumber("8")
        C8_Device.call_sendPhoneNumber("0")
        C8_Device.call_sendPhoneNumber("0")
        C8_Device.call_sendPhoneNumber("4")
        print(C8_Device.clickDial("V"))
        time.sleep(2)
        print(C8_Device.clickDial("G"))

        time.sleep(10)


if __name__ == '__main__':
    # 进行代码调试
    oneTest()






