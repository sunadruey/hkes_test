import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize("env",yaml.safe_load(open('/Users/yuanbao/PycharmProjects/hkes_test/data/env.yaml')))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print(env['test'])
        elif "dev" in env:
            print("这是开发环境")


    def test_yaml(self):
        print(yaml.safe_load('/Users/yuanbao/PycharmProjects/hkes_test/data/env.yaml'))
