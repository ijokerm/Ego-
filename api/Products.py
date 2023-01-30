""" 商品请求封装
1、导包
2、封装测试类
--定义初始化/接口方法
"""
import requests

import app


class Products_API():
    # 定义初始化方法 --定义实例化之后的对象属性
    def __init__(self):
        self.classify_url = app.BASE_URL + "/api/v1/category/all"
        self.classifyPro_url = app.BASE_URL + "/api/v1/product/by_category"
        self.products_url = app.BASE_URL + "/api/v1/product/{}"

    # 定义接口方法 --获取商品分类
    def classify_pro(self):
        return requests.get(self.classify_url)
    # 定义接口方法 --获取商品分类下的商品
    def classifyPro(self,pid):
        data = {"id":pid}
        return requests.get(self.classifyPro_url,params=data)
    # 定义接口方法 --获取商品信息
    def products_info(self):
        return requests.get(self.products_url.format(app.cid))


if __name__ == '__main__':
   pr = Products_API()

   print(pr.classify_url)
   print(pr.classifyPro(app.pid))
   print(pr.products_info())