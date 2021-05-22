class Test_Demo():

    # 类的前后执行的
    def setup_class(self):
        print("初始化。。。")

    def teardown_class(self):
        print("清理。。。")
    #   方法的前后执行
    def setup(self):
        print("set初始化。。。")

    def teardown(self):
        print("tear清理。。。")


    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10


