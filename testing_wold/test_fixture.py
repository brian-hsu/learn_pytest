import pytest

# 定義一個fixture，用於在測試用例之前執行的操作
@pytest.fixture
def setup_and_teardown_example():
    # 執行測試用例之前的操作
    print("Setup: 执行测试用例之前的操作")

    # 這裡的 yield 將區分測試用例之前和之後的操作
    yield

    # 執行測試用例之後的操作
    print("Teardown: 执行测试用例之后的操作")

@pytest.fixture(scope="module")
def once_setup():
    # 執行測試用例之前的操作
    print("所有 function 之前只有執行一次")

# 測試用例1
def test_case_1(setup_and_teardown_example, once_setup):
    print("Test Case 1: 执行测试用例1")
    assert 1 == 1

# 測試用例2
def test_case_2(setup_and_teardown_example, once_setup):
    print("Test Case 2: 执行测试用例2")
    assert "hello" == "world"

# 測試用例3
def test_case_3(setup_and_teardown_example, once_setup):
    print("Test Case 3: 执行测试用例3")
    assert True is True

