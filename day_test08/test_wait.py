from day_test08.test_001 import Main


class TestWait:
    def setup(self):
        main=Main()
        main.click_first_link().title()