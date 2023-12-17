import pytest


# 定義三個測試用例，並為它們分配不同的標籤
@pytest.mark.Smoke
def test_smoke_case_1():
    assert 1 == 1


@pytest.mark.P2
def test_sanity_case_1():
    print("mark p2")
    assert 2 == 2


@pytest.mark.Regression
def test_regression_case_1():
    assert 3 == 3


# 再定義一些測試用例，可以屬於多個類別
@pytest.mark.Smoke
@pytest.mark.Sanity
def test_combined_case_1():
    print("mark smoke")
    print("mark sanity")
    assert 4 == 4


@pytest.mark.P1
@pytest.mark.Regression
def test_combined_case_2():
    print("mark p1")
    print("mark regression")
    assert 5 == 5


# 執行只帶有特定標籤的測試用例
# 使用以下命令執行smoke測試用例：
# pytest -m smoke
# 使用以下命令執行sanity測試用例：
# pytest -m sanity
# 使用以下命令執行帶有sanity和regression標籤的測試用例：
# pytest -m "sanity and regression"
def test_execute_specific_tags():
    pass
