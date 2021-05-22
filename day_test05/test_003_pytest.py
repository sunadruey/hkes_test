import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    @pytest.mark.parametrize("key1,b",[(1,1),(2,2),(3,4)])
    def test_two(key1,b):

        assert key1==b

    @pytest.fixture()
    def login():
        username ="Jerry"
        return  username

    def test_login(self,login):
        print(f"test login= {login}")
