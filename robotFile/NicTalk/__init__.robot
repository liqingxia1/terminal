*** Settings ***
Library    andpylib.Mobile
Library    selenium2library
Library    Collections

Set Suite Variable   @{list}

Suite Setup       androidThread    5.1.1    com.nictalk.start    com.xinwei.cootalk.view.activity.SplashActivity    c47ad30c  # 启动app
Suite Teardown   closeApp                                                # 关闭app
