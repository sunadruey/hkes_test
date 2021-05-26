import sys
import os
import yaml
import pytest



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.calculator import Calculators


# 解析数据文件
# def get_datas():
#     with open('../data/caluc.yml') as f:
#         datas=yaml.safe_load(f)
#     add_datas=datas['add']['datas']
#     add_ids=datas['add']['ids']
#     print(add_datas)
#     print(add_ids)
#     add_ids=datas['add']['ids']
#
#     return [add_datas,add_ids]

# 解析测试步骤文件
def steps(addstepsfiles,calc,a,b,expect):
    with open(addstepsfiles) as f:
        steps=yaml.safe_load(f)
        for step in steps:
            if 'add' == step:
                print('step_add')
                result=calc.add(a, b)

            elif 'add1' == step:
                print('step_add1')
                result = calc.add(a, b)
            assert expect==result

class TestCalue:

    def setup(self):
        self.calc = Calculators()

    # @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids=get_datas()[1])
    # def test_add(self,a,b,expect):
    #     result=self.calc.add(a,b)
    #     assert  result==expect

    def test_add_steps(self):
        a=1
        b=2
        expect=2
        steps('/Users/yuanbao/PycharmProjects/hkes_test/steps/add_step.yml',self.calc,a,b,expect)

        # assert 2 == self.calc.add(1,1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add(-1, 1)

