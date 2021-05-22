import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.calculator import Calculators

class TestCalu:

    def setup(self):
        self.calc=Calculators()

    def teardown(self):
        print("tear清理。。。")

    def test_add(self):
        reuslt=self.calc.add(2,3)
        assert  reuslt==5

    def test_add2(self):
        reuslt=self.calc.add(3,3)
        assert  reuslt==6



