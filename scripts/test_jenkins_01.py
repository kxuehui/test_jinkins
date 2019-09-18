import allure


class Test001:
    @allure.step("测试步骤")
    def test_func(self):
        print("测试信息")
        assert True
