import  pytest

@pytest.mark.login
def test_login1():
    print("登录成功1！")

@pytest.mark.login
def test_login2():
    print("登录成功2！")

@pytest.mark.search
def test_search1():
    print("搜索成功1！")

@pytest.mark.search
def test_search2():
    print("搜索成功2！")







