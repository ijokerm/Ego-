""" 测试商品
1、导包
2、定义测试类
 --初始化方法/调用已经封装的测试接口
"""
import unittest
import logging

import app
from api.Products import Products_API


class TestProducts(unittest.TestCase):
    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.pro_api = Products_API()

    # 测试商品分类
    def test01_classify(self):
        # 准备测试数据
        # 发送请求
        response = self.pro_api.classify_pro()
        json_data = response.json()
        logging.info(f"测试商品分类结果为：{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(6,len(json_data))
        self.assertEqual("果味",json_data[0].get("name"))
    # 测试 获取商品分类下的商品
    def test02_classify_pro(self):
        # 准备测试数据
        pid = app.pid
        # 发送请求
        response = self.pro_api.classifyPro(pid)
        json_data = response.json()
        logging.info(f"获取商品分类下的商品结果为：{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(8,len(json_data))
        self.assertEqual("冬木红枣 500克",json_data[3].get("name"))
    # 测试 获取商品信息
    def test03_products_info(self):
        # 准备数据
        # 发送请求
        response =  self.pro_api.products_info()
        json_data = response.json()
        logging.info(f"获取商品信息为：{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(2,json_data.get("id"))
        self.assertEqual("梨花带雨 3个",json_data.get("name"))
