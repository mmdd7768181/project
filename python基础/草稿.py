from DecryptLogin import login

lg = login.Login()
infos_return, session = lg.jingdong(username='你的账号', password="你的密码")

print(infos_return,session)
