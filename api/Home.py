""" 首页请求封装
1、导包
2、封装测试类
--定义初始化方法/定义接口方法
"""
import requests

import app


class Home_API():
    # 定义初始化方法：定义实例化之后的对象属性
    def __init__(self):
        self.banner_url = app.BASE_URL + "/api/v1/banner/{}"
        self.theme_url = app.BASE_URL + "/api/v1/theme"
        self.recentpro_url = app.BASE_URL + "/api/v1/product/recent"

    # 定义接口方法 --获取轮播图
    def get_banner(self,banner_id):
        new_url = self.banner_url.format(banner_id)
        return requests.get(new_url)
    # 获取专题栏位
    def get_theme(self,ids):
        # ids=1,2,3 --转化为JSON数据和url拼接 {"ids":"1,2,3"}
        data = {"ids":ids}
        return requests.get(self.theme_url,params=data)
    # 获取最近新品
    def get_rencentpro(self):
        return requests.get(self.recentpro_url)

if __name__ == '__main__':
    pr = Home_API()
    print(pr.get_theme(app.ids))




