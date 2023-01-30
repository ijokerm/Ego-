""" 测试用户
1、导包
2、定义测试接口类
--定义初始化方法/调用接口方法
"""
import logging
import unittest

import app
from api.User import User_API


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化接口对象
        cls.user_api = User_API()

    # 调用 获取token 的测试方法
    def test01_get_token(self):
        """
        1.准备测试数据
        2.发送请求
        3.断言
        :return:
        """
        code = app.code
        response = self.user_api.get_token(code)
        json_data = response.json()  # 将得到的响应JSON格式化
        logging.info(f"获取token的结果为：{json_data}")
        self.assertEqual(200,response.status_code)
        self.assertEqual(32,len(json_data.get("token")))    # 断言token的长度是否为32位
        self.assertIn("token",json_data)    # 断言包含token关键字
        # 保存token到app.py配置文件中
        app.header["token"] = json_data.get("token")
        logging.info(f"保存的token结果为：{app.header['token']}") # 日志打印执行细节

    # 调用 验证token 的测试方法
    def test02_verify_token(self):
        # 1.准备测试数据
        token = app.header["token"]
        # 2.发送请求
        response = self.user_api.verify_token(token)
        json_data = response.json()
        logging.info(f"验证token的结果为：{json_data}")
        # 3.断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(True,json_data.get("isValid"))
        self.assertTrue(json_data.get("isValid"))

    # 调用 获取地址信息 的测试方法
    def test03_get_address(self):
        # 1.测试数据
        # 2.发送请求
        response = self.user_api.get_address()
        json_data = response.json()
        logging.info(f"获取地址信息结果为：{json_data}")
        # 3.断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(app.name,json_data.get("name"))