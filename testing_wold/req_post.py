import requests
import json

# 設定API URL
base_url = "https://reqres.in/api/users"

# 構建請求體的JSON
data = {
    "name": "brian",
    "job": "leader"
}

def test_status_code():
    # 將數據轉換成JSON格式
    json_data = json.dumps(data)

    # 發送POST請求
    response = requests.post(base_url, data=json_data)

    # 檢查響應內容
    print(response.content)
    print(response.text)

    json_response = json.loads(response.text)
    print(json_response)

    header = response.headers
    print(header['Content-Type'])
    print(header.get('Content-Type'))

    # 如果需要，進行錯誤處理和響應驗證
    if response.status_code == 201:
        print("Resource created successfully.")
    else:
        print("Failed to create the resource.")
