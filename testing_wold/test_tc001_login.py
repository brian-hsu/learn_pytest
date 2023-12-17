# 引入必要的庫
import pytest


# 定義第一個測試用例方法
def test_TC001_Login_Logout_Testing():
    print("This is our first test case code.")
    assert 1 + 1 == 2


# 定義第二個測試用例方法
def test_002_Registration_Testing():
    print("This is our second test case code.")
    assert 2 * 3 == 6

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


# 執行所有測試用例
if __name__ == "__main__":
    pytest.main(["-v"])  # 使用"-v"參數以詳細模式執行測試
