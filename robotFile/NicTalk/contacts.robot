*** Settings ***
Library    andpylib.Mobile
Library    andpylib.CooTalk
Library    andpylib.KeyEvents

*** Test Cases ***
新建联系人
    clicContacts
    clickAddAFriends
    clickAddPhoneContacts    tom    15988884456
    back
    ${var} =    searchContacts_name    tom
    should be true  ${var}==1

编辑联系人
    clicContacts
    searchContacts_name    tom    1
    editContacts    程戏    18977777777
    back
    ${var} =    searchContacts_name    程戏
    should be true  ${var}==1

搜索联系人并拨打电话使用v网
    clicContacts
    searchContacts_name    程戏
    ${var} =   call_ContactsList    V
    should be true  ${var}==1


搜索联系人并拨打电话使用G网
    clicContacts
    searchContacts_name    程戏
    ${var} =   call_ContactsList    G
    should be true  ${var}==1

删除联系人
    clicContacts
    searchContacts_name    程戏    1
    deleteContact
    ${var} =    searchContacts_name    程戏
    should be true  ${var}==0


