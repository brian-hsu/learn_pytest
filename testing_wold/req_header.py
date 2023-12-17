import requests

# 指定 API URL
url = "https://httpbin.org/get"

# 創建一個包含自訂標頭的字典
header_data = {
    'my_h1': 'sdfdsfsdf',
    'my_h2': 'sdfsdfsdgfgdfgdf'
}

def test_header():
    # 發送 GET 請求並包含自訂標頭
    response = requests.get(url, headers=header_data)

    # 輸出響應內容
    print(response.text)
