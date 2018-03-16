*** Settings ***
Library    andpylib.Mobile
Library    andpylib.DataConnection
Library    andpylib.KeyEvents
Library    andpylib.Browser
*** Test Cases ***
#打开移动网络
#    setNetwork_none
#    ${info}=    mobileNetwork
#    log to console  ${info}

打开wifi
    setNetwork_none
    ${info}=    wifiOpen
    log to console  ${info}








