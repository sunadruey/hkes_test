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

    def test_add2(self):
        test_data=[[1,1,2],[100,100,200],[0.1,0.1,0.2]]
        for i in range(0,len(test_data)):
            reuslt = self.calc.add(test_data[i][0], test_data[i][1])
            assert reuslt == test_data[i][2]

    # 参数并给测试用例命名--浮点数特殊处理
    @pytest.mark.parametrize('a, b, expect', [(0.1,0.2,0.3),(0.1,0.1,0.2)],ids=['case1','case2'])
    def test_add(self,a,b,expect):
        reuslt=self.calc.add(a,b)
        assert  round(reuslt,2)==expect


    # 参数并给测试用例命名--除数为零
    @pytest.mark.parametrize('a, b, expect', [(0.1, 0, True), (10, 0, True)], ids=['case1', 'case2'])
    def test_add3(self,a,b,expect):
        with pytest.raises(ZeroDivisionError):
            self.calc.add(a, b)
        # try:
        #     reuslt=self.calc.add(1,0)
        # except ZeroDivisionError:
        #     print("除数为零")


