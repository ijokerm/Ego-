"""项目配置文件"""
import os
# 获取项目根目录
BASE_DIR = os.path.dirname(__file__)  # __file__内置属性 app.py当前目录
# print(BASE_DIR)
BASE_URL = "http://e.cn"
# 轮播图的编号
bid = 1
# 主图数量
ids = "1,2,3"
# 获取商品信息ID
pid = 2
# 分类id
cid = 2
# 请求头
header = {"Content-Type": "application/json",
          "token": "ad84ca4d5e0051bf7baecd2454fa4f0a"
          }
code = "083V3vFa1IU4HE0g2MFa16xpX53V3vFB"
# 用户名
name = "春天的熊"
# 商品ID
product_id = 8
# 账户
count = 8
# 订单ID
order_id = 11

if __name__ == '__main__':
    print(header["token"])


