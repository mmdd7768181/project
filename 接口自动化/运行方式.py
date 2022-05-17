from requests import request

agreement="http"
host="shop-xo.hctestedu.com"
port="80"
path="/index.php"
url=f"{agreement}://{host}:{port}{path}"
print(url)

method="post"
params={"s":"/index/user/reg"}
headers={"X_Requested-With":"XMLHttpRequest"}
data={}
json={"accounts":"testuitest",
      "pwd":"123454",
      "type":"",} # 必须要加这个逗号，符合字典要求，在python中可以识别，但是在jmter中不行，会报错
r=req
req=request(method=method,url=url,headers=headers,)
print(req.content)
print(req.json())