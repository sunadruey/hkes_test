from modules import calculator

class TestCalu:

    def test_add(self):
        c = calculator()
        reuslt=c.add(2,3)
        assert  reuslt==5




