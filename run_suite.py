""" 批量执行测试用例
1、导包
2、创建测试套件对象
3、添加测试用例到套件
4、批量执行测试用例
"""
import unittest

import app
from script.test_Home import TestHome
from script.test_Order import TestOrder
from script.test_Products import TestProducts
from script.test_User import TestUser
from unittestreport import TestRunner
suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestHome))
suite.addTest(unittest.makeSuite(TestProducts))
suite.addTest(unittest.makeSuite(TestUser))
suite.addTest(unittest.makeSuite(TestOrder))

# runner = unittest.TextTestRunner()  # 实例化执行器对象
# runner.run(suite)

# 5.生成测试报告
# 5.1定义测试报告文件
rep_file = app.BASE_DIR + '/report/Ego.html'
# 5.2创建第三方执行器对象
runner = TestRunner(suite,      # 测试套件对象
                    filename=rep_file, # 测试报告文件
                    title="Ego小程序项目接口测试报告",
                    tester="春天的熊",
                    desc="V1.0",
                    templates=1)  # 报告的模板

runner.run()

# 5.3执行器调用run方法执行生成测试报告