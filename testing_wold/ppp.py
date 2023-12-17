import requests

# 定義基本的URL
base_url = "https://httpbin.org/get"

# 創建參數字典
params = {
    "name": "Testing word",
    "email": "testingwordIndia@gmail.com",
    "number": "918743913121"
}

def test_pp():
    # 發送帶有參數的GET請求
    response = requests.get(base_url, params=params)

    # 印出伺服器回應
    print("Response Text:")
    print(response.text)
