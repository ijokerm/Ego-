"""测试首页
1、导包
2、定义测试类
--初始化方法/调用已封装的测试接口
"""
import logging
import unittest

import app
from api.Home import Home_API


class TestHome(unittest.TestCase):
    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.home_api = Home_API()

    # 测试首页轮播图
    def test01_get_banner(self):
        # 测试数据
        # 发送请求
        banner_id = app.bid
        response = self.home_api.get_banner(banner_id)
        json_data = response.json()
        logging.info(f"获取轮播图请求的结果为：+{json_data}")
        # 结果断言
        self.assertEqual(200,response.status_code)  #断言响应状态码
        self.assertEqual(banner_id,json_data.get("id"))
    # 测试首页专题栏位
    def test02_get_theme(self):
        # 测试数据
        ids = app.ids
        # 发送请求
        response = self.home_api.get_theme(ids)
        json_data = response.json()
        logging.info(f"获取专题栏位请求的结果为：+{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertIsNotNone(len(json_data))  # 断言列表的长度大于0
        self.assertEqual(1,json_data[0].get("id"))
    # 测试最近新品
    def test03_get_recent(self):
        # 测试数据
        # 发送请求
        response = self.home_api.get_rencentpro()
        json_data = response.json()
        logging.info(f"获取最近新品请求的结果为：+{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertIsNotNone(len(json_data))  # 断言列表的长度大于0




