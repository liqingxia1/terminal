*** Settings ***
Library    andpylib.Mobile
Suite Setup       android    5.1.1    com.android.mms    .ui.ConversationList    c47ad30c  # 启动app
Suite Teardown   closeApp                                                # 关闭app
