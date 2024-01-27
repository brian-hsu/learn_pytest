import pytest

def function_that_raises_exception():
    raise Exception('some info')

def test_exception():
    with pytest.raises(Exception) as excinfo:   
        function_that_raises_exception()   
    assert str(excinfo.value) == 'some info'


def test_login_failed():
    # 模拟错误的用户名和密码
    invalid_username = "invalid_user"
    invalid_password = "invalid_password"

    # 使用 pytest.raises 来验证登录失败时是否会引发预期的异常
    with pytest.raises(LoginFailedException):
        # 调用登录 API，传入错误的用户名和密码
        response = login_api(invalid_username, invalid_password)