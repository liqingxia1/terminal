*** Settings ***
Library    andpylib.Mobile
Library    andpylib.SMS
Library    andpylib.KeyEvents

*** Test Cases ***
#获取短信列表联系人信息
#    [Setup]    Run Keywords    newSMSButton
#    ...    AND    receivePeople    10010
#    ...    AND    InformationContent    5
#    ...    AND    sendWay    M
#
#    ...    AND    newSMSButton
#    ...    AND    receivePeople    10086
#    ...    AND    quickReply
#    ...    AND    importTemplateButton
#    ...    AND    importTemplate    我过会儿打给您。
#    ...    AND     sendWay    M
#
#    ${smsInfoList}=  getSMSList
#    log to console    ${smsInfoList}
#
#    [Teardown]    Run Keywords   delSingleMessage    10010    删除
#    ...    AND     delSingleMessage    10086    删除

新建收件人和短信内容，并发送
    newSMSButton
    receivePeople    10010
    InformationContent    5
    sendWay    M
    [Teardown]    delSingleMessage    10010    删除



新建收件人和使用模板内容，并发送
    newSMSButton
    receivePeople    10086
    quickReply
    importTemplateButton
    importTemplate    我过会儿打给您。
    sendWay    M
    [Teardown]    delSingleMessage    10086    删除


#删除所有短信
#    [Setup]    Run Keywords    newSMSButton
#    ...    AND    receivePeople    10010
#    ...    AND    InformationContent    5
#    ...    AND    sendWay    M
#
#    ...    AND    newSMSButton
#    ...    AND    receivePeople    10086
#    ...    AND    quickReply
#    ...    AND    importTemplateButton
#    ...    AND    importTemplate    我过会儿打给您。
#    ...    AND     sendWay    M
#
#    quickReply
#    delAllMessage    取消
#    quickReply
#    ${sms}=  delAllMessage    删除
#    log to console    ${sms}

删除单条短信
    [Setup]    Run Keywords    newSMSButton
    ...    AND    receivePeople    10010
    ...    AND    InformationContent    5
    ...    AND    sendWay    M

    delSingleMessage    10010   删除

#获取短信模板列表信息
#   [Setup]    Run Keywords   moreOptions
#    ...    AND    clickSetting
#
#    ...    AND    clickSMSTemplate
#    ...    AND    newTemplate     我在忙，现在不方便接听电话！！！    确定
#
#
#    ...    AND    clickSMSTemplate
#    ...    AND    newTemplate     现在不方便接听电话    确定
#
#    ${sms}=  getTemplateList
#    log to console    ${sms}
#
#    [Teardown]    Run Keywords     delTemplateList    我在忙，现在不方便接听电话！！！
#    ...    AND    delTemplateList    现在不方便接听电话
#    ...    AND    Upward
#    ...    AND    Upward

新建常用语句
    moreOptions
    clickSetting

    clickSMSTemplate
    ${ruInfo}=    newTemplate     我在忙，现在不方便接听电话！！！    确定
    log to console    ${ruInfo}

    [Teardown]    Run Keywords     delTemplateList    我在忙，现在不方便接听电话！！！
    ...    AND    Upward
    ...    AND    Upward


修改常用语句
    [Setup]    Run Keywords     moreOptions
    ...    AND    clickSetting

    ...    AND    clickSMSTemplate
    ...    AND    newTemplate     我在忙，现在不方便接听电话！！！    确定

    ${ruInfo}=    editTemplate    我在忙，现在不方便接听电话！！！    我过会打给你    确定
    log to console    ${ruInfo}


    [Teardown]    Run Keywords     delTemplateList    我过会打给你
    ...    AND    Upward
    ...    AND    Upward


删除常用语句
    [Setup]    Run Keywords     moreOptions
    ...    AND    clickSetting

    ...    AND    clickSMSTemplate
    ...    AND    newTemplate     我在忙，现在不方便接听电话！！！    确定

    ${ruInfo}=     delTemplateList    我在忙，现在不方便接听电话！！！
    log to console    ${ruInfo}






