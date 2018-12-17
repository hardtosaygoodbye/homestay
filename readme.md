### url_header: http://homestay.swiftwhale.cn/api/v1/

#### 注册
url: user/sign_up/  
method: post  
param: {"phone":"17600000000","password":"xxxxxxxxx"}  
return: {"code":0, "user":{"id":1,"phone":"17600000000"}, "token":"xxxxxxxxxxx"}  

#### 登录
url: user/sign_in/  
method: post  
param: {"phone":"17600000000", "password":"xxxxx"}  
return: {"code":0, "user":{"id":1, "phone":"17600000000"}, "token":"xxxxxxxxx"}  

#### 获取当前用户信息
url: user/current_user/  
method: get  
param: {"token":"xxxxxxxxxx"}  
return {"code":0, "user":{"id":1, "phone":"17600000000"}}  

#### 修改个人数据
url: user/current_user/  
method: patch  
param: {"token": "xxxxxxxx","xxxx":"xxxxx"}  
return: {"code":0, "user": {"id":1,"phone":"17600000000"}}  

#### 搜索房源
url: house/house_list/  
method: get  
param: {"keyword":"xxxxx","check_in_date":"2018-9-10","check_out_date":"2018-9-11"}  
return: {
    "code": 0,
    "houses": [
        {
            "id": 3,
            "cover": "http://www.baidu.com",
            "desc": "测试房屋",
            "address": "文汇路",
            "comment_score": "5.0",
            "price": "1000.00"
        }
    ]
}  

#### 房屋详情
url: house/house_detail/  
method: get  
param: {"house_id":1}  
return: {"code":0, "house":{}}  

#### 预定房间
url: order/order/  
method: post  
param: {
            "house_id":1,
            "name":"入住者姓名",
            "id_card":"310110199701010000",
            "person_num": 2,
            "check_in_date": "2018-9-10",
            "check_out_date": "2018-9-11",
            "phone": "17600000000"，
            "token":"xxxxxxx"
        }
return: {
    "code":0,
    "detail":"预定成功"
}
