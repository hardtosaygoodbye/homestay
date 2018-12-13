# url_header: http://192.168.1.100:8000/api/v1/

# 发送短信
url: user/sms/
method: post
param: {"phone":"17600000000"}
return: {"code":0, "detail":"验证码发送成功"}

# 登录
url: user/login/
method: post
param: {"phone":"17600000000","code":"000000"}
return: {"code":0, "user":{"id":1,"phone":"17600000000"}, "token":"xxxxxxxxxxx"}

# 获取当前用户信息
url: user/current_user/
method: get
param: {"token":"xxxxxxxxxx"}
return {"code":0, "user":{"id":1, "phone":"17600000000"}}

# 修改个人数据
url: user/current_user/
method: patch
param: {"token": "xxxxxxxx","xxxx":"xxxxx"}
return: {"code":0, "user": {"id":1,"phone":"17600000000"}}

# 搜索房源
url: house/house_list/
method: get
param: {"keyword":"xxxxx"}
return: {"code":0, "houses": [{...}]}

# 房屋详情
url: house/house_detail/
method: get
param: {"house_id":1}
return: {"code":0, "house":{}}

