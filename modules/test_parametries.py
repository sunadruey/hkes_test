import pytest
from modules.calculator import Calculators

class TestCalu:

    def setup(self):
        self.calc=Calculators()

    def teardown(self):
        print("tear清理。。。")

    # 参数并给测试用例命名
    @pytest.mark.parametrize('a, b, expect', [(1,1,2),(100,100,200),(0.1,0.1,0.2)],ids=['case1','case2','case3'])
    def test_add(self,a,b,expect):
        reuslt=self.calc.add(a,b)
        assert  reuslt==expect

    def test_add(self):
        test_data=[[1,1,2],[100,100,200],[0.1,0.1,0.2]]
        for i in range(0,len(test_data)):
            reuslt = self.calc.add(test_data[i][0], test_data[i][1])
            assert reuslt == test_data[i][2]

