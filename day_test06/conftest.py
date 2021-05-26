import pytest
@pytest.fixture(autouse=True,scope="function",params=['jeery','tom'])
def login(request):
    print("登录操作")
    username=request.param
    # yield  ['tom','123456']
    yield username
    print("退出操作")

@pytest.fixture()
def conn_db():
    print("完成数据连接")
