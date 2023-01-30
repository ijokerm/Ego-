""" 演示 订单模块 测试接口的封装
1、导包
2、封装接口类
"""
import requests

import app


class Order_API():
    # 定义初始化方法 --定义实例化之后的对象属性
    def __init__(self):
        self.order_url = app.BASE_URL + "/api/v1/order"
        self.check_url = app.BASE_URL + "/api/v1/order/{}"

    # 定义接口方法 --创建订单
    def create_order(self):
        return requests.post(self.order_url,headers=app.header,
                      json={"products":[{"product_id":app.product_id,"count":app.count}]})
    # 定义接口方法 --查看订单
    def check_order(self,order_id):
        new_url = self.check_url.format(order_id)
        return requests.get(new_url,headers=app.header)


