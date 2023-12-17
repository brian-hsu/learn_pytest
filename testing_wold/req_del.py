import requests
import pytest

url = "https://reqres.in/api/users/3"


def test_del():
    # 发送GET请求
    response = requests.delete(url)

    # 验证状态码
    assert response.status_code == 204