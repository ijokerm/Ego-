""" 演示用户模块测试接口的封装
1、导包
2、封装接口类
"""
import requests

import app


class User_API():
    def __init__(self):
        self.token_url = app.BASE_URL + "/api/v1/token/user"
        self.verify_url = app.BASE_URL + "/api/v1/token/verify"
        self.address_url = app.BASE_URL + "/api/v1/address"
    # 获取token的接口测试方法
    def get_token(self,code):
        data = {"code":code}
        return requests.post(self.token_url,headers=app.header,json=data)
    # 验证token的封装
    def verify_token(self,token):
        data = {"token":token}
        return requests.post(self.verify_url,headers=app.header,json=data)
    # 获取地址信息
    def get_address(self):
        return requests.get(self.address_url,headers=app.header)

