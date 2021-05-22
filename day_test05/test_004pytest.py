import  yaml
import pytest
@pytest.mark.parametrize(("a","b"),yaml.safe_load(open("/Users/yuanbao/PycharmProjects/hkes_test/data/date.yaml")))
class TestData:
    def test_data(selfself,a,b):
        print(a+b)