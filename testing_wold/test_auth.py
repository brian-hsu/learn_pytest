import requests
import pytest
from requests.auth import HTTPBasicAuth

# 定義基本身份驗證的使用者名稱和密碼
username = "br"
password = "fsdnfkdsjh23423"

# 定義要訪問的API的URL
api_url = f"https://httpbin.org/basic-auth/{username}/{password}"

@pytest.mark.Auth
def test_auth_function():
    # 傳送帶有基本身份驗證的GET請求
    response = requests.get(api_url, auth=HTTPBasicAuth(username, password))

    # 檢查響應狀態碼
    if response.status_code == 200:
        # 成功訪問API，處理響應資料
        data = response.json()
        print("API Response:")
        print(data)
    else:
        print("Failed to access the API. Status code:", response.status_code)

# test_auth_function()
