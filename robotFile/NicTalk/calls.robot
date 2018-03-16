*** Settings ***
Library    andpylib.Mobile
Library    andpylib.CooTalk
Library    andpylib.KeyEvents

*** Test Cases ***
登录NicTalk
    loginCooTalk    柬埔寨    0383030081    123456

拨打112
    clickPhone
    call_sendPhoneNumber    1
    call_sendPhoneNumber    1
    call_sendPhoneNumber    2
    ${var} =    clickDial
    should be true  ${var}==1

V网使用拨号盘输入拨打电话
    clear_PhoneNumber
    setNetwork_wifi
    BuiltIn.Sleep  2
    call_sendPhoneNumber    1
    call_sendPhoneNumber    3
    call_sendPhoneNumber    5
    call_sendPhoneNumber    9
    call_sendPhoneNumber    8
    call_sendPhoneNumber    2
    call_sendPhoneNumber    4
    call_sendPhoneNumber    7
    call_sendPhoneNumber    6
    call_sendPhoneNumber    1
    call_sendPhoneNumber    4
    ${var} =    clickDial    V
    should be true  ${var}==1

G网拨打13570818004
    clear_PhoneNumber
    BuiltIn.Sleep  2
    send_PhoneNumber    13570818004
    ${var} =    clickDial    G
    should be true  ${var}==1
