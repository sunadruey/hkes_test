import sys
import os
import yaml
import pytest



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.calculator import Calculators

def get_datas():
    with open('../data/caluc.yml') as f:
        datas=yaml.safe_load(f)
    add_datas=datas['add']['datas']
    add_ids=datas['add']['ids']
    print(add_datas)
    print(add_ids)
    add_ids=datas['add']['ids']

    return [add_datas,add_ids]

class TestCalue:

    def setup(self):
        self.calc = Calculators()

    @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids=get_datas()[1])
    def test_add(self,a,b,expect):
        result=self.calc.add(a,b)
        assert  result==expect

