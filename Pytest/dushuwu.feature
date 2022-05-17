Feature:读书屋小说网站
    Scenario:场景1--正常登陆
        Given 用户名 17621166752 密码 cm7768181

        When 打开登录
        And 输入用户名
        And 输入密码
        And 点击登录按钮

        Then 页面中应包含登出链接，文字为退出

        

