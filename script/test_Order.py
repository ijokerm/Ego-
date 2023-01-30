""" 测试订单模块
1.导包
2.定义测试类
--初始化方法/调用已经封装的测试接口
"""
import unittest
import logging

import app
from api.Order import Order_API


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.order_api = Order_API()

    # 测试 创建订单
    def test01_create_order(self):
        # 测试数据
        # 发送请求
        response = self.order_api.create_order()
        json_data = response.json()
        logging.info(f"创建订单结果为：{json_data}") # 记录测试日志
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertTrue(json_data.get("pass"))
    # 测试查看订单
    def test02_check_order(self):
        # 准备测试数据
        order_id = app.order_id
        # 发送请求
        response = self.order_api.check_order(order_id)
        json_data = response.json()
        logging.info(f"查看订单的结果为：{json_data}")
        # 断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(16,len(json_data.get("order_no")))
