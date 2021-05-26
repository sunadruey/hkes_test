import  pytest
#  pytest test_fixture.py --setup-show
# yield 前面的操作相当于setup 后面的操作相当于teardown

def test_case1(login,conn_db):
    print(login)
    print(conn_db)
    print("用例1")

def test_case2():
    print("用例2")

@pytest.mark.usefixtures("login")
def test_case3():

    print("用例3")