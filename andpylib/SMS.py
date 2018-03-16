from andpylib.Mobile import Mobile
from andpylib.Swipes import Swipes
import time,traceback

class SMS(Mobile):
    #短信界面点击┇
    def moreOptions(self):#
        Mobile.phone.find_element_by_accessibility_id("更多选项").click()

    #短信界面点击┇后点击设置
    def clickSetting(self):
        code = u'new UiSelector().text("设置")'
        Mobile.phone.find_element_by_android_uiautomator(code).click()

    #短信界面点击┇点击设置，点击短信模板
    def clickSMSTemplate(self):
        code =u'new UiSelector().className("android.widget.TextView").text("短信模板")'
        swp = Swipes()
        while True:
            ele= Mobile.phone.find_elements_by_android_uiautomator(code)
            # 没有找到
            if len(ele)<=0:
                swp.swipeUp()
                continue
            # 找到了
            break
        Mobile.phone.find_element_by_android_uiautomator(code).click()

    #短信界面点击┇点击设置，点击短信模板，点击新建模板
    def newTemplate(self,message,choice):
        code = u'new UiSelector().text("新建模板")'
        Mobile.phone.find_element_by_android_uiautomator(code).click()
        Mobile.phone.find_element_by_id("com.android.mms:id/edit_tempsms_editor").send_keys(message)
        if choice=="确定":
            xpath = u'//android.widget.Button[@text="确定"]'
            Mobile.phone.find_element_by_xpath(xpath).click()
            # Mobile.phone.find_element_by_android_uiautomator('new Uiselector().className("android.widget.Button").text("确定")').click()

            #判断是否添加成功
            list=self.getTemplateList()
            if message in list:
                return "模板添加成功"
            else:
                return "模板添加失败"
        elif choice=="取消":
            xpath = u'//android.widget.Button[@text="取消"]'
            Mobile.phone.find_element_by_xpath(xpath).click()
            # Mobile.phone.find_element_by_android_uiautomator('new Uiselector().className("android.widget.Button").text("取消")').click()
        else:
            print ("输入错误")


    #短信界面点击┇点击设置，点击短信模板，获取模板列表(可以获取短信列表的短信内容信息)
    def getTemplateList(self):
        code = u'new UiSelector().className("android.widget.TextView")'
        eles= Mobile.phone.find_elements_by_android_uiautomator(code)
        eles=eles[4:len(eles)]
        list=[]
        for ele in eles:
            list.append(ele.text)
        if len(list) == 0:
            return "模板列表为空"
        else:
            return list

    #短信界面点击┇点击设置，点击短信模板，删除单个模板
    def delTemplateList(self,parameter):
        list=self.getTemplateList()

        if parameter in list:
            code = u'new UiSelector().text("'+parameter+'")'
            el=Mobile.phone.find_element_by_android_uiautomator(code)
            elx = el.location.get('x')
            ely = el.location.get('y')
            Mobile.phone.swipe(elx, ely, elx, ely, 10000)
            #点击删除按钮
            code = u'new UiSelector().text("删除")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()
        else:
            print ("不存在")

    #短信界面点击┇点击设置，点击短信模板，删除所有模板
    def delAllTemplateList(self):
         while True:
             code = u'new UiSelector().className("android.widget.TextView")'
             eles = Mobile.phone.find_elements_by_android_uiautomator(code)
             eles = eles[4:len(eles)]

             if len(eles)<=0:
                 break
             for ele in eles:
                 code = u'new UiSelector().text("' + ele.text + '")'
                 el = Mobile.phone.find_element_by_name(ele.text)
                 elx = el.location.get('x')
                 ely = el.location.get('y')
                 Mobile.phone.swipe(elx, ely, elx, ely, 10000)

                 # 点击删除按钮
                 code = u'new UiSelector().text("删除")'
                 Mobile.phone.find_element_by_android_uiautomator(code).click()
                 break

    #短信界面点击┇点击设置，点击短信模板，选择一个模板点击修改
    def editTemplate(self,before,aftermessage,choice):#,opt,message,choice
        # code = u'new UiSelector().className("android.widget.TextView")'
        # eles = Mobile.phone.find_elements_by_android_uiautomator(code)
        # eles = eles[4:len(eles)]
        # print(eles)
        # list = []
        # for ele in eles:
        #     print(ele.text)
        #     list.append(ele.text)
        list = self.getTemplateList()

        if before in list:
            code =u'new UiSelector().text("'+before+'")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()
            ele=Mobile.phone.find_element_by_id("com.android.mms:id/edit_tempsms_editor")
            ele.clear()
            ele.send_keys(aftermessage)
            if choice == "确定":
                xpath = u'//android.widget.Button[@text="确定"]'
                Mobile.phone.find_element_by_xpath(xpath).click()
                # Mobile.phone.find_element_by_android_uiautomator('new Uiselector().className("android.widget.Button").text("确定")').click()

                # 判断是否修改成功
                list = self.getTemplateList()
                if aftermessage in list:
                    return "模板修改成功"
                else:
                    return "模板修改失败"
            elif choice == "取消":
                xpath = u'//android.widget.Button[@text="取消"]'
                Mobile.phone.find_element_by_xpath(xpath).click()
                # Mobile.phone.find_element_by_android_uiautomator('new Uiselector().className("android.widget.Button").text("取消")').click()
        else:
            print("输入错误")


    # 获取短信列表
    def getSMSList(self):
        eles=Mobile.phone.find_elements_by_id("com.android.mms:id/from")
        list=[]
        for ele in eles:
            list.append(ele.text)
        if len(list)==0:
            return "短信列表为空"
        else:
            return  list


    #点击新增信息按钮
    def newSMSButton(self,):

        # 点击新增短信按钮
        Mobile.phone.find_element_by_accessibility_id("新信息").click()

    #点击添加短信里面的┇
    def quickReply(self):
        #点击更多选项
        Mobile.phone.find_element_by_accessibility_id("更多选项").click()

    #点击添加短信里面的┇，后点击导入模板
    def importTemplateButton(self):
        code = u'new UiSelector().text("导入模板")'
        Mobile.phone.find_element_by_android_uiautomator(code).click()

    # 点击添加短信里面的┇，后点击导入模板，点击想要导入的模板
    def importTemplate(self,template):
        code = u'new UiSelector().className("android.widget.TextView")'
        eles = Mobile.phone.find_elements_by_android_uiautomator(code)
        list = []
        for ele in eles:
            print(ele.text)
            list.append(ele.text)

        if template in list:
            print (1)
            code = u'new UiSelector().text("'+template+'")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()
        else:
            print ("没有找到")

    #短信接收人
    def receivePeople(self, recipients):
        # 接收者
        Mobile.phone.find_element_by_id("com.android.mms:id/recipients_editor").send_keys(recipients)

    #信息内容
    def InformationContent(self, message):
        # 短信内容
        Mobile.phone.find_element_by_id("com.android.mms:id/embedded_text_editor_btnstyle").send_keys(message)

    #短信发送方式
    def sendWay(self,MG):
        time.sleep(3)
        if MG=="M":
            Mobile.phone.find_element_by_id("com.android.mms:id/second_send_button_sms_view").click()

        elif MG=="G":
            Mobile.phone.find_element_by_id("com.android.mms:id/first_send_button_sms_view").click()

        else:
            print("输入信息错误")
        time.sleep(5)
        Mobile.phone.keyevent(4)
        # self.Upward()


    #删除所有短信
    def delAllMessage(self,choice):
        code = u'new UiSelector().text("删除所有会话")'
        Mobile.phone.find_element_by_android_uiautomator(code).click()
        if choice == "删除":
            code=u'new UiSelector().text("删除")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()

            # 判断是否删除成功
            list = self.getSMSList()
            if len(list)==0:
                return "所有短信已经删除成功"
            else:
                return "没有短信可删除删除短信失败"
        elif choice == "取消":
            code = u'new UiSelector().text("取消")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()

    #删除单条短信
    def delSingleMessage(self,mesage, choice):
        time.sleep(10)
        list = self.getSMSList()
        if mesage in list:
            code =u'new UiSelector().text("'+mesage+'")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()
            self.quickReply()
            code = u'new UiSelector().text("删除会话")'
            Mobile.phone.find_element_by_android_uiautomator(code).click()
            if choice == "删除":
                code = u'new UiSelector().text("删除")'
                Mobile.phone.find_element_by_android_uiautomator(code).click()

                # 判断是否删除成功
                list = self.getSMSList()
                if mesage in list:
                    return "短信已经删除成功"
                else:
                    return "删除短信失败"
            elif choice == "取消":
                code = u'new UiSelector().text("取消")'
                Mobile.phone.find_element_by_android_uiautomator(code).click()

        else:
            print("不存在")


    # #删除多条
    # def delMultipleMessage(self, mesage, choice):
    #
    #     list = self.getSMSList()
    #     if mesage in list:
    #         el = Mobile.phone.find_element_by_name(mesage)
    #         elx = el.location.get('x')
    #         ely = el.location.get('y')
    #         Mobile.phone.swipe(elx, ely, elx, ely, 100000)
    #
    #         # 点击删除按钮
    #         code = u'new UiSelector().text("删除")'
    #         Mobile.phone.find_element_by_android_uiautomator(code).click()
    #
    #     else:
    #         print("不存在")

    def Upward(self):
        # Mobile.phone.find_element_by_accessibility_id("向上导航").click()
        v1 = Mobile.phone.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.ImageButton ").text("向上导航")')
        v2 = Mobile.phone.find_elements_by_id("android:id/up")
        if len(v1)>0 :
            Mobile.phone.find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.ImageButton ").text("向上导航")').click()
        elif len(v2)>0:
            Mobile.phone.find_element_by_id("android:id/up").click()
        else:
            Mobile.phone.keyevent(4)






if __name__ == '__main__':
    s=SMS()
    s.android("5.1.1","com.android.mms",".ui.ConversationList")
    s.newSMSButton()



    s.quickReply()
    # s.sendSMS("123456","中国","G")

    # s.getSMSList()
    # s.moreOptions()
    # s.getSMSList()
    # s.newSMSButton()
    # s.receivePeople("10086")
    # s.quickReply()
    # s.importTemplateButton()
    # s.importTemplate("我过会儿打给您。")
    # s.InformationContent("aaaaaaaaaa")
    # s.sendWay("G")
    # s.delAllMessage("取消")
    # s.delSingleMessage("10086","取消")



    s.clickSetting()
    s.clickSMSTemplate()
    # s.delAllTemplateList()
    s.newTemplate("现在不方便接听电话","确定")
    s.delTemplateList("现在不方便接听电话")

    # s.newTemplate("现在不方便接听电话aa", "确定")
    # s.editTemplate("现在不方便接听电话aa","aaaaaaaaaaaaa","确定")
    # # s.delTemplateList()
    # s.getTemplateList()

    # s.newTemplate("现在不方便接听电话","取消z")
